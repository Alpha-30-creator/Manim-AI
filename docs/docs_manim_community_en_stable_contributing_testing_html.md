ContentsMenuExpandLight modeDark modeAuto light/dark, in light modeAuto light/dark, in dark mode[Skip to content](https://docs.manim.community/en/stable/contributing/testing.html#furo-main-content)

[Back to top](https://docs.manim.community/en/stable/contributing/testing.html#)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

# Adding Tests [¶](https://docs.manim.community/en/stable/contributing/testing.html\#adding-tests "Link to this heading")

If you are adding new features to manim, you should add appropriate tests for them. Tests prevent
manim from breaking at each change by checking that no other
feature has been broken and/or been unintentionally modified.

Warning

The full tests suite requires Cairo 1.18 in order to run all tests.
However, Cairo 1.18 may not be available from your package manager,
like `apt`, and it is very likely that you have an older version installed,
e.g., 1.16. If you run tests with a version prior to 1.18,
many tests will be skipped. Those tests are not skipped in the online CI.

If you want to run all tests locally, you need to install Cairo 1.18 or above.
You can do so by compiling Cairo from source:

1. download `cairo-1.18.0.tar.xz` from
[here](https://www.cairographics.org/releases/).
and uncompress it;

2. open the INSTALL file and follow the instructions (you might need to install
`meson` and `ninja`);

3. run the tests suite and verify that the Cairo version is correct.


## How Manim tests [¶](https://docs.manim.community/en/stable/contributing/testing.html\#how-manim-tests "Link to this heading")

Manim uses pytest as its testing framework.
To start the testing process, go to the root directory of the project and run pytest in your terminal.
Any errors that occur during testing will be displayed in the terminal.

Some useful pytest flags:

- `-x` will make pytest stop at the first failure it encounters

- `-s` will make pytest display all the print messages (including those during scene generation, like DEBUG messages)

- `--skip_slow` will skip the (arbitrarily) slow tests

- `--show_diff` will show a visual comparison in case a unit test is failing.


### How it Works [¶](https://docs.manim.community/en/stable/contributing/testing.html\#how-it-works "Link to this heading")

At the moment there are three types of tests:

1. Unit Tests:

Tests for most of the basic functionalities of manim. For example, there a test for
`Mobject`, that checks if it can be added to a Scene, etc.

2. Graphical unit tests:
Because `manim` is a graphics library, we test frames. To do so, we create test scenes that render a specific feature.
When pytest runs, it compares the result of the test to the control data, either at 6 fps or just the last frame. If it matches, the tests
pass. If the test and control data differ, the tests fail. You can use `--show_diff` flag with `pytest` to visually
see the differences. The `extract_frames.py` script lets you see all the frames of a test.

3. Videos format tests:

As Manim is a video library, we have to test videos as well. Unfortunately,
we cannot directly test video content as rendered videos can
differ slightly depending on the system (for reasons related to
ffmpeg). Therefore, we only compare video configuration values, exported in
.json.


## Architecture [¶](https://docs.manim.community/en/stable/contributing/testing.html\#architecture "Link to this heading")

The `manim/tests` directory looks like this:

```
.
├── conftest.py
├── control_data
│   ├── graphical_units_data
│   │   ├── creation
│   │   │   ├── DrawBorderThenFillTest.npy
│   │   │   ├── FadeInFromDownTest.npy
│   │   │   ├── FadeInFromLargeTest.npy
│   │   │   ├── FadeInFromTest.npy
│   │   │   ├── FadeInTest.npy
│   │   │   ├── ...
│   │   ├── geometry
│   │   │   ├── AnnularSectorTest.npy
│   │   │   ├── AnnulusTest.npy
│   │   │   ├── ArcBetweenPointsTest.npy
│   │   │   ├── ArcTest.npy
│   │   │   ├── CircleTest.npy
│   │   │   ├── CoordinatesTest.npy
│   │   │   ├── ...
│   │   ├── graph
│   │   │   ├── ...
|   |   |   | ...
│   └── videos_data
│       ├── SquareToCircleWithDefaultValues.json
│       └── SquareToCircleWithlFlag.json
├── helpers
│   ├── graphical_units.py
│   ├── __init__.py
│   └── video_utils.py
├── __init__.py
├── test_camera.py
├── test_config.py
├── test_copy.py
├── test_vectorized_mobject.py
├── test_graphical_units
│   ├── conftest.py
│   ├── __init__.py
│   ├── test_creation.py
│   ├── test_geometry.py
│   ├── test_graph.py
│   ├── test_indication.py
│   ├── test_movements.py
│   ├── test_threed.py
│   ├── test_transform.py
│   └── test_updaters.py
├── test_logging
│   ├── basic_scenes.py
│   ├── expected.txt
│   ├── testloggingconfig.cfg
│   └── test_logging.py
├── test_scene_rendering
│   ├── conftest.py
│   ├── __init__.py
│   ├── simple_scenes.py
│   ├── standard_config.cfg
│   └── test_cli_flags.py
└── utils
    ├── commands.py
    ├── __init__.py
    ├── testing_utils.py
    └── video_tester.py
   ...

```

Copy to clipboard

## The Main Directories [¶](https://docs.manim.community/en/stable/contributing/testing.html\#the-main-directories "Link to this heading")

- `control_data/`:

The directory containing control data. `control_data/graphical_units_data/` contains the expected and correct frame data for graphical tests, and
`control_data/videos_data/` contains the .json files used to check videos.

- `test_graphical_units/`:

Contains graphical tests.

- `test_scene_rendering/`:

For tests that need to render a scene in some way, such as tests for CLI
flags (end-to-end tests).

- `utils/`:

Useful internal functions used by pytest.



Note



fixtures are not contained here, they are in `conftest.py`.

- `helpers/`:

Helper functions for developers to setup graphical/video tests.


## Adding a New Test [¶](https://docs.manim.community/en/stable/contributing/testing.html\#adding-a-new-test "Link to this heading")

### Unit Tests [¶](https://docs.manim.community/en/stable/contributing/testing.html\#unit-tests "Link to this heading")

Pytest determines which functions are tests by searching for files whose
names begin with “test\_”, and then within those files for functions
beginning with “test” and classes beginning with “Test”. These kinds of
tests must be in `tests/` (e.g. `tests/test_container.py`).

### Graphical Unit Test [¶](https://docs.manim.community/en/stable/contributing/testing.html\#graphical-unit-test "Link to this heading")

The test must be written in the correct file (i.e. the file that corresponds to the appropriate category the feature belongs to) and follow the structure
of unit tests.

For example, to test the `Circle` VMobject which resides in
`manim/mobject/geometry.py`, add the CircleTest to
`test/test_geometry.py`.

The name of the module is indicated by the variable \_\_module\_test\_\_, that **must** be declared in any graphical test file. The module name is used to store the graphical control data.

Important

You will need to use the `frames_comparison` decorator to create a test. The test function **must** accept a
parameter named `scene` that will be used like `self` in a standard `construct` method.

Here’s an example in `test_geometry.py`:

```
from manim import *
from manim.utils.testing.frames_comparison import frames_comparison

__module_test__ = "geometry"

@frames_comparison
def test_circle(scene):
    circle = Circle()
    scene.play(Animation(circle))

```

Copy to clipboard

The decorator can be used with or without parentheses. **By default, the test only tests the last frame. To enable multi-frame testing, you have to set \`\`last\_frame=False\`\` in the parameters.**

```
@frames_comparison(last_frame=False)
def test_circle(scene):
    circle = Circle()
    scene.play(Animation(circle))

```

Copy to clipboard

You can also specify, when needed, which base scene you need (ThreeDScene, for example) :

```
@frames_comparison(last_frame=False, base_scene=ThreeDScene)
def test_circle(scene):
    circle = Circle()
    scene.play(Animation(circle))

```

Copy to clipboard

Feel free to check the documentation of `@frames_comparison` for more.

Note that tests name must follow the syntax `test_<thing_to_test>`, otherwise pytest will not recognize it as a test.

Warning

If you run pytest now, you will get a `FileNotFound` error. This is because
you have not created control data for your test.

To create the control data for your test, you have to use the flag `--set_test` along with pytest.
For the example above, it would be

```
pytest test_geometry.py::test_circle --set_test -s

```

Copy to clipboard

( `-s` is here to see manim logs, so you can see what’s going on).

If you want to see all the control data frames (e.g. to make sure your test is doing what you want), use the
`extract_frames.py` script. The first parameter is the path to a `.npz` file and the second parameter is the
directory you want the frames created. The frames will be named `frame0.png`, `frame1.png`, etc.

```
python scripts/extract_frames.py tests/test_graphical_units/control_data/plot/axes.npz output

```

Copy to clipboard

Please make sure to add the control data to git as soon as it is produced with `git add <your-control-data.npz>`.

### Videos tests [¶](https://docs.manim.community/en/stable/contributing/testing.html\#videos-tests "Link to this heading")

To test videos generated, we use the decorator
`tests.utils.videos_tester.video_comparison`:

```
@video_comparison(
    "SquareToCircleWithlFlag.json", "videos/simple_scenes/480p15/SquareToCircle.mp4"
)
def test_basic_scene_l_flag(tmp_path, manim_cfg_file, simple_scenes_path):
    scene_name = "SquareToCircle"
    command = [\
        "python",\
        "-m",\
        "manim",\
        simple_scenes_path,\
        scene_name,\
        "-l",\
        "--media_dir",\
        str(tmp_path),\
    ]
    out, err, exit_code = capture(command)
    assert exit_code == 0, err

```

Copy to clipboard

Note

`assert exit*\ code == 0, err` is used in case of the command fails
to run. The decorator takes two arguments: json name and the path
to where the video should be generated, starting from the `media/` dir.

Note the fixtures here:

- tmp\_path is a pytest fixture to get a tmp\_path. Manim will output here, according to the flag `--media_dir`.

- `manim_cfg_file` fixture that return a path pointing to `test_scene_rendering/standard_config.cfg`. It’s just to shorten the code, in the case multiple tests need to use this cfg file.

- `simple_scenes_path` same as above, except for `test_scene_rendering/simple_scene.py`


You have to generate a `.json` file first to be able to test your video. To
do that, use `helpers.save_control_data_from_video`.

For instance, a test that will check if the l flag works properly will first
require rendering a video using the -l flag from a scene. Then we will test
(in this case, SquareToCircle), that lives in
`test_scene_rendering/simple_scene.py`. Change directories to `tests/`,
create a file (e.g. `create\_data.py`) that you will remove as soon as
you’re done. Then run:

```
save_control_data_from_video("<path-to-video>", "SquareToCircleWithlFlag.json")

```

Copy to clipboard

Running this will save
`control_data/videos_data/SquareToCircleWithlFlag.json`, which will
look like this:

```
{
    "name": "SquareToCircleWithlFlag",
    "config": {
        "codec_name": "h264",
        "width": 854,
        "height": 480,
        "avg_frame_rate": "15/1",
        "duration": "1.000000",
        "nb_frames": "15"
    }
}

```

Copy to clipboard

If you have any questions, please don’t hesitate to ask on [Discord](https://www.manim.community/discord/), in your pull request, or in an issue.

[**Document Extraction for Developers** Transform docs into structured data with Sensible. **Try for free →**](https://server.ethicalads.io/proxy/click/8517/019600e2-b9be-70c2-8568-2eb6569c1931/)

[Ads by EthicalAds](https://www.ethicalads.io/advertisers/topics/data-science/?ref=ea-text)

![](https://server.ethicalads.io/proxy/view/8517/019600e2-b9be-70c2-8568-2eb6569c1931/)