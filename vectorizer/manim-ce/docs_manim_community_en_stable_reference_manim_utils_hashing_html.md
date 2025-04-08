ContentsMenuExpandLight modeDark modeAuto light/dark, in light modeAuto light/dark, in dark mode[Skip to content](https://docs.manim.community/en/stable/reference/manim.utils.hashing.html#furo-main-content)

[Back to top](https://docs.manim.community/en/stable/reference/manim.utils.hashing.html#)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

# hashing [¶](https://docs.manim.community/en/stable/reference/manim.utils.hashing.html\#module-manim.utils.hashing "Link to this heading")

Utilities for scene caching.

Functions

get\_hash\_from\_play\_call( _scene\_object_, _camera\_object_, _animations\_list_, _current\_mobjects\_list_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/utils/hashing.html#get_hash_from_play_call) [¶](https://docs.manim.community/en/stable/reference/manim.utils.hashing.html#manim.utils.hashing.get_hash_from_play_call "Link to this definition")

Take the list of animations and a list of mobjects and output their hashes. This is meant to be used for scene.play function.

Parameters:

- **scene\_object** ( [_Scene_](https://docs.manim.community/en/stable/reference/manim.scene.scene.Scene.html#manim.scene.scene.Scene "manim.scene.scene.Scene")) – The scene object.

- **camera\_object** ( [_Camera_](https://docs.manim.community/en/stable/reference/manim.camera.camera.Camera.html#manim.camera.camera.Camera "manim.camera.camera.Camera") _\|_ _OpenGLCamera_) – The camera object used in the scene.

- **animations\_list** ( _Iterable_ _\[_ [_Animation_](https://docs.manim.community/en/stable/reference/manim.animation.animation.Animation.html#manim.animation.animation.Animation "manim.animation.animation.Animation") _\]_) – The list of animations.

- **current\_mobjects\_list** ( _Iterable_ _\[_ [_Mobject_](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject") _\]_) – The list of mobjects.


Returns:

A string concatenation of the respective hashes of camera\_object, animations\_list and current\_mobjects\_list, separated by \_.

Return type:

`str`

get\_json( _obj_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/utils/hashing.html#get_json) [¶](https://docs.manim.community/en/stable/reference/manim.utils.hashing.html#manim.utils.hashing.get_json "Link to this definition")

Recursively serialize object to JSON using the `CustomEncoder` class.

Parameters:

**obj** ( _dict_) – The dict to flatten

Returns:

The flattened object

Return type:

`str`

[**The AI Agent that gets your codebase** Copilot & Cursor letting you down? Try Augment. **Install Now**](https://server.ethicalads.io/proxy/click/8458/019600e2-a8ec-7943-ac10-cb72b1ef49d7/)

[Ads by EthicalAds](https://www.ethicalads.io/advertisers/?ref=ea-text)

![](https://server.ethicalads.io/proxy/view/8458/019600e2-a8ec-7943-ac10-cb72b1ef49d7/)