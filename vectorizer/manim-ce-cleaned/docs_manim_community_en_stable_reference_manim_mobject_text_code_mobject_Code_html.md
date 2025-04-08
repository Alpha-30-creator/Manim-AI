# Code [¶](https://docs.manim.community/en/stable/reference/manim.mobject.text.code_mobject.Code.html\#code "Link to this heading")

Qualified name: `manim.mobject.text.code\_mobject.Code`

_class_ Code( _code\_file=None_, _code\_string=None_, _language=None_, _formatter\_style='vim'_, _tab\_width=4_, _add\_line\_numbers=True_, _line\_numbers\_from=1_, _background='rectangle'_, _background\_config=None_, _paragraph\_config=None_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/mobject/text/code_mobject.html#Code) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.text.code_mobject.Code.html#manim.mobject.text.code_mobject.Code "Link to this definition")

Bases: [`VMobject`](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject "manim.mobject.types.vectorized_mobject.VMobject")

A highlighted source code listing.

Examples

Normal usage:

```
listing = Code(
    "helloworldcpp.cpp",
    tab_width=4,
    formatter_style="emacs",
    background="window",
    language="cpp",
    background_config={"stroke_color": WHITE},
    paragraph_config={"font": "Noto Sans Mono"},
)

```

Copy to clipboard

We can also render code passed as a string. As the automatic language
detection can be a bit flaky, it is recommended to specify the language
explicitly:

Example: CodeFromString [¶](https://docs.manim.community/en/stable/reference/manim.mobject.text.code_mobject.Code.html#codefromstring)

![../_images/CodeFromString-1.png](https://docs.manim.community/en/stable/_images/CodeFromString-1.png)

```
from manim import *

class CodeFromString(Scene):
    def construct(self):
        code = '''from manim import Scene, Square

class FadeInSquare(Scene):
    def construct(self):
        s = Square()
        self.play(FadeIn(s))
        self.play(s.animate.scale(2))
        self.wait()'''

        rendered_code = Code(
            code_string=code,
            language="python",
            background="window",
            background_config={"stroke_color": "maroon"},
        )
        self.add(rendered_code)

```

Copy to clipboard

Make interactive

Parameters:

- **code\_file** ( [_StrPath_](https://docs.manim.community/en/stable/reference/manim.typing.html#manim.typing.StrPath "manim.typing.StrPath") _\|_ _None_) – The path to the code file to display.

- **code\_string** ( _str_ _\|_ _None_) – Alternatively, the code string to display.

- **language** ( _str_ _\|_ _None_) – The programming language of the code. If not specified, it will be
guessed from the file extension or the code itself.

- **formatter\_style** ( _str_) – The style to use for the code highlighting. Defaults to `"vim"`.
A list of all available styles can be obtained by calling
[`Code.get_styles_list()`](https://docs.manim.community/en/stable/reference/manim.mobject.text.code_mobject.Code.html#manim.mobject.text.code_mobject.Code.get_styles_list "manim.mobject.text.code_mobject.Code.get_styles_list").

- **tab\_width** ( _int_) – The width of a tab character in spaces. Defaults to 4.

- **add\_line\_numbers** ( _bool_) – Whether to display line numbers. Defaults to `True`.

- **line\_numbers\_from** ( _int_) – The first line number to display. Defaults to 1.

- **background** ( _Literal_ _\[_ _'rectangle'_ _,_ _'window'_ _\]_) – The type of background to use. Can be either `"rectangle"` (the
default) or `"window"`.

- **background\_config** ( _dict_ _\[_ _str_ _,_ _Any_ _\]_ _\|_ _None_) – Keyword arguments passed to the background constructor. Default
settings are stored in the class attribute
`default_background_config` (which can also be modified
directly).

- **paragraph\_config** ( _dict_ _\[_ _str_ _,_ _Any_ _\]_ _\|_ _None_) – Keyword arguments passed to the constructor of the
[`Paragraph`](https://docs.manim.community/en/stable/reference/manim.mobject.text.text_mobject.Paragraph.html#manim.mobject.text.text_mobject.Paragraph "manim.mobject.text.text_mobject.Paragraph") objects holding the code, and the line
numbers. Default settings are stored in the class attribute
`default_paragraph_config` (which can also be modified
directly).


Methods

|     |     |
| --- | --- |
| [`get_styles_list`](https://docs.manim.community/en/stable/reference/manim.mobject.text.code_mobject.Code.html#manim.mobject.text.code_mobject.Code.get_styles_list "manim.mobject.text.code_mobject.Code.get_styles_list") | Get the list of all available formatter styles. |

Attributes

|     |     |
| --- | --- |
| `animate` | Used to animate the application of any method of `self`. |
| `animation_overrides` |  |
| `color` |  |
| `default_background_config` |  |
| `default_paragraph_config` |  |
| `depth` | The depth of the mobject. |
| `fill_color` | If there are multiple colors (for gradient) this returns the first one |
| `height` | The height of the mobject. |
| `n_points_per_curve` |  |
| `sheen_factor` |  |
| `stroke_color` |  |
| `width` | The width of the mobject. |

\_original\_\_init\_\_( _code\_file=None_, _code\_string=None_, _language=None_, _formatter\_style='vim'_, _tab\_width=4_, _add\_line\_numbers=True_, _line\_numbers\_from=1_, _background='rectangle'_, _background\_config=None_, _paragraph\_config=None_) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.text.code_mobject.Code.html#manim.mobject.text.code_mobject.Code._original__init__ "Link to this definition")

Initialize self. See help(type(self)) for accurate signature.

Parameters:

- **code\_file** ( [_StrPath_](https://docs.manim.community/en/stable/reference/manim.typing.html#manim.typing.StrPath "manim.typing.StrPath") _\|_ _None_)

- **code\_string** ( _str_ _\|_ _None_)

- **language** ( _str_ _\|_ _None_)

- **formatter\_style** ( _str_)

- **tab\_width** ( _int_)

- **add\_line\_numbers** ( _bool_)

- **line\_numbers\_from** ( _int_)

- **background** ( _Literal_ _\[_ _'rectangle'_ _,_ _'window'_ _\]_)

- **background\_config** ( _dict_ _\[_ _str_ _,_ _Any_ _\]_ _\|_ _None_)

- **paragraph\_config** ( _dict_ _\[_ _str_ _,_ _Any_ _\]_ _\|_ _None_)


_classmethod_ get\_styles\_list() [\[source\]](https://docs.manim.community/en/stable/_modules/manim/mobject/text/code_mobject.html#Code.get_styles_list) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.text.code_mobject.Code.html#manim.mobject.text.code_mobject.Code.get_styles_list "Link to this definition")

Get the list of all available formatter styles.

Return type:

list\[str\]