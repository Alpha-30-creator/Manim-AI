# scene\_file\_writer [¶](https://docs.manim.community/en/stable/reference/manim.scene.scene_file_writer.html\#module-manim.scene.scene_file_writer "Link to this heading")

The interface between scenes and ffmpeg.

Classes

|     |     |
| --- | --- |
| [`SceneFileWriter`](https://docs.manim.community/en/stable/reference/manim.scene.scene_file_writer.SceneFileWriter.html#manim.scene.scene_file_writer.SceneFileWriter "manim.scene.scene_file_writer.SceneFileWriter") | SceneFileWriter is the object that actually writes the animations played, into video files, using FFMPEG. |

Functions

convert\_audio( _input\_path_, _output\_path_, _codec\_name_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/scene/scene_file_writer.html#convert_audio) [¶](https://docs.manim.community/en/stable/reference/manim.scene.scene_file_writer.html#manim.scene.scene_file_writer.convert_audio "Link to this definition")Parameters:

- **input\_path** ( _Path_)

- **output\_path** ( _Path_)

- **codec\_name** ( _str_)


to\_av\_frame\_rate( _fps_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/scene/scene_file_writer.html#to_av_frame_rate) [¶](https://docs.manim.community/en/stable/reference/manim.scene.scene_file_writer.html#manim.scene.scene_file_writer.to_av_frame_rate "Link to this definition")