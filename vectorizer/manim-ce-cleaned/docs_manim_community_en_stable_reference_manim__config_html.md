# \_config [¶](https://docs.manim.community/en/stable/reference/manim._config.html\#module-manim._config "Link to this heading")

Set the global config and logger.

Functions

tempconfig( _temp_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/_config.html#tempconfig) [¶](https://docs.manim.community/en/stable/reference/manim._config.html#manim._config.tempconfig "Link to this definition")

Context manager that temporarily modifies the global `config` object.

Inside the `with` statement, the modified config will be used. After
context manager exits, the config will be restored to its original state.

Parameters:

**temp** ( [_ManimConfig_](https://docs.manim.community/en/stable/reference/manim._config.utils.ManimConfig.html#manim._config.utils.ManimConfig "manim._config.utils.ManimConfig") _\|_ _dict_ _\[_ _str_ _,_ _Any_ _\]_) – Object whose keys will be used to temporarily update the global
`config`.

Return type:

_Generator_\[None, None, None\]

Examples

Use `with tempconfig({...})` to temporarily change the default values of
certain config options.

```
>>> config["frame_height"]
8.0
>>> with tempconfig({"frame_height": 100.0}):
...     print(config["frame_height"])
100.0
>>> config["frame_height"]
8.0

```

Copy to clipboard