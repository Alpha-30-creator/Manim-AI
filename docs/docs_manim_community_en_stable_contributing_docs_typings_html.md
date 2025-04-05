ContentsMenuExpandLight modeDark modeAuto light/dark, in light modeAuto light/dark, in dark mode[Skip to content](https://docs.manim.community/en/stable/contributing/docs/typings.html#furo-main-content)

[Back to top](https://docs.manim.community/en/stable/contributing/docs/typings.html#)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

# Typing Conventions [¶](https://docs.manim.community/en/stable/contributing/docs/typings.html\#typing-conventions "Link to this heading")

Warning

This section is still a work in progress.

## Adding type hints to functions and parameters [¶](https://docs.manim.community/en/stable/contributing/docs/typings.html\#adding-type-hints-to-functions-and-parameters "Link to this heading")

Manim is currently in the process of adding type hints into the library. In this
section, you will find information about the standards used and some general
guidelines.

If you’ve never used type hints before, this is a good place to get started:
[https://realpython.com/python-type-checking/#hello-types](https://realpython.com/python-type-checking/#hello-types).

### Typing standards [¶](https://docs.manim.community/en/stable/contributing/docs/typings.html\#typing-standards "Link to this heading")

Manim uses [mypy](https://mypy-lang.org/) to type check its codebase. You will find a list of configuration values in the `mypy.ini` configuration file.
To be able to use the newest typing features not available in the lowest
supported Python version, make use of [typing\_extensions](https://pypi.org/project/typing-extensions/).

To be able to use the new Union syntax ( `|`) and builtins subscripting, use
the `from __future__ import annotations` import.

### Typing guidelines [¶](https://docs.manim.community/en/stable/contributing/docs/typings.html\#typing-guidelines "Link to this heading")

- Manim has a dedicated [`typing`](https://docs.manim.community/en/stable/reference/manim.typing.html#module-manim.typing "manim.typing") module where type aliases are provided.
Most of them may seem redundant, in particular the ones related to `numpy`.
This is in anticipation of the support for shape type hinting
( [related issue](https://github.com/numpy/numpy/issues/16544)). Besides the
pending shape support, using the correct type aliases will help users understand
which shape should be used.

- For typings of generic collections, check out [this](https://docs.python.org/3/library/collections.abc.html#collections-abstract-base-classes)
link.

- Always use a type hint of `None` for functions that does not return
a value (this also applies to `__init__`), e.g.:


```
def height(self, value) -> None:
    self.scale_to_fit_height(value)

```

Copy to clipboard

- For variables representing paths, use the `StrPath` or `StrOrBytesPath`
type alias defined in the [`typing`](https://docs.manim.community/en/stable/reference/manim.typing.html#module-manim.typing "manim.typing") module.

- `*args` and `**kwargs` shouldn’t be left untyped (in most cases you can
use `Any`).

- Following [PEP 484](https://peps.python.org/pep-0484/#the-numeric-tower),
use `float` instead of `int | float`.

- Use `x | y` instead of `Union[x, y]`

- Mobjects have the typehint `Mobject`, e.g.:


```
def match_color(self, mobject: "Mobject"):
    """Match the color with the color of another :class:`~.Mobject`."""
    return self.set_color(mobject.get_color())

```

Copy to clipboard

- Always parametrize generics ( `list[int]` instead of `list`,
`type[Any]` instead of `type`, etc.). This also applies to callables.


```
rate_func: Callable[[float], float] = lambda t: smooth(1 - t)

```

Copy to clipboard

- Use `TypeVar` when you want to “link” type hints as being the same type.
Consider `Mobject.copy`, which returns a new instance of the same class.
It would be type-hinted as:


```
T = TypeVar("T")

def copy(self: T) -> T: ...

```

Copy to clipboard

- Use `typing.Iterable` whenever the function works with _any_ iterable, not a specific type.

- Prefer `numpy.typing.NDArray` over `numpy.ndarray`


```
import numpy as np

if TYPE_CHECKING:
    import numpy.typing as npt

def foo() -> npt.NDArray[float]:
    return np.array([1, 0, 1])

```

Copy to clipboard

- If a method returns `self`, use `typing_extensions.Self`.


```
if TYPE_CHECKING:
    from typing_extensions import Self

class CustomMobject:
    def set_color(self, color: ManimColor) -> Self:
        ...
        return self

```

Copy to clipboard

- If the function returns a container of a specific length each time, consider using `tuple` instead of `list`.


```
def foo() -> tuple[float, float, float]:
    return (0, 0, 0)

```

Copy to clipboard

- If a function works with a parameter as long as said parameter has a `__getitem__`, `__iter___` and `__len__` method,
the typehint of the parameter should be `collections.abc.Mapping`. If it also supports `__setitem__` and/or `__delitem__`, it
should be marked as `collections.abc.MutableMapping`.

- Typehinting something as `object` means that only attributes available on every Python object should be accessed,
like `__str__` and so on. On the other hand, literally any attribute can be accessed on a variable with the `Any` typehint -
it’s more freeing than the `object` typehint, and makes mypy stop typechecking the variable. Note that whenever possible,
try to keep typehints as specific as possible.

- If objects are imported purely for type hint purposes, keep it under an `if typing.TYPE_CHECKING` guard, to prevent them from
being imported at runtime (helps library performance). Do not forget to use the `from __future__ import annotations` import to avoid having runtime `NameError` exceptions.


```
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from manim.typing import Vector3D
# type stuff with Vector3D

```

Copy to clipboard

## Missing Sections for typehints are: [¶](https://docs.manim.community/en/stable/contributing/docs/typings.html\#missing-sections-for-typehints-are "Link to this heading")

- Mypy and numpy import errors: [https://realpython.com/python-type-checking/#running-mypy](https://realpython.com/python-type-checking/#running-mypy)

- Explain `mypy.ini` (see above link)


[**Document Extraction for Developers** Transform docs into structured data with Sensible. **Try for free →**](https://server.ethicalads.io/proxy/click/8517/019600e4-87f1-7e42-9827-6a4e4e5dc94d/)

[Ads by EthicalAds](https://www.ethicalads.io/advertisers/topics/data-science/?ref=ea-text)

![](https://server.ethicalads.io/proxy/view/8517/019600e4-87f1-7e42-9827-6a4e4e5dc94d/)