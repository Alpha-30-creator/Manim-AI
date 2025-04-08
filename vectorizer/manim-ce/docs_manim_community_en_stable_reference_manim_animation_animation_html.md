ContentsMenuExpandLight modeDark modeAuto light/dark, in light modeAuto light/dark, in dark mode[Skip to content](https://docs.manim.community/en/stable/reference/manim.animation.animation.html#furo-main-content)

[Back to top](https://docs.manim.community/en/stable/reference/manim.animation.animation.html#)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

# animation [¶](https://docs.manim.community/en/stable/reference/manim.animation.animation.html\#module-manim.animation.animation "Link to this heading")

Animate mobjects.

Classes

|     |     |
| --- | --- |
| [`Add`](https://docs.manim.community/en/stable/reference/manim.animation.animation.Add.html#manim.animation.animation.Add "manim.animation.animation.Add") | Add Mobjects to a scene, without animating them in any other way. |
| [`Animation`](https://docs.manim.community/en/stable/reference/manim.animation.animation.Animation.html#manim.animation.animation.Animation "manim.animation.animation.Animation") | An animation. |
| [`Wait`](https://docs.manim.community/en/stable/reference/manim.animation.animation.Wait.html#manim.animation.animation.Wait "manim.animation.animation.Wait") | A "no operation" animation. |

Functions

override\_animation( _animation\_class_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/animation/animation.html#override_animation) [¶](https://docs.manim.community/en/stable/reference/manim.animation.animation.html#manim.animation.animation.override_animation "Link to this definition")

Decorator used to mark methods as overrides for specific [`Animation`](https://docs.manim.community/en/stable/reference/manim.animation.animation.Animation.html#manim.animation.animation.Animation "manim.animation.animation.Animation") types.

Should only be used to decorate methods of classes derived from [`Mobject`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject").
`Animation` overrides get inherited to subclasses of the `Mobject` who defined
them. They don’t override subclasses of the `Animation` they override.

See also

[`add_animation_override()`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject.add_animation_override "manim.mobject.mobject.Mobject.add_animation_override")

Parameters:

**animation\_class** ( _type_ _\[_ [_Animation_](https://docs.manim.community/en/stable/reference/manim.animation.animation.Animation.html#manim.animation.animation.Animation "manim.animation.animation.Animation") _\]_) – The animation to be overridden.

Returns:

The actual decorator. This marks the method as overriding an animation.

Return type:

Callable\[\[Callable\], Callable\]

Examples

Example: OverrideAnimationExample [¶](https://docs.manim.community/en/stable/reference/manim.animation.animation.html#overrideanimationexample)

```
from manim import *

class MySquare(Square):
    @override_animation(FadeIn)
    def _fade_in_override(self, **kwargs):
        return Create(self, **kwargs)

class OverrideAnimationExample(Scene):
    def construct(self):
        self.play(FadeIn(MySquare()))

```

Copy to clipboard

Make interactive

prepare\_animation( _anim_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/animation/animation.html#prepare_animation) [¶](https://docs.manim.community/en/stable/reference/manim.animation.animation.html#manim.animation.animation.prepare_animation "Link to this definition")

Returns either an unchanged animation, or the animation built
from a passed animation factory.

Examples

```
>>> from manim import Square, FadeIn
>>> s = Square()
>>> prepare_animation(FadeIn(s))
FadeIn(Square)

```

Copy to clipboard

```
>>> prepare_animation(s.animate.scale(2).rotate(42))
_MethodAnimation(Square)

```

Copy to clipboard

```
>>> prepare_animation(42)
Traceback (most recent call last):
...
TypeError: Object 42 cannot be converted to an animation

```

Copy to clipboard

Parameters:

**anim** ( [_Animation_](https://docs.manim.community/en/stable/reference/manim.animation.animation.Animation.html#manim.animation.animation.Animation "manim.animation.animation.Animation") _\|_ _\_AnimationBuilder_)

Return type:

[_Animation_](https://docs.manim.community/en/stable/reference/manim.animation.animation.Animation.html#manim.animation.animation.Animation "manim.animation.animation.Animation")

[**The AI Agent that gets your codebase** Copilot & Cursor letting you down? Try Augment. **Install Now**](https://server.ethicalads.io/proxy/click/8458/019600e6-34b5-7800-b430-7b3240060a41/)

[Ads by EthicalAds](https://www.ethicalads.io/advertisers/?ref=ea-text)

![](https://server.ethicalads.io/proxy/view/8458/019600e6-34b5-7800-b430-7b3240060a41/)