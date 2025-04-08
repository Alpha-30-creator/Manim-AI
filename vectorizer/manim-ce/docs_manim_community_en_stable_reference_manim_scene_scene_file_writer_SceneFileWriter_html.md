ContentsMenuExpandLight modeDark modeAuto light/dark, in light modeAuto light/dark, in dark mode[Skip to content](https://docs.manim.community/en/stable/reference/manim.scene.scene_file_writer.SceneFileWriter.html#furo-main-content)

[Back to top](https://docs.manim.community/en/stable/reference/manim.scene.scene_file_writer.SceneFileWriter.html#)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

# SceneFileWriter [¶](https://docs.manim.community/en/stable/reference/manim.scene.scene_file_writer.SceneFileWriter.html\#scenefilewriter "Link to this heading")

Qualified name: `manim.scene.scene\_file\_writer.SceneFileWriter`

_class_ SceneFileWriter( _renderer_, _scene\_name_, _\*\*kwargs_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/scene/scene_file_writer.html#SceneFileWriter) [¶](https://docs.manim.community/en/stable/reference/manim.scene.scene_file_writer.SceneFileWriter.html#manim.scene.scene_file_writer.SceneFileWriter "Link to this definition")

Bases: `object`

SceneFileWriter is the object that actually writes the animations
played, into video files, using FFMPEG.
This is mostly for Manim’s internal use. You will rarely, if ever,
have to use the methods for this class, unless tinkering with the very
fabric of Manim’s reality.

Parameters:

- **renderer** ( _CairoRenderer_ _\|_ _OpenGLRenderer_)

- **scene\_name** ( [_StrPath_](https://docs.manim.community/en/stable/reference/manim.typing.html#manim.typing.StrPath "manim.typing.StrPath"))

- **kwargs** ( _Any_)


sections [¶](https://docs.manim.community/en/stable/reference/manim.scene.scene_file_writer.SceneFileWriter.html#manim.scene.scene_file_writer.SceneFileWriter.sections "Link to this definition")

used to segment scene

Type:

list of [`Section`](https://docs.manim.community/en/stable/reference/manim.scene.section.Section.html#manim.scene.section.Section "manim.scene.section.Section")

sections\_output\_dir [¶](https://docs.manim.community/en/stable/reference/manim.scene.scene_file_writer.SceneFileWriter.html#manim.scene.scene_file_writer.SceneFileWriter.sections_output_dir "Link to this definition")

where are section videos stored

Type:

`pathlib.Path`

output\_name [¶](https://docs.manim.community/en/stable/reference/manim.scene.scene_file_writer.SceneFileWriter.html#manim.scene.scene_file_writer.SceneFileWriter.output_name "Link to this definition")

name of movie without extension and basis for section video names

Type:

str

Some useful attributes are:“write\_to\_movie” (bool=False)

Whether or not to write the animations into a video file.

“movie\_file\_extension” (str=”.mp4”)

The file-type extension of the outputted video.

“partial\_movie\_files”

List of all the partial-movie files.

Methods

|     |     |
| --- | --- |
| [`add_audio_segment`](https://docs.manim.community/en/stable/reference/manim.scene.scene_file_writer.SceneFileWriter.html#manim.scene.scene_file_writer.SceneFileWriter.add_audio_segment "manim.scene.scene_file_writer.SceneFileWriter.add_audio_segment") | This method adds an audio segment from an AudioSegment type object and suitable parameters. |
| [`add_partial_movie_file`](https://docs.manim.community/en/stable/reference/manim.scene.scene_file_writer.SceneFileWriter.html#manim.scene.scene_file_writer.SceneFileWriter.add_partial_movie_file "manim.scene.scene_file_writer.SceneFileWriter.add_partial_movie_file") | Adds a new partial movie file path to scene.partial\_movie\_files and current section from a hash. |
| [`add_sound`](https://docs.manim.community/en/stable/reference/manim.scene.scene_file_writer.SceneFileWriter.html#manim.scene.scene_file_writer.SceneFileWriter.add_sound "manim.scene.scene_file_writer.SceneFileWriter.add_sound") | This method adds an audio segment from a sound file. |
| [`begin_animation`](https://docs.manim.community/en/stable/reference/manim.scene.scene_file_writer.SceneFileWriter.html#manim.scene.scene_file_writer.SceneFileWriter.begin_animation "manim.scene.scene_file_writer.SceneFileWriter.begin_animation") | Used internally by manim to stream the animation to FFMPEG for displaying or writing to a file. |
| [`clean_cache`](https://docs.manim.community/en/stable/reference/manim.scene.scene_file_writer.SceneFileWriter.html#manim.scene.scene_file_writer.SceneFileWriter.clean_cache "manim.scene.scene_file_writer.SceneFileWriter.clean_cache") | Will clean the cache by removing the oldest partial\_movie\_files. |
| [`close_partial_movie_stream`](https://docs.manim.community/en/stable/reference/manim.scene.scene_file_writer.SceneFileWriter.html#manim.scene.scene_file_writer.SceneFileWriter.close_partial_movie_stream "manim.scene.scene_file_writer.SceneFileWriter.close_partial_movie_stream") | Close the currently opened video container. |
| `combine_files` |  |
| [`combine_to_movie`](https://docs.manim.community/en/stable/reference/manim.scene.scene_file_writer.SceneFileWriter.html#manim.scene.scene_file_writer.SceneFileWriter.combine_to_movie "manim.scene.scene_file_writer.SceneFileWriter.combine_to_movie") | Used internally by Manim to combine the separate partial movie files that make up a Scene into a single video file for that Scene. |
| [`combine_to_section_videos`](https://docs.manim.community/en/stable/reference/manim.scene.scene_file_writer.SceneFileWriter.html#manim.scene.scene_file_writer.SceneFileWriter.combine_to_section_videos "manim.scene.scene_file_writer.SceneFileWriter.combine_to_section_videos") | Concatenate partial movie files for each section. |
| [`create_audio_segment`](https://docs.manim.community/en/stable/reference/manim.scene.scene_file_writer.SceneFileWriter.html#manim.scene.scene_file_writer.SceneFileWriter.create_audio_segment "manim.scene.scene_file_writer.SceneFileWriter.create_audio_segment") | Creates an empty, silent, Audio Segment. |
| [`encode_and_write_frame`](https://docs.manim.community/en/stable/reference/manim.scene.scene_file_writer.SceneFileWriter.html#manim.scene.scene_file_writer.SceneFileWriter.encode_and_write_frame "manim.scene.scene_file_writer.SceneFileWriter.encode_and_write_frame") | For internal use only: takes a given frame in `np.ndarray` format and write it to the stream |
| [`end_animation`](https://docs.manim.community/en/stable/reference/manim.scene.scene_file_writer.SceneFileWriter.html#manim.scene.scene_file_writer.SceneFileWriter.end_animation "manim.scene.scene_file_writer.SceneFileWriter.end_animation") | Internally used by Manim to stop streaming to FFMPEG gracefully. |
| [`finish`](https://docs.manim.community/en/stable/reference/manim.scene.scene_file_writer.SceneFileWriter.html#manim.scene.scene_file_writer.SceneFileWriter.finish "manim.scene.scene_file_writer.SceneFileWriter.finish") | Finishes writing to the FFMPEG buffer or writing images to output directory. |
| [`finish_last_section`](https://docs.manim.community/en/stable/reference/manim.scene.scene_file_writer.SceneFileWriter.html#manim.scene.scene_file_writer.SceneFileWriter.finish_last_section "manim.scene.scene_file_writer.SceneFileWriter.finish_last_section") | Delete current section if it is empty. |
| [`flush_cache_directory`](https://docs.manim.community/en/stable/reference/manim.scene.scene_file_writer.SceneFileWriter.html#manim.scene.scene_file_writer.SceneFileWriter.flush_cache_directory "manim.scene.scene_file_writer.SceneFileWriter.flush_cache_directory") | Delete all the cached partial movie files |
| [`get_resolution_directory`](https://docs.manim.community/en/stable/reference/manim.scene.scene_file_writer.SceneFileWriter.html#manim.scene.scene_file_writer.SceneFileWriter.get_resolution_directory "manim.scene.scene_file_writer.SceneFileWriter.get_resolution_directory") | Get the name of the resolution directory directly containing the video file. |
| [`init_audio`](https://docs.manim.community/en/stable/reference/manim.scene.scene_file_writer.SceneFileWriter.html#manim.scene.scene_file_writer.SceneFileWriter.init_audio "manim.scene.scene_file_writer.SceneFileWriter.init_audio") | Preps the writer for adding audio to the movie. |
| [`init_output_directories`](https://docs.manim.community/en/stable/reference/manim.scene.scene_file_writer.SceneFileWriter.html#manim.scene.scene_file_writer.SceneFileWriter.init_output_directories "manim.scene.scene_file_writer.SceneFileWriter.init_output_directories") | Initialise output directories. |
| [`is_already_cached`](https://docs.manim.community/en/stable/reference/manim.scene.scene_file_writer.SceneFileWriter.html#manim.scene.scene_file_writer.SceneFileWriter.is_already_cached "manim.scene.scene_file_writer.SceneFileWriter.is_already_cached") | Will check if a file named with hash\_invocation exists. |
| [`listen_and_write`](https://docs.manim.community/en/stable/reference/manim.scene.scene_file_writer.SceneFileWriter.html#manim.scene.scene_file_writer.SceneFileWriter.listen_and_write "manim.scene.scene_file_writer.SceneFileWriter.listen_and_write") | For internal use only: blocks until new frame is available on the queue. |
| [`next_section`](https://docs.manim.community/en/stable/reference/manim.scene.scene_file_writer.SceneFileWriter.html#manim.scene.scene_file_writer.SceneFileWriter.next_section "manim.scene.scene_file_writer.SceneFileWriter.next_section") | Create segmentation cut here. |
| [`open_partial_movie_stream`](https://docs.manim.community/en/stable/reference/manim.scene.scene_file_writer.SceneFileWriter.html#manim.scene.scene_file_writer.SceneFileWriter.open_partial_movie_stream "manim.scene.scene_file_writer.SceneFileWriter.open_partial_movie_stream") | Open a container holding a video stream. |
| `output_image` |  |
| [`print_file_ready_message`](https://docs.manim.community/en/stable/reference/manim.scene.scene_file_writer.SceneFileWriter.html#manim.scene.scene_file_writer.SceneFileWriter.print_file_ready_message "manim.scene.scene_file_writer.SceneFileWriter.print_file_ready_message") | Prints the "File Ready" message to STDOUT. |
| [`save_final_image`](https://docs.manim.community/en/stable/reference/manim.scene.scene_file_writer.SceneFileWriter.html#manim.scene.scene_file_writer.SceneFileWriter.save_final_image "manim.scene.scene_file_writer.SceneFileWriter.save_final_image") | The name is a misnomer. |
| [`write_frame`](https://docs.manim.community/en/stable/reference/manim.scene.scene_file_writer.SceneFileWriter.html#manim.scene.scene_file_writer.SceneFileWriter.write_frame "manim.scene.scene_file_writer.SceneFileWriter.write_frame") | Used internally by Manim to write a frame to the FFMPEG input buffer. |
| [`write_subcaption_file`](https://docs.manim.community/en/stable/reference/manim.scene.scene_file_writer.SceneFileWriter.html#manim.scene.scene_file_writer.SceneFileWriter.write_subcaption_file "manim.scene.scene_file_writer.SceneFileWriter.write_subcaption_file") | Writes the subcaption file. |

Attributes

|     |     |
| --- | --- |
| `force_output_as_scene_name` |  |

add\_audio\_segment( _new\_segment_, _time=None_, _gain\_to\_background=None_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/scene/scene_file_writer.html#SceneFileWriter.add_audio_segment) [¶](https://docs.manim.community/en/stable/reference/manim.scene.scene_file_writer.SceneFileWriter.html#manim.scene.scene_file_writer.SceneFileWriter.add_audio_segment "Link to this definition")

This method adds an audio segment from an
AudioSegment type object and suitable parameters.

Parameters:

- **new\_segment** ( _AudioSegment_) – The audio segment to add

- **time** ( _float_ _\|_ _None_) – the timestamp at which the
sound should be added.

- **gain\_to\_background** ( _float_ _\|_ _None_) – The gain of the segment from the background.


add\_partial\_movie\_file( _hash\_animation_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/scene/scene_file_writer.html#SceneFileWriter.add_partial_movie_file) [¶](https://docs.manim.community/en/stable/reference/manim.scene.scene_file_writer.SceneFileWriter.html#manim.scene.scene_file_writer.SceneFileWriter.add_partial_movie_file "Link to this definition")

Adds a new partial movie file path to scene.partial\_movie\_files and current section from a hash.
This method will compute the path from the hash. In addition to that it adds the new animation to the current section.

Parameters:

**hash\_animation** ( _str_) – Hash of the animation.

add\_sound( _sound\_file_, _time=None_, _gain=None_, _\*\*kwargs_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/scene/scene_file_writer.html#SceneFileWriter.add_sound) [¶](https://docs.manim.community/en/stable/reference/manim.scene.scene_file_writer.SceneFileWriter.html#manim.scene.scene_file_writer.SceneFileWriter.add_sound "Link to this definition")

This method adds an audio segment from a sound file.

Parameters:

- **sound\_file** ( _str_) – The path to the sound file.

- **time** ( _float_ _\|_ _None_) – The timestamp at which the audio should be added.

- **gain** ( _float_ _\|_ _None_) – The gain of the given audio segment.

- **\*\*kwargs** – This method uses add\_audio\_segment, so any keyword arguments
used there can be referenced here.


begin\_animation( _allow\_write=False_, _file\_path=None_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/scene/scene_file_writer.html#SceneFileWriter.begin_animation) [¶](https://docs.manim.community/en/stable/reference/manim.scene.scene_file_writer.SceneFileWriter.html#manim.scene.scene_file_writer.SceneFileWriter.begin_animation "Link to this definition")

Used internally by manim to stream the animation to FFMPEG for
displaying or writing to a file.

Parameters:

- **allow\_write** ( _bool_) – Whether or not to write to a video file.

- **file\_path** ( [_StrPath_](https://docs.manim.community/en/stable/reference/manim.typing.html#manim.typing.StrPath "manim.typing.StrPath") _\|_ _None_)


Return type:

None

clean\_cache() [\[source\]](https://docs.manim.community/en/stable/_modules/manim/scene/scene_file_writer.html#SceneFileWriter.clean_cache) [¶](https://docs.manim.community/en/stable/reference/manim.scene.scene_file_writer.SceneFileWriter.html#manim.scene.scene_file_writer.SceneFileWriter.clean_cache "Link to this definition")

Will clean the cache by removing the oldest partial\_movie\_files.

close\_partial\_movie\_stream() [\[source\]](https://docs.manim.community/en/stable/_modules/manim/scene/scene_file_writer.html#SceneFileWriter.close_partial_movie_stream) [¶](https://docs.manim.community/en/stable/reference/manim.scene.scene_file_writer.SceneFileWriter.html#manim.scene.scene_file_writer.SceneFileWriter.close_partial_movie_stream "Link to this definition")

Close the currently opened video container.

Used internally by Manim to first flush the remaining packages
in the video stream holding a partial file, and then close
the corresponding container.

Return type:

None

combine\_to\_movie() [\[source\]](https://docs.manim.community/en/stable/_modules/manim/scene/scene_file_writer.html#SceneFileWriter.combine_to_movie) [¶](https://docs.manim.community/en/stable/reference/manim.scene.scene_file_writer.SceneFileWriter.html#manim.scene.scene_file_writer.SceneFileWriter.combine_to_movie "Link to this definition")

Used internally by Manim to combine the separate
partial movie files that make up a Scene into a single
video file for that Scene.

combine\_to\_section\_videos() [\[source\]](https://docs.manim.community/en/stable/_modules/manim/scene/scene_file_writer.html#SceneFileWriter.combine_to_section_videos) [¶](https://docs.manim.community/en/stable/reference/manim.scene.scene_file_writer.SceneFileWriter.html#manim.scene.scene_file_writer.SceneFileWriter.combine_to_section_videos "Link to this definition")

Concatenate partial movie files for each section.

Return type:

None

create\_audio\_segment() [\[source\]](https://docs.manim.community/en/stable/_modules/manim/scene/scene_file_writer.html#SceneFileWriter.create_audio_segment) [¶](https://docs.manim.community/en/stable/reference/manim.scene.scene_file_writer.SceneFileWriter.html#manim.scene.scene_file_writer.SceneFileWriter.create_audio_segment "Link to this definition")

Creates an empty, silent, Audio Segment.

encode\_and\_write\_frame( _frame_, _num\_frames_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/scene/scene_file_writer.html#SceneFileWriter.encode_and_write_frame) [¶](https://docs.manim.community/en/stable/reference/manim.scene.scene_file_writer.SceneFileWriter.html#manim.scene.scene_file_writer.SceneFileWriter.encode_and_write_frame "Link to this definition")

For internal use only: takes a given frame in `np.ndarray` format and
write it to the stream

Parameters:

- **frame** ( [_PixelArray_](https://docs.manim.community/en/stable/reference/manim.typing.html#manim.typing.PixelArray "manim.typing.PixelArray"))

- **num\_frames** ( _int_)


Return type:

None

end\_animation( _allow\_write=False_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/scene/scene_file_writer.html#SceneFileWriter.end_animation) [¶](https://docs.manim.community/en/stable/reference/manim.scene.scene_file_writer.SceneFileWriter.html#manim.scene.scene_file_writer.SceneFileWriter.end_animation "Link to this definition")

Internally used by Manim to stop streaming to
FFMPEG gracefully.

Parameters:

**allow\_write** ( _bool_) – Whether or not to write to a video file.

Return type:

None

finish() [\[source\]](https://docs.manim.community/en/stable/_modules/manim/scene/scene_file_writer.html#SceneFileWriter.finish) [¶](https://docs.manim.community/en/stable/reference/manim.scene.scene_file_writer.SceneFileWriter.html#manim.scene.scene_file_writer.SceneFileWriter.finish "Link to this definition")

Finishes writing to the FFMPEG buffer or writing images
to output directory.
Combines the partial movie files into the
whole scene.
If save\_last\_frame is True, saves the last
frame in the default image directory.

Return type:

None

finish\_last\_section() [\[source\]](https://docs.manim.community/en/stable/_modules/manim/scene/scene_file_writer.html#SceneFileWriter.finish_last_section) [¶](https://docs.manim.community/en/stable/reference/manim.scene.scene_file_writer.SceneFileWriter.html#manim.scene.scene_file_writer.SceneFileWriter.finish_last_section "Link to this definition")

Delete current section if it is empty.

Return type:

None

flush\_cache\_directory() [\[source\]](https://docs.manim.community/en/stable/_modules/manim/scene/scene_file_writer.html#SceneFileWriter.flush_cache_directory) [¶](https://docs.manim.community/en/stable/reference/manim.scene.scene_file_writer.SceneFileWriter.html#manim.scene.scene_file_writer.SceneFileWriter.flush_cache_directory "Link to this definition")

Delete all the cached partial movie files

get\_resolution\_directory() [\[source\]](https://docs.manim.community/en/stable/_modules/manim/scene/scene_file_writer.html#SceneFileWriter.get_resolution_directory) [¶](https://docs.manim.community/en/stable/reference/manim.scene.scene_file_writer.SceneFileWriter.html#manim.scene.scene_file_writer.SceneFileWriter.get_resolution_directory "Link to this definition")

Get the name of the resolution directory directly containing
the video file.

This method gets the name of the directory that immediately contains the
video file. This name is `<height_in_pixels_of_video>p<frame_rate>`.
For example, if you are rendering an 854x480 px animation at 15fps,
the name of the directory that immediately contains the video, file
will be `480p15`.

The file structure should look something like:

```
MEDIA_DIR
    |--Tex
    |--texts
    |--videos
    |--<name_of_file_containing_scene>
        |--<height_in_pixels_of_video>p<frame_rate>
            |--<scene_name>.mp4

```

Copy to clipboard

Returns:

The name of the directory.

Return type:

`str`

init\_audio() [\[source\]](https://docs.manim.community/en/stable/_modules/manim/scene/scene_file_writer.html#SceneFileWriter.init_audio) [¶](https://docs.manim.community/en/stable/reference/manim.scene.scene_file_writer.SceneFileWriter.html#manim.scene.scene_file_writer.SceneFileWriter.init_audio "Link to this definition")

Preps the writer for adding audio to the movie.

init\_output\_directories( _scene\_name_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/scene/scene_file_writer.html#SceneFileWriter.init_output_directories) [¶](https://docs.manim.community/en/stable/reference/manim.scene.scene_file_writer.SceneFileWriter.html#manim.scene.scene_file_writer.SceneFileWriter.init_output_directories "Link to this definition")

Initialise output directories.

Notes

The directories are read from `config`, for example
`config['media_dir']`. If the target directories don’t already
exist, they will be created.

Parameters:

**scene\_name** ( [_StrPath_](https://docs.manim.community/en/stable/reference/manim.typing.html#manim.typing.StrPath "manim.typing.StrPath"))

Return type:

None

is\_already\_cached( _hash\_invocation_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/scene/scene_file_writer.html#SceneFileWriter.is_already_cached) [¶](https://docs.manim.community/en/stable/reference/manim.scene.scene_file_writer.SceneFileWriter.html#manim.scene.scene_file_writer.SceneFileWriter.is_already_cached "Link to this definition")

Will check if a file named with hash\_invocation exists.

Parameters:

**hash\_invocation** ( _str_) – The hash corresponding to an invocation to either scene.play or scene.wait.

Returns:

Whether the file exists.

Return type:

`bool`

listen\_and\_write() [\[source\]](https://docs.manim.community/en/stable/_modules/manim/scene/scene_file_writer.html#SceneFileWriter.listen_and_write) [¶](https://docs.manim.community/en/stable/reference/manim.scene.scene_file_writer.SceneFileWriter.html#manim.scene.scene_file_writer.SceneFileWriter.listen_and_write "Link to this definition")

For internal use only: blocks until new frame is available on the queue.

next\_section( _name_, _type\__, _skip\_animations_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/scene/scene_file_writer.html#SceneFileWriter.next_section) [¶](https://docs.manim.community/en/stable/reference/manim.scene.scene_file_writer.SceneFileWriter.html#manim.scene.scene_file_writer.SceneFileWriter.next_section "Link to this definition")

Create segmentation cut here.

Parameters:

- **name** ( _str_)

- **type\_** ( _str_)

- **skip\_animations** ( _bool_)


Return type:

None

open\_partial\_movie\_stream( _file\_path=None_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/scene/scene_file_writer.html#SceneFileWriter.open_partial_movie_stream) [¶](https://docs.manim.community/en/stable/reference/manim.scene.scene_file_writer.SceneFileWriter.html#manim.scene.scene_file_writer.SceneFileWriter.open_partial_movie_stream "Link to this definition")

Open a container holding a video stream.

This is used internally by Manim initialize the container holding
the video stream of a partial movie file.

Return type:

None

print\_file\_ready\_message( _file\_path_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/scene/scene_file_writer.html#SceneFileWriter.print_file_ready_message) [¶](https://docs.manim.community/en/stable/reference/manim.scene.scene_file_writer.SceneFileWriter.html#manim.scene.scene_file_writer.SceneFileWriter.print_file_ready_message "Link to this definition")

Prints the “File Ready” message to STDOUT.

save\_final\_image( _image_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/scene/scene_file_writer.html#SceneFileWriter.save_final_image) [¶](https://docs.manim.community/en/stable/reference/manim.scene.scene_file_writer.SceneFileWriter.html#manim.scene.scene_file_writer.SceneFileWriter.save_final_image "Link to this definition")

The name is a misnomer. This method saves the image
passed to it as an in the default image directory.

Parameters:

**image** ( _ndarray_) – The pixel array of the image to save.

write\_frame( _frame\_or\_renderer_, _num\_frames=1_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/scene/scene_file_writer.html#SceneFileWriter.write_frame) [¶](https://docs.manim.community/en/stable/reference/manim.scene.scene_file_writer.SceneFileWriter.html#manim.scene.scene_file_writer.SceneFileWriter.write_frame "Link to this definition")

Used internally by Manim to write a frame to
the FFMPEG input buffer.

Parameters:

- **frame\_or\_renderer** ( _np.ndarray_ _\|_ _OpenGLRenderer_) – Pixel array of the frame.

- **num\_frames** ( _int_) – The number of times to write frame.


write\_subcaption\_file() [\[source\]](https://docs.manim.community/en/stable/_modules/manim/scene/scene_file_writer.html#SceneFileWriter.write_subcaption_file) [¶](https://docs.manim.community/en/stable/reference/manim.scene.scene_file_writer.SceneFileWriter.html#manim.scene.scene_file_writer.SceneFileWriter.write_subcaption_file "Link to this definition")

Writes the subcaption file.