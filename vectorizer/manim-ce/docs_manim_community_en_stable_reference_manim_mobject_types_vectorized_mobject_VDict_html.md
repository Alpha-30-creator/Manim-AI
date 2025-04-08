ContentsMenuExpandLight modeDark modeAuto light/dark, in light modeAuto light/dark, in dark mode[Skip to content](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VDict.html#furo-main-content)

[Back to top](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VDict.html#)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

# VDict [¶](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VDict.html\#vdict "Link to this heading")

Qualified name: `manim.mobject.types.vectorized\_mobject.VDict`

_class_ VDict( _mapping\_or\_iterable={}_, _show\_keys=False_, _\*\*kwargs_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/mobject/types/vectorized_mobject.html#VDict) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VDict.html#manim.mobject.types.vectorized_mobject.VDict "Link to this definition")

Bases: [`VMobject`](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject "manim.mobject.types.vectorized_mobject.VMobject")

A VGroup-like class, also offering submobject access by
key, like a python dict

Parameters:

- **mapping\_or\_iterable** ( _Mapping_ _\[_ _Hashable_ _,_ [_VMobject_](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject "manim.mobject.types.vectorized_mobject.VMobject") _\]_ _\|_ _Iterable_ _\[_ _tuple_ _\[_ _Hashable_ _,_ [_VMobject_](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject "manim.mobject.types.vectorized_mobject.VMobject") _\]_ _\]_) – The parameter specifying the key-value mapping of keys and mobjects.

- **show\_keys** ( _bool_) – Whether to also display the key associated with
the mobject. This might be useful when debugging,
especially when there are a lot of mobjects in the
[`VDict`](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VDict.html#manim.mobject.types.vectorized_mobject.VDict "manim.mobject.types.vectorized_mobject.VDict"). Defaults to False.

- **kwargs** – Other arguments to be passed to Mobject.


show\_keys [¶](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VDict.html#manim.mobject.types.vectorized_mobject.VDict.show_keys "Link to this definition")

Whether to also display the key associated with
the mobject. This might be useful when debugging,
especially when there are a lot of mobjects in the
[`VDict`](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VDict.html#manim.mobject.types.vectorized_mobject.VDict "manim.mobject.types.vectorized_mobject.VDict"). When displayed, the key is towards
the left of the mobject.
Defaults to False.

Type:

`bool`

submob\_dict [¶](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VDict.html#manim.mobject.types.vectorized_mobject.VDict.submob_dict "Link to this definition")

Is the actual python dictionary that is used to bind
the keys to the mobjects.

Type:

`dict`

Examples

Example: ShapesWithVDict [¶](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VDict.html#shapeswithvdict)

```
from manim import *

class ShapesWithVDict(Scene):
    def construct(self):
        square = Square().set_color(RED)
        circle = Circle().set_color(YELLOW).next_to(square, UP)

        # create dict from list of tuples each having key-mobject pair
        pairs = [("s", square), ("c", circle)]
        my_dict = VDict(pairs, show_keys=True)

        # display it just like a VGroup
        self.play(Create(my_dict))
        self.wait()

        text = Tex("Some text").set_color(GREEN).next_to(square, DOWN)

        # add a key-value pair by wrapping it in a single-element list of tuple
        # after attrs branch is merged, it will be easier like `.add(t=text)`
        my_dict.add([("t", text)])
        self.wait()

        rect = Rectangle().next_to(text, DOWN)
        # can also do key assignment like a python dict
        my_dict["r"] = rect

        # access submobjects like a python dict
        my_dict["t"].set_color(PURPLE)
        self.play(my_dict["t"].animate.scale(3))
        self.wait()

        # also supports python dict styled reassignment
        my_dict["t"] = Tex("Some other text").set_color(BLUE)
        self.wait()

        # remove submobject by key
        my_dict.remove("t")
        self.wait()

        self.play(Uncreate(my_dict["s"]))
        self.wait()

        self.play(FadeOut(my_dict["c"]))
        self.wait()

        self.play(FadeOut(my_dict["r"], shift=DOWN))
        self.wait()

        # you can also make a VDict from an existing dict of mobjects
        plain_dict = {
            1: Integer(1).shift(DOWN),
            2: Integer(2).shift(2 * DOWN),
            3: Integer(3).shift(3 * DOWN),
        }

        vdict_from_plain_dict = VDict(plain_dict)
        vdict_from_plain_dict.shift(1.5 * (UP + LEFT))
        self.play(Create(vdict_from_plain_dict))

        # you can even use zip
        vdict_using_zip = VDict(zip(["s", "c", "r"], [Square(), Circle(), Rectangle()]))
        vdict_using_zip.shift(1.5 * RIGHT)
        self.play(Create(vdict_using_zip))
        self.wait()

```

Copy to clipboard

Make interactive

Methods

|     |     |
| --- | --- |
| [`add`](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VDict.html#manim.mobject.types.vectorized_mobject.VDict.add "manim.mobject.types.vectorized_mobject.VDict.add") | Adds the key-value pairs to the [`VDict`](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VDict.html#manim.mobject.types.vectorized_mobject.VDict "manim.mobject.types.vectorized_mobject.VDict") object. |
| [`add_key_value_pair`](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VDict.html#manim.mobject.types.vectorized_mobject.VDict.add_key_value_pair "manim.mobject.types.vectorized_mobject.VDict.add_key_value_pair") | A utility function used by [`add()`](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VDict.html#manim.mobject.types.vectorized_mobject.VDict.add "manim.mobject.types.vectorized_mobject.VDict.add") to add the key-value pair to [`submob_dict`](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VDict.html#manim.mobject.types.vectorized_mobject.VDict.submob_dict "manim.mobject.types.vectorized_mobject.VDict.submob_dict"). |
| [`get_all_submobjects`](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VDict.html#manim.mobject.types.vectorized_mobject.VDict.get_all_submobjects "manim.mobject.types.vectorized_mobject.VDict.get_all_submobjects") | To get all the submobjects associated with a particular [`VDict`](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VDict.html#manim.mobject.types.vectorized_mobject.VDict "manim.mobject.types.vectorized_mobject.VDict") object |
| [`remove`](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VDict.html#manim.mobject.types.vectorized_mobject.VDict.remove "manim.mobject.types.vectorized_mobject.VDict.remove") | Removes the mobject from the [`VDict`](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VDict.html#manim.mobject.types.vectorized_mobject.VDict "manim.mobject.types.vectorized_mobject.VDict") object having the key key |

Attributes

|     |     |
| --- | --- |
| `animate` | Used to animate the application of any method of `self`. |
| `animation_overrides` |  |
| `color` |  |
| `depth` | The depth of the mobject. |
| `fill_color` | If there are multiple colors (for gradient) this returns the first one |
| `height` | The height of the mobject. |
| `n_points_per_curve` |  |
| `sheen_factor` |  |
| `stroke_color` |  |
| `width` | The width of the mobject. |

\_original\_\_init\_\_( _mapping\_or\_iterable={}_, _show\_keys=False_, _\*\*kwargs_) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VDict.html#manim.mobject.types.vectorized_mobject.VDict._original__init__ "Link to this definition")

Initialize self. See help(type(self)) for accurate signature.

Parameters:

- **mapping\_or\_iterable** ( _Mapping_ _\[_ _Hashable_ _,_ [_VMobject_](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject "manim.mobject.types.vectorized_mobject.VMobject") _\]_ _\|_ _Iterable_ _\[_ _tuple_ _\[_ _Hashable_ _,_ [_VMobject_](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject "manim.mobject.types.vectorized_mobject.VMobject") _\]_ _\]_)

- **show\_keys** ( _bool_)


Return type:

None

add( _mapping\_or\_iterable_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/mobject/types/vectorized_mobject.html#VDict.add) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VDict.html#manim.mobject.types.vectorized_mobject.VDict.add "Link to this definition")

Adds the key-value pairs to the [`VDict`](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VDict.html#manim.mobject.types.vectorized_mobject.VDict "manim.mobject.types.vectorized_mobject.VDict") object.

Also, it internally adds the value to the submobjects `list`
of [`Mobject`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject"), which is responsible for actual on-screen display.

Parameters:

**mapping\_or\_iterable** ( _Mapping_ _\[_ _Hashable_ _,_ [_VMobject_](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject "manim.mobject.types.vectorized_mobject.VMobject") _\]_ _\|_ _Iterable_ _\[_ _tuple_ _\[_ _Hashable_ _,_ [_VMobject_](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject "manim.mobject.types.vectorized_mobject.VMobject") _\]_ _\]_) – The parameter specifying the key-value mapping of keys and mobjects.

Returns:

Returns the [`VDict`](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VDict.html#manim.mobject.types.vectorized_mobject.VDict "manim.mobject.types.vectorized_mobject.VDict") object on which this method was called.

Return type:

[`VDict`](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VDict.html#manim.mobject.types.vectorized_mobject.VDict "manim.mobject.types.vectorized_mobject.VDict")

Examples

Normal usage:

```
square_obj = Square()
my_dict.add([("s", square_obj)])

```

Copy to clipboard

add\_key\_value\_pair( _key_, _value_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/mobject/types/vectorized_mobject.html#VDict.add_key_value_pair) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VDict.html#manim.mobject.types.vectorized_mobject.VDict.add_key_value_pair "Link to this definition")

A utility function used by [`add()`](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VDict.html#manim.mobject.types.vectorized_mobject.VDict.add "manim.mobject.types.vectorized_mobject.VDict.add") to add the key-value pair
to [`submob_dict`](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VDict.html#manim.mobject.types.vectorized_mobject.VDict.submob_dict "manim.mobject.types.vectorized_mobject.VDict.submob_dict"). Not really meant to be used externally.

Parameters:

- **key** ( _Hashable_) – The key of the submobject to be added.

- **value** ( [_VMobject_](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject "manim.mobject.types.vectorized_mobject.VMobject")) – The mobject associated with the key


Return type:

None

Raises:

**TypeError** – If the value is not an instance of VMobject

Examples

Normal usage:

```
square_obj = Square()
self.add_key_value_pair("s", square_obj)

```

Copy to clipboard

get\_all\_submobjects() [\[source\]](https://docs.manim.community/en/stable/_modules/manim/mobject/types/vectorized_mobject.html#VDict.get_all_submobjects) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VDict.html#manim.mobject.types.vectorized_mobject.VDict.get_all_submobjects "Link to this definition")

To get all the submobjects associated with a particular [`VDict`](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VDict.html#manim.mobject.types.vectorized_mobject.VDict "manim.mobject.types.vectorized_mobject.VDict") object

Returns:

All the submobjects associated with the [`VDict`](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VDict.html#manim.mobject.types.vectorized_mobject.VDict "manim.mobject.types.vectorized_mobject.VDict") object

Return type:

`dict_values`

Examples

Normal usage:

```
for submob in my_dict.get_all_submobjects():
    self.play(Create(submob))

```

Copy to clipboard

remove( _key_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/mobject/types/vectorized_mobject.html#VDict.remove) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VDict.html#manim.mobject.types.vectorized_mobject.VDict.remove "Link to this definition")

Removes the mobject from the [`VDict`](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VDict.html#manim.mobject.types.vectorized_mobject.VDict "manim.mobject.types.vectorized_mobject.VDict") object having the key key

Also, it internally removes the mobject from the submobjects `list`
of [`Mobject`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject"), (which is responsible for removing it from the screen)

Parameters:

**key** ( _Hashable_) – The key of the submoject to be removed.

Returns:

Returns the [`VDict`](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VDict.html#manim.mobject.types.vectorized_mobject.VDict "manim.mobject.types.vectorized_mobject.VDict") object on which this method was called.

Return type:

[`VDict`](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VDict.html#manim.mobject.types.vectorized_mobject.VDict "manim.mobject.types.vectorized_mobject.VDict")

Examples

Normal usage:

```
my_dict.remove("square")

```

Copy to clipboard

[**The AI Agent that gets your codebase** Copilot & Cursor letting you down? Try Augment. **Install Now**](https://server.ethicalads.io/proxy/click/8458/019600f6-c613-71f1-bb8b-78ab088a88f1/)

[Ads by EthicalAds](https://www.ethicalads.io/advertisers/?ref=ea-text)

![](https://server.ethicalads.io/proxy/view/8458/019600f6-c613-71f1-bb8b-78ab088a88f1/)