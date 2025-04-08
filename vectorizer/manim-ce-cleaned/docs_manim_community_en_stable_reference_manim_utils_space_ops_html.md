# space\_ops [¶](https://docs.manim.community/en/stable/reference/manim.utils.space_ops.html\#module-manim.utils.space_ops "Link to this heading")

Utility functions for two- and three-dimensional vectors.

Functions

R3\_to\_complex( _point_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/utils/space_ops.html#R3_to_complex) [¶](https://docs.manim.community/en/stable/reference/manim.utils.space_ops.html#manim.utils.space_ops.R3_to_complex "Link to this definition")Parameters:

**point** ( _Sequence_ _\[_ _float_ _\]_)

Return type:

_ndarray_

angle\_axis\_from\_quaternion( _quaternion_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/utils/space_ops.html#angle_axis_from_quaternion) [¶](https://docs.manim.community/en/stable/reference/manim.utils.space_ops.html#manim.utils.space_ops.angle_axis_from_quaternion "Link to this definition")

Gets angle and axis from a quaternion.

Parameters:

**quaternion** ( _Sequence_ _\[_ _float_ _\]_) – The quaternion from which we get the angle and axis.

Returns:

Gives the angle and axis

Return type:

Sequence\[float\]

angle\_between\_vectors( _v1_, _v2_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/utils/space_ops.html#angle_between_vectors) [¶](https://docs.manim.community/en/stable/reference/manim.utils.space_ops.html#manim.utils.space_ops.angle_between_vectors "Link to this definition")

Returns the angle between two vectors.
This angle will always be between 0 and pi

Parameters:

- **v1** ( _ndarray_) – The first vector.

- **v2** ( _ndarray_) – The second vector.


Returns:

The angle between the vectors.

Return type:

float

angle\_of\_vector( _vector_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/utils/space_ops.html#angle_of_vector) [¶](https://docs.manim.community/en/stable/reference/manim.utils.space_ops.html#manim.utils.space_ops.angle_of_vector "Link to this definition")

Returns polar coordinate theta when vector is projected on xy plane.

Parameters:

**vector** ( _Sequence_ _\[_ _float_ _\]_ _\|_ _ndarray_) – The vector to find the angle for.

Returns:

The angle of the vector projected.

Return type:

float

cartesian\_to\_spherical( _vec_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/utils/space_ops.html#cartesian_to_spherical) [¶](https://docs.manim.community/en/stable/reference/manim.utils.space_ops.html#manim.utils.space_ops.cartesian_to_spherical "Link to this definition")

Returns an array of numbers corresponding to each
polar coordinate value (distance, phi, theta).

Parameters:

**vec** ( _Sequence_ _\[_ _float_ _\]_) – A numpy array `[x, y, z]`.

Return type:

_ndarray_

center\_of\_mass( _points_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/utils/space_ops.html#center_of_mass) [¶](https://docs.manim.community/en/stable/reference/manim.utils.space_ops.html#manim.utils.space_ops.center_of_mass "Link to this definition")

Gets the center of mass of the points in space.

Parameters:

**points** ( [_PointNDLike\_Array_](https://docs.manim.community/en/stable/reference/manim.typing.html#manim.typing.PointNDLike_Array "manim.typing.PointNDLike_Array")) – The points to find the center of mass from.

Returns:

The center of mass of the points.

Return type:

np.ndarray

compass\_directions( _n=4_, _start\_vect=array(\[1.,0.,0.\])_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/utils/space_ops.html#compass_directions) [¶](https://docs.manim.community/en/stable/reference/manim.utils.space_ops.html#manim.utils.space_ops.compass_directions "Link to this definition")

Finds the cardinal directions using tau.

Parameters:

- **n** ( _int_) – The amount to be rotated, by default 4

- **start\_vect** ( _ndarray_) – The direction for the angle to start with, by default RIGHT


Returns:

The angle which has been rotated.

Return type:

np.ndarray

complex\_func\_to\_R3\_func( _complex\_func_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/utils/space_ops.html#complex_func_to_R3_func) [¶](https://docs.manim.community/en/stable/reference/manim.utils.space_ops.html#manim.utils.space_ops.complex_func_to_R3_func "Link to this definition")Parameters:

**complex\_func** ( _Callable_ _\[_ _\[_ _complex_ _\]_ _,_ _complex_ _\]_)

Return type:

_Callable_\[\[ [_Point3DLike_](https://docs.manim.community/en/stable/reference/manim.typing.html#manim.typing.Point3DLike "manim.typing.Point3DLike")\], [_Point3D_](https://docs.manim.community/en/stable/reference/manim.typing.html#manim.typing.Point3D "manim.typing.Point3D")\]

complex\_to\_R3( _complex\_num_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/utils/space_ops.html#complex_to_R3) [¶](https://docs.manim.community/en/stable/reference/manim.utils.space_ops.html#manim.utils.space_ops.complex_to_R3 "Link to this definition")Parameters:

**complex\_num** ( _complex_)

Return type:

_ndarray_

cross( _v1_, _v2_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/utils/space_ops.html#cross) [¶](https://docs.manim.community/en/stable/reference/manim.utils.space_ops.html#manim.utils.space_ops.cross "Link to this definition")Parameters:

- **v1** ( [_Vector3D_](https://docs.manim.community/en/stable/reference/manim.typing.html#manim.typing.Vector3D "manim.typing.Vector3D"))

- **v2** ( [_Vector3D_](https://docs.manim.community/en/stable/reference/manim.typing.html#manim.typing.Vector3D "manim.typing.Vector3D"))


Return type:

[_Vector3D_](https://docs.manim.community/en/stable/reference/manim.typing.html#manim.typing.Vector3D "manim.typing.Vector3D")

cross2d( _a_, _b_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/utils/space_ops.html#cross2d) [¶](https://docs.manim.community/en/stable/reference/manim.utils.space_ops.html#manim.utils.space_ops.cross2d "Link to this definition")

Compute the determinant(s) of the passed
vector (sequences).

Parameters:

- **a** ( [_Vector2D_](https://docs.manim.community/en/stable/reference/manim.typing.html#manim.typing.Vector2D "manim.typing.Vector2D") _\|_ [_Vector2D\_Array_](https://docs.manim.community/en/stable/reference/manim.typing.html#manim.typing.Vector2D_Array "manim.typing.Vector2D_Array")) – A vector or a sequence of vectors.

- **b** ( [_Vector2D_](https://docs.manim.community/en/stable/reference/manim.typing.html#manim.typing.Vector2D "manim.typing.Vector2D") _\|_ [_Vector2D\_Array_](https://docs.manim.community/en/stable/reference/manim.typing.html#manim.typing.Vector2D_Array "manim.typing.Vector2D_Array")) – A vector or a sequence of vectors.


Returns:

The determinant or sequence of determinants
of the first two components of the specified
vectors.

Return type:

Sequence\[float\] \| float

Examples

```
>>> cross2d(np.array([1, 2]), np.array([3, 4]))
np.int64(-2)
>>> cross2d(
...     np.array([[1, 2, 0], [1, 0, 0]]),
...     np.array([[3, 4, 0], [0, 1, 0]]),
... )
array([-2,  1])

```

Copy to clipboard

earclip\_triangulation( _verts_, _ring\_ends_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/utils/space_ops.html#earclip_triangulation) [¶](https://docs.manim.community/en/stable/reference/manim.utils.space_ops.html#manim.utils.space_ops.earclip_triangulation "Link to this definition")

Returns a list of indices giving a triangulation
of a polygon, potentially with holes.

Parameters:

- **verts** ( _ndarray_) – verts is a numpy array of points.

- **ring\_ends** ( _list_) – ring\_ends is a list of indices indicating where
the ends of new paths are.


Returns:

A list of indices giving a triangulation of a polygon.

Return type:

list

find\_intersection( _p0s_, _v0s_, _p1s_, _v1s_, _threshold=1e-05_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/utils/space_ops.html#find_intersection) [¶](https://docs.manim.community/en/stable/reference/manim.utils.space_ops.html#manim.utils.space_ops.find_intersection "Link to this definition")

Return the intersection of a line passing through p0 in direction v0
with one passing through p1 in direction v1 (or array of intersections
from arrays of such points/directions).
For 3d values, it returns the point on the ray p0 + v0 \* t closest to the
ray p1 + v1 \* t

Parameters:

- **p0s** ( [_Point3DLike\_Array_](https://docs.manim.community/en/stable/reference/manim.typing.html#manim.typing.Point3DLike_Array "manim.typing.Point3DLike_Array"))

- **v0s** ( [_Vector3D\_Array_](https://docs.manim.community/en/stable/reference/manim.typing.html#manim.typing.Vector3D_Array "manim.typing.Vector3D_Array"))

- **p1s** ( [_Point3DLike\_Array_](https://docs.manim.community/en/stable/reference/manim.typing.html#manim.typing.Point3DLike_Array "manim.typing.Point3DLike_Array"))

- **v1s** ( [_Vector3D\_Array_](https://docs.manim.community/en/stable/reference/manim.typing.html#manim.typing.Vector3D_Array "manim.typing.Vector3D_Array"))

- **threshold** ( _float_)


Return type:

list\[ [_Point3D_](https://docs.manim.community/en/stable/reference/manim.typing.html#manim.typing.Point3D "manim.typing.Point3D")\]

get\_unit\_normal( _v1_, _v2_, _tol=1e-06_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/utils/space_ops.html#get_unit_normal) [¶](https://docs.manim.community/en/stable/reference/manim.utils.space_ops.html#manim.utils.space_ops.get_unit_normal "Link to this definition")

Gets the unit normal of the vectors.

Parameters:

- **v1** ( [_Vector3D_](https://docs.manim.community/en/stable/reference/manim.typing.html#manim.typing.Vector3D "manim.typing.Vector3D")) – The first vector.

- **v2** ( [_Vector3D_](https://docs.manim.community/en/stable/reference/manim.typing.html#manim.typing.Vector3D "manim.typing.Vector3D")) – The second vector

- **tol** ( _float_) – \[description\], by default 1e-6


Returns:

The normal of the two vectors.

Return type:

np.ndarray

get\_winding\_number( _points_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/utils/space_ops.html#get_winding_number) [¶](https://docs.manim.community/en/stable/reference/manim.utils.space_ops.html#manim.utils.space_ops.get_winding_number "Link to this definition")

Determine the number of times a polygon winds around the origin.

The orientation is measured mathematically positively, i.e.,
counterclockwise.

Parameters:

**points** ( _Sequence_ _\[_ _ndarray_ _\]_) – The vertices of the polygon being queried.

Return type:

float

Examples

```
>>> from manim import Square, get_winding_number
>>> polygon = Square()
>>> get_winding_number(polygon.get_vertices())
np.float64(1.0)
>>> polygon.shift(2 * UP)
Square
>>> get_winding_number(polygon.get_vertices())
np.float64(0.0)

```

Copy to clipboard

line\_intersection( _line1_, _line2_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/utils/space_ops.html#line_intersection) [¶](https://docs.manim.community/en/stable/reference/manim.utils.space_ops.html#manim.utils.space_ops.line_intersection "Link to this definition")

Returns the intersection point of two lines, each defined by
a pair of distinct points lying on the line.

Parameters:

- **line1** ( _Sequence_ _\[_ _ndarray_ _\]_) – A list of two points that determine the first line.

- **line2** ( _Sequence_ _\[_ _ndarray_ _\]_) – A list of two points that determine the second line.


Returns:

The intersection points of the two lines which are intersecting.

Return type:

np.ndarray

Raises:

**ValueError** – Error is produced if the two lines don’t intersect with each other
or if the coordinates don’t lie on the xy-plane.

midpoint( _point1_, _point2_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/utils/space_ops.html#midpoint) [¶](https://docs.manim.community/en/stable/reference/manim.utils.space_ops.html#manim.utils.space_ops.midpoint "Link to this definition")

Gets the midpoint of two points.

Parameters:

- **point1** ( _Sequence_ _\[_ _float_ _\]_) – The first point.

- **point2** ( _Sequence_ _\[_ _float_ _\]_) – The second point.


Returns:

The midpoint of the points

Return type:

[Union](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.boolean_ops.Union.html#manim.mobject.geometry.boolean_ops.Union "manim.mobject.geometry.boolean_ops.Union")\[float, np.ndarray\]

norm\_squared( _v_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/utils/space_ops.html#norm_squared) [¶](https://docs.manim.community/en/stable/reference/manim.utils.space_ops.html#manim.utils.space_ops.norm_squared "Link to this definition")Parameters:

**v** ( _float_)

Return type:

float

normalize( _vect_, _fall\_back=None_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/utils/space_ops.html#normalize) [¶](https://docs.manim.community/en/stable/reference/manim.utils.space_ops.html#manim.utils.space_ops.normalize "Link to this definition")Parameters:

- **vect** ( _ndarray_ _\|_ _tuple_ _\[_ _float_ _\]_)

- **fall\_back** ( _ndarray_ _\|_ _None_)


Return type:

_ndarray_

normalize\_along\_axis( _array_, _axis_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/utils/space_ops.html#normalize_along_axis) [¶](https://docs.manim.community/en/stable/reference/manim.utils.space_ops.html#manim.utils.space_ops.normalize_along_axis "Link to this definition")

Normalizes an array with the provided axis.

Parameters:

- **array** ( _ndarray_) – The array which has to be normalized.

- **axis** ( _ndarray_) – The axis to be normalized to.


Returns:

Array which has been normalized according to the axis.

Return type:

np.ndarray

perpendicular\_bisector( _line_, _norm\_vector=array(\[0.,0.,1.\])_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/utils/space_ops.html#perpendicular_bisector) [¶](https://docs.manim.community/en/stable/reference/manim.utils.space_ops.html#manim.utils.space_ops.perpendicular_bisector "Link to this definition")

Returns a list of two points that correspond
to the ends of the perpendicular bisector of the
two points given.

Parameters:

- **line** ( _Sequence_ _\[_ _ndarray_ _\]_) – a list of two numpy array points (corresponding
to the ends of a line).

- **norm\_vector** ( [_Vector3D_](https://docs.manim.community/en/stable/reference/manim.typing.html#manim.typing.Vector3D "manim.typing.Vector3D")) – the vector perpendicular to both the line given
and the perpendicular bisector.


Returns:

A list of two numpy array points that correspond
to the ends of the perpendicular bisector

Return type:

list

quaternion\_conjugate( _quaternion_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/utils/space_ops.html#quaternion_conjugate) [¶](https://docs.manim.community/en/stable/reference/manim.utils.space_ops.html#manim.utils.space_ops.quaternion_conjugate "Link to this definition")

Used for finding the conjugate of the quaternion

Parameters:

**quaternion** ( _Sequence_ _\[_ _float_ _\]_) – The quaternion for which you want to find the conjugate for.

Returns:

The conjugate of the quaternion.

Return type:

np.ndarray

quaternion\_from\_angle\_axis( _angle_, _axis_, _axis\_normalized=False_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/utils/space_ops.html#quaternion_from_angle_axis) [¶](https://docs.manim.community/en/stable/reference/manim.utils.space_ops.html#manim.utils.space_ops.quaternion_from_angle_axis "Link to this definition")

Gets a quaternion from an angle and an axis.
For more information, check [this Wikipedia page](https://en.wikipedia.org/wiki/Conversion_between_quaternions_and_Euler_angles).

Parameters:

- **angle** ( _float_) – The angle for the quaternion.

- **axis** ( _ndarray_) – The axis for the quaternion

- **axis\_normalized** ( _bool_) – Checks whether the axis is normalized, by default False


Returns:

Gives back a quaternion from the angle and axis

Return type:

list\[float\]

quaternion\_mult( _\*quats_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/utils/space_ops.html#quaternion_mult) [¶](https://docs.manim.community/en/stable/reference/manim.utils.space_ops.html#manim.utils.space_ops.quaternion_mult "Link to this definition")

Gets the Hamilton product of the quaternions provided.
For more information, check [this Wikipedia page](https://en.wikipedia.org/wiki/Quaternion).

Returns:

Returns a list of product of two quaternions.

Return type:

[Union](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.boolean_ops.Union.html#manim.mobject.geometry.boolean_ops.Union "manim.mobject.geometry.boolean_ops.Union")\[np.ndarray, List\[ [Union](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.boolean_ops.Union.html#manim.mobject.geometry.boolean_ops.Union "manim.mobject.geometry.boolean_ops.Union")\[float, np.ndarray\]\]\]

Parameters:

**quats** ( _Sequence_ _\[_ _float_ _\]_)

regular\_vertices( _n_, _\*_, _radius=1_, _start\_angle=None_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/utils/space_ops.html#regular_vertices) [¶](https://docs.manim.community/en/stable/reference/manim.utils.space_ops.html#manim.utils.space_ops.regular_vertices "Link to this definition")

Generates regularly spaced vertices around a circle centered at the origin.

Parameters:

- **n** ( _int_) – The number of vertices

- **radius** ( _float_) – The radius of the circle that the vertices are placed on.

- **start\_angle** ( _float_ _\|_ _None_) –

The angle the vertices start at.

If unspecified, for even `n` values, `0` will be used.
For odd `n` values, 90 degrees is used.


Returns:

- **vertices** ( `numpy.ndarray`) – The regularly spaced vertices.

- **start\_angle** ( `float`) – The angle the vertices start at.


Return type:

tuple\[ _ndarray_, float\]

rotate\_vector( _vector_, _angle_, _axis=array(\[0.,0.,1.\])_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/utils/space_ops.html#rotate_vector) [¶](https://docs.manim.community/en/stable/reference/manim.utils.space_ops.html#manim.utils.space_ops.rotate_vector "Link to this definition")

Function for rotating a vector.

Parameters:

- **vector** ( _ndarray_) – The vector to be rotated.

- **angle** ( _float_) – The angle to be rotated by.

- **axis** ( _ndarray_) – The axis to be rotated, by default OUT


Returns:

The rotated vector with provided angle and axis.

Return type:

np.ndarray

Raises:

**ValueError** – If vector is not of dimension 2 or 3.

rotation\_about\_z( _angle_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/utils/space_ops.html#rotation_about_z) [¶](https://docs.manim.community/en/stable/reference/manim.utils.space_ops.html#manim.utils.space_ops.rotation_about_z "Link to this definition")

Returns a rotation matrix for a given angle.

Parameters:

**angle** ( _float_) – Angle for the rotation matrix.

Returns:

Gives back the rotated matrix.

Return type:

np.ndarray

rotation\_matrix( _angle_, _axis_, _homogeneous=False_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/utils/space_ops.html#rotation_matrix) [¶](https://docs.manim.community/en/stable/reference/manim.utils.space_ops.html#manim.utils.space_ops.rotation_matrix "Link to this definition")

Rotation in R^3 about a specified axis of rotation.

Parameters:

- **angle** ( _float_)

- **axis** ( _ndarray_)

- **homogeneous** ( _bool_)


Return type:

_ndarray_

rotation\_matrix\_from\_quaternion( _quat_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/utils/space_ops.html#rotation_matrix_from_quaternion) [¶](https://docs.manim.community/en/stable/reference/manim.utils.space_ops.html#manim.utils.space_ops.rotation_matrix_from_quaternion "Link to this definition")Parameters:

**quat** ( _ndarray_)

Return type:

_ndarray_

rotation\_matrix\_transpose( _angle_, _axis_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/utils/space_ops.html#rotation_matrix_transpose) [¶](https://docs.manim.community/en/stable/reference/manim.utils.space_ops.html#manim.utils.space_ops.rotation_matrix_transpose "Link to this definition")Parameters:

- **angle** ( _float_)

- **axis** ( _ndarray_)


Return type:

_ndarray_

rotation\_matrix\_transpose\_from\_quaternion( _quat_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/utils/space_ops.html#rotation_matrix_transpose_from_quaternion) [¶](https://docs.manim.community/en/stable/reference/manim.utils.space_ops.html#manim.utils.space_ops.rotation_matrix_transpose_from_quaternion "Link to this definition")

Converts the quaternion, quat, to an equivalent rotation matrix representation.
For more information, check [this page](https://in.mathworks.com/help/driving/ref/quaternion.rotmat.html).

Parameters:

**quat** ( _ndarray_) – The quaternion which is to be converted.

Returns:

Gives back the Rotation matrix representation, returned as a 3-by-3
matrix or 3-by-3-by-N multidimensional array.

Return type:

List\[np.ndarray\]

shoelace( _x\_y_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/utils/space_ops.html#shoelace) [¶](https://docs.manim.community/en/stable/reference/manim.utils.space_ops.html#manim.utils.space_ops.shoelace "Link to this definition")

2D implementation of the shoelace formula.

Returns:

Returns signed area.

Return type:

`float`

Parameters:

**x\_y** ( [_Point2D\_Array_](https://docs.manim.community/en/stable/reference/manim.typing.html#manim.typing.Point2D_Array "manim.typing.Point2D_Array"))

shoelace\_direction( _x\_y_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/utils/space_ops.html#shoelace_direction) [¶](https://docs.manim.community/en/stable/reference/manim.utils.space_ops.html#manim.utils.space_ops.shoelace_direction "Link to this definition")

Uses the area determined by the shoelace method to determine whether
the input set of points is directed clockwise or counterclockwise.

Returns:

Either `"CW"` or `"CCW"`.

Return type:

`str`

Parameters:

**x\_y** ( [_Point2D\_Array_](https://docs.manim.community/en/stable/reference/manim.typing.html#manim.typing.Point2D_Array "manim.typing.Point2D_Array"))

spherical\_to\_cartesian( _spherical_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/utils/space_ops.html#spherical_to_cartesian) [¶](https://docs.manim.community/en/stable/reference/manim.utils.space_ops.html#manim.utils.space_ops.spherical_to_cartesian "Link to this definition")

Returns a numpy array `[x, y, z]` based on the spherical
coordinates given.

Parameters:

**spherical** ( _Sequence_ _\[_ _float_ _\]_) –

A list of three floats that correspond to the following:

r - The distance between the point and the origin.

theta - The azimuthal angle of the point to the positive x-axis.

phi - The vertical angle of the point to the positive z-axis.

Return type:

_ndarray_

thick\_diagonal( _dim_, _thickness=2_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/utils/space_ops.html#thick_diagonal) [¶](https://docs.manim.community/en/stable/reference/manim.utils.space_ops.html#manim.utils.space_ops.thick_diagonal "Link to this definition")Parameters:

- **dim** ( _int_)

- **thickness** ( _int_)


Return type:

[_MatrixMN_](https://docs.manim.community/en/stable/reference/manim.typing.html#manim.typing.MatrixMN "manim.typing.MatrixMN")

z\_to\_vector( _vector_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/utils/space_ops.html#z_to_vector) [¶](https://docs.manim.community/en/stable/reference/manim.utils.space_ops.html#manim.utils.space_ops.z_to_vector "Link to this definition")

Returns some matrix in SO(3) which takes the z-axis to the
(normalized) vector provided as an argument

Parameters:

**vector** ( _ndarray_)

Return type:

_ndarray_