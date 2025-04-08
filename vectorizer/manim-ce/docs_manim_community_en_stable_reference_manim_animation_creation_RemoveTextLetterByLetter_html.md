ContentsMenuExpandLight modeDark modeAuto light/dark, in light modeAuto light/dark, in dark mode[Skip to content](https://docs.manim.community/en/stable/reference/manim.animation.creation.RemoveTextLetterByLetter.html#furo-main-content)

[Back to top](https://docs.manim.community/en/stable/reference/manim.animation.creation.RemoveTextLetterByLetter.html#)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

# RemoveTextLetterByLetter [¶](https://docs.manim.community/en/stable/reference/manim.animation.creation.RemoveTextLetterByLetter.html\#removetextletterbyletter "Link to this heading")

Qualified name: `manim.animation.creation.RemoveTextLetterByLetter`

_class_ RemoveTextLetterByLetter( _mobject=None_, _\*args_, _use\_override=True_, _\*\*kwargs_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/animation/creation.html#RemoveTextLetterByLetter) [¶](https://docs.manim.community/en/stable/reference/manim.animation.creation.RemoveTextLetterByLetter.html#manim.animation.creation.RemoveTextLetterByLetter "Link to this definition")

Bases: [`AddTextLetterByLetter`](https://docs.manim.community/en/stable/reference/manim.animation.creation.AddTextLetterByLetter.html#manim.animation.creation.AddTextLetterByLetter "manim.animation.creation.AddTextLetterByLetter")

Remove a [`Text`](https://docs.manim.community/en/stable/reference/manim.mobject.text.text_mobject.Text.html#manim.mobject.text.text_mobject.Text "manim.mobject.text.text_mobject.Text") letter by letter from the scene.

Parameters:

- **time\_per\_char** ( _float_) – Frequency of appearance of the letters.

- **tip::** ( _.._) – This is currently only possible for class:~.Text and not for class:~.MathTex

- **text** ( [_Text_](https://docs.manim.community/en/stable/reference/manim.mobject.text.text_mobject.Text.html#manim.mobject.text.text_mobject.Text "manim.mobject.text.text_mobject.Text"))

- **suspend\_mobject\_updating** ( _bool_)

- **int\_func** ( _Callable_ _\[_ _\[_ _np.ndarray_ _\]_ _,_ _np.ndarray_ _\]_)

- **rate\_func** ( _Callable_ _\[_ _\[_ _float_ _\]_ _,_ _float_ _\]_)

- **run\_time** ( _float_ _\|_ _None_)


Methods

|
|

Attributes

|     |     |
| --- | --- |
| `run_time` |  |

\_original\_\_init\_\_( _text_, _suspend\_mobject\_updating=False_, _int\_func=<ufunc'ceil'>_, _rate\_func=<functionlinear>_, _time\_per\_char=0.1_, _run\_time=None_, _reverse\_rate\_function=True_, _introducer=False_, _remover=True_, _\*\*kwargs_) [¶](https://docs.manim.community/en/stable/reference/manim.animation.creation.RemoveTextLetterByLetter.html#manim.animation.creation.RemoveTextLetterByLetter._original__init__ "Link to this definition")

Initialize self. See help(type(self)) for accurate signature.

Parameters:

- **text** ( [_Text_](https://docs.manim.community/en/stable/reference/manim.mobject.text.text_mobject.Text.html#manim.mobject.text.text_mobject.Text "manim.mobject.text.text_mobject.Text"))

- **suspend\_mobject\_updating** ( _bool_)

- **int\_func** ( _Callable_ _\[_ _\[_ _np.ndarray_ _\]_ _,_ _np.ndarray_ _\]_)

- **rate\_func** ( _Callable_ _\[_ _\[_ _float_ _\]_ _,_ _float_ _\]_)

- **time\_per\_char** ( _float_)

- **run\_time** ( _float_ _\|_ _None_)


Return type:

None