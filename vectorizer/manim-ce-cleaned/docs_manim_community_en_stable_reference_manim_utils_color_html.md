# color [¶](https://docs.manim.community/en/stable/reference/manim.utils.color.html\#module-manim.utils.color "Link to this heading")

Utilities for working with colors and predefined color constants.

## Color data structure [¶](https://docs.manim.community/en/stable/reference/manim.utils.color.html\#color-data-structure "Link to this heading")

|     |     |
| --- | --- |
| [`core`](https://docs.manim.community/en/stable/reference/manim.utils.color.core.html#module-manim.utils.color.core "manim.utils.color.core") | Manim's (internal) color data structure and some utilities for color conversion. |

## Predefined colors [¶](https://docs.manim.community/en/stable/reference/manim.utils.color.html\#predefined-colors "Link to this heading")

There are several predefined colors available in Manim:

- The colors listed in [`color.manim_colors`](https://docs.manim.community/en/stable/reference/manim.utils.color.manim_colors.html#module-manim.utils.color.manim_colors "manim.utils.color.manim_colors") are loaded into
Manim’s global name space.

- The colors in [`color.AS2700`](https://docs.manim.community/en/stable/reference/manim.utils.color.AS2700.html#module-manim.utils.color.AS2700 "manim.utils.color.AS2700"), [`color.BS381`](https://docs.manim.community/en/stable/reference/manim.utils.color.BS381.html#module-manim.utils.color.BS381 "manim.utils.color.BS381"),
[`color.DVIPSNAMES`](https://docs.manim.community/en/stable/reference/manim.utils.color.DVIPSNAMES.html#module-manim.utils.color.DVIPSNAMES "manim.utils.color.DVIPSNAMES"), [`color.SVGNAMES`](https://docs.manim.community/en/stable/reference/manim.utils.color.SVGNAMES.html#module-manim.utils.color.SVGNAMES "manim.utils.color.SVGNAMES"), [`color.X11`](https://docs.manim.community/en/stable/reference/manim.utils.color.X11.html#module-manim.utils.color.X11 "manim.utils.color.X11") and
[`color.XKCD`](https://docs.manim.community/en/stable/reference/manim.utils.color.XKCD.html#module-manim.utils.color.XKCD "manim.utils.color.XKCD") need to be accessed via their module (which are available
in Manim’s global name space), or imported separately. For example:





```
>>> from manim import XKCD
>>> XKCD.AVOCADO
ManimColor('#90B134')

```

Copy to clipboard



Or, alternatively:





```
>>> from manim.utils.color.XKCD import AVOCADO
>>> AVOCADO
ManimColor('#90B134')

```

Copy to clipboard


The following modules contain the predefined color constants:

|     |     |
| --- | --- |
| [`manim_colors`](https://docs.manim.community/en/stable/reference/manim.utils.color.manim_colors.html#module-manim.utils.color.manim_colors "manim.utils.color.manim_colors") | Colors included in the global name space. |
| [`AS2700`](https://docs.manim.community/en/stable/reference/manim.utils.color.AS2700.html#module-manim.utils.color.AS2700 "manim.utils.color.AS2700") | Australian Color Standard |
| [`BS381`](https://docs.manim.community/en/stable/reference/manim.utils.color.BS381.html#module-manim.utils.color.BS381 "manim.utils.color.BS381") | British Color Standard |
| [`DVIPSNAMES`](https://docs.manim.community/en/stable/reference/manim.utils.color.DVIPSNAMES.html#module-manim.utils.color.DVIPSNAMES "manim.utils.color.DVIPSNAMES") | dvips Colors |
| [`SVGNAMES`](https://docs.manim.community/en/stable/reference/manim.utils.color.SVGNAMES.html#module-manim.utils.color.SVGNAMES "manim.utils.color.SVGNAMES") | SVG 1.1 Colors |
| [`XKCD`](https://docs.manim.community/en/stable/reference/manim.utils.color.XKCD.html#module-manim.utils.color.XKCD "manim.utils.color.XKCD") | Colors from the XKCD Color Name Survey |
| [`X11`](https://docs.manim.community/en/stable/reference/manim.utils.color.X11.html#module-manim.utils.color.X11 "manim.utils.color.X11") | X11 Colors |

[**Watch Our Demo** video to see firsthand how to upgrade your site with end-to-end AI Search.](https://server.ethicalads.io/proxy/click/8294/019600e7-8ff6-75d1-a0c4-cbf072d6581b/)

[Ads by EthicalAds](https://www.ethicalads.io/advertisers/topics/frontend-web/?ref=ea-text)

![](https://server.ethicalads.io/proxy/view/8294/019600e7-8ff6-75d1-a0c4-cbf072d6581b/)