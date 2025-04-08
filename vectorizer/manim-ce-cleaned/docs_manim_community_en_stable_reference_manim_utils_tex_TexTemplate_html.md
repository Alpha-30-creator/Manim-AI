# TexTemplate [¶](https://docs.manim.community/en/stable/reference/manim.utils.tex.TexTemplate.html\#textemplate "Link to this heading")

Qualified name: `manim.utils.tex.TexTemplate`

_class_ TexTemplate( _tex\_compiler='latex'_, _description=''_, _output\_format='.dvi'_, _documentclass='\\\documentclass\[preview\]{standalone}'_, _preamble='\\\usepackage\[english\]{babel}\\n\\\usepackage{amsmath}\\n\\\usepackage{amssymb}'_, _placeholder\_text='YourTextHere'_, _post\_doc\_commands=''_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/utils/tex.html#TexTemplate) [¶](https://docs.manim.community/en/stable/reference/manim.utils.tex.TexTemplate.html#manim.utils.tex.TexTemplate "Link to this definition")

Bases: `object`

TeX templates are used to create `Tex` and `MathTex` objects.

Methods

|     |     |
| --- | --- |
| [`add_to_document`](https://docs.manim.community/en/stable/reference/manim.utils.tex.TexTemplate.html#manim.utils.tex.TexTemplate.add_to_document "manim.utils.tex.TexTemplate.add_to_document") | Adds text to the TeX template just after begin{document}, e.g. `\boldmath`. |
| [`add_to_preamble`](https://docs.manim.community/en/stable/reference/manim.utils.tex.TexTemplate.html#manim.utils.tex.TexTemplate.add_to_preamble "manim.utils.tex.TexTemplate.add_to_preamble") | Adds text to the TeX template's preamble (e.g. definitions, packages). |
| [`copy`](https://docs.manim.community/en/stable/reference/manim.utils.tex.TexTemplate.html#manim.utils.tex.TexTemplate.copy "manim.utils.tex.TexTemplate.copy") | Create a deep copy of the TeX template instance. |
| [`from_file`](https://docs.manim.community/en/stable/reference/manim.utils.tex.TexTemplate.html#manim.utils.tex.TexTemplate.from_file "manim.utils.tex.TexTemplate.from_file") | Create an instance by reading the content of a file. |
| [`get_texcode_for_expression`](https://docs.manim.community/en/stable/reference/manim.utils.tex.TexTemplate.html#manim.utils.tex.TexTemplate.get_texcode_for_expression "manim.utils.tex.TexTemplate.get_texcode_for_expression") | Inserts expression verbatim into TeX template. |
| [`get_texcode_for_expression_in_env`](https://docs.manim.community/en/stable/reference/manim.utils.tex.TexTemplate.html#manim.utils.tex.TexTemplate.get_texcode_for_expression_in_env "manim.utils.tex.TexTemplate.get_texcode_for_expression_in_env") | Inserts expression into TeX template wrapped in `\begin{environment}` and `\end{environment}`. |

Attributes

|     |     |
| --- | --- |
| [`body`](https://docs.manim.community/en/stable/reference/manim.utils.tex.TexTemplate.html#manim.utils.tex.TexTemplate.body "manim.utils.tex.TexTemplate.body") | The entire TeX template. |
| [`description`](https://docs.manim.community/en/stable/reference/manim.utils.tex.TexTemplate.html#manim.utils.tex.TexTemplate.description "manim.utils.tex.TexTemplate.description") | A description of the template |
| [`documentclass`](https://docs.manim.community/en/stable/reference/manim.utils.tex.TexTemplate.html#manim.utils.tex.TexTemplate.documentclass "manim.utils.tex.TexTemplate.documentclass") | The command defining the documentclass, e.g. `\documentclass[preview]{standalone}`. |
| [`output_format`](https://docs.manim.community/en/stable/reference/manim.utils.tex.TexTemplate.html#manim.utils.tex.TexTemplate.output_format "manim.utils.tex.TexTemplate.output_format") | The output format resulting from compilation, e.g. `.dvi` or `.pdf`. |
| [`placeholder_text`](https://docs.manim.community/en/stable/reference/manim.utils.tex.TexTemplate.html#manim.utils.tex.TexTemplate.placeholder_text "manim.utils.tex.TexTemplate.placeholder_text") | Text in the document that will be replaced by the expression to be rendered. |
| [`post_doc_commands`](https://docs.manim.community/en/stable/reference/manim.utils.tex.TexTemplate.html#manim.utils.tex.TexTemplate.post_doc_commands "manim.utils.tex.TexTemplate.post_doc_commands") | Text (definitions, commands) to be inserted at right after `\begin{document}`, e.g. `\boldmath`. |
| [`preamble`](https://docs.manim.community/en/stable/reference/manim.utils.tex.TexTemplate.html#manim.utils.tex.TexTemplate.preamble "manim.utils.tex.TexTemplate.preamble") | The document's preamble, i.e. the part between `\documentclass` and `\begin{document}`. |
| [`tex_compiler`](https://docs.manim.community/en/stable/reference/manim.utils.tex.TexTemplate.html#manim.utils.tex.TexTemplate.tex_compiler "manim.utils.tex.TexTemplate.tex_compiler") | The TeX compiler to be used, e.g. `latex`, `pdflatex` or `lualatex`. |

Parameters:

- **tex\_compiler** ( _str_)

- **description** ( _str_)

- **output\_format** ( _str_)

- **documentclass** ( _str_)

- **preamble** ( _str_)

- **placeholder\_text** ( _str_)

- **post\_doc\_commands** ( _str_)


\_body _:str_ _=''_ [¶](https://docs.manim.community/en/stable/reference/manim.utils.tex.TexTemplate.html#manim.utils.tex.TexTemplate._body "Link to this definition")

A custom body, can be set from a file.

add\_to\_document( _txt_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/utils/tex.html#TexTemplate.add_to_document) [¶](https://docs.manim.community/en/stable/reference/manim.utils.tex.TexTemplate.html#manim.utils.tex.TexTemplate.add_to_document "Link to this definition")

Adds text to the TeX template just after begin{document}, e.g. `\boldmath`.

Parameters:

**txt** ( _str_) – String containing the text to be added.

Return type:

Self

add\_to\_preamble( _txt_, _prepend=False_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/utils/tex.html#TexTemplate.add_to_preamble) [¶](https://docs.manim.community/en/stable/reference/manim.utils.tex.TexTemplate.html#manim.utils.tex.TexTemplate.add_to_preamble "Link to this definition")

Adds text to the TeX template’s preamble (e.g. definitions, packages). Text can be inserted at the beginning or at the end of the preamble.

Parameters:

- **txt** ( _str_) – String containing the text to be added, e.g. `\usepackage{hyperref}`.

- **prepend** ( _bool_) – Whether the text should be added at the beginning of the preamble, i.e. right after `\documentclass`.
Default is to add it at the end of the preamble, i.e. right before `\begin{document}`.


Return type:

Self

_property_ body _:str_ [¶](https://docs.manim.community/en/stable/reference/manim.utils.tex.TexTemplate.html#manim.utils.tex.TexTemplate.body "Link to this definition")

The entire TeX template.

copy() [\[source\]](https://docs.manim.community/en/stable/_modules/manim/utils/tex.html#TexTemplate.copy) [¶](https://docs.manim.community/en/stable/reference/manim.utils.tex.TexTemplate.html#manim.utils.tex.TexTemplate.copy "Link to this definition")

Create a deep copy of the TeX template instance.

Return type:

Self

description _:str_ _=''_ [¶](https://docs.manim.community/en/stable/reference/manim.utils.tex.TexTemplate.html#manim.utils.tex.TexTemplate.description "Link to this definition")

A description of the template

documentclass _:str_ _='\\\documentclass\[preview\]{standalone}'_ [¶](https://docs.manim.community/en/stable/reference/manim.utils.tex.TexTemplate.html#manim.utils.tex.TexTemplate.documentclass "Link to this definition")

The command defining the documentclass, e.g. `\documentclass[preview]{standalone}`.

_classmethod_ from\_file( _file='tex\_template.tex'_, _\*\*kwargs_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/utils/tex.html#TexTemplate.from_file) [¶](https://docs.manim.community/en/stable/reference/manim.utils.tex.TexTemplate.html#manim.utils.tex.TexTemplate.from_file "Link to this definition")

Create an instance by reading the content of a file.

Using the `add_to_preamble` and `add_to_document` methods on this instance
will have no effect, as the body is read from the file.

Parameters:

- **file** ( [_StrPath_](https://docs.manim.community/en/stable/reference/manim.typing.html#manim.typing.StrPath "manim.typing.StrPath"))

- **kwargs** ( _Any_)


Return type:

Self

get\_texcode\_for\_expression( _expression_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/utils/tex.html#TexTemplate.get_texcode_for_expression) [¶](https://docs.manim.community/en/stable/reference/manim.utils.tex.TexTemplate.html#manim.utils.tex.TexTemplate.get_texcode_for_expression "Link to this definition")

Inserts expression verbatim into TeX template.

Parameters:

**expression** ( _str_) – The string containing the expression to be typeset, e.g. `$\sqrt{2}$`

Returns:

LaTeX code based on current template, containing the given `expression` and ready for typesetting

Return type:

`str`

get\_texcode\_for\_expression\_in\_env( _expression_, _environment_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/utils/tex.html#TexTemplate.get_texcode_for_expression_in_env) [¶](https://docs.manim.community/en/stable/reference/manim.utils.tex.TexTemplate.html#manim.utils.tex.TexTemplate.get_texcode_for_expression_in_env "Link to this definition")

Inserts expression into TeX template wrapped in `\begin{environment}` and `\end{environment}`.

Parameters:

- **expression** ( _str_) – The string containing the expression to be typeset, e.g. `$\sqrt{2}$`.

- **environment** ( _str_) – The string containing the environment in which the expression should be typeset, e.g. `align*`.


Returns:

LaTeX code based on template, containing the given expression inside its environment, ready for typesetting

Return type:

`str`

output\_format _:str_ _='.dvi'_ [¶](https://docs.manim.community/en/stable/reference/manim.utils.tex.TexTemplate.html#manim.utils.tex.TexTemplate.output_format "Link to this definition")

The output format resulting from compilation, e.g. `.dvi` or `.pdf`.

placeholder\_text _:str_ _='YourTextHere'_ [¶](https://docs.manim.community/en/stable/reference/manim.utils.tex.TexTemplate.html#manim.utils.tex.TexTemplate.placeholder_text "Link to this definition")

Text in the document that will be replaced by the expression to be rendered.

post\_doc\_commands _:str_ _=''_ [¶](https://docs.manim.community/en/stable/reference/manim.utils.tex.TexTemplate.html#manim.utils.tex.TexTemplate.post_doc_commands "Link to this definition")

Text (definitions, commands) to be inserted at right after `\begin{document}`, e.g. `\boldmath`.

preamble _:str_ _='\\\usepackage\[english\]{babel}\\n\\\usepackage{amsmath}\\n\\\usepackage{amssymb}'_ [¶](https://docs.manim.community/en/stable/reference/manim.utils.tex.TexTemplate.html#manim.utils.tex.TexTemplate.preamble "Link to this definition")

The document’s preamble, i.e. the part between `\documentclass` and `\begin{document}`.

tex\_compiler _:str_ _='latex'_ [¶](https://docs.manim.community/en/stable/reference/manim.utils.tex.TexTemplate.html#manim.utils.tex.TexTemplate.tex_compiler "Link to this definition")

The TeX compiler to be used, e.g. `latex`, `pdflatex` or `lualatex`.

[Maintain search performance with GenAI. **Read On**](https://server.ethicalads.io/proxy/click/8443/019600e7-72eb-71c2-ac5d-c527ad001c69/)

[Ads by EthicalAds](https://www.ethicalads.io/advertisers/topics/backend-web/?ref=ea-text)

![](https://server.ethicalads.io/proxy/view/8443/019600e7-72eb-71c2-ac5d-c527ad001c69/)