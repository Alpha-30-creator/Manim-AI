ContentsMenuExpandLight modeDark modeAuto light/dark, in light modeAuto light/dark, in dark mode[Skip to content](https://docs.manim.community/en/stable/reference/manim.utils.docbuild.manim_directive.ManimDirective.html#furo-main-content)

[Back to top](https://docs.manim.community/en/stable/reference/manim.utils.docbuild.manim_directive.ManimDirective.html#)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

# ManimDirective [¶](https://docs.manim.community/en/stable/reference/manim.utils.docbuild.manim_directive.ManimDirective.html\#manimdirective "Link to this heading")

Qualified name: `manim.utils.docbuild.manim\_directive.ManimDirective`

_class_ ManimDirective( _name_, _arguments_, _options_, _content_, _lineno_, _content\_offset_, _block\_text_, _state_, _state\_machine_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/utils/docbuild/manim_directive.html#ManimDirective) [¶](https://docs.manim.community/en/stable/reference/manim.utils.docbuild.manim_directive.ManimDirective.html#manim.utils.docbuild.manim_directive.ManimDirective "Link to this definition")

Bases: `Directive`

The manim directive, rendering videos while building
the documentation.

See the module docstring for documentation.

Methods

|     |     |
| --- | --- |
| `run` |  |

Attributes

|     |     |
| --- | --- |
| [`final_argument_whitespace`](https://docs.manim.community/en/stable/reference/manim.utils.docbuild.manim_directive.ManimDirective.html#manim.utils.docbuild.manim_directive.ManimDirective.final_argument_whitespace "manim.utils.docbuild.manim_directive.ManimDirective.final_argument_whitespace") | May the final argument contain whitespace? |
| [`has_content`](https://docs.manim.community/en/stable/reference/manim.utils.docbuild.manim_directive.ManimDirective.html#manim.utils.docbuild.manim_directive.ManimDirective.has_content "manim.utils.docbuild.manim_directive.ManimDirective.has_content") | May the directive have content? |
| [`option_spec`](https://docs.manim.community/en/stable/reference/manim.utils.docbuild.manim_directive.ManimDirective.html#manim.utils.docbuild.manim_directive.ManimDirective.option_spec "manim.utils.docbuild.manim_directive.ManimDirective.option_spec") | Mapping of option names to validator functions. |
| [`optional_arguments`](https://docs.manim.community/en/stable/reference/manim.utils.docbuild.manim_directive.ManimDirective.html#manim.utils.docbuild.manim_directive.ManimDirective.optional_arguments "manim.utils.docbuild.manim_directive.ManimDirective.optional_arguments") | Number of optional arguments after the required arguments. |
| [`required_arguments`](https://docs.manim.community/en/stable/reference/manim.utils.docbuild.manim_directive.ManimDirective.html#manim.utils.docbuild.manim_directive.ManimDirective.required_arguments "manim.utils.docbuild.manim_directive.ManimDirective.required_arguments") | Number of required directive arguments. |

final\_argument\_whitespace _=True_ [¶](https://docs.manim.community/en/stable/reference/manim.utils.docbuild.manim_directive.ManimDirective.html#manim.utils.docbuild.manim_directive.ManimDirective.final_argument_whitespace "Link to this definition")

May the final argument contain whitespace?

has\_content _=True_ [¶](https://docs.manim.community/en/stable/reference/manim.utils.docbuild.manim_directive.ManimDirective.html#manim.utils.docbuild.manim_directive.ManimDirective.has_content "Link to this definition")

May the directive have content?

option\_spec _={'hide\_source':<class'bool'>,'no\_autoplay':<class'bool'>,'quality':<functionManimDirective.<lambda>>,'ref\_classes':<functionManimDirective.<lambda>>,'ref\_functions':<functionManimDirective.<lambda>>,'ref\_methods':<functionManimDirective.<lambda>>,'ref\_modules':<functionManimDirective.<lambda>>,'save\_as\_gif':<class'bool'>,'save\_last\_frame':<class'bool'>}_ [¶](https://docs.manim.community/en/stable/reference/manim.utils.docbuild.manim_directive.ManimDirective.html#manim.utils.docbuild.manim_directive.ManimDirective.option_spec "Link to this definition")

Mapping of option names to validator functions.

optional\_arguments _=0_ [¶](https://docs.manim.community/en/stable/reference/manim.utils.docbuild.manim_directive.ManimDirective.html#manim.utils.docbuild.manim_directive.ManimDirective.optional_arguments "Link to this definition")

Number of optional arguments after the required arguments.

required\_arguments _=1_ [¶](https://docs.manim.community/en/stable/reference/manim.utils.docbuild.manim_directive.ManimDirective.html#manim.utils.docbuild.manim_directive.ManimDirective.required_arguments "Link to this definition")

Number of required directive arguments.