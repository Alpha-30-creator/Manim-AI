# iterables [¶](https://docs.manim.community/en/stable/reference/manim.utils.iterables.html\#module-manim.utils.iterables "Link to this heading")

Operations on iterables.

TypeVar’s

_class_ T [¶](https://docs.manim.community/en/stable/reference/manim.utils.iterables.html#manim.utils.iterables.T "Link to this definition")

```
TypeVar('T')

```

Copy to clipboard

_class_ U [¶](https://docs.manim.community/en/stable/reference/manim.utils.iterables.html#manim.utils.iterables.U "Link to this definition")

```
TypeVar('U')

```

Copy to clipboard

_class_ F [¶](https://docs.manim.community/en/stable/reference/manim.utils.iterables.html#manim.utils.iterables.F "Link to this definition")

```
TypeVar('F', np.float64, np.int_)
```

_class_ H [¶](https://docs.manim.community/en/stable/reference/manim.utils.iterables.html#manim.utils.iterables.H "Link to this definition")

```
TypeVar('H', bound=Hashable)

```

Copy to clipboard

Functions

adjacent\_n\_tuples( _objects_, _n_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/utils/iterables.html#adjacent_n_tuples) [¶](https://docs.manim.community/en/stable/reference/manim.utils.iterables.html#manim.utils.iterables.adjacent_n_tuples "Link to this definition")

Returns the Sequence objects cyclically split into n length tuples.

See also

[`adjacent_pairs`](https://docs.manim.community/en/stable/reference/manim.utils.iterables.html#manim.utils.iterables.adjacent_pairs "manim.utils.iterables.adjacent_pairs")

alias with n=2

Examples

```
>>> list(adjacent_n_tuples([1, 2, 3, 4], 2))
[(1, 2), (2, 3), (3, 4), (4, 1)]
>>> list(adjacent_n_tuples([1, 2, 3, 4], 3))
[(1, 2, 3), (2, 3, 4), (3, 4, 1), (4, 1, 2)]

```

Copy to clipboard

Parameters:

- **objects** ( _Sequence_ _\[_ [_T_](https://docs.manim.community/en/stable/reference/manim.utils.iterables.html#manim.utils.iterables.T "manim.utils.iterables.T") _\]_)

- **n** ( _int_)


Return type:

zip\[tuple\[ [T](https://docs.manim.community/en/stable/reference/manim.utils.iterables.html#manim.utils.iterables.T "manim.utils.iterables.T"), …\]\]

adjacent\_pairs( _objects_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/utils/iterables.html#adjacent_pairs) [¶](https://docs.manim.community/en/stable/reference/manim.utils.iterables.html#manim.utils.iterables.adjacent_pairs "Link to this definition")

Alias for `adjacent_n_tuples(objects, 2)`.

See also

[`adjacent_n_tuples`](https://docs.manim.community/en/stable/reference/manim.utils.iterables.html#manim.utils.iterables.adjacent_n_tuples "manim.utils.iterables.adjacent_n_tuples")

Examples

```
>>> list(adjacent_pairs([1, 2, 3, 4]))
[(1, 2), (2, 3), (3, 4), (4, 1)]

```

Copy to clipboard

Parameters:

**objects** ( _Sequence_ _\[_ [_T_](https://docs.manim.community/en/stable/reference/manim.utils.iterables.html#manim.utils.iterables.T "manim.utils.iterables.T") _\]_)

Return type:

zip\[tuple\[ [T](https://docs.manim.community/en/stable/reference/manim.utils.iterables.html#manim.utils.iterables.T "manim.utils.iterables.T"), …\]\]

all\_elements\_are\_instances( _iterable_, _Class_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/utils/iterables.html#all_elements_are_instances) [¶](https://docs.manim.community/en/stable/reference/manim.utils.iterables.html#manim.utils.iterables.all_elements_are_instances "Link to this definition")

Returns `True` if all elements of iterable are instances of Class.
False otherwise.

Parameters:

- **iterable** ( _Iterable_ _\[_ _object_ _\]_)

- **Class** ( _type_ _\[_ _object_ _\]_)


Return type:

bool

batch\_by\_property( _items_, _property\_func_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/utils/iterables.html#batch_by_property) [¶](https://docs.manim.community/en/stable/reference/manim.utils.iterables.html#manim.utils.iterables.batch_by_property "Link to this definition")

Takes in a Sequence, and returns a list of tuples, (batch, prop)
such that all items in a batch have the same output when
put into the Callable property\_func, and such that chaining all these
batches together would give the original Sequence (i.e. order is
preserved).

Examples

```
>>> batch_by_property([(1, 2), (3, 4), (5, 6, 7), (8, 9)], len)
[([(1, 2), (3, 4)], 2), ([(5, 6, 7)], 3), ([(8, 9)], 2)]

```

Copy to clipboard

Parameters:

- **items** ( _Iterable_ _\[_ [_T_](https://docs.manim.community/en/stable/reference/manim.utils.iterables.html#manim.utils.iterables.T "manim.utils.iterables.T") _\]_)

- **property\_func** ( _Callable_ _\[_ _\[_ [_T_](https://docs.manim.community/en/stable/reference/manim.utils.iterables.html#manim.utils.iterables.T "manim.utils.iterables.T") _\]_ _,_ [_U_](https://docs.manim.community/en/stable/reference/manim.utils.iterables.html#manim.utils.iterables.U "manim.utils.iterables.U") _\]_)


Return type:

list\[tuple\[list\[ [_T_](https://docs.manim.community/en/stable/reference/manim.utils.iterables.html#manim.utils.iterables.T "manim.utils.iterables.T")\], [_U_](https://docs.manim.community/en/stable/reference/manim.utils.iterables.html#manim.utils.iterables.U "manim.utils.iterables.U") \| None\]\]

concatenate\_lists( _\*list\_of\_lists_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/utils/iterables.html#concatenate_lists) [¶](https://docs.manim.community/en/stable/reference/manim.utils.iterables.html#manim.utils.iterables.concatenate_lists "Link to this definition")

Combines the Iterables provided as arguments into one list.

Examples

```
>>> concatenate_lists([1, 2], [3, 4], [5])
[1, 2, 3, 4, 5]

```

Copy to clipboard

Parameters:

**list\_of\_lists** ( _Iterable_ _\[_ [_T_](https://docs.manim.community/en/stable/reference/manim.utils.iterables.html#manim.utils.iterables.T "manim.utils.iterables.T") _\]_)

Return type:

list\[ [_T_](https://docs.manim.community/en/stable/reference/manim.utils.iterables.html#manim.utils.iterables.T "manim.utils.iterables.T")\]

hash\_obj( _obj_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/utils/iterables.html#hash_obj) [¶](https://docs.manim.community/en/stable/reference/manim.utils.iterables.html#manim.utils.iterables.hash_obj "Link to this definition")

Determines a hash, even of potentially mutable objects.

Parameters:

**obj** ( _object_)

Return type:

int

list\_difference\_update( _l1_, _l2_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/utils/iterables.html#list_difference_update) [¶](https://docs.manim.community/en/stable/reference/manim.utils.iterables.html#manim.utils.iterables.list_difference_update "Link to this definition")

Returns a list containing all the elements of l1 not in l2.

Examples

```
>>> list_difference_update([1, 2, 3, 4], [2, 4])
[1, 3]

```

Copy to clipboard

Parameters:

- **l1** ( _Iterable_ _\[_ [_T_](https://docs.manim.community/en/stable/reference/manim.utils.iterables.html#manim.utils.iterables.T "manim.utils.iterables.T") _\]_)

- **l2** ( _Iterable_ _\[_ [_T_](https://docs.manim.community/en/stable/reference/manim.utils.iterables.html#manim.utils.iterables.T "manim.utils.iterables.T") _\]_)


Return type:

list\[ [_T_](https://docs.manim.community/en/stable/reference/manim.utils.iterables.html#manim.utils.iterables.T "manim.utils.iterables.T")\]

list\_update( _l1_, _l2_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/utils/iterables.html#list_update) [¶](https://docs.manim.community/en/stable/reference/manim.utils.iterables.html#manim.utils.iterables.list_update "Link to this definition")Used instead of `set.update()` to maintain order,

making sure duplicates are removed from l1, not l2.
Removes overlap of l1 and l2 and then concatenates l2 unchanged.

Examples

```
>>> list_update([1, 2, 3], [2, 4, 4])
[1, 3, 2, 4, 4]

```

Copy to clipboard

Parameters:

- **l1** ( _Iterable_ _\[_ [_T_](https://docs.manim.community/en/stable/reference/manim.utils.iterables.html#manim.utils.iterables.T "manim.utils.iterables.T") _\]_)

- **l2** ( _Iterable_ _\[_ [_T_](https://docs.manim.community/en/stable/reference/manim.utils.iterables.html#manim.utils.iterables.T "manim.utils.iterables.T") _\]_)


Return type:

list\[ [_T_](https://docs.manim.community/en/stable/reference/manim.utils.iterables.html#manim.utils.iterables.T "manim.utils.iterables.T")\]

listify( _obj:str_)→list\[str\] [\[source\]](https://docs.manim.community/en/stable/_modules/manim/utils/iterables.html#listify) [¶](https://docs.manim.community/en/stable/reference/manim.utils.iterables.html#manim.utils.iterables.listify "Link to this definition")listify( _obj:Iterable\[ [T](https://docs.manim.community/en/stable/reference/manim.utils.iterables.html#manim.utils.iterables.T "manim.utils.iterables.T")\]_)→list\[ [T](https://docs.manim.community/en/stable/reference/manim.utils.iterables.html#manim.utils.iterables.T "manim.utils.iterables.T")\]listify( _obj:[T](https://docs.manim.community/en/stable/reference/manim.utils.iterables.html#manim.utils.iterables.T "manim.utils.iterables.T")_)→list\[ [T](https://docs.manim.community/en/stable/reference/manim.utils.iterables.html#manim.utils.iterables.T "manim.utils.iterables.T")\]

Converts obj to a list intelligently.

Examples

```
>>> listify("str")
['str']
>>> listify((1, 2))
[1, 2]
>>> listify(len)
[<built-in function len>]

```

Copy to clipboard

make\_even( _iterable\_1_, _iterable\_2_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/utils/iterables.html#make_even) [¶](https://docs.manim.community/en/stable/reference/manim.utils.iterables.html#manim.utils.iterables.make_even "Link to this definition")Extends the shorter of the two iterables with duplicate values until its

length is equal to the longer iterable (favours earlier elements).

See also

[`make_even_by_cycling`](https://docs.manim.community/en/stable/reference/manim.utils.iterables.html#manim.utils.iterables.make_even_by_cycling "manim.utils.iterables.make_even_by_cycling")

cycles elements instead of favouring earlier ones

Examples

```
>>> make_even([1, 2], [3, 4, 5, 6])
([1, 1, 2, 2], [3, 4, 5, 6])

>>> make_even([1, 2], [3, 4, 5, 6, 7])
([1, 1, 1, 2, 2], [3, 4, 5, 6, 7])

```

Copy to clipboard

Parameters:

- **iterable\_1** ( _Iterable_ _\[_ [_T_](https://docs.manim.community/en/stable/reference/manim.utils.iterables.html#manim.utils.iterables.T "manim.utils.iterables.T") _\]_)

- **iterable\_2** ( _Iterable_ _\[_ [_U_](https://docs.manim.community/en/stable/reference/manim.utils.iterables.html#manim.utils.iterables.U "manim.utils.iterables.U") _\]_)


Return type:

tuple\[list\[ [_T_](https://docs.manim.community/en/stable/reference/manim.utils.iterables.html#manim.utils.iterables.T "manim.utils.iterables.T")\], list\[ [_U_](https://docs.manim.community/en/stable/reference/manim.utils.iterables.html#manim.utils.iterables.U "manim.utils.iterables.U")\]\]

make\_even\_by\_cycling( _iterable\_1_, _iterable\_2_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/utils/iterables.html#make_even_by_cycling) [¶](https://docs.manim.community/en/stable/reference/manim.utils.iterables.html#manim.utils.iterables.make_even_by_cycling "Link to this definition")Extends the shorter of the two iterables with duplicate values until its

length is equal to the longer iterable (cycles over shorter iterable).

See also

[`make_even`](https://docs.manim.community/en/stable/reference/manim.utils.iterables.html#manim.utils.iterables.make_even "manim.utils.iterables.make_even")

favours earlier elements instead of cycling them

Examples

```
>>> make_even_by_cycling([1, 2], [3, 4, 5, 6])
([1, 2, 1, 2], [3, 4, 5, 6])

>>> make_even_by_cycling([1, 2], [3, 4, 5, 6, 7])
([1, 2, 1, 2, 1], [3, 4, 5, 6, 7])

```

Copy to clipboard

Parameters:

- **iterable\_1** ( _Collection_ _\[_ [_T_](https://docs.manim.community/en/stable/reference/manim.utils.iterables.html#manim.utils.iterables.T "manim.utils.iterables.T") _\]_)

- **iterable\_2** ( _Collection_ _\[_ [_U_](https://docs.manim.community/en/stable/reference/manim.utils.iterables.html#manim.utils.iterables.U "manim.utils.iterables.U") _\]_)


Return type:

tuple\[list\[ [_T_](https://docs.manim.community/en/stable/reference/manim.utils.iterables.html#manim.utils.iterables.T "manim.utils.iterables.T")\], list\[ [_U_](https://docs.manim.community/en/stable/reference/manim.utils.iterables.html#manim.utils.iterables.U "manim.utils.iterables.U")\]\]

remove\_list\_redundancies( _lst_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/utils/iterables.html#remove_list_redundancies) [¶](https://docs.manim.community/en/stable/reference/manim.utils.iterables.html#manim.utils.iterables.remove_list_redundancies "Link to this definition")

Used instead of `list(set(l))` to maintain order.
Keeps the last occurrence of each element.

Parameters:

**lst** ( _Reversible_ _\[_ [_H_](https://docs.manim.community/en/stable/reference/manim.utils.iterables.html#manim.utils.iterables.H "manim.utils.iterables.H") _\]_)

Return type:

list\[ [_H_](https://docs.manim.community/en/stable/reference/manim.utils.iterables.html#manim.utils.iterables.H "manim.utils.iterables.H")\]

remove\_nones( _sequence_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/utils/iterables.html#remove_nones) [¶](https://docs.manim.community/en/stable/reference/manim.utils.iterables.html#manim.utils.iterables.remove_nones "Link to this definition")

Removes elements where bool(x) evaluates to False.

Examples

```
>>> remove_nones(["m", "", "l", 0, 42, False, True])
['m', 'l', 42, True]

```

Copy to clipboard

Parameters:

**sequence** ( _Iterable_ _\[_ [_T_](https://docs.manim.community/en/stable/reference/manim.utils.iterables.html#manim.utils.iterables.T "manim.utils.iterables.T") _\|_ _None_ _\]_)

Return type:

list\[ [_T_](https://docs.manim.community/en/stable/reference/manim.utils.iterables.html#manim.utils.iterables.T "manim.utils.iterables.T")\]

resize\_array( _nparray_, _length_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/utils/iterables.html#resize_array) [¶](https://docs.manim.community/en/stable/reference/manim.utils.iterables.html#manim.utils.iterables.resize_array "Link to this definition")Extends/truncates nparray so that `len(result) == length`.

The elements of nparray are cycled to achieve the desired length.

See also

[`resize_preserving_order`](https://docs.manim.community/en/stable/reference/manim.utils.iterables.html#manim.utils.iterables.resize_preserving_order "manim.utils.iterables.resize_preserving_order")

favours earlier elements instead of cycling them

[`make_even_by_cycling`](https://docs.manim.community/en/stable/reference/manim.utils.iterables.html#manim.utils.iterables.make_even_by_cycling "manim.utils.iterables.make_even_by_cycling")

similar cycling behaviour for balancing 2 iterables

Examples

```
>>> points = np.array([[1, 2], [3, 4]])
>>> resize_array(points, 1)
array([[1, 2]])
>>> resize_array(points, 3)
array([[1, 2],\
       [3, 4],\
       [1, 2]])
>>> resize_array(points, 2)
array([[1, 2],\
       [3, 4]])

```

Copy to clipboard

Parameters:

- **nparray** ( _npt.NDArray_ _\[_ [_F_](https://docs.manim.community/en/stable/reference/manim.utils.iterables.html#manim.utils.iterables.F "manim.utils.iterables.F") _\]_)

- **length** ( _int_)


Return type:

npt.NDArray\[ [F](https://docs.manim.community/en/stable/reference/manim.utils.iterables.html#manim.utils.iterables.F "manim.utils.iterables.F")\]

resize\_preserving\_order( _nparray_, _length_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/utils/iterables.html#resize_preserving_order) [¶](https://docs.manim.community/en/stable/reference/manim.utils.iterables.html#manim.utils.iterables.resize_preserving_order "Link to this definition")Extends/truncates nparray so that `len(result) == length`.

The elements of nparray are duplicated to achieve the desired length
(favours earlier elements).

Constructs a zeroes array of length if nparray is empty.

See also

[`resize_array`](https://docs.manim.community/en/stable/reference/manim.utils.iterables.html#manim.utils.iterables.resize_array "manim.utils.iterables.resize_array")

cycles elements instead of favouring earlier ones

[`make_even`](https://docs.manim.community/en/stable/reference/manim.utils.iterables.html#manim.utils.iterables.make_even "manim.utils.iterables.make_even")

similar earlier-favouring behaviour for balancing 2 iterables

Examples

```
>>> resize_preserving_order(np.array([]), 5)
array([0., 0., 0., 0., 0.])

>>> nparray = np.array([[1, 2], [3, 4]])
>>> resize_preserving_order(nparray, 1)
array([[1, 2]])

>>> resize_preserving_order(nparray, 3)
array([[1, 2],\
       [1, 2],\
       [3, 4]])

```

Copy to clipboard

Parameters:

- **nparray** ( _npt.NDArray_ _\[_ _np.float64_ _\]_)

- **length** ( _int_)


Return type:

npt.NDArray\[np.float64\]

resize\_with\_interpolation( _nparray_, _length_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/utils/iterables.html#resize_with_interpolation) [¶](https://docs.manim.community/en/stable/reference/manim.utils.iterables.html#manim.utils.iterables.resize_with_interpolation "Link to this definition")Extends/truncates nparray so that `len(result) == length`.

New elements are interpolated to achieve the desired length.

Note that if nparray’s length changes, its dtype may too
(e.g. int -> float: see Examples)

See also

[`resize_array`](https://docs.manim.community/en/stable/reference/manim.utils.iterables.html#manim.utils.iterables.resize_array "manim.utils.iterables.resize_array")

cycles elements instead of interpolating

[`resize_preserving_order`](https://docs.manim.community/en/stable/reference/manim.utils.iterables.html#manim.utils.iterables.resize_preserving_order "manim.utils.iterables.resize_preserving_order")

favours earlier elements instead of interpolating

Examples

```
>>> nparray = np.array([[1, 2], [3, 4]])
>>> resize_with_interpolation(nparray, 1)
array([[1., 2.]])
>>> resize_with_interpolation(nparray, 4)
array([[1.        , 2.        ],\
       [1.66666667, 2.66666667],\
       [2.33333333, 3.33333333],\
       [3.        , 4.        ]])
>>> nparray = np.array([[[1, 2], [3, 4]]])
>>> nparray = np.array([[1, 2], [3, 4], [5, 6]])
>>> resize_with_interpolation(nparray, 4)
array([[1.        , 2.        ],\
       [2.33333333, 3.33333333],\
       [3.66666667, 4.66666667],\
       [5.        , 6.        ]])
>>> nparray = np.array([[1, 2], [3, 4], [1, 2]])
>>> resize_with_interpolation(nparray, 4)
array([[1.        , 2.        ],\
       [2.33333333, 3.33333333],\
       [2.33333333, 3.33333333],\
       [1.        , 2.        ]])

```

Copy to clipboard

Parameters:

- **nparray** ( _npt.NDArray_ _\[_ [_F_](https://docs.manim.community/en/stable/reference/manim.utils.iterables.html#manim.utils.iterables.F "manim.utils.iterables.F") _\]_)

- **length** ( _int_)


Return type:

npt.NDArray\[ [F](https://docs.manim.community/en/stable/reference/manim.utils.iterables.html#manim.utils.iterables.F "manim.utils.iterables.F")\]

stretch\_array\_to\_length( _nparray_, _length_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/utils/iterables.html#stretch_array_to_length) [¶](https://docs.manim.community/en/stable/reference/manim.utils.iterables.html#manim.utils.iterables.stretch_array_to_length "Link to this definition")Parameters:

- **nparray** ( _npt.NDArray_ _\[_ [_F_](https://docs.manim.community/en/stable/reference/manim.utils.iterables.html#manim.utils.iterables.F "manim.utils.iterables.F") _\]_)

- **length** ( _int_)


Return type:

npt.NDArray\[ [F](https://docs.manim.community/en/stable/reference/manim.utils.iterables.html#manim.utils.iterables.F "manim.utils.iterables.F")\]

tuplify( _obj:str_)→tuple\[str\] [\[source\]](https://docs.manim.community/en/stable/_modules/manim/utils/iterables.html#tuplify) [¶](https://docs.manim.community/en/stable/reference/manim.utils.iterables.html#manim.utils.iterables.tuplify "Link to this definition")tuplify( _obj:Iterable\[ [T](https://docs.manim.community/en/stable/reference/manim.utils.iterables.html#manim.utils.iterables.T "manim.utils.iterables.T")\]_)→tuple\[ [T](https://docs.manim.community/en/stable/reference/manim.utils.iterables.html#manim.utils.iterables.T "manim.utils.iterables.T")\]tuplify( _obj:[T](https://docs.manim.community/en/stable/reference/manim.utils.iterables.html#manim.utils.iterables.T "manim.utils.iterables.T")_)→tuple\[ [T](https://docs.manim.community/en/stable/reference/manim.utils.iterables.html#manim.utils.iterables.T "manim.utils.iterables.T")\]

Converts obj to a tuple intelligently.

Examples

```
>>> tuplify("str")
('str',)
>>> tuplify([1, 2])
(1, 2)
>>> tuplify(len)
(<built-in function len>,)

```

Copy to clipboard

uniq\_chain( _\*args_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/utils/iterables.html#uniq_chain) [¶](https://docs.manim.community/en/stable/reference/manim.utils.iterables.html#manim.utils.iterables.uniq_chain "Link to this definition")Returns a generator that yields all unique elements of the Iterables

provided via args in the order provided.

Examples

```
>>> gen = uniq_chain([1, 2], [2, 3], [1, 4, 4])
>>> from collections.abc import Generator
>>> isinstance(gen, Generator)
True
>>> tuple(gen)
(1, 2, 3, 4)

```

Copy to clipboard

Parameters:

**args** ( _Iterable_ _\[_ [_T_](https://docs.manim.community/en/stable/reference/manim.utils.iterables.html#manim.utils.iterables.T "manim.utils.iterables.T") _\]_)

Return type:

_Generator_\[ [_T_](https://docs.manim.community/en/stable/reference/manim.utils.iterables.html#manim.utils.iterables.T "manim.utils.iterables.T"), None, None\]