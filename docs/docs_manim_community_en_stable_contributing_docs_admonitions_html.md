ContentsMenuExpandLight modeDark modeAuto light/dark, in light modeAuto light/dark, in dark mode[Skip to content](https://docs.manim.community/en/stable/contributing/docs/admonitions.html#furo-main-content)

[Back to top](https://docs.manim.community/en/stable/contributing/docs/admonitions.html#)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

# Adding Admonitions [¶](https://docs.manim.community/en/stable/contributing/docs/admonitions.html\#adding-admonitions "Link to this heading")

## Adding Blocks for Tip, Note, Important etc. (Admonitions) [¶](https://docs.manim.community/en/stable/contributing/docs/admonitions.html\#adding-blocks-for-tip-note-important-etc-admonitions "Link to this heading")

The following directives are called Admonitions. You
can use them to point out additional or important
information. Here are some examples:

### See also [¶](https://docs.manim.community/en/stable/contributing/docs/admonitions.html\#see-also "Link to this heading")

```
.. seealso::
     Some ideas at :mod:`~.tex_mobject`, :class:`~.Mobject`, :meth:`~.Mobject.add_updater`, :attr:`~.Mobject.depth`, :func:`~.make_config_parser`

```

Copy to clipboard

See also

Some ideas at [`tex_mobject`](https://docs.manim.community/en/stable/reference/manim.mobject.text.tex_mobject.html#module-manim.mobject.text.tex_mobject "manim.mobject.text.tex_mobject"), [`Mobject`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject"), [`add_updater()`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject.add_updater "manim.mobject.mobject.Mobject.add_updater"), [`depth`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject.depth "manim.mobject.mobject.Mobject.depth"), [`make_config_parser()`](https://docs.manim.community/en/stable/reference/manim._config.utils.html#manim._config.utils.make_config_parser "manim._config.utils.make_config_parser")

### Note [¶](https://docs.manim.community/en/stable/contributing/docs/admonitions.html\#note "Link to this heading")

```
.. note::
   A note

```

Copy to clipboard

Note

A note

### Tip [¶](https://docs.manim.community/en/stable/contributing/docs/admonitions.html\#tip "Link to this heading")

```
.. tip::
   A tip

```

Copy to clipboard

Tip

A tip

You may also use the admonition **hint**, but this is very similar
and **tip** is more commonly used in the documentation.

### Important [¶](https://docs.manim.community/en/stable/contributing/docs/admonitions.html\#important "Link to this heading")

```
.. important::
   Some important information which should be considered.

```

Copy to clipboard

Important

Some important information which should be considered.

### Warning [¶](https://docs.manim.community/en/stable/contributing/docs/admonitions.html\#warning "Link to this heading")

```
.. warning::
   Some text pointing out something that people should be warned about.

```

Copy to clipboard

Warning

Some text pointing out something that people should be warned about.

You may also use the admonitions **caution** or even **danger** if the
severity of the warning must be stressed.

### Attention [¶](https://docs.manim.community/en/stable/contributing/docs/admonitions.html\#attention "Link to this heading")

```
.. attention::
   A attention

```

Copy to clipboard

Attention

A attention

You can find further information about Admonitions here: [https://pradyunsg.me/furo/reference/admonitions/](https://pradyunsg.me/furo/reference/admonitions/)