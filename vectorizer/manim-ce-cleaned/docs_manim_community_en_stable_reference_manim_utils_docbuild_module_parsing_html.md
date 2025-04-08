# module\_parsing [¶](https://docs.manim.community/en/stable/reference/manim.utils.docbuild.module_parsing.html\#module-manim.utils.docbuild.module_parsing "Link to this heading")

Read and parse all the Manim modules and extract documentation from them.

Type Aliases

_class_ AliasInfo [¶](https://docs.manim.community/en/stable/reference/manim.utils.docbuild.module_parsing.html#manim.utils.docbuild.module_parsing.AliasInfo "Link to this definition")

```
dict[str, str]

```

Copy to clipboard

Dictionary with a definition key containing the definition of
a `TypeAlias` as a string, and optionally a doc key containing
the documentation for that alias, if it exists.

_class_ AliasCategoryDict [¶](https://docs.manim.community/en/stable/reference/manim.utils.docbuild.module_parsing.html#manim.utils.docbuild.module_parsing.AliasCategoryDict "Link to this definition")

```xref py py-class docutils literal notranslate
dict[str, AliasInfo]
```

Dictionary which holds an [`AliasInfo`](https://docs.manim.community/en/stable/reference/manim.utils.docbuild.module_parsing.html#manim.utils.docbuild.module_parsing.AliasInfo "manim.utils.docbuild.module_parsing.AliasInfo") for every alias name in a same
category.

_class_ ModuleLevelAliasDict [¶](https://docs.manim.community/en/stable/reference/manim.utils.docbuild.module_parsing.html#manim.utils.docbuild.module_parsing.ModuleLevelAliasDict "Link to this definition")

```xref py py-class docutils literal notranslate
dict[str, AliasCategoryDict]
```

Dictionary containing every `TypeAlias` defined in a module,
classified by category in different [`AliasCategoryDict`](https://docs.manim.community/en/stable/reference/manim.utils.docbuild.module_parsing.html#manim.utils.docbuild.module_parsing.AliasCategoryDict "manim.utils.docbuild.module_parsing.AliasCategoryDict") objects.

_class_ ModuleTypeVarDict [¶](https://docs.manim.community/en/stable/reference/manim.utils.docbuild.module_parsing.html#manim.utils.docbuild.module_parsing.ModuleTypeVarDict "Link to this definition")

```
dict[str, str]

```

Copy to clipboard

Dictionary containing every `TypeVar` defined in a module.

_class_ AliasDocsDict [¶](https://docs.manim.community/en/stable/reference/manim.utils.docbuild.module_parsing.html#manim.utils.docbuild.module_parsing.AliasDocsDict "Link to this definition")

```xref py py-class docutils literal notranslate
dict[str, ModuleLevelAliasDict]
```

Dictionary which, for every module in Manim, contains documentation
about their module-level attributes which are explicitly defined as
`TypeAlias`, separating them from the rest of attributes.

_class_ DataDict [¶](https://docs.manim.community/en/stable/reference/manim.utils.docbuild.module_parsing.html#manim.utils.docbuild.module_parsing.DataDict "Link to this definition")

```
dict[str, list[str]]

```

Copy to clipboard

Type for a dictionary which, for every module, contains a list with
the names of all their DOCUMENTED module-level attributes (identified
by Sphinx via the `data` role, hence the name) which are NOT
explicitly defined as `TypeAlias`.

_class_ TypeVarDict [¶](https://docs.manim.community/en/stable/reference/manim.utils.docbuild.module_parsing.html#manim.utils.docbuild.module_parsing.TypeVarDict "Link to this definition")

```xref py py-class docutils literal notranslate
dict[str, ModuleTypeVarDict]
```

A dictionary mapping module names to dictionaries of `TypeVar` objects.

Functions

parse\_module\_attributes() [\[source\]](https://docs.manim.community/en/stable/_modules/manim/utils/docbuild/module_parsing.html#parse_module_attributes) [¶](https://docs.manim.community/en/stable/reference/manim.utils.docbuild.module_parsing.html#manim.utils.docbuild.module_parsing.parse_module_attributes "Link to this definition")

Read all files, generate Abstract Syntax Trees from them, and
extract useful information about the type aliases defined in the
files: the category they belong to, their definition and their
description, separating them from the “regular” module attributes.

Returns:

- **ALIAS\_DOCS\_DICT** ( [`AliasDocsDict`](https://docs.manim.community/en/stable/reference/manim.utils.docbuild.module_parsing.html#manim.utils.docbuild.module_parsing.AliasDocsDict "manim.utils.docbuild.module_parsing.AliasDocsDict")) – A dictionary containing the information from all the type
aliases in Manim. See [`AliasDocsDict`](https://docs.manim.community/en/stable/reference/manim.utils.docbuild.module_parsing.html#manim.utils.docbuild.module_parsing.AliasDocsDict "manim.utils.docbuild.module_parsing.AliasDocsDict") for more information.

- **DATA\_DICT** ( [`DataDict`](https://docs.manim.community/en/stable/reference/manim.utils.docbuild.module_parsing.html#manim.utils.docbuild.module_parsing.DataDict "manim.utils.docbuild.module_parsing.DataDict")) – A dictionary containing the names of all DOCUMENTED
module-level attributes which are not a `TypeAlias`.

- **TYPEVAR\_DICT** ( [`TypeVarDict`](https://docs.manim.community/en/stable/reference/manim.utils.docbuild.module_parsing.html#manim.utils.docbuild.module_parsing.TypeVarDict "manim.utils.docbuild.module_parsing.TypeVarDict")) – A dictionary containing the definitions of `TypeVar` objects,
organized by modules.


Return type:

tuple\[ [_AliasDocsDict_](https://docs.manim.community/en/stable/reference/manim.utils.docbuild.module_parsing.html#manim.utils.docbuild.module_parsing.AliasDocsDict "manim.utils.docbuild.module_parsing.AliasDocsDict"), [_DataDict_](https://docs.manim.community/en/stable/reference/manim.utils.docbuild.module_parsing.html#manim.utils.docbuild.module_parsing.DataDict "manim.utils.docbuild.module_parsing.DataDict"), [_TypeVarDict_](https://docs.manim.community/en/stable/reference/manim.utils.docbuild.module_parsing.html#manim.utils.docbuild.module_parsing.TypeVarDict "manim.utils.docbuild.module_parsing.TypeVarDict")\]