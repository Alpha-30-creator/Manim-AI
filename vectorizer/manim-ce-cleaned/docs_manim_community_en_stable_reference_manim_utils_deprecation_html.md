# deprecation [¶](https://docs.manim.community/en/stable/reference/manim.utils.deprecation.html\#module-manim.utils.deprecation "Link to this heading")

Decorators for deprecating classes, functions and function parameters.

TypeVar’s

_class_ T [¶](https://docs.manim.community/en/stable/reference/manim.utils.deprecation.html#manim.utils.deprecation.T "Link to this definition")

```
TypeVar('T')

```

Copy to clipboard

Functions

deprecated( _func:Callable\[\[...\], [T](https://docs.manim.community/en/stable/reference/manim.utils.deprecation.html#manim.utils.deprecation.T "manim.utils.deprecation.T")\]_, _since:str\|None=None_, _until:str\|None=None_, _replacement:str\|None=None_, _message:str\|None=''_)→Callable\[\[...\], [T](https://docs.manim.community/en/stable/reference/manim.utils.deprecation.html#manim.utils.deprecation.T "manim.utils.deprecation.T")\] [\[source\]](https://docs.manim.community/en/stable/_modules/manim/utils/deprecation.html#deprecated) [¶](https://docs.manim.community/en/stable/reference/manim.utils.deprecation.html#manim.utils.deprecation.deprecated "Link to this definition")deprecated( _func:None=None_, _since:str\|None=None_, _until:str\|None=None_, _replacement:str\|None=None_, _message:str\|None=''_)→Callable\[\[Callable\[\[...\], [T](https://docs.manim.community/en/stable/reference/manim.utils.deprecation.html#manim.utils.deprecation.T "manim.utils.deprecation.T")\]\],Callable\[\[...\], [T](https://docs.manim.community/en/stable/reference/manim.utils.deprecation.html#manim.utils.deprecation.T "manim.utils.deprecation.T")\]\]

Decorator to mark a callable as deprecated.

The decorated callable will cause a warning when used. The docstring of the
deprecated callable is adjusted to indicate that this callable is deprecated.

Parameters:

- **func** – The function to be decorated. Should not be set by the user.

- **since** – The version or date since deprecation.

- **until** – The version or date until removal of the deprecated callable.

- **replacement** – The identifier of the callable replacing the deprecated one.

- **message** – The reason for why the callable has been deprecated.


Returns:

The decorated callable.

Return type:

Callable

Examples

Basic usage:

```
from manim.utils.deprecation import deprecated

@deprecated
def foo(**kwargs):
    pass

@deprecated
class Bar:
    def __init__(self):
        pass

    @deprecated
    def baz(self):
        pass

foo()
# WARNING  The function foo has been deprecated and may be removed in a later version.

a = Bar()
# WARNING  The class Bar has been deprecated and may be removed in a later version.

a.baz()
# WARNING  The method Bar.baz has been deprecated and may be removed in a later version.

```

Copy to clipboard

You can specify additional information for a more precise warning:

```
from manim.utils.deprecation import deprecated

@deprecated(
    since="v0.2", until="v0.4", replacement="bar", message="It is cooler."
)
def foo():
    pass

foo()
# WARNING  The function foo has been deprecated since v0.2 and is expected to be removed after v0.4. Use bar instead. It is cooler.

```

Copy to clipboard

You may also use dates instead of versions:

```
from manim.utils.deprecation import deprecated

@deprecated(since="05/01/2021", until="06/01/2021")
def foo():
    pass

foo()
# WARNING  The function foo has been deprecated since 05/01/2021 and is expected to be removed after 06/01/2021.

```

Copy to clipboard

deprecated\_params( _params=None_, _since=None_, _until=None_, _message=''_, _redirections=None_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/utils/deprecation.html#deprecated_params) [¶](https://docs.manim.community/en/stable/reference/manim.utils.deprecation.html#manim.utils.deprecation.deprecated_params "Link to this definition")

Decorator to mark parameters of a callable as deprecated.

It can also be used to automatically redirect deprecated parameter values to their
replacements.

Parameters:

- **params** ( _str_ _\|_ _Iterable_ _\[_ _str_ _\]_ _\|_ _None_) –

The parameters to be deprecated. Can consist of:


  - An iterable of strings, with each element representing a parameter to deprecate

  - A single string, with parameter names separated by commas or spaces.


- **since** ( _str_ _\|_ _None_) – The version or date since deprecation.

- **until** ( _str_ _\|_ _None_) – The version or date until removal of the deprecated callable.

- **message** ( _str_) – The reason for why the callable has been deprecated.

- **redirections** ( _None_ _\|_ _Iterable_ _\[_ _tuple_ _\[_ _str_ _,_ _str_ _\]_ _\|_ _Callable_ _\[_ _\[_ _..._ _\]_ _,_ _dict_ _\[_ _str_ _,_ _Any_ _\]_ _\]_ _\]_) –

A list of parameter redirections. Each redirection can be one of the following:


  - A tuple of two strings. The first string defines the name of the deprecated
    parameter; the second string defines the name of the parameter to redirect to,
    when attempting to use the first string.

  - A function performing the mapping operation. The parameter names of the
    function determine which parameters are used as input. The function must
    return a dictionary which contains the redirected arguments.


Redirected parameters are also implicitly deprecated.

Returns:

The decorated callable.

Return type:

Callable

Raises:

- **ValueError** – If no parameters are defined (neither explicitly nor implicitly).

- **ValueError** – If defined parameters are invalid python identifiers.


Examples

Basic usage:

```
from manim.utils.deprecation import deprecated_params

@deprecated_params(params="a, b, c")
def foo(**kwargs):
    pass

foo(x=2, y=3, z=4)
# No warning

foo(a=2, b=3, z=4)
# WARNING  The parameters a and b of method foo have been deprecated and may be removed in a later version.

```

Copy to clipboard

You can also specify additional information for a more precise warning:

```
from manim.utils.deprecation import deprecated_params

@deprecated_params(
    params="a, b, c",
    since="v0.2",
    until="v0.4",
    message="The letters x, y, z are cooler.",
)
def foo(**kwargs):
    pass

foo(a=2)
# WARNING  The parameter a of method foo has been deprecated since v0.2 and is expected to be removed after v0.4. The letters x, y, z are cooler.

```

Copy to clipboard

Basic parameter redirection:

```
from manim.utils.deprecation import deprecated_params

@deprecated_params(
    redirections=[\
        # Two ways to redirect one parameter to another:\
        ("old_param", "new_param"),\
        lambda old_param2: {"new_param22": old_param2},\
    ]
)
def foo(**kwargs):
    return kwargs

foo(x=1, old_param=2)
# WARNING  The parameter old_param of method foo has been deprecated and may be removed in a later version.
# returns {"x": 1, "new_param": 2}

```

Copy to clipboard

Redirecting using a calculated value:

```
from manim.utils.deprecation import deprecated_params

@deprecated_params(
    redirections=[lambda runtime_in_ms: {"run_time": runtime_in_ms / 1000}]
)
def foo(**kwargs):
    return kwargs

foo(runtime_in_ms=500)
# WARNING  The parameter runtime_in_ms of method foo has been deprecated and may be removed in a later version.
# returns {"run_time": 0.5}

```

Copy to clipboard

Redirecting multiple parameter values to one:

```
from manim.utils.deprecation import deprecated_params

@deprecated_params(
    redirections=[lambda buff_x=1, buff_y=1: {"buff": (buff_x, buff_y)}]
)
def foo(**kwargs):
    return kwargs

foo(buff_x=2)
# WARNING  The parameter buff_x of method foo has been deprecated and may be removed in a later version.
# returns {"buff": (2, 1)}

```

Copy to clipboard

Redirect one parameter to multiple:

```
from manim.utils.deprecation import deprecated_params

@deprecated_params(
    redirections=[\
        lambda buff=1: {"buff_x": buff[0], "buff_y": buff[1]}\
        if isinstance(buff, tuple)\
        else {"buff_x": buff, "buff_y": buff}\
    ]
)
def foo(**kwargs):
    return kwargs

foo(buff=0)
# WARNING  The parameter buff of method foo has been deprecated and may be removed in a later version.
# returns {"buff_x": 0, buff_y: 0}

foo(buff=(1, 2))
# WARNING  The parameter buff of method foo has been deprecated and may be removed in a later version.
# returns {"buff_x": 1, buff_y: 2}

```

Copy to clipboard