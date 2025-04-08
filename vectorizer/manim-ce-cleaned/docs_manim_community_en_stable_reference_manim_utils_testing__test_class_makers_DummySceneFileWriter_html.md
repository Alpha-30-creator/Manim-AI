# DummySceneFileWriter [¶](https://docs.manim.community/en/stable/reference/manim.utils.testing._test_class_makers.DummySceneFileWriter.html\#dummyscenefilewriter "Link to this heading")

Qualified name: `manim.utils.testing.\_test\_class\_makers.DummySceneFileWriter`

_class_ DummySceneFileWriter( _renderer_, _scene\_name_, _\*\*kwargs_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/utils/testing/_test_class_makers.html#DummySceneFileWriter) [¶](https://docs.manim.community/en/stable/reference/manim.utils.testing._test_class_makers.DummySceneFileWriter.html#manim.utils.testing._test_class_makers.DummySceneFileWriter "Link to this definition")

Bases: [`SceneFileWriter`](https://docs.manim.community/en/stable/reference/manim.scene.scene_file_writer.SceneFileWriter.html#manim.scene.scene_file_writer.SceneFileWriter "manim.scene.scene_file_writer.SceneFileWriter")

Delegate of SceneFileWriter used to test the frames.

Methods

|     |     |
| --- | --- |
| [`add_partial_movie_file`](https://docs.manim.community/en/stable/reference/manim.utils.testing._test_class_makers.DummySceneFileWriter.html#manim.utils.testing._test_class_makers.DummySceneFileWriter.add_partial_movie_file "manim.utils.testing._test_class_makers.DummySceneFileWriter.add_partial_movie_file") | Adds a new partial movie file path to scene.partial\_movie\_files and current section from a hash. |
| [`begin_animation`](https://docs.manim.community/en/stable/reference/manim.utils.testing._test_class_makers.DummySceneFileWriter.html#manim.utils.testing._test_class_makers.DummySceneFileWriter.begin_animation "manim.utils.testing._test_class_makers.DummySceneFileWriter.begin_animation") | Used internally by manim to stream the animation to FFMPEG for displaying or writing to a file. |
| [`clean_cache`](https://docs.manim.community/en/stable/reference/manim.utils.testing._test_class_makers.DummySceneFileWriter.html#manim.utils.testing._test_class_makers.DummySceneFileWriter.clean_cache "manim.utils.testing._test_class_makers.DummySceneFileWriter.clean_cache") | Will clean the cache by removing the oldest partial\_movie\_files. |
| [`combine_to_movie`](https://docs.manim.community/en/stable/reference/manim.utils.testing._test_class_makers.DummySceneFileWriter.html#manim.utils.testing._test_class_makers.DummySceneFileWriter.combine_to_movie "manim.utils.testing._test_class_makers.DummySceneFileWriter.combine_to_movie") | Used internally by Manim to combine the separate partial movie files that make up a Scene into a single video file for that Scene. |
| [`combine_to_section_videos`](https://docs.manim.community/en/stable/reference/manim.utils.testing._test_class_makers.DummySceneFileWriter.html#manim.utils.testing._test_class_makers.DummySceneFileWriter.combine_to_section_videos "manim.utils.testing._test_class_makers.DummySceneFileWriter.combine_to_section_videos") | Concatenate partial movie files for each section. |
| [`end_animation`](https://docs.manim.community/en/stable/reference/manim.utils.testing._test_class_makers.DummySceneFileWriter.html#manim.utils.testing._test_class_makers.DummySceneFileWriter.end_animation "manim.utils.testing._test_class_makers.DummySceneFileWriter.end_animation") | Internally used by Manim to stop streaming to FFMPEG gracefully. |
| [`init_output_directories`](https://docs.manim.community/en/stable/reference/manim.utils.testing._test_class_makers.DummySceneFileWriter.html#manim.utils.testing._test_class_makers.DummySceneFileWriter.init_output_directories "manim.utils.testing._test_class_makers.DummySceneFileWriter.init_output_directories") | Initialise output directories. |
| [`write_frame`](https://docs.manim.community/en/stable/reference/manim.utils.testing._test_class_makers.DummySceneFileWriter.html#manim.utils.testing._test_class_makers.DummySceneFileWriter.write_frame "manim.utils.testing._test_class_makers.DummySceneFileWriter.write_frame") | Used internally by Manim to write a frame to the FFMPEG input buffer. |

Attributes

|     |     |
| --- | --- |
| `force_output_as_scene_name` |  |

Parameters:

- **renderer** ( _CairoRenderer_ _\|_ _OpenGLRenderer_)

- **scene\_name** ( [_StrPath_](https://docs.manim.community/en/stable/reference/manim.typing.html#manim.typing.StrPath "manim.typing.StrPath"))

- **kwargs** ( _Any_)


add\_partial\_movie\_file( _hash\_animation_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/utils/testing/_test_class_makers.html#DummySceneFileWriter.add_partial_movie_file) [¶](https://docs.manim.community/en/stable/reference/manim.utils.testing._test_class_makers.DummySceneFileWriter.html#manim.utils.testing._test_class_makers.DummySceneFileWriter.add_partial_movie_file "Link to this definition")

Adds a new partial movie file path to scene.partial\_movie\_files and current section from a hash.
This method will compute the path from the hash. In addition to that it adds the new animation to the current section.

Parameters:

**hash\_animation** ( _str_) – Hash of the animation.

Return type:

None

begin\_animation( _allow\_write=True_, _file\_path=None_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/utils/testing/_test_class_makers.html#DummySceneFileWriter.begin_animation) [¶](https://docs.manim.community/en/stable/reference/manim.utils.testing._test_class_makers.DummySceneFileWriter.html#manim.utils.testing._test_class_makers.DummySceneFileWriter.begin_animation "Link to this definition")

Used internally by manim to stream the animation to FFMPEG for
displaying or writing to a file.

Parameters:

- **allow\_write** ( _bool_) – Whether or not to write to a video file.

- **file\_path** ( [_StrPath_](https://docs.manim.community/en/stable/reference/manim.typing.html#manim.typing.StrPath "manim.typing.StrPath") _\|_ _None_)


Return type:

Any

clean\_cache() [\[source\]](https://docs.manim.community/en/stable/_modules/manim/utils/testing/_test_class_makers.html#DummySceneFileWriter.clean_cache) [¶](https://docs.manim.community/en/stable/reference/manim.utils.testing._test_class_makers.DummySceneFileWriter.html#manim.utils.testing._test_class_makers.DummySceneFileWriter.clean_cache "Link to this definition")

Will clean the cache by removing the oldest partial\_movie\_files.

Return type:

None

combine\_to\_movie() [\[source\]](https://docs.manim.community/en/stable/_modules/manim/utils/testing/_test_class_makers.html#DummySceneFileWriter.combine_to_movie) [¶](https://docs.manim.community/en/stable/reference/manim.utils.testing._test_class_makers.DummySceneFileWriter.html#manim.utils.testing._test_class_makers.DummySceneFileWriter.combine_to_movie "Link to this definition")

Used internally by Manim to combine the separate
partial movie files that make up a Scene into a single
video file for that Scene.

Return type:

None

combine\_to\_section\_videos() [\[source\]](https://docs.manim.community/en/stable/_modules/manim/utils/testing/_test_class_makers.html#DummySceneFileWriter.combine_to_section_videos) [¶](https://docs.manim.community/en/stable/reference/manim.utils.testing._test_class_makers.DummySceneFileWriter.html#manim.utils.testing._test_class_makers.DummySceneFileWriter.combine_to_section_videos "Link to this definition")

Concatenate partial movie files for each section.

Return type:

None

end\_animation( _allow\_write=False_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/utils/testing/_test_class_makers.html#DummySceneFileWriter.end_animation) [¶](https://docs.manim.community/en/stable/reference/manim.utils.testing._test_class_makers.DummySceneFileWriter.html#manim.utils.testing._test_class_makers.DummySceneFileWriter.end_animation "Link to this definition")

Internally used by Manim to stop streaming to
FFMPEG gracefully.

Parameters:

**allow\_write** ( _bool_) – Whether or not to write to a video file.

Return type:

None

init\_output\_directories( _scene\_name_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/utils/testing/_test_class_makers.html#DummySceneFileWriter.init_output_directories) [¶](https://docs.manim.community/en/stable/reference/manim.utils.testing._test_class_makers.DummySceneFileWriter.html#manim.utils.testing._test_class_makers.DummySceneFileWriter.init_output_directories "Link to this definition")

Initialise output directories.

Notes

The directories are read from `config`, for example
`config['media_dir']`. If the target directories don’t already
exist, they will be created.

Parameters:

**scene\_name** ( [_StrPath_](https://docs.manim.community/en/stable/reference/manim.typing.html#manim.typing.StrPath "manim.typing.StrPath"))

Return type:

None

write\_frame( _frame\_or\_renderer_, _num\_frames=1_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/utils/testing/_test_class_makers.html#DummySceneFileWriter.write_frame) [¶](https://docs.manim.community/en/stable/reference/manim.utils.testing._test_class_makers.DummySceneFileWriter.html#manim.utils.testing._test_class_makers.DummySceneFileWriter.write_frame "Link to this definition")

Used internally by Manim to write a frame to
the FFMPEG input buffer.

Parameters:

- **frame\_or\_renderer** ( [_PixelArray_](https://docs.manim.community/en/stable/reference/manim.typing.html#manim.typing.PixelArray "manim.typing.PixelArray") _\|_ _OpenGLRenderer_) – Pixel array of the frame.

- **num\_frames** ( _int_) – The number of times to write frame.


Return type:

None