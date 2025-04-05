ContentsMenuExpandLight modeDark modeAuto light/dark, in light modeAuto light/dark, in dark mode[Skip to content](https://docs.manim.community/en/stable/reference/manim._config.logger_utils.JSONFormatter.html#furo-main-content)

[Back to top](https://docs.manim.community/en/stable/reference/manim._config.logger_utils.JSONFormatter.html#)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

# JSONFormatter [¶](https://docs.manim.community/en/stable/reference/manim._config.logger_utils.JSONFormatter.html\#jsonformatter "Link to this heading")

Qualified name: `manim.\_config.logger\_utils.JSONFormatter`

_class_ JSONFormatter( _fmt=None_, _datefmt=None_, _style='%'_, _validate=True_, _\*_, _defaults=None_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/_config/logger_utils.html#JSONFormatter) [¶](https://docs.manim.community/en/stable/reference/manim._config.logger_utils.JSONFormatter.html#manim._config.logger_utils.JSONFormatter "Link to this definition")

Bases: `Formatter`

A formatter that outputs logs in a custom JSON format.

This class is used internally for testing purposes.

Initialize the formatter with specified format strings.

Initialize the formatter either with the specified format string, or a
default as described above. Allow for specialized date formatting with
the optional datefmt argument. If datefmt is omitted, you get an
ISO8601-like (or RFC 3339-like) format.

Use a style parameter of ‘%’, ‘{’ or ‘$’ to specify that you want to
use one of %-formatting, `str.format()` ( `{}`) formatting or
`string.Template` formatting in your format string.

Changed in version 3.2: Added the `style` parameter.

Methods

|     |     |
| --- | --- |
| [`format`](https://docs.manim.community/en/stable/reference/manim._config.logger_utils.JSONFormatter.html#manim._config.logger_utils.JSONFormatter.format "manim._config.logger_utils.JSONFormatter.format") | Format the record in a custom JSON format. |

Attributes

|     |     |
| --- | --- |
| `default_msec_format` |  |
| `default_time_format` |  |

format( _record_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/_config/logger_utils.html#JSONFormatter.format) [¶](https://docs.manim.community/en/stable/reference/manim._config.logger_utils.JSONFormatter.html#manim._config.logger_utils.JSONFormatter.format "Link to this definition")

Format the record in a custom JSON format.

Parameters:

**record** ( _LogRecord_)

Return type:

str