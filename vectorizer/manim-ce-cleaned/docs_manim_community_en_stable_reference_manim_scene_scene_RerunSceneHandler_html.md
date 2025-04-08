# RerunSceneHandler [¶](https://docs.manim.community/en/stable/reference/manim.scene.scene.RerunSceneHandler.html\#rerunscenehandler "Link to this heading")

Qualified name: `manim.scene.scene.RerunSceneHandler`

_class_ RerunSceneHandler( _queue_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/scene/scene.html#RerunSceneHandler) [¶](https://docs.manim.community/en/stable/reference/manim.scene.scene.RerunSceneHandler.html#manim.scene.scene.RerunSceneHandler "Link to this definition")

Bases: `FileSystemEventHandler`

A class to handle rerunning a Scene after the input file is modified.

Methods

|     |     |
| --- | --- |
| [`on_modified`](https://docs.manim.community/en/stable/reference/manim.scene.scene.RerunSceneHandler.html#manim.scene.scene.RerunSceneHandler.on_modified "manim.scene.scene.RerunSceneHandler.on_modified") | Called when a file or directory is modified. |

on\_modified( _event_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/scene/scene.html#RerunSceneHandler.on_modified) [¶](https://docs.manim.community/en/stable/reference/manim.scene.scene.RerunSceneHandler.html#manim.scene.scene.RerunSceneHandler.on_modified "Link to this definition")

Called when a file or directory is modified.

Parameters:

**event** ( `DirModifiedEvent` or `FileModifiedEvent`) – Event representing file/directory modification.