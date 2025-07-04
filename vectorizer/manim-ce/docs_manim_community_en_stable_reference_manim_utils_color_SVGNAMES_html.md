ContentsMenuExpandLight modeDark modeAuto light/dark, in light modeAuto light/dark, in dark mode[Skip to content](https://docs.manim.community/en/stable/reference/manim.utils.color.SVGNAMES.html#furo-main-content)

[Back to top](https://docs.manim.community/en/stable/reference/manim.utils.color.SVGNAMES.html#)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

# SVGNAMES [¶](https://docs.manim.community/en/stable/reference/manim.utils.color.SVGNAMES.html\#module-manim.utils.color.SVGNAMES "Link to this heading")

SVG 1.1 Colors

This module contains the colors defined in the SVG 1.1 specification, which are commonly
accessed as named colors in LaTeX via the `\usepackage[svgnames]{xcolor}` package.

To use the colors from this list, access them directly from the module (which
is exposed to Manim’s global name space):

```
>>> from manim import SVGNAMES
>>> SVGNAMES.LIGHTCORAL
ManimColor('#EF7F7F')

```

Copy to clipboard

## List of Color Constants [¶](https://docs.manim.community/en/stable/reference/manim.utils.color.SVGNAMES.html\#list-of-color-constants "Link to this heading")

These hex values are derived from those specified in the `xcolor` package
documentation (see [https://ctan.org/pkg/xcolor](https://ctan.org/pkg/xcolor)):

| Color Name | RGB Hex Code | Color Name | RGB Hex Code |
| --- | --- | --- | --- |
| `ALICEBLUE` | `#EFF7FF` | `ANTIQUEWHITE` | `#F9EAD7` |
| `AQUA` | `#00FFFF` | `AQUAMARINE` | `#7EFFD3` |
| `AZURE` | `#EFFFFF` | `BEIGE` | `#F4F4DC` |
| `BISQUE` | `#FFE3C4` | `BLACK` | `#000000` |
| `BLANCHEDALMOND` | `#FFEACD` | `BLUE` | `#0000FF` |
| `BLUEVIOLET` | `#892BE2` | `BROWN` | `#A52A2A` |
| `BURLYWOOD` | `#DDB787` | `CADETBLUE` | `#5E9EA0` |
| `CHARTREUSE` | `#7EFF00` | `CHOCOLATE` | `#D2681D` |
| `CORAL` | `#FF7E4F` | `CORNFLOWERBLUE` | `#6395ED` |
| `CORNSILK` | `#FFF7DC` | `CRIMSON` | `#DC143B` |
| `CYAN` | `#00FFFF` | `DARKBLUE` | `#00008A` |
| `DARKCYAN` | `#008A8A` | `DARKGOLDENROD` | `#B7850B` |
| `DARKGRAY` | `#A9A9A9` | `DARKGREEN` | `#006300` |
| `DARKGREY` | `#A9A9A9` | `DARKKHAKI` | `#BCB66B` |
| `DARKMAGENTA` | `#8A008A` | `DARKOLIVEGREEN` | `#546B2F` |
| `DARKORANGE` | `#FF8C00` | `DARKORCHID` | `#9931CC` |
| `DARKRED` | `#8A0000` | `DARKSALMON` | `#E8967A` |
| `DARKSEAGREEN` | `#8EBB8E` | `DARKSLATEBLUE` | `#483D8A` |
| `DARKSLATEGRAY` | `#2F4F4F` | `DARKSLATEGREY` | `#2F4F4F` |
| `DARKTURQUOISE` | `#00CED1` | `DARKVIOLET` | `#9300D3` |
| `DEEPPINK` | `#FF1492` | `DEEPSKYBLUE` | `#00BFFF` |
| `DIMGRAY` | `#686868` | `DIMGREY` | `#686868` |
| `DODGERBLUE` | `#1D90FF` | `FIREBRICK` | `#B12121` |
| `FLORALWHITE` | `#FFF9EF` | `FORESTGREEN` | `#218A21` |
| `FUCHSIA` | `#FF00FF` | `GAINSBORO` | `#DCDCDC` |
| `GHOSTWHITE` | `#F7F7FF` | `GOLD` | `#FFD700` |
| `GOLDENROD` | `#DAA51F` | `GRAY` | `#7F7F7F` |
| `GREEN` | `#007F00` | `GREENYELLOW` | `#ADFF2F` |
| `GREY` | `#7F7F7F` | `HONEYDEW` | `#EFFFEF` |
| `HOTPINK` | `#FF68B3` | `INDIANRED` | `#CD5B5B` |
| `INDIGO` | `#4A0082` | `IVORY` | `#FFFFEF` |
| `KHAKI` | `#EFE58C` | `LAVENDER` | `#E5E5F9` |
| `LAVENDERBLUSH` | `#FFEFF4` | `LAWNGREEN` | `#7CFC00` |
| `LEMONCHIFFON` | `#FFF9CD` | `LIGHTBLUE` | `#ADD8E5` |
| `LIGHTCORAL` | `#EF7F7F` | `LIGHTCYAN` | `#E0FFFF` |
| `LIGHTGOLDENROD` | `#EDDD82` | `LIGHTGOLDENRODYELLOW` | `#F9F9D2` |
| `LIGHTGRAY` | `#D3D3D3` | `LIGHTGREEN` | `#90ED90` |
| `LIGHTGREY` | `#D3D3D3` | `LIGHTPINK` | `#FFB5C0` |
| `LIGHTSALMON` | `#FFA07A` | `LIGHTSEAGREEN` | `#1FB1AA` |
| `LIGHTSKYBLUE` | `#87CEF9` | `LIGHTSLATEBLUE` | `#8470FF` |
| `LIGHTSLATEGRAY` | `#778799` | `LIGHTSLATEGREY` | `#778799` |
| `LIGHTSTEELBLUE` | `#AFC4DD` | `LIGHTYELLOW` | `#FFFFE0` |
| `LIME` | `#00FF00` | `LIMEGREEN` | `#31CD31` |
| `LINEN` | `#F9EFE5` | `MAGENTA` | `#FF00FF` |
| `MAROON` | `#7F0000` | `MEDIUMAQUAMARINE` | `#66CDAA` |
| `MEDIUMBLUE` | `#0000CD` | `MEDIUMORCHID` | `#BA54D3` |
| `MEDIUMPURPLE` | `#9270DB` | `MEDIUMSEAGREEN` | `#3BB271` |
| `MEDIUMSLATEBLUE` | `#7B68ED` | `MEDIUMSPRINGGREEN` | `#00F99A` |
| `MEDIUMTURQUOISE` | `#48D1CC` | `MEDIUMVIOLETRED` | `#C61584` |
| `MIDNIGHTBLUE` | `#181870` | `MINTCREAM` | `#F4FFF9` |
| `MISTYROSE` | `#FFE3E1` | `MOCCASIN` | `#FFE3B5` |
| `NAVAJOWHITE` | `#FFDDAD` | `NAVY` | `#00007F` |
| `NAVYBLUE` | `#00007F` | `OLDLACE` | `#FCF4E5` |
| `OLIVE` | `#7F7F00` | `OLIVEDRAB` | `#6B8D22` |
| `ORANGE` | `#FFA500` | `ORANGERED` | `#FF4400` |
| `ORCHID` | `#DA70D6` | `PALEGOLDENROD` | `#EDE8AA` |
| `PALEGREEN` | `#97FB97` | `PALETURQUOISE` | `#AFEDED` |
| `PALEVIOLETRED` | `#DB7092` | `PAPAYAWHIP` | `#FFEED4` |
| `PEACHPUFF` | `#FFDAB8` | `PERU` | `#CD843F` |
| `PINK` | `#FFBFCA` | `PLUM` | `#DDA0DD` |
| `POWDERBLUE` | `#AFE0E5` | `PURPLE` | `#7F007F` |
| `RED` | `#FF0000` | `ROSYBROWN` | `#BB8E8E` |
| `ROYALBLUE` | `#4168E1` | `SADDLEBROWN` | `#8A4413` |
| `SALMON` | `#F97F72` | `SANDYBROWN` | `#F3A45F` |
| `SEAGREEN` | `#2D8A56` | `SEASHELL` | `#FFF4ED` |
| `SIENNA` | `#A0512C` | `SILVER` | `#BFBFBF` |
| `SKYBLUE` | `#87CEEA` | `SLATEBLUE` | `#6959CD` |
| `SLATEGRAY` | `#707F90` | `SLATEGREY` | `#707F90` |
| `SNOW` | `#FFF9F9` | `SPRINGGREEN` | `#00FF7E` |
| `STEELBLUE` | `#4682B3` | `TAN` | `#D2B38C` |
| `TEAL` | `#007F7F` | `THISTLE` | `#D8BFD8` |
| `TOMATO` | `#FF6347` | `TURQUOISE` | `#3FE0CF` |
| `VIOLET` | `#ED82ED` | `VIOLETRED` | `#D01F90` |
| `WHEAT` | `#F4DDB2` | `WHITE` | `#FFFFFF` |
| `WHITESMOKE` | `#F4F4F4` | `YELLOW` | `#FFFF00` |
| `YELLOWGREEN` | `#9ACD30` |

[**The AI Agent that gets your codebase** Copilot & Cursor letting you down? Try Augment. **Install Now**](https://server.ethicalads.io/proxy/click/8458/019600e6-6dea-7a03-b231-74087e43bd33/)

[Ads by EthicalAds](https://www.ethicalads.io/advertisers/?ref=ea-text)

![](https://server.ethicalads.io/proxy/view/8458/019600e6-6dea-7a03-b231-74087e43bd33/)