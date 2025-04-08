ContentsMenuExpandLight modeDark modeAuto light/dark, in light modeAuto light/dark, in dark mode[Skip to content](https://docs.manim.community/en/stable/reference/manim.utils.bezier.html#furo-main-content)

[Back to top](https://docs.manim.community/en/stable/reference/manim.utils.bezier.html#)

Toggle Light / Dark / Auto color theme

Toggle table of contents sidebar

# bezier [¶](https://docs.manim.community/en/stable/reference/manim.utils.bezier.html\#module-manim.utils.bezier "Link to this heading")

Utility functions related to Bézier curves.

Functions

bezier( _points:[BezierPointsLike](https://docs.manim.community/en/stable/reference/manim.typing.html#manim.typing.BezierPointsLike "manim.typing.BezierPointsLike")_)→Callable\[\[float\| [ColVector](https://docs.manim.community/en/stable/reference/manim.typing.html#manim.typing.ColVector "manim.typing.ColVector")\], [Point3D](https://docs.manim.community/en/stable/reference/manim.typing.html#manim.typing.Point3D "manim.typing.Point3D") \| [Point3D\_Array](https://docs.manim.community/en/stable/reference/manim.typing.html#manim.typing.Point3D_Array "manim.typing.Point3D_Array")\] [\[source\]](https://docs.manim.community/en/stable/_modules/manim/utils/bezier.html#bezier) [¶](https://docs.manim.community/en/stable/reference/manim.utils.bezier.html#manim.utils.bezier.bezier "Link to this definition")bezier( _points:Sequence\[ [Point3DLike\_Array](https://docs.manim.community/en/stable/reference/manim.typing.html#manim.typing.Point3DLike_Array "manim.typing.Point3DLike_Array")\]_)→Callable\[\[float\| [ColVector](https://docs.manim.community/en/stable/reference/manim.typing.html#manim.typing.ColVector "manim.typing.ColVector")\], [Point3D\_Array](https://docs.manim.community/en/stable/reference/manim.typing.html#manim.typing.Point3D_Array "manim.typing.Point3D_Array")\]

Classic implementation of a Bézier curve.

Parameters:

**points** – (d+1,3)-shaped array of d+1 control points defining a single Bézier
curve of degree d. Alternatively, for vectorization purposes, `points` can
also be a (d+1,M,3)-shaped sequence of d+1 arrays of M
control points each, which define M Bézier curves instead.

Returns:

**bezier\_func** – Function describing the Bézier curve. The behaviour of this function depends on
the shape of `points`:

> - If `points` was a (d+1,3) array representing a single Bézier curve,
> then `bezier_func` can receive either:
>
>
>   - a `float` `t`, in which case it returns a
>     single (1,3)-shaped [`Point3D`](https://docs.manim.community/en/stable/reference/manim.typing.html#manim.typing.Point3D "manim.typing.Point3D") representing the evaluation
>     of the Bézier at `t`, or
>
>   - an (n,1)-shaped [`ColVector`](https://docs.manim.community/en/stable/reference/manim.typing.html#manim.typing.ColVector "manim.typing.ColVector")
>     containing n values to evaluate the Bézier curve at, returning instead
>     an (n,3)-shaped [`Point3D_Array`](https://docs.manim.community/en/stable/reference/manim.typing.html#manim.typing.Point3D_Array "manim.typing.Point3D_Array") containing the points
>     resulting from evaluating the Bézier at each of the n values.
>
>
> Warning
>
> If passing a vector of t-values to `bezier_func`, it **must**
> be a column vector/matrix of shape (n,1). Passing an 1D array of
> shape (n,) is not supported and **will result in undefined behaviour**.
>
> - If `points` was a (d+1,M,3) array describing M Bézier curves,
> then `bezier_func` can receive either:
>
>
>   - a `float` `t`, in which case it returns an
>     (M,3)-shaped [`Point3D_Array`](https://docs.manim.community/en/stable/reference/manim.typing.html#manim.typing.Point3D_Array "manim.typing.Point3D_Array") representing the evaluation
>     of the M Bézier curves at the same value `t`, or
>
>   - an (M,1)-shaped
>     [`ColVector`](https://docs.manim.community/en/stable/reference/manim.typing.html#manim.typing.ColVector "manim.typing.ColVector") containing M values, such that the i-th
>     Bézier curve defined by `points` is evaluated at the corresponding i-th
>     value in `t`, returning again an (M,3)-shaped [`Point3D_Array`](https://docs.manim.community/en/stable/reference/manim.typing.html#manim.typing.Point3D_Array "manim.typing.Point3D_Array")
>     containing those M evaluations.
>
>
> Warning
>
> Unlike the previous case, if you pass a [`ColVector`](https://docs.manim.community/en/stable/reference/manim.typing.html#manim.typing.ColVector "manim.typing.ColVector") to `bezier_func`,
> it **must** contain exactly M values, each value for each of the M
> Bézier curves defined by `points`. Any array of shape other than (M,1) **will result in undefined behaviour**.

Return type:

`typing.Callable` \[\[ `float` \| [`ColVector`](https://docs.manim.community/en/stable/reference/manim.typing.html#manim.typing.ColVector "manim.typing.ColVector")\], [`Point3D`](https://docs.manim.community/en/stable/reference/manim.typing.html#manim.typing.Point3D "manim.typing.Point3D") \| [`Point3D_Array`](https://docs.manim.community/en/stable/reference/manim.typing.html#manim.typing.Point3D_Array "manim.typing.Point3D_Array")\]

bezier\_remap( _bezier\_tuples_, _new\_number\_of\_curves_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/utils/bezier.html#bezier_remap) [¶](https://docs.manim.community/en/stable/reference/manim.utils.bezier.html#manim.utils.bezier.bezier_remap "Link to this definition")

Subdivides each curve in `bezier_tuples` into as many parts as necessary, until the final number of
curves reaches a desired amount, `new_number_of_curves`.

Parameters:

- **bezier\_tuples** ( [_BezierPointsLike\_Array_](https://docs.manim.community/en/stable/reference/manim.typing.html#manim.typing.BezierPointsLike_Array "manim.typing.BezierPointsLike_Array")) –

An array of multiple Bézier curves of degree d to be remapped. The shape of this array
must be `(current_number_of_curves, nppc, dim)`, where:


  - `current_number_of_curves` is the current amount of curves in the array `bezier_tuples`,

  - `nppc` is the amount of points per curve, such that their degree is `nppc-1`, and

  - `dim` is the dimension of the points, usually 3.


- **new\_number\_of\_curves** ( _int_) – The number of curves that the output will contain. This needs to be higher than the current number.


Returns:

The new array of shape `(new_number_of_curves, nppc, dim)`,
containing the new Bézier curves after the remap.

Return type:

[`BezierPoints_Array`](https://docs.manim.community/en/stable/reference/manim.typing.html#manim.typing.BezierPoints_Array "manim.typing.BezierPoints_Array")

get\_quadratic\_approximation\_of\_cubic( _a0:[Point3DLike](https://docs.manim.community/en/stable/reference/manim.typing.html#manim.typing.Point3DLike "manim.typing.Point3DLike")_, _h0:[Point3DLike](https://docs.manim.community/en/stable/reference/manim.typing.html#manim.typing.Point3DLike "manim.typing.Point3DLike")_, _h1:[Point3DLike](https://docs.manim.community/en/stable/reference/manim.typing.html#manim.typing.Point3DLike "manim.typing.Point3DLike")_, _a1:[Point3DLike](https://docs.manim.community/en/stable/reference/manim.typing.html#manim.typing.Point3DLike "manim.typing.Point3DLike")_)→[QuadraticSpline](https://docs.manim.community/en/stable/reference/manim.typing.html#manim.typing.QuadraticSpline "manim.typing.QuadraticSpline") [\[source\]](https://docs.manim.community/en/stable/_modules/manim/utils/bezier.html#get_quadratic_approximation_of_cubic) [¶](https://docs.manim.community/en/stable/reference/manim.utils.bezier.html#manim.utils.bezier.get_quadratic_approximation_of_cubic "Link to this definition")get\_quadratic\_approximation\_of\_cubic( _a0:[Point3DLike\_Array](https://docs.manim.community/en/stable/reference/manim.typing.html#manim.typing.Point3DLike_Array "manim.typing.Point3DLike_Array")_, _h0:[Point3DLike\_Array](https://docs.manim.community/en/stable/reference/manim.typing.html#manim.typing.Point3DLike_Array "manim.typing.Point3DLike_Array")_, _h1:[Point3DLike\_Array](https://docs.manim.community/en/stable/reference/manim.typing.html#manim.typing.Point3DLike_Array "manim.typing.Point3DLike_Array")_, _a1:[Point3DLike\_Array](https://docs.manim.community/en/stable/reference/manim.typing.html#manim.typing.Point3DLike_Array "manim.typing.Point3DLike_Array")_)→[QuadraticBezierPath](https://docs.manim.community/en/stable/reference/manim.typing.html#manim.typing.QuadraticBezierPath "manim.typing.QuadraticBezierPath")

If `a0`, `h0`, `h1` and `a1` are the control points of a cubic
Bézier curve, approximate the curve with two quadratic Bézier curves and
return an array of 6 points, where the first 3 points represent the first
quadratic curve and the last 3 represent the second one.

Otherwise, if `a0`, `h0`, `h1` and `a1` are \_arrays\_ of N
points representing N cubic Bézier curves, return an array of
6N points where each group of 6 consecutive points
approximates each of the N curves in a similar way as above.

Note

If the cubic spline given by the original cubic Bézier curves is
smooth, this algorithm will generate a quadratic spline which is also
smooth.

If a cubic Bézier is given by

C(t)=(1−t)3A0+3(1−t)2tH0+3(1−t)t2H1+t3A1

where A0, H0, H1 and A1 are its
control points, then this algorithm should generate two quadratic
Béziers given by

Q0(t)=(1−t)2A0+2(1−t)tM0+t2KQ1(t)=(1−t)2K+2(1−t)tM1+t2A1

where M0 and M1 are the respective handles to be
found for both curves, and K is the end anchor of the 1st curve
and the start anchor of the 2nd, which must also be found.

To solve for M0, M1 and K, three conditions
can be imposed:

1. Q0′(0)=12C′(0). The derivative of the first
quadratic curve at t=0 should be proportional to that of
the original cubic curve, also at t=0. Because the cubic
curve is split into two parts, it is necessary to divide this by
two: the speed of a point travelling through the curve should be
half of the original. This gives:



Q0′(0)=12C′(0)2(M0−A0)=32(H0−A0)2M0−2A0=32H0−32A02M0=32H0+12A0M0=14(3H0+A0)

2. Q1′(1)=12C′(1). The derivative of the second
quadratic curve at t=1 should be half of that of the
original cubic curve for the same reasons as above, also at
t=1. This gives:



Q1′(1)=12C′(1)2(A1−M1)=32(A1−H1)2A1−2M1=32A1−32H1−2M1=−12A1−32H1M1=14(3H1+A1)

3. Q0′(1)=Q1′(0). The derivatives of both quadratic curves
should match at the point K, in order for the final spline
to be smooth. This gives:



Q0′(1)=Q1′(0)2(K−M0)=2(M1−K)2K−2M0=2M1−2K4K=2M0+2M1K=12(M0+M1)


This is sufficient to find proper control points for the quadratic
Bézier curves.

Parameters:

- **a0** – The start anchor of a single cubic Bézier curve, or an array of
N start anchors for N curves.

- **h0** – The first handle of a single cubic Bézier curve, or an array of
N first handles for N curves.

- **h1** – The second handle of a single cubic Bézier curve, or an array of
N second handles for N curves.

- **a1** – The end anchor of a single cubic Bézier curve, or an array of
N end anchors for N curves.


Returns:

An array containing either 6 points for 2 quadratic Bézier curves
approximating the original cubic curve, or 6N points for
2N quadratic curves approximating N cubic curves.

Return type:

result

Raises:

**ValueError** – If `a0`, `h0`, `h1` and `a1` have different dimensions, or
if their number of dimensions is not 1 or 2.

get\_smooth\_closed\_cubic\_bezier\_handle\_points( _anchors_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/utils/bezier.html#get_smooth_closed_cubic_bezier_handle_points) [¶](https://docs.manim.community/en/stable/reference/manim.utils.bezier.html#manim.utils.bezier.get_smooth_closed_cubic_bezier_handle_points "Link to this definition")

Special case of [`get_smooth_cubic_bezier_handle_points()`](https://docs.manim.community/en/stable/reference/manim.utils.bezier.html#manim.utils.bezier.get_smooth_cubic_bezier_handle_points "manim.utils.bezier.get_smooth_cubic_bezier_handle_points"),
when the `anchors` form a closed loop.

Note

A system of equations must be solved to get the first handles of
every Bézier curve (referred to as H1).
Then H2 (the second handles) can be obtained separately.

See also

The equations were obtained from:

- [Conditions on control points for continuous curvature. (2016). Jaco Stuifbergen.](http://www.jacos.nl/jacos_html/spline/theory/theory_2.html)


In general, if there are N+1 anchors, there will be N Bézier curves
and thus N pairs of handles to find. We must solve the following
system of equations for the 1st handles (example for N=5):

(4100114100014100014110014)(H1,0H1,1H1,2H1,3H1,4)=(4A0+2A14A1+2A24A2+2A34A3+2A44A4+2A5)

which will be expressed as RH1=D.

R is almost a tridiagonal matrix, so we could use Thomas’ algorithm.

See also

[Tridiagonal matrix algorithm. Wikipedia.](https://en.wikipedia.org/wiki/Tridiagonal_matrix_algorithm)

However, R has ones at the opposite corners. A solution to this is
the first decomposition proposed in the link below, with α=1:

See also

[Tridiagonal matrix algorithm # Variants. Wikipedia.](https://en.wikipedia.org/wiki/Tridiagonal_matrix_algorithm#Variants)

R=(4100114100014100014110014)=(3100014100014100014100013)+(1000100000000000000010001)=(3100014100014100014100013)+(10001)(10001)=T+uvt

We decompose R=T+uvt, where T is a tridiagonal matrix, and
u,v are N-D vectors such that u0=uN−1=v0=vN−1=1,
and ui=vi=0,∀i∈{1,...,N−2}.

Thus:

RH1=D⇒(T+uvt)H1=D

If we find a vector q such that Tq=u:

⇒(T+Tqvt)H1=D⇒T(I+qvt)H1=D⇒H1=(I+qvt)−1T−1D

According to Sherman-Morrison’s formula:

See also

[Sherman-Morrison’s formula. Wikipedia.](https://en.wikipedia.org/wiki/Sherman%E2%80%93Morrison_formula)

(I+qvt)−1=I−11+vtqqvt

If we find Y=T−1D, or in other words, if we solve for
Y in TY=D:

H1=(I+qvt)−1T−1D=(I+qvt)−1Y=(I−11+vtqqvt)Y=Y−11+vtqqvtY

Therefore, we must solve for q and Y in Tq=u and TY=D.
As T is now tridiagonal, we shall use Thomas’ algorithm.

Define:

- a=\[a0,a1,...,aN−2\] as T’s lower diagonal of N−1 elements,
such that a0=a1=...=aN−2=1, so this diagonal is filled with ones;

- b=\[b0,b1,...,bN−2,bN−1\] as T’s main diagonal of N elements,
such that b0=bN−1=3, and b1=b2=...=bN−2=4;

- c=\[c0,c1,...,cN−2\] as T’s upper diagonal of N−1 elements,
such that c0=c1=...=cN−2=1: this diagonal is also filled with ones.


If, according to Thomas’ algorithm, we define:

c0′=c0b0ci′=cibi−ai−1ci−1′,∀i∈{1,...,N−2}u0′=u0b0ui′=ui−ai−1ui−1′bi−ai−1ci−1′,∀i∈{1,...,N−1}D0′=1b0D0Di′=1bi−ai−1ci−1′(Di−ai−1Di−1′),∀i∈{1,...,N−1}

Then:

c0′=13ci′=14−ci−1′,∀i∈{1,...,N−2}u0′=13ui′=−ui−1′4−ci−1′=−ci′ui−1′,∀i∈{1,...,N−2}uN−1′=1−uN−2′3−cN−2′D0′=13(4A0+2A1)Di′=14−ci−1′(4Ai+2Ai+1−Di−1′)=ci(4Ai+2Ai+1−Di−1′),∀i∈{1,...,N−2}DN−1′=13−cN−2′(4AN−1+2AN−DN−2′)

Finally, we can do Backward Substitution to find q and Y:

qN−1=uN−1′qi=ui′−ci′qi+1,∀i∈{0,...,N−2}YN−1=DN−1′Yi=Di′−ci′Yi+1,∀i∈{0,...,N−2}

With those values, we can finally calculate H1=Y−11+vtqqvtY.
Given that v0=vN−1=1, and v1=v2=...=vN−2=0, its dot products
with q and Y are respectively vtq=q0+qN−1 and
vtY=Y0+YN−1. Thus:

H1=Y−11+q0+qN−1q(Y0+YN−1)

Once we have H1, we can get H2 (the array of second handles) as follows:

H2,i=2Ai+1−H1,i+1,∀i∈{0,...,N−2}H2,N−1=2A0−H1,0

Because the matrix R always follows the same pattern (and thus T,u,v as well),
we can define a memo list for c′ and u′ to avoid recalculation. We cannot
memoize D and Y, however, because they are always different matrices. We
cannot make a memo for q either, but we can calculate it faster because u′
can be memoized.

Parameters:

**anchors** ( [_Point3DLike\_Array_](https://docs.manim.community/en/stable/reference/manim.typing.html#manim.typing.Point3DLike_Array "manim.typing.Point3DLike_Array")) – Anchors of a closed cubic spline.

Returns:

A tuple of two arrays: one containing the 1st handle for every curve in
the closed cubic spline, and the other containing the 2nd handles.

Return type:

`tuple` \[ [`Point3D_Array`](https://docs.manim.community/en/stable/reference/manim.typing.html#manim.typing.Point3D_Array "manim.typing.Point3D_Array"), [`Point3D_Array`](https://docs.manim.community/en/stable/reference/manim.typing.html#manim.typing.Point3D_Array "manim.typing.Point3D_Array")\]

get\_smooth\_cubic\_bezier\_handle\_points( _anchors_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/utils/bezier.html#get_smooth_cubic_bezier_handle_points) [¶](https://docs.manim.community/en/stable/reference/manim.utils.bezier.html#manim.utils.bezier.get_smooth_cubic_bezier_handle_points "Link to this definition")

Given an array of anchors for a cubic spline (array of connected cubic
Bézier curves), compute the 1st and 2nd handle for every curve, so that
the resulting spline is smooth.

Parameters:

**anchors** ( [_Point3DLike\_Array_](https://docs.manim.community/en/stable/reference/manim.typing.html#manim.typing.Point3DLike_Array "manim.typing.Point3DLike_Array")) – Anchors of a cubic spline.

Returns:

A tuple of two arrays: one containing the 1st handle for every curve in
the cubic spline, and the other containing the 2nd handles.

Return type:

`tuple` \[ [`Point3D_Array`](https://docs.manim.community/en/stable/reference/manim.typing.html#manim.typing.Point3D_Array "manim.typing.Point3D_Array"), [`Point3D_Array`](https://docs.manim.community/en/stable/reference/manim.typing.html#manim.typing.Point3D_Array "manim.typing.Point3D_Array")\]

get\_smooth\_open\_cubic\_bezier\_handle\_points( _anchors_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/utils/bezier.html#get_smooth_open_cubic_bezier_handle_points) [¶](https://docs.manim.community/en/stable/reference/manim.utils.bezier.html#manim.utils.bezier.get_smooth_open_cubic_bezier_handle_points "Link to this definition")

Special case of [`get_smooth_cubic_bezier_handle_points()`](https://docs.manim.community/en/stable/reference/manim.utils.bezier.html#manim.utils.bezier.get_smooth_cubic_bezier_handle_points "manim.utils.bezier.get_smooth_cubic_bezier_handle_points"),
when the `anchors` do not form a closed loop.

Note

A system of equations must be solved to get the first handles of
every Bèzier curve (referred to as H1).
Then H2 (the second handles) can be obtained separately.

See also

The equations were obtained from:

- [Smooth Bézier Spline Through Prescribed Points. (2012). Particle in Cell Consulting LLC.](https://www.particleincell.com/2012/bezier-splines/)

- [Conditions on control points for continuous curvature. (2016). Jaco Stuifbergen.](http://www.jacos.nl/jacos_html/spline/theory/theory_2.html)


Warning

The equations in the first webpage have some typos which were corrected in the comments.

In general, if there are N+1 anchors, there will be N Bézier curves
and thus N pairs of handles to find. We must solve the following
system of equations for the 1st handles (example for N=5):

(2100014100014100014100027)(H1,0H1,1H1,2H1,3H1,4)=(A0+2A14A1+2A24A2+2A34A3+2A48A4+A5)

which will be expressed as TH1=D.
T is a tridiagonal matrix, so the system can be solved in O(N)
operations. Here we shall use Thomas’ algorithm or the tridiagonal matrix
algorithm.

See also

[Tridiagonal matrix algorithm. Wikipedia.](https://en.wikipedia.org/wiki/Tridiagonal_matrix_algorithm)

Define:

- a=\[a0,a1,...,aN−2\] as T’s lower diagonal of N−1 elements,
such that a0=a1=...=aN−3=1, and aN−2=2;

- b=\[b0,b1,...,bN−2,bN−1\] as T’s main diagonal of N elements,
such that b0=2, b1=b2=...=bN−2=4, and bN−1=7;

- c=\[c0,c1,...,cN−2\] as T’s upper diagonal of N−1 elements,
such that c0=c1=...=cN−2=1: this diagonal is filled with ones.


If, according to Thomas’ algorithm, we define:

c0′=c0b0ci′=cibi−ai−1ci−1′,∀i∈{1,...,N−2}D0′=1b0D0Di′=1bi−ai−1c′i−1(Di−ai−1Di−1′),∀i∈{1,...,N−1}

Then:

c0′=0.5ci′=14−ci−1′,∀i∈{1,...,N−2}D0′=0.5A0+A1Di′=14−ci−1′(4Ai+2Ai+1−Di−1′)=ci(4Ai+2Ai+1−Di−1′),∀i∈{1,...,N−2}DN−1′=17−2cN−2′(8AN−1+AN−2DN−2′)

Finally, we can do Backward Substitution to find H1:

H1,N−1=DN−1′H1,i=Di′−ci′H1,i+1,∀i∈{0,...,N−2}

Once we have H1, we can get H2 (the array of second handles) as follows:

H2,i=2Ai+1−H1,i+1,∀i∈{0,...,N−2}H2,N−1=0.5AN+0.5H1,N−1

As the matrix T always follows the same pattern, we can define a memo list
for c′ to avoid recalculation. We cannot do the same for D, however,
because it is always a different matrix.

Parameters:

**anchors** ( [_Point3DLike\_Array_](https://docs.manim.community/en/stable/reference/manim.typing.html#manim.typing.Point3DLike_Array "manim.typing.Point3DLike_Array")) – Anchors of an open cubic spline.

Returns:

A tuple of two arrays: one containing the 1st handle for every curve in
the open cubic spline, and the other containing the 2nd handles.

Return type:

`tuple` \[ [`Point3D_Array`](https://docs.manim.community/en/stable/reference/manim.typing.html#manim.typing.Point3D_Array "manim.typing.Point3D_Array"), [`Point3D_Array`](https://docs.manim.community/en/stable/reference/manim.typing.html#manim.typing.Point3D_Array "manim.typing.Point3D_Array")\]

integer\_interpolate( _start_, _end_, _alpha_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/utils/bezier.html#integer_interpolate) [¶](https://docs.manim.community/en/stable/reference/manim.utils.bezier.html#manim.utils.bezier.integer_interpolate "Link to this definition")

This is a variant of interpolate that returns an integer and the residual

Parameters:

- **start** ( _float_) – The start of the range

- **end** ( _float_) – The end of the range

- **alpha** ( _float_) – a float between 0 and 1.


Returns:

This returns an integer between start and end (inclusive) representing
appropriate interpolation between them, along with a
“residue” representing a new proportion between the
returned integer and the next one of the
list.

Return type:

tuple\[int, float\]

Example

```
>>> integer, residue = integer_interpolate(start=0, end=10, alpha=0.46)
>>> np.allclose((integer, residue), (4, 0.6))
True

```

Copy to clipboard

interpolate( _start:float_, _end:float_, _alpha:float_)→float [\[source\]](https://docs.manim.community/en/stable/_modules/manim/utils/bezier.html#interpolate) [¶](https://docs.manim.community/en/stable/reference/manim.utils.bezier.html#manim.utils.bezier.interpolate "Link to this definition")interpolate( _start:float_, _end:float_, _alpha:[ColVector](https://docs.manim.community/en/stable/reference/manim.typing.html#manim.typing.ColVector "manim.typing.ColVector")_)→[ColVector](https://docs.manim.community/en/stable/reference/manim.typing.html#manim.typing.ColVector "manim.typing.ColVector")interpolate( _start:[Point3D](https://docs.manim.community/en/stable/reference/manim.typing.html#manim.typing.Point3D "manim.typing.Point3D")_, _end:[Point3D](https://docs.manim.community/en/stable/reference/manim.typing.html#manim.typing.Point3D "manim.typing.Point3D")_, _alpha:float_)→[Point3D](https://docs.manim.community/en/stable/reference/manim.typing.html#manim.typing.Point3D "manim.typing.Point3D")interpolate( _start:[Point3D](https://docs.manim.community/en/stable/reference/manim.typing.html#manim.typing.Point3D "manim.typing.Point3D")_, _end:[Point3D](https://docs.manim.community/en/stable/reference/manim.typing.html#manim.typing.Point3D "manim.typing.Point3D")_, _alpha:[ColVector](https://docs.manim.community/en/stable/reference/manim.typing.html#manim.typing.ColVector "manim.typing.ColVector")_)→[Point3D\_Array](https://docs.manim.community/en/stable/reference/manim.typing.html#manim.typing.Point3D_Array "manim.typing.Point3D_Array")

Linearly interpolates between two values `start` and `end`.

Parameters:

- **start** – The start of the range.

- **end** – The end of the range.

- **alpha** – A float between 0 and 1, or an (n,1) column vector containing
n floats between 0 and 1 to interpolate in a vectorized fashion.


Returns:

The result of the linear interpolation.

- If `start` and `end` are of type `float`, and:

  - `alpha` is also a `float`, the return is simply another `float`.

  - `alpha` is a [`ColVector`](https://docs.manim.community/en/stable/reference/manim.typing.html#manim.typing.ColVector "manim.typing.ColVector"), the return is another [`ColVector`](https://docs.manim.community/en/stable/reference/manim.typing.html#manim.typing.ColVector "manim.typing.ColVector").
- If `start` and `end` are of type [`Point3D`](https://docs.manim.community/en/stable/reference/manim.typing.html#manim.typing.Point3D "manim.typing.Point3D"), and:

  - `alpha` is a `float`, the return is another [`Point3D`](https://docs.manim.community/en/stable/reference/manim.typing.html#manim.typing.Point3D "manim.typing.Point3D").

  - `alpha` is a [`ColVector`](https://docs.manim.community/en/stable/reference/manim.typing.html#manim.typing.ColVector "manim.typing.ColVector"), the return is a [`Point3D_Array`](https://docs.manim.community/en/stable/reference/manim.typing.html#manim.typing.Point3D_Array "manim.typing.Point3D_Array").

Return type:

`float` \| [`ColVector`](https://docs.manim.community/en/stable/reference/manim.typing.html#manim.typing.ColVector "manim.typing.ColVector") \| [`Point3D`](https://docs.manim.community/en/stable/reference/manim.typing.html#manim.typing.Point3D "manim.typing.Point3D") \| [`Point3D_Array`](https://docs.manim.community/en/stable/reference/manim.typing.html#manim.typing.Point3D_Array "manim.typing.Point3D_Array")

inverse\_interpolate( _start:float_, _end:float_, _value:float_)→float [\[source\]](https://docs.manim.community/en/stable/_modules/manim/utils/bezier.html#inverse_interpolate) [¶](https://docs.manim.community/en/stable/reference/manim.utils.bezier.html#manim.utils.bezier.inverse_interpolate "Link to this definition")inverse\_interpolate( _start:float_, _end:float_, _value:[Point3D](https://docs.manim.community/en/stable/reference/manim.typing.html#manim.typing.Point3D "manim.typing.Point3D")_)→[Point3D](https://docs.manim.community/en/stable/reference/manim.typing.html#manim.typing.Point3D "manim.typing.Point3D")inverse\_interpolate( _start:[Point3D](https://docs.manim.community/en/stable/reference/manim.typing.html#manim.typing.Point3D "manim.typing.Point3D")_, _end:[Point3D](https://docs.manim.community/en/stable/reference/manim.typing.html#manim.typing.Point3D "manim.typing.Point3D")_, _value:[Point3D](https://docs.manim.community/en/stable/reference/manim.typing.html#manim.typing.Point3D "manim.typing.Point3D")_)→[Point3D](https://docs.manim.community/en/stable/reference/manim.typing.html#manim.typing.Point3D "manim.typing.Point3D")

Perform inverse interpolation to determine the alpha
values that would produce the specified `value`
given the `start` and `end` values or points.

Parameters:

- **start** – The start value or point of the interpolation.

- **end** – The end value or point of the interpolation.

- **value** – The value or point for which the alpha value
should be determined.


Returns:

- _The alpha values producing the given input_

- when interpolating between `start` and `end`.


Example

```
>>> inverse_interpolate(start=2, end=6, value=4)
np.float64(0.5)

>>> start = np.array([1, 2, 1])
>>> end = np.array([7, 8, 11])
>>> value = np.array([4, 5, 5])
>>> inverse_interpolate(start, end, value)
array([0.5, 0.5, 0.4])

```

Copy to clipboard

is\_closed( _points_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/utils/bezier.html#is_closed) [¶](https://docs.manim.community/en/stable/reference/manim.utils.bezier.html#manim.utils.bezier.is_closed "Link to this definition")

Returns `True` if the spline given by `points` is closed, by
checking if its first and last points are close to each other, or\`\`False\`\`
otherwise.

Note

This function reimplements `np.allclose()`, because repeated
calling of `np.allclose()` for only 2 points is inefficient.

Parameters:

**points** ( [_Point3D\_Array_](https://docs.manim.community/en/stable/reference/manim.typing.html#manim.typing.Point3D_Array "manim.typing.Point3D_Array")) – An array of points defining a spline.

Returns:

Whether the first and last points of the array are close enough or not
to be considered the same, thus considering the defined spline as
closed.

Return type:

`bool`

Examples

```
>>> import numpy as np
>>> from manim import is_closed
>>> is_closed(
...     np.array(
...         [\
...             [0, 0, 0],\
...             [1, 2, 3],\
...             [3, 2, 1],\
...             [0, 0, 0],\
...         ]
...     )
... )
True
>>> is_closed(
...     np.array(
...         [\
...             [0, 0, 0],\
...             [1, 2, 3],\
...             [3, 2, 1],\
...             [1e-10, 1e-10, 1e-10],\
...         ]
...     )
... )
True
>>> is_closed(
...     np.array(
...         [\
...             [0, 0, 0],\
...             [1, 2, 3],\
...             [3, 2, 1],\
...             [1e-2, 1e-2, 1e-2],\
...         ]
...     )
... )
False

```

Copy to clipboard

match\_interpolate( _new\_start:float_, _new\_end:float_, _old\_start:float_, _old\_end:float_, _old\_value:float_)→float [\[source\]](https://docs.manim.community/en/stable/_modules/manim/utils/bezier.html#match_interpolate) [¶](https://docs.manim.community/en/stable/reference/manim.utils.bezier.html#manim.utils.bezier.match_interpolate "Link to this definition")match\_interpolate( _new\_start:float_, _new\_end:float_, _old\_start:float_, _old\_end:float_, _old\_value:[Point3D](https://docs.manim.community/en/stable/reference/manim.typing.html#manim.typing.Point3D "manim.typing.Point3D")_)→[Point3D](https://docs.manim.community/en/stable/reference/manim.typing.html#manim.typing.Point3D "manim.typing.Point3D")

Interpolate a value from an old range to a new range.

Parameters:

- **new\_start** – The start of the new range.

- **new\_end** – The end of the new range.

- **old\_start** – The start of the old range.

- **old\_end** – The end of the old range.

- **old\_value** – The value within the old range whose corresponding
value in the new range (with the same alpha value)
is desired.


Return type:

The interpolated value within the new range.

Examples

```
>>> match_interpolate(0, 100, 10, 20, 15)
np.float64(50.0)

```

Copy to clipboard

mid( _start:float_, _end:float_)→float [\[source\]](https://docs.manim.community/en/stable/_modules/manim/utils/bezier.html#mid) [¶](https://docs.manim.community/en/stable/reference/manim.utils.bezier.html#manim.utils.bezier.mid "Link to this definition")mid( _start:[Point3D](https://docs.manim.community/en/stable/reference/manim.typing.html#manim.typing.Point3D "manim.typing.Point3D")_, _end:[Point3D](https://docs.manim.community/en/stable/reference/manim.typing.html#manim.typing.Point3D "manim.typing.Point3D")_)→[Point3D](https://docs.manim.community/en/stable/reference/manim.typing.html#manim.typing.Point3D "manim.typing.Point3D")

Returns the midpoint between two values.

Parameters:

- **start** – The first value

- **end** – The second value


Return type:

The midpoint between the two values

partial\_bezier\_points( _points_, _a_, _b_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/utils/bezier.html#partial_bezier_points) [¶](https://docs.manim.community/en/stable/reference/manim.utils.bezier.html#manim.utils.bezier.partial_bezier_points "Link to this definition")

Given an array of `points` which define a Bézier curve, and two numbers a,b
such that 0≤a<b≤1, return an array of the same size, which describes the
portion of the original Bézier curve on the interval \[a,b\].

[`partial_bezier_points()`](https://docs.manim.community/en/stable/reference/manim.utils.bezier.html#manim.utils.bezier.partial_bezier_points "manim.utils.bezier.partial_bezier_points") is conceptually equivalent to calling [`split_bezier()`](https://docs.manim.community/en/stable/reference/manim.utils.bezier.html#manim.utils.bezier.split_bezier "manim.utils.bezier.split_bezier")
twice and discarding unused Bézier curves, but this is more efficient and doesn’t waste
computations.

See also

See [`split_bezier()`](https://docs.manim.community/en/stable/reference/manim.utils.bezier.html#manim.utils.bezier.split_bezier "manim.utils.bezier.split_bezier") for an explanation on how to split Bézier curves.

Note

To find the portion of a Bézier curve with t between a and b:

1. Split the curve at t=a and extract its 2nd subcurve.

2. We cannot evaluate the new subcurve at t=b because its range of values for t is different.
To find the correct value, we need to transform the interval \[a,1\] into \[0,1\]
by first subtracting a to get \[0,1−a\] and then dividing by 1−a. Thus, our new
value must be t=b−a1−a. Define u=b−a1−a.

3. Split the subcurve at t=u and extract its 1st subcurve.


The final portion is a linear combination of points, and thus the process can be
summarized as a linear transformation by some matrix in terms of a and b.
This matrix is given explicitly for Bézier curves up to degree 3, which are often used in Manim.
For higher degrees, the algorithm described previously is used.

For the case of a quadratic Bézier curve:

- Step 1:


H1′=((1−a)22(1−a)aa20(1−a)a001)(p0p1p2)

- Step 2:


H0″=(100(1−u)u0(1−u)22(1−u)uu2)H1′=(100(1−u)u0(1−u)22(1−u)uu2)((1−a)22(1−a)aa20(1−a)a001)(p0p1p2)=((1−a)22(1−a)aa2(1−a)(1−b)a(1−b)+(1−a)bab(1−b)22(1−b)bb2)(p0p1p2)

from where one can define a (3,3) matrix P2 which, when applied over
the array of `points`, will return the desired partial quadratic Bézier curve:

P2=((1−a)22(1−a)aa2(1−a)(1−b)a(1−b)+(1−a)bab(1−b)22(1−b)bb2)

Similarly, for the cubic Bézier curve case, one can define the following
(4,4) matrix P3:

P3=((1−a)33(1−a)2a3(1−a)a2a3(1−a)2(1−b)2(1−a)a(1−b)+(1−a)2ba2(1−b)+2(1−a)aba2b(1−a)(1−b)2a(1−b)2+2(1−a)(1−b)b2a(1−b)b+(1−a)b2ab2(1−b)33(1−b)2b3(1−b)b2b3)

Parameters:

- **points** ( [_BezierPointsLike_](https://docs.manim.community/en/stable/reference/manim.typing.html#manim.typing.BezierPointsLike "manim.typing.BezierPointsLike")) – set of points defining the bezier curve.

- **a** ( _float_) – lower bound of the desired partial bezier curve.

- **b** ( _float_) – upper bound of the desired partial bezier curve.


Returns:

An array containing the control points defining the partial Bézier curve.

Return type:

[`BezierPoints`](https://docs.manim.community/en/stable/reference/manim.typing.html#manim.typing.BezierPoints "manim.typing.BezierPoints")

point\_lies\_on\_bezier( _point_, _control\_points_, _round\_to=1e-06_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/utils/bezier.html#point_lies_on_bezier) [¶](https://docs.manim.community/en/stable/reference/manim.utils.bezier.html#manim.utils.bezier.point_lies_on_bezier "Link to this definition")

Checks if a given point lies on the bezier curves with the given control points.

This is done by solving the bezier polynomial with the point as the constant term; if
any real roots exist, the point lies on the bezier curve.

Parameters:

- **point** ( [_Point3DLike_](https://docs.manim.community/en/stable/reference/manim.typing.html#manim.typing.Point3DLike "manim.typing.Point3DLike")) – The Cartesian Coordinates of the point to check.

- **control\_points** ( [_BezierPointsLike_](https://docs.manim.community/en/stable/reference/manim.typing.html#manim.typing.BezierPointsLike "manim.typing.BezierPointsLike")) – The Cartesian Coordinates of the ordered control
points of the bezier curve on which the point may
or may not lie.

- **round\_to** ( _float_) – A float whose number of decimal places all values
such as coordinates of points will be rounded.


Returns:

Whether the point lies on the curve.

Return type:

bool

proportions\_along\_bezier\_curve\_for\_point( _point_, _control\_points_, _round\_to=1e-06_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/utils/bezier.html#proportions_along_bezier_curve_for_point) [¶](https://docs.manim.community/en/stable/reference/manim.utils.bezier.html#manim.utils.bezier.proportions_along_bezier_curve_for_point "Link to this definition")

Obtains the proportion along the bezier curve corresponding to a given point
given the bezier curve’s control points.

The bezier polynomial is constructed using the coordinates of the given point
as well as the bezier curve’s control points. On solving the polynomial for each dimension,
if there are roots common to every dimension, those roots give the proportion along the
curve the point is at. If there are no real roots, the point does not lie on the curve.

Parameters:

- **point** ( [_Point3DLike_](https://docs.manim.community/en/stable/reference/manim.typing.html#manim.typing.Point3DLike "manim.typing.Point3DLike")) – The Cartesian Coordinates of the point whose parameter
should be obtained.

- **control\_points** ( [_BezierPointsLike_](https://docs.manim.community/en/stable/reference/manim.typing.html#manim.typing.BezierPointsLike "manim.typing.BezierPointsLike")) – The Cartesian Coordinates of the ordered control
points of the bezier curve on which the point may
or may not lie.

- **round\_to** ( _float_) – A float whose number of decimal places all values
such as coordinates of points will be rounded.


Returns:

List containing possible parameters (the proportions along the bezier curve)
for the given point on the given bezier curve.
This usually only contains one or zero elements, but if the
point is, say, at the beginning/end of a closed loop, may return
a list with more than 1 value, corresponding to the beginning and
end etc. of the loop.

Return type:

np.ndarray\[float\]

Raises:

**ValueError** – When `point` and the control points have different shapes.

split\_bezier( _points_, _t_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/utils/bezier.html#split_bezier) [¶](https://docs.manim.community/en/stable/reference/manim.utils.bezier.html#manim.utils.bezier.split_bezier "Link to this definition")

Split a Bézier curve at argument `t` into two curves.

Note

See also

[A Primer on Bézier Curves #10: Splitting curves. Pomax.](https://pomax.github.io/bezierinfo/#splitting)

As an example for a cubic Bézier curve, let p0,p1,p2,p3 be the points
needed for the curve C0=\[p0,p1,p2,p3\].

Define the 3 linear Béziers L0,L1,L2 as interpolations of p0,p1,p2,p3:

L0(t)=p0+t(p1−p0)L1(t)=p1+t(p2−p1)L2(t)=p2+t(p3−p2)

Define the 2 quadratic Béziers Q0,Q1 as interpolations of L0,L1,L2:

Q0(t)=L0(t)+t(L1(t)−L0(t))Q1(t)=L1(t)+t(L2(t)−L1(t))

Then C0 is the following interpolation of Q0 and Q1:

C0(t)=Q0(t)+t(Q1(t)−Q0(t))

Evaluating C0 at a value t=t′ splits C0 into two cubic Béziers H0
and H1, defined by some of the points we calculated earlier:

H0=\[p0,L0(t′),Q0(t′),C0(t′)\]H1=\[p0(t′),Q1(t′),L2(t′),p3\]

As the resulting curves are obtained from linear combinations of `points`, everything can
be encoded into a matrix for efficiency, which is done for Bézier curves of degree up to 3.

See also

[A Primer on Bézier Curves #11: Splitting curves using matrices. Pomax.](https://pomax.github.io/bezierinfo/#matrixsplit)

For the simpler case of a quadratic Bézier curve:

H0=(p0(1−t)p0+tp1(1−t)2p0+2(1−t)tp1+t2p2)=(100(1−t)t0(1−t)22(1−t)tt2)(p0p1p2)H1=((1−t)2p0+2(1−t)tp1+t2p2(1−t)p1+tp2p2)=((1−t)22(1−t)tt20(1−t)t001)(p0p1p2)

from where one can define a (6,3) split matrix S2 which can multiply
the array of `points` to compute the return value:

S2=(100(1−t)t0(1−t)22(1−t)tt2(1−t)22(1−t)tt20(1−t)t001)S2P=(100(1−t)t0(1−t)22(1−t)tt2(1−t)22(1−t)tt20(1−t)t001)(p0p1p2)=(\|H0\|\|H1\|)

For the previous example with a cubic Bézier curve:

H0=(p0(1−t)p0+tp1(1−t)2p0+2(1−t)tp1+t2p2(1−t)3p0+3(1−t)2tp1+3(1−t)t2p2+t3p3)=(1000(1−t)t00(1−t)22(1−t)tt20(1−t)33(1−t)2t3(1−t)t2t3)(p0p1p2p3)H1=((1−t)3p0+3(1−t)2tp1+3(1−t)t2p2+t3p3(1−t)2p1+2(1−t)tp2+t2p3(1−t)p2+tp3p3)=((1−t)33(1−t)2t3(1−t)t2t30(1−t)22(1−t)tt200(1−t)t0001)(p0p1p2p3)

from where one can define a (8,4) split matrix S3 which can multiply
the array of `points` to compute the return value:

S3=(1000(1−t)t00(1−t)22(1−t)tt20(1−t)33(1−t)2t3(1−t)t2t3(1−t)33(1−t)2t3(1−t)t2t30(1−t)22(1−t)tt200(1−t)t0001)S3P=(1000(1−t)t00(1−t)22(1−t)tt20(1−t)33(1−t)2t3(1−t)t2t3(1−t)33(1−t)2t3(1−t)t2t30(1−t)22(1−t)tt200(1−t)t0001)(p0p1p2p3)=(\|H0\|\|H1\|)

Parameters:

- **points** ( [_BezierPointsLike_](https://docs.manim.community/en/stable/reference/manim.typing.html#manim.typing.BezierPointsLike "manim.typing.BezierPointsLike")) – The control points of the Bézier curve.

- **t** ( _float_) – The `t`-value at which to split the Bézier curve.


Returns:

An array containing the control points defining the two Bézier curves.

Return type:

[`Point3D_Array`](https://docs.manim.community/en/stable/reference/manim.typing.html#manim.typing.Point3D_Array "manim.typing.Point3D_Array")

subdivide\_bezier( _points_, _n\_divisions_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/utils/bezier.html#subdivide_bezier) [¶](https://docs.manim.community/en/stable/reference/manim.utils.bezier.html#manim.utils.bezier.subdivide_bezier "Link to this definition")

Subdivide a Bézier curve into n subcurves which have the same shape.

The points at which the curve is split are located at the
arguments t=in, for i∈{1,...,n−1}.

See also

- See [`split_bezier()`](https://docs.manim.community/en/stable/reference/manim.utils.bezier.html#manim.utils.bezier.split_bezier "manim.utils.bezier.split_bezier") for an explanation on how to split Bézier curves.

- See [`partial_bezier_points()`](https://docs.manim.community/en/stable/reference/manim.utils.bezier.html#manim.utils.bezier.partial_bezier_points "manim.utils.bezier.partial_bezier_points") for an extra understanding of this function.


Note

The resulting subcurves can be expressed as linear combinations of
`points`, which can be encoded in a single matrix that is precalculated
for 2nd and 3rd degree Bézier curves.

As an example for a quadratic Bézier curve: taking inspiration from the
explanation in [`partial_bezier_points()`](https://docs.manim.community/en/stable/reference/manim.utils.bezier.html#manim.utils.bezier.partial_bezier_points "manim.utils.bezier.partial_bezier_points"), where the following matrix
P2 was defined to extract the portion of a quadratic Bézier
curve for t∈\[a,b\]:

P2=((1−a)22(1−a)aa2(1−a)(1−b)a(1−b)+(1−a)bab(1−b)22(1−b)bb2)

the plan is to replace \[a,b\] with
\[i−1n,in\],∀i∈{1,...,n}.

As an example for n=2 divisions, construct P1 for
the interval \[0,12\], and P2 for the
interval \[12,1\]:

P1=(1000.50.500.250.50.25),P2=(0.250.50.2500.50.5001)

Therefore, the following (6,3) subdivision matrix D2 can be
constructed, which will subdivide an array of `points` into 2 parts:

D2=(M1M2)=(1000.50.500.250.50.250.250.50.2500.50.5001)

For quadratic and cubic Bézier curves, the subdivision matrices are memoized for
efficiency. For higher degree curves, an iterative algorithm inspired by the
one from [`split_bezier()`](https://docs.manim.community/en/stable/reference/manim.utils.bezier.html#manim.utils.bezier.split_bezier "manim.utils.bezier.split_bezier") is used instead.

![../_images/bezier_subdivision_example.png](https://docs.manim.community/en/stable/_images/bezier_subdivision_example.png)Parameters:

- **points** ( [_BezierPointsLike_](https://docs.manim.community/en/stable/reference/manim.typing.html#manim.typing.BezierPointsLike "manim.typing.BezierPointsLike")) – The control points of the Bézier curve.

- **n\_divisions** ( _int_) – The number of curves to subdivide the Bézier curve into


Returns:

An array containing the points defining the new n subcurves.

Return type:

[`Spline`](https://docs.manim.community/en/stable/reference/manim.typing.html#manim.typing.Spline "manim.typing.Spline")