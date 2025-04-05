ContentsMenuExpandLight modeDark modeAuto light/dark, in light modeAuto light/dark, in dark mode[Skip to content](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.html#furo-main-content)

[Back to top](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.html#)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

# mobject [¶](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.html\#module-manim.mobject.mobject "Link to this heading")

Base classes for objects that can be displayed.

Type Aliases

_class_ TimeBasedUpdater [¶](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.html#manim.mobject.mobject.TimeBasedUpdater "Link to this definition")

```
Callable[['Mobject', float], object]

```

Copy to clipboard

_class_ NonTimeBasedUpdater [¶](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.html#manim.mobject.mobject.NonTimeBasedUpdater "Link to this definition")

```
Callable[['Mobject'], object]

```

Copy to clipboard

_class_ Updater [¶](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.html#manim.mobject.mobject.Updater "Link to this definition")

```xref py py-class docutils literal notranslate
NonTimeBasedUpdater` | TimeBasedUpdater`
```

Classes

|     |     |
| --- | --- |
| [`Group`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Group.html#manim.mobject.mobject.Group "manim.mobject.mobject.Group") | Groups together multiple [`Mobjects`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject"). |
| [`Mobject`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject") | Mathematical Object: base class for objects that can be displayed on screen. |

Functions

override\_animate( _method_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/mobject/mobject.html#override_animate) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.html#manim.mobject.mobject.override_animate "Link to this definition")

Decorator for overriding method animations.

This allows to specify a method (returning an [`Animation`](https://docs.manim.community/en/stable/reference/manim.animation.animation.Animation.html#manim.animation.animation.Animation "manim.animation.animation.Animation"))
which is called when the decorated method is used with the `.animate` syntax
for animating the application of a method.

See also

[`Mobject.animate`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject.animate "manim.mobject.mobject.Mobject.animate")

Note

Overridden methods cannot be combined with normal or other overridden
methods using method chaining with the `.animate` syntax.

Examples

Example: AnimationOverrideExample [¶](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.html#animationoverrideexample)

```
from manim import *

class CircleWithContent(VGroup):
    def __init__(self, content):
        super().__init__()
        self.circle = Circle()
        self.content = content
        self.add(self.circle, content)
        content.move_to(self.circle.get_center())

    def clear_content(self):
        self.remove(self.content)
        self.content = None

    @override_animate(clear_content)
    def _clear_content_animation(self, anim_args=None):
        if anim_args is None:
            anim_args = {}
        anim = Uncreate(self.content, **anim_args)
        self.clear_content()
        return anim

class AnimationOverrideExample(Scene):
    def construct(self):
        t = Text("hello!")
        my_mobject = CircleWithContent(t)
        self.play(Create(my_mobject))
        self.play(my_mobject.animate.clear_content())
        self.wait()

```

Copy to clipboard

Make interactive

Return type:

_LambdaType_

[**Watch Our Demo** video to see firsthand how to upgrade your site with end-to-end AI Search.](https://server.ethicalads.io/proxy/click/8298/019600f0-ad9d-77f1-99ec-090563eda2fc/)

[Ads by EthicalAds](https://www.ethicalads.io/advertisers/topics/backend-web/?ref=ea-text)

![](https://server.ethicalads.io/proxy/view/8298/019600f0-ad9d-77f1-99ec-090563eda2fc/)