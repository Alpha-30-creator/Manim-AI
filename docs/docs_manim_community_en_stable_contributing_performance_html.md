ContentsMenuExpandLight modeDark modeAuto light/dark, in light modeAuto light/dark, in dark mode[Skip to content](https://docs.manim.community/en/stable/contributing/performance.html#furo-main-content)

[Back to top](https://docs.manim.community/en/stable/contributing/performance.html#)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

# Improving performance [¶](https://docs.manim.community/en/stable/contributing/performance.html\#improving-performance "Link to this heading")

One of Manim’s main flaws as an animation library is its slow performance.
As of time of writing (January 2022), the library is still very unoptimized.
As such, we highly encourage contributors to help out in optimizing the code.

## Profiling [¶](https://docs.manim.community/en/stable/contributing/performance.html\#profiling "Link to this heading")

Before the library can be optimized, we first need to identify the bottlenecks
in performance via profiling. There are numerous Python profilers available for
this purpose; some examples include cProfile and Scalene.

### Running an animation as a script [¶](https://docs.manim.community/en/stable/contributing/performance.html\#running-an-animation-as-a-script "Link to this heading")

Most instructions for profilers assume you can run the python file directly as a
script from the command line. While Manim animations are usually run from the
command-line, we can run them as scripts by adding something like the following
to the bottom of the file:

```
with tempconfig({"quality": "medium_quality", "disable_caching": True}):
    scene = SceneName()
    scene.render()

```

Copy to clipboard

Where `SceneName` is the name of the scene you want to run. You can then run the
file directly, and can thus follow the instructions for most profilers.

### An example: profiling with cProfile and SnakeViz [¶](https://docs.manim.community/en/stable/contributing/performance.html\#an-example-profiling-with-cprofile-and-snakeviz "Link to this heading")

Install SnakeViz:

```
pip install snakeviz

```

Copy to clipboard

cProfile is included with in Python’s standard library and does not need to be installed.

Suppose we want to profile `SquareToCircle`. Then we add and save the following code
to `square_to_circle.py`:

```
from manim import *

class SquareToCircle(Scene):
    def construct(self):
        s = Square()
        c = Circle()
        self.add(s)
        self.play(Transform(s, c))

with tempconfig({"quality": "medium_quality", "disable_caching": True}):
    scene = SquareToCircle()
    scene.render()

```

Copy to clipboard

Now run the following in the terminal:

```
python -m cProfile -o square_to_circle.txt square_to_circle.py

```

Copy to clipboard

This will create a file called `square_to_circle.txt`.

Now, we can run SnakeViz on the profile file:

```
snakeviz square_to_circle.txt

```

Copy to clipboard

A browser window or tab will open with a visualization of the profile, which should
look something like this:

![../_images/snakeviz.png](https://docs.manim.community/en/stable/_images/snakeviz.png)