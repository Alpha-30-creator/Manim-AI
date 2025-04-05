ContentsMenuExpandLight modeDark modeAuto light/dark, in light modeAuto light/dark, in dark mode[Skip to content](https://docs.manim.community/en/stable/reference/manim.utils.config_ops.html#furo-main-content)

[Back to top](https://docs.manim.community/en/stable/reference/manim.utils.config_ops.html#)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

# config\_ops [¶](https://docs.manim.community/en/stable/reference/manim.utils.config_ops.html\#module-manim.utils.config_ops "Link to this heading")

Utilities that might be useful for configuration dictionaries.

Classes

|     |     |
| --- | --- |
| [`DictAsObject`](https://docs.manim.community/en/stable/reference/manim.utils.config_ops.DictAsObject.html#manim.utils.config_ops.DictAsObject "manim.utils.config_ops.DictAsObject") |  |

Functions

merge\_dicts\_recursively( _\*dicts_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/utils/config_ops.html#merge_dicts_recursively) [¶](https://docs.manim.community/en/stable/reference/manim.utils.config_ops.html#manim.utils.config_ops.merge_dicts_recursively "Link to this definition")

Creates a dict whose keyset is the union of all the
input dictionaries. The value for each key is based
on the first dict in the list with that key.

dicts later in the list have higher priority

When values are dictionaries, it is applied recursively

Parameters:

**dicts** ( _dict_ _\[_ _Any_ _,_ _Any_ _\]_)

Return type:

dict\[ _Any_, _Any_\]

update\_dict\_recursively( _current\_dict_, _\*others_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/utils/config_ops.html#update_dict_recursively) [¶](https://docs.manim.community/en/stable/reference/manim.utils.config_ops.html#manim.utils.config_ops.update_dict_recursively "Link to this definition")Parameters:

- **current\_dict** ( _dict_ _\[_ _Any_ _,_ _Any_ _\]_)

- **others** ( _dict_ _\[_ _Any_ _,_ _Any_ _\]_)


Return type:

None