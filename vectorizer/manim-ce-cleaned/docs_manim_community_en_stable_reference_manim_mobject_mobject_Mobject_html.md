# Mobject [¶](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html\#mobject "Link to this heading")

Qualified name: `manim.mobject.mobject.Mobject`

_class_ Mobject( _color=ManimColor('#FFFFFF')_, _name=None_, _dim=3_, _target=None_, _z\_index=0_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/mobject/mobject.html#Mobject) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "Link to this definition")

Bases: `object`

Mathematical Object: base class for objects that can be displayed on screen.

There is a compatibility layer that allows for
getting and setting generic attributes with `get_*`
and `set_*` methods. See [`set()`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject.set "manim.mobject.mobject.Mobject.set") for more details.

Parameters:

- **color** ( [_ParsableManimColor_](https://docs.manim.community/en/stable/reference/manim.utils.color.core.html#manim.utils.color.core.ParsableManimColor "manim.utils.color.core.ParsableManimColor") _\|_ _list_ _\[_ [_ParsableManimColor_](https://docs.manim.community/en/stable/reference/manim.utils.color.core.html#manim.utils.color.core.ParsableManimColor "manim.utils.color.core.ParsableManimColor") _\]_)

- **name** ( _str_ _\|_ _None_)

- **dim** ( _int_)

- **z\_index** ( _float_)


submobjects [¶](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject.submobjects "Link to this definition")

The contained objects.

Type:

List\[ [`Mobject`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject")\]

points [¶](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject.points "Link to this definition")

The points of the objects.

See also

[`VMobject`](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject "manim.mobject.types.vectorized_mobject.VMobject")

Type:

`numpy.ndarray`

Methods

|     |     |
| --- | --- |
| [`add`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject.add "manim.mobject.mobject.Mobject.add") | Add mobjects as submobjects. |
| [`add_animation_override`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject.add_animation_override "manim.mobject.mobject.Mobject.add_animation_override") | Add an animation override. |
| [`add_background_rectangle`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject.add_background_rectangle "manim.mobject.mobject.Mobject.add_background_rectangle") | Add a BackgroundRectangle as submobject. |
| `add_background_rectangle_to_family_members_with_points` |  |
| `add_background_rectangle_to_submobjects` |  |
| `add_n_more_submobjects` |  |
| [`add_to_back`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject.add_to_back "manim.mobject.mobject.Mobject.add_to_back") | Add all passed mobjects to the back of the submobjects. |
| [`add_updater`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject.add_updater "manim.mobject.mobject.Mobject.add_updater") | Add an update function to this mobject. |
| [`align_data`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject.align_data "manim.mobject.mobject.Mobject.align_data") | Aligns the data of this mobject with another mobject. |
| [`align_on_border`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject.align_on_border "manim.mobject.mobject.Mobject.align_on_border") | Direction just needs to be a vector pointing towards side or corner in the 2d plane. |
| `align_points` |  |
| `align_points_with_larger` |  |
| `align_submobjects` |  |
| [`align_to`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject.align_to "manim.mobject.mobject.Mobject.align_to") | Aligns mobject to another [`Mobject`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject") in a certain direction. |
| [`animation_override_for`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject.animation_override_for "manim.mobject.mobject.Mobject.animation_override_for") | Returns the function defining a specific animation override for this class. |
| [`apply_complex_function`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject.apply_complex_function "manim.mobject.mobject.Mobject.apply_complex_function") | Applies a complex function to a [`Mobject`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject"). |
| `apply_function` |  |
| `apply_function_to_position` |  |
| `apply_function_to_submobject_positions` |  |
| `apply_matrix` |  |
| `apply_over_attr_arrays` |  |
| `apply_points_function_about_point` |  |
| [`apply_to_family`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject.apply_to_family "manim.mobject.mobject.Mobject.apply_to_family") | Apply a function to `self` and every submobject with points recursively. |
| [`arrange`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject.arrange "manim.mobject.mobject.Mobject.arrange") | Sorts [`Mobject`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject") next to each other on screen. |
| [`arrange_in_grid`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject.arrange_in_grid "manim.mobject.mobject.Mobject.arrange_in_grid") | Arrange submobjects in a grid. |
| [`arrange_submobjects`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject.arrange_submobjects "manim.mobject.mobject.Mobject.arrange_submobjects") | Arrange the position of [`submobjects`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject.submobjects "manim.mobject.mobject.Mobject.submobjects") with a small buffer. |
| [`become`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject.become "manim.mobject.mobject.Mobject.become") | Edit points, colors and submobjects to be identical to another [`Mobject`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject") |
| [`center`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject.center "manim.mobject.mobject.Mobject.center") | Moves the center of the mobject to the center of the scene. |
| [`clear_updaters`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject.clear_updaters "manim.mobject.mobject.Mobject.clear_updaters") | Remove every updater. |
| [`copy`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject.copy "manim.mobject.mobject.Mobject.copy") | Create and return an identical copy of the [`Mobject`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject") including all [`submobjects`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject.submobjects "manim.mobject.mobject.Mobject.submobjects"). |
| `fade` |  |
| `fade_to` |  |
| `family_members_with_points` |  |
| [`flip`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject.flip "manim.mobject.mobject.Mobject.flip") | Flips/Mirrors an mobject about its center. |
| [`generate_points`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject.generate_points "manim.mobject.mobject.Mobject.generate_points") | Initializes [`points`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject.points "manim.mobject.mobject.Mobject.points") and therefore the shape. |
| `generate_target` |  |
| [`get_all_points`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject.get_all_points "manim.mobject.mobject.Mobject.get_all_points") | Return all points from this mobject and all submobjects. |
| `get_array_attrs` |  |
| [`get_bottom`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject.get_bottom "manim.mobject.mobject.Mobject.get_bottom") | Get bottom Point3Ds of a box bounding the [`Mobject`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject") |
| `get_boundary_point` |  |
| [`get_center`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject.get_center "manim.mobject.mobject.Mobject.get_center") | Get center Point3Ds |
| `get_center_of_mass` |  |
| [`get_color`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject.get_color "manim.mobject.mobject.Mobject.get_color") | Returns the color of the [`Mobject`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject") |
| [`get_coord`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject.get_coord "manim.mobject.mobject.Mobject.get_coord") | Meant to generalize `get_x`, `get_y` and `get_z` |
| [`get_corner`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject.get_corner "manim.mobject.mobject.Mobject.get_corner") | Get corner Point3Ds for certain direction. |
| [`get_critical_point`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject.get_critical_point "manim.mobject.mobject.Mobject.get_critical_point") | Picture a box bounding the [`Mobject`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject"). |
| [`get_edge_center`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject.get_edge_center "manim.mobject.mobject.Mobject.get_edge_center") | Get edge Point3Ds for certain direction. |
| [`get_end`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject.get_end "manim.mobject.mobject.Mobject.get_end") | Returns the point, where the stroke that surrounds the [`Mobject`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject") ends. |
| `get_extremum_along_dim` |  |
| `get_family` |  |
| `get_family_updaters` |  |
| `get_group_class` |  |
| `get_image` |  |
| [`get_left`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject.get_left "manim.mobject.mobject.Mobject.get_left") | Get left Point3Ds of a box bounding the [`Mobject`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject") |
| [`get_merged_array`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject.get_merged_array "manim.mobject.mobject.Mobject.get_merged_array") | Return all of a given attribute from this mobject and all submobjects. |
| [`get_midpoint`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject.get_midpoint "manim.mobject.mobject.Mobject.get_midpoint") | Get Point3Ds of the middle of the path that forms the [`Mobject`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject"). |
| [`get_mobject_type_class`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject.get_mobject_type_class "manim.mobject.mobject.Mobject.get_mobject_type_class") | Return the base class of this mobject type. |
| [`get_nadir`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject.get_nadir "manim.mobject.mobject.Mobject.get_nadir") | Get nadir (opposite the zenith) Point3Ds of a box bounding a 3D [`Mobject`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject"). |
| `get_num_points` |  |
| `get_pieces` |  |
| [`get_point_mobject`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject.get_point_mobject "manim.mobject.mobject.Mobject.get_point_mobject") | The simplest [`Mobject`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject") to be transformed to or from self. |
| `get_points_defining_boundary` |  |
| [`get_right`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject.get_right "manim.mobject.mobject.Mobject.get_right") | Get right Point3Ds of a box bounding the [`Mobject`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject") |
| [`get_start`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject.get_start "manim.mobject.mobject.Mobject.get_start") | Returns the point, where the stroke that surrounds the [`Mobject`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject") starts. |
| [`get_start_and_end`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject.get_start_and_end "manim.mobject.mobject.Mobject.get_start_and_end") | Returns starting and ending point of a stroke as a `tuple`. |
| [`get_time_based_updaters`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject.get_time_based_updaters "manim.mobject.mobject.Mobject.get_time_based_updaters") | Return all updaters using the `dt` parameter. |
| [`get_top`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject.get_top "manim.mobject.mobject.Mobject.get_top") | Get top Point3Ds of a box bounding the [`Mobject`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject") |
| [`get_updaters`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject.get_updaters "manim.mobject.mobject.Mobject.get_updaters") | Return all updaters. |
| [`get_x`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject.get_x "manim.mobject.mobject.Mobject.get_x") | Returns x Point3D of the center of the [`Mobject`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject") as `float` |
| [`get_y`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject.get_y "manim.mobject.mobject.Mobject.get_y") | Returns y Point3D of the center of the [`Mobject`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject") as `float` |
| [`get_z`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject.get_z "manim.mobject.mobject.Mobject.get_z") | Returns z Point3D of the center of the [`Mobject`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject") as `float` |
| `get_z_index_reference_point` |  |
| [`get_zenith`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject.get_zenith "manim.mobject.mobject.Mobject.get_zenith") | Get zenith Point3Ds of a box bounding a 3D [`Mobject`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject"). |
| [`has_no_points`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject.has_no_points "manim.mobject.mobject.Mobject.has_no_points") | Check if [`Mobject`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject") _does not_ contains points. |
| [`has_points`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject.has_points "manim.mobject.mobject.Mobject.has_points") | Check if [`Mobject`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject") contains points. |
| [`has_time_based_updater`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject.has_time_based_updater "manim.mobject.mobject.Mobject.has_time_based_updater") | Test if `self` has a time based updater. |
| [`init_colors`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject.init_colors "manim.mobject.mobject.Mobject.init_colors") | Initializes the colors. |
| [`insert`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject.insert "manim.mobject.mobject.Mobject.insert") | Inserts a mobject at a specific position into self.submobjects |
| [`interpolate`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject.interpolate "manim.mobject.mobject.Mobject.interpolate") | Turns this [`Mobject`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject") into an interpolation between `mobject1` and `mobject2`. |
| `interpolate_color` |  |
| [`invert`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject.invert "manim.mobject.mobject.Mobject.invert") | Inverts the list of [`submobjects`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject.submobjects "manim.mobject.mobject.Mobject.submobjects"). |
| `is_off_screen` |  |
| [`length_over_dim`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject.length_over_dim "manim.mobject.mobject.Mobject.length_over_dim") | Measure the length of an [`Mobject`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject") in a certain direction. |
| [`match_color`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject.match_color "manim.mobject.mobject.Mobject.match_color") | Match the color with the color of another [`Mobject`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject"). |
| [`match_coord`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject.match_coord "manim.mobject.mobject.Mobject.match_coord") | Match the Point3Ds with the Point3Ds of another [`Mobject`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject"). |
| [`match_depth`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject.match_depth "manim.mobject.mobject.Mobject.match_depth") | Match the depth with the depth of another [`Mobject`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject"). |
| [`match_dim_size`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject.match_dim_size "manim.mobject.mobject.Mobject.match_dim_size") | Match the specified dimension with the dimension of another [`Mobject`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject"). |
| [`match_height`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject.match_height "manim.mobject.mobject.Mobject.match_height") | Match the height with the height of another [`Mobject`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject"). |
| [`match_points`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject.match_points "manim.mobject.mobject.Mobject.match_points") | Edit points, positions, and submobjects to be identical to another [`Mobject`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject"), while keeping the style unchanged. |
| [`match_updaters`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject.match_updaters "manim.mobject.mobject.Mobject.match_updaters") | Match the updaters of the given mobject. |
| [`match_width`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject.match_width "manim.mobject.mobject.Mobject.match_width") | Match the width with the width of another [`Mobject`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject"). |
| [`match_x`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject.match_x "manim.mobject.mobject.Mobject.match_x") | Match x coord. |
| [`match_y`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject.match_y "manim.mobject.mobject.Mobject.match_y") | Match y coord. |
| [`match_z`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject.match_z "manim.mobject.mobject.Mobject.match_z") | Match z coord. |
| [`move_to`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject.move_to "manim.mobject.mobject.Mobject.move_to") | Move center of the [`Mobject`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject") to certain Point3D. |
| [`next_to`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject.next_to "manim.mobject.mobject.Mobject.next_to") | Move this [`Mobject`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject") next to another's [`Mobject`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject") or Point3D. |
| `nonempty_submobjects` |  |
| [`null_point_align`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject.null_point_align "manim.mobject.mobject.Mobject.null_point_align") | If a [`Mobject`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject") with points is being aligned to one without, treat both as groups, and push the one with points into its own submobjects list. |
| `point_from_proportion` |  |
| `pose_at_angle` |  |
| `proportion_from_point` |  |
| `push_self_into_submobjects` |  |
| `put_start_and_end_on` |  |
| [`reduce_across_dimension`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject.reduce_across_dimension "manim.mobject.mobject.Mobject.reduce_across_dimension") | Find the min or max value from a dimension across all points in this and submobjects. |
| [`remove`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject.remove "manim.mobject.mobject.Mobject.remove") | Remove [`submobjects`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject.submobjects "manim.mobject.mobject.Mobject.submobjects"). |
| [`remove_updater`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject.remove_updater "manim.mobject.mobject.Mobject.remove_updater") | Remove an updater. |
| [`repeat`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject.repeat "manim.mobject.mobject.Mobject.repeat") | This can make transition animations nicer |
| `repeat_submobject` |  |
| `replace` |  |
| `rescale_to_fit` |  |
| [`reset_points`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject.reset_points "manim.mobject.mobject.Mobject.reset_points") | Sets [`points`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject.points "manim.mobject.mobject.Mobject.points") to be an empty array. |
| [`restore`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject.restore "manim.mobject.mobject.Mobject.restore") | Restores the state that was previously saved with [`save_state()`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject.save_state "manim.mobject.mobject.Mobject.save_state"). |
| [`resume_updating`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject.resume_updating "manim.mobject.mobject.Mobject.resume_updating") | Enable updating from updaters and animations. |
| `reverse_points` |  |
| [`rotate`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject.rotate "manim.mobject.mobject.Mobject.rotate") | Rotates the [`Mobject`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject") about a certain point. |
| [`rotate_about_origin`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject.rotate_about_origin "manim.mobject.mobject.Mobject.rotate_about_origin") | Rotates the [`Mobject`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject") about the ORIGIN, which is at \[0,0,0\]. |
| [`save_image`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject.save_image "manim.mobject.mobject.Mobject.save_image") | Saves an image of only this [`Mobject`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject") at its position to a png file. |
| [`save_state`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject.save_state "manim.mobject.mobject.Mobject.save_state") | Save the current state (position, color & size). |
| [`scale`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject.scale "manim.mobject.mobject.Mobject.scale") | Scale the size by a factor. |
| [`scale_to_fit_depth`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject.scale_to_fit_depth "manim.mobject.mobject.Mobject.scale_to_fit_depth") | Scales the [`Mobject`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject") to fit a depth while keeping width/height proportional. |
| [`scale_to_fit_height`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject.scale_to_fit_height "manim.mobject.mobject.Mobject.scale_to_fit_height") | Scales the [`Mobject`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject") to fit a height while keeping width/depth proportional. |
| [`scale_to_fit_width`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject.scale_to_fit_width "manim.mobject.mobject.Mobject.scale_to_fit_width") | Scales the [`Mobject`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject") to fit a width while keeping height/depth proportional. |
| [`set`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject.set "manim.mobject.mobject.Mobject.set") | Sets attributes. |
| [`set_color`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject.set_color "manim.mobject.mobject.Mobject.set_color") | Condition is function which takes in one arguments, (x, y, z). |
| [`set_color_by_gradient`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject.set_color_by_gradient "manim.mobject.mobject.Mobject.set_color_by_gradient") |  |
| `set_colors_by_radial_gradient` |  |
| `set_coord` |  |
| [`set_default`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject.set_default "manim.mobject.mobject.Mobject.set_default") | Sets the default values of keyword arguments. |
| `set_submobject_colors_by_gradient` |  |
| `set_submobject_colors_by_radial_gradient` |  |
| [`set_x`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject.set_x "manim.mobject.mobject.Mobject.set_x") | Set x value of the center of the [`Mobject`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject") ( `int` or `float`) |
| [`set_y`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject.set_y "manim.mobject.mobject.Mobject.set_y") | Set y value of the center of the [`Mobject`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject") ( `int` or `float`) |
| [`set_z`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject.set_z "manim.mobject.mobject.Mobject.set_z") | Set z value of the center of the [`Mobject`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject") ( `int` or `float`) |
| [`set_z_index`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject.set_z_index "manim.mobject.mobject.Mobject.set_z_index") | Sets the [`Mobject`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject")'s `z_index` to the value specified in z\_index\_value. |
| [`set_z_index_by_z_Point3D`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject.set_z_index_by_z_Point3D "manim.mobject.mobject.Mobject.set_z_index_by_z_Point3D") | Sets the [`Mobject`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject")'s z Point3D to the value of `z_index`. |
| [`shift`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject.shift "manim.mobject.mobject.Mobject.shift") | Shift by the given vectors. |
| `shift_onto_screen` |  |
| `show` |  |
| [`shuffle`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject.shuffle "manim.mobject.mobject.Mobject.shuffle") | Shuffles the list of [`submobjects`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject.submobjects "manim.mobject.mobject.Mobject.submobjects"). |
| [`shuffle_submobjects`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject.shuffle_submobjects "manim.mobject.mobject.Mobject.shuffle_submobjects") | Shuffles the order of [`submobjects`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject.submobjects "manim.mobject.mobject.Mobject.submobjects") |
| [`sort`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject.sort "manim.mobject.mobject.Mobject.sort") | Sorts the list of [`submobjects`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject.submobjects "manim.mobject.mobject.Mobject.submobjects") by a function defined by `submob_func`. |
| [`sort_submobjects`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject.sort_submobjects "manim.mobject.mobject.Mobject.sort_submobjects") | Sort the [`submobjects`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject.submobjects "manim.mobject.mobject.Mobject.submobjects") |
| `space_out_submobjects` |  |
| `split` |  |
| `stretch` |  |
| `stretch_about_point` |  |
| [`stretch_to_fit_depth`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject.stretch_to_fit_depth "manim.mobject.mobject.Mobject.stretch_to_fit_depth") | Stretches the [`Mobject`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject") to fit a depth, not keeping width/height proportional. |
| [`stretch_to_fit_height`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject.stretch_to_fit_height "manim.mobject.mobject.Mobject.stretch_to_fit_height") | Stretches the [`Mobject`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject") to fit a height, not keeping width/depth proportional. |
| [`stretch_to_fit_width`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject.stretch_to_fit_width "manim.mobject.mobject.Mobject.stretch_to_fit_width") | Stretches the [`Mobject`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject") to fit a width, not keeping height/depth proportional. |
| `surround` |  |
| [`suspend_updating`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject.suspend_updating "manim.mobject.mobject.Mobject.suspend_updating") | Disable updating from updaters and animations. |
| `throw_error_if_no_points` |  |
| [`to_corner`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject.to_corner "manim.mobject.mobject.Mobject.to_corner") | Moves this [`Mobject`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject") to the given corner of the screen. |
| [`to_edge`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject.to_edge "manim.mobject.mobject.Mobject.to_edge") | Moves this [`Mobject`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject") to the given edge of the screen, without affecting its position in the other dimension. |
| `to_original_color` |  |
| [`update`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject.update "manim.mobject.mobject.Mobject.update") | Apply all updaters. |

Attributes

|     |     |
| --- | --- |
| [`animate`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject.animate "manim.mobject.mobject.Mobject.animate") | Used to animate the application of any method of `self`. |
| `animation_overrides` |  |
| [`depth`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject.depth "manim.mobject.mobject.Mobject.depth") | The depth of the mobject. |
| [`height`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject.height "manim.mobject.mobject.Mobject.height") | The height of the mobject. |
| [`width`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject.width "manim.mobject.mobject.Mobject.width") | The width of the mobject. |

_classmethod_\_add\_intrinsic\_animation\_overrides() [\[source\]](https://docs.manim.community/en/stable/_modules/manim/mobject/mobject.html#Mobject._add_intrinsic_animation_overrides) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject._add_intrinsic_animation_overrides "Link to this definition")

Initializes animation overrides marked with the [`override_animation()`](https://docs.manim.community/en/stable/reference/manim.animation.animation.html#manim.animation.animation.override_animation "manim.animation.animation.override_animation")
decorator.

Return type:

None

\_assert\_valid\_submobjects( _submobjects_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/mobject/mobject.html#Mobject._assert_valid_submobjects) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject._assert_valid_submobjects "Link to this definition")

Check that all submobjects are actually instances of
[`Mobject`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject"), and that none of them is `self` (a
[`Mobject`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject") cannot contain itself).

This is an auxiliary function called when adding Mobjects to the
[`submobjects`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject.submobjects "manim.mobject.mobject.Mobject.submobjects") list.

This function is intended to be overridden by subclasses such as
`VMobject`, which should assert that only other VMobjects
may be added into it.

Parameters:

**submobjects** ( _Iterable_ _\[_ [_Mobject_](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject") _\]_) – The list containing values to validate.

Returns:

The Mobject itself.

Return type:

[`Mobject`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject")

Raises:

- **TypeError** – If any of the values in submobjects is not a [`Mobject`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject").

- **ValueError** – If there was an attempt to add a [`Mobject`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject") as its own
submobject.


add( _\*mobjects_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/mobject/mobject.html#Mobject.add) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject.add "Link to this definition")

Add mobjects as submobjects.

The mobjects are added to [`submobjects`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject.submobjects "manim.mobject.mobject.Mobject.submobjects").

Subclasses of mobject may implement `+` and `+=` dunder methods.

Parameters:

**mobjects** ( [_Mobject_](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject")) – The mobjects to add.

Returns:

`self`

Return type:

[`Mobject`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject")

Raises:

- **ValueError** – When a mobject tries to add itself.

- **TypeError** – When trying to add an object that is not an instance of [`Mobject`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject").


Notes

A mobject cannot contain itself, and it cannot contain a submobject
more than once. If the parent mobject is displayed, the newly-added
submobjects will also be displayed (i.e. they are automatically added
to the parent Scene).

See also

[`remove()`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject.remove "manim.mobject.mobject.Mobject.remove"), [`add_to_back()`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject.add_to_back "manim.mobject.mobject.Mobject.add_to_back")

Examples

```
>>> outer = Mobject()
>>> inner = Mobject()
>>> outer = outer.add(inner)

```

Copy to clipboard

Duplicates are not added again:

```
>>> outer = outer.add(inner)
>>> len(outer.submobjects)
1

```

Copy to clipboard

Only Mobjects can be added:

```
>>> outer.add(3)
Traceback (most recent call last):
...
TypeError: Only values of type Mobject can be added as submobjects of Mobject, but the value 3 (at index 0) is of type int.

```

Copy to clipboard

Adding an object to itself raises an error:

```
>>> outer.add(outer)
Traceback (most recent call last):
...
ValueError: Cannot add Mobject as a submobject of itself (at index 0).

```

Copy to clipboard

A given mobject cannot be added as a submobject
twice to some parent:

```
>>> parent = Mobject(name="parent")
>>> child = Mobject(name="child")
>>> parent.add(child, child)
[...] WARNING  ...
parent
>>> parent.submobjects
[child]

```

Copy to clipboard

_classmethod_ add\_animation\_override( _animation\_class_, _override\_func_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/mobject/mobject.html#Mobject.add_animation_override) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject.add_animation_override "Link to this definition")

Add an animation override.

This does not apply to subclasses.

Parameters:

- **animation\_class** ( _type_ _\[_ [_Animation_](https://docs.manim.community/en/stable/reference/manim.animation.animation.Animation.html#manim.animation.animation.Animation "manim.animation.animation.Animation") _\]_) – The animation type to be overridden

- **override\_func** ( [_FunctionOverride_](https://docs.manim.community/en/stable/reference/manim.typing.html#manim.typing.FunctionOverride "manim.typing.FunctionOverride")) – The function returning an animation replacing the default animation. It gets
passed the parameters given to the animation constructor.


Raises:

**MultiAnimationOverrideException** – If the overridden animation was already overridden.

Return type:

None

add\_background\_rectangle( _color=None_, _opacity=0.75_, _\*\*kwargs_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/mobject/mobject.html#Mobject.add_background_rectangle) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject.add_background_rectangle "Link to this definition")

Add a BackgroundRectangle as submobject.

The BackgroundRectangle is added behind other submobjects.

This can be used to increase the mobjects visibility in front of a noisy background.

Parameters:

- **color** ( [_ParsableManimColor_](https://docs.manim.community/en/stable/reference/manim.utils.color.core.html#manim.utils.color.core.ParsableManimColor "manim.utils.color.core.ParsableManimColor") _\|_ _None_) – The color of the BackgroundRectangle

- **opacity** ( _float_) – The opacity of the BackgroundRectangle

- **kwargs** – Additional keyword arguments passed to the BackgroundRectangle constructor


Returns:

`self`

Return type:

[`Mobject`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject")

See also

[`add_to_back()`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject.add_to_back "manim.mobject.mobject.Mobject.add_to_back"), [`BackgroundRectangle`](https://docs.manim.community/en/stable/reference/manim.mobject.geometry.shape_matchers.BackgroundRectangle.html#manim.mobject.geometry.shape_matchers.BackgroundRectangle "manim.mobject.geometry.shape_matchers.BackgroundRectangle")

add\_to\_back( _\*mobjects_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/mobject/mobject.html#Mobject.add_to_back) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject.add_to_back "Link to this definition")

Add all passed mobjects to the back of the submobjects.

If [`submobjects`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject.submobjects "manim.mobject.mobject.Mobject.submobjects") already contains the given mobjects, they just get moved
to the back instead.

Parameters:

**mobjects** ( [_Mobject_](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject")) – The mobjects to add.

Returns:

`self`

Return type:

[`Mobject`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject")

Note

Technically, this is done by adding (or moving) the mobjects to
the head of [`submobjects`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject.submobjects "manim.mobject.mobject.Mobject.submobjects"). The head of this list is rendered
first, which places the corresponding mobjects behind the
subsequent list members.

Raises:

- **ValueError** – When a mobject tries to add itself.

- **TypeError** – When trying to add an object that is not an instance of [`Mobject`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject").


Parameters:

**mobjects** ( [_Mobject_](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject"))

Return type:

Self

Notes

A mobject cannot contain itself, and it cannot contain a submobject
more than once. If the parent mobject is displayed, the newly-added
submobjects will also be displayed (i.e. they are automatically added
to the parent Scene).

See also

[`remove()`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject.remove "manim.mobject.mobject.Mobject.remove"), [`add()`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject.add "manim.mobject.mobject.Mobject.add")

add\_updater( _update\_function_, _index=None_, _call\_updater=False_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/mobject/mobject.html#Mobject.add_updater) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject.add_updater "Link to this definition")

Add an update function to this mobject.

Update functions, or updaters in short, are functions that are applied to the
Mobject in every frame.

Parameters:

- **update\_function** ( [_Updater_](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.html#manim.mobject.mobject.Updater "manim.mobject.mobject.Updater")) – The update function to be added.
Whenever [`update()`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject.update "manim.mobject.mobject.Mobject.update") is called, this update function gets called using
`self` as the first parameter.
The updater can have a second parameter `dt`. If it uses this parameter,
it gets called using a second value `dt`, usually representing the time
in seconds since the last call of [`update()`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject.update "manim.mobject.mobject.Mobject.update").

- **index** ( _int_ _\|_ _None_) – The index at which the new updater should be added in `self.updaters`.
In case `index` is `None` the updater will be added at the end.

- **call\_updater** ( _bool_) – Whether or not to call the updater initially. If `True`, the updater will
be called using `dt=0`.


Returns:

`self`

Return type:

[`Mobject`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject")

Examples

Example: NextToUpdater [¶](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#nexttoupdater)

```
from manim import *

class NextToUpdater(Scene):
    def construct(self):
        def dot_position(mobject):
            mobject.set_value(dot.get_center()[0])
            mobject.next_to(dot)

        dot = Dot(RIGHT*3)
        label = DecimalNumber()
        label.add_updater(dot_position)
        self.add(dot, label)

        self.play(Rotating(dot, about_point=ORIGIN, angle=TAU, run_time=TAU, rate_func=linear))

```

Copy to clipboard

Make interactive

Example: DtUpdater [¶](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#dtupdater)

```
from manim import *

class DtUpdater(Scene):
    def construct(self):
        square = Square()

        #Let the square rotate 90° per second
        square.add_updater(lambda mobject, dt: mobject.rotate(dt*90*DEGREES))
        self.add(square)
        self.wait(2)

```

Copy to clipboard

Make interactive

See also

[`get_updaters()`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject.get_updaters "manim.mobject.mobject.Mobject.get_updaters"), [`remove_updater()`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject.remove_updater "manim.mobject.mobject.Mobject.remove_updater"), [`UpdateFromFunc`](https://docs.manim.community/en/stable/reference/manim.animation.updaters.update.UpdateFromFunc.html#manim.animation.updaters.update.UpdateFromFunc "manim.animation.updaters.update.UpdateFromFunc")

align\_data( _mobject_, _skip\_point\_alignment=False_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/mobject/mobject.html#Mobject.align_data) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject.align_data "Link to this definition")

Aligns the data of this mobject with another mobject.

Afterwards, the two mobjects will have the same number of submobjects
(see `align_submobjects()`), the same parent structure (see
[`null_point_align()`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject.null_point_align "manim.mobject.mobject.Mobject.null_point_align")). If `skip_point_alignment` is false,
they will also have the same number of points (see [`align_points()`](https://docs.manim.community/en/stable/reference/manim.mobject.types.vectorized_mobject.VMobject.html#manim.mobject.types.vectorized_mobject.VMobject.align_points "manim.mobject.types.vectorized_mobject.VMobject.align_points")).

Parameters:

- **mobject** ( [_Mobject_](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject")) – The other mobject this mobject should be aligned to.

- **skip\_point\_alignment** ( _bool_) – Controls whether or not the computationally expensive
point alignment is skipped (default: False).


Return type:

None

align\_on\_border( _direction_, _buff=0.5_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/mobject/mobject.html#Mobject.align_on_border) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject.align_on_border "Link to this definition")

Direction just needs to be a vector pointing towards side or
corner in the 2d plane.

Parameters:

- **direction** ( [_Vector3D_](https://docs.manim.community/en/stable/reference/manim.typing.html#manim.typing.Vector3D "manim.typing.Vector3D"))

- **buff** ( _float_)


Return type:

Self

align\_to( _mobject\_or\_point_, _direction=array(\[0.,0.,0.\])_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/mobject/mobject.html#Mobject.align_to) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject.align_to "Link to this definition")

Aligns mobject to another [`Mobject`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject") in a certain direction.

Examples:
mob1.align\_to(mob2, UP) moves mob1 vertically so that its
top edge lines ups with mob2’s top edge.

Parameters:

- **mobject\_or\_point** ( [_Mobject_](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject") _\|_ [_Point3DLike_](https://docs.manim.community/en/stable/reference/manim.typing.html#manim.typing.Point3DLike "manim.typing.Point3DLike"))

- **direction** ( [_Vector3D_](https://docs.manim.community/en/stable/reference/manim.typing.html#manim.typing.Vector3D "manim.typing.Vector3D"))


Return type:

Self

_property_ animate _:\_AnimationBuilder\|Self_ [¶](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject.animate "Link to this definition")

Used to animate the application of any method of `self`.

Any method called on `animate` is converted to an animation of applying
that method on the mobject itself.

For example, `square.set_fill(WHITE)` sets the fill color of a square,
while `square.animate.set_fill(WHITE)` animates this action.

Multiple methods can be put in a single animation once via chaining:

```
self.play(my_mobject.animate.shift(RIGHT).rotate(PI))

```

Copy to clipboard

Warning

Passing multiple animations for the same [`Mobject`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject") in one
call to [`play()`](https://docs.manim.community/en/stable/reference/manim.scene.scene.Scene.html#manim.scene.scene.Scene.play "manim.scene.scene.Scene.play") is discouraged and will most likely
not work properly. Instead of writing an animation like

```
self.play(
    my_mobject.animate.shift(RIGHT), my_mobject.animate.rotate(PI)
)

```

Copy to clipboard

make use of method chaining.

Keyword arguments that can be passed to [`Scene.play()`](https://docs.manim.community/en/stable/reference/manim.scene.scene.Scene.html#manim.scene.scene.Scene.play "manim.scene.scene.Scene.play") can be passed
directly after accessing `.animate`, like so:

```
self.play(my_mobject.animate(rate_func=linear).shift(RIGHT))

```

Copy to clipboard

This is especially useful when animating simultaneous `.animate` calls that
you want to behave differently:

```
self.play(
    mobject1.animate(run_time=2).rotate(PI),
    mobject2.animate(rate_func=there_and_back).shift(RIGHT),
)

```

Copy to clipboard

See also

[`override_animate()`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.html#manim.mobject.mobject.override_animate "manim.mobject.mobject.override_animate")

Examples

Example: AnimateExample [¶](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#animateexample)

```
from manim import *

class AnimateExample(Scene):
    def construct(self):
        s = Square()
        self.play(Create(s))
        self.play(s.animate.shift(RIGHT))
        self.play(s.animate.scale(2))
        self.play(s.animate.rotate(PI / 2))
        self.play(Uncreate(s))

```

Copy to clipboard

Make interactive

Example: AnimateChainExample [¶](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#animatechainexample)

```
from manim import *

class AnimateChainExample(Scene):
    def construct(self):
        s = Square()
        self.play(Create(s))
        self.play(s.animate.shift(RIGHT).scale(2).rotate(PI / 2))
        self.play(Uncreate(s))

```

Copy to clipboard

Make interactive

Example: AnimateWithArgsExample [¶](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#animatewithargsexample)

```
from manim import *

class AnimateWithArgsExample(Scene):
    def construct(self):
        s = Square()
        c = Circle()

        VGroup(s, c).arrange(RIGHT, buff=2)
        self.add(s, c)

        self.play(
            s.animate(run_time=2).rotate(PI / 2),
            c.animate(rate_func=there_and_back).shift(RIGHT),
        )

```

Copy to clipboard

Make interactive

Warning

`.animate`

will interpolate the [`Mobject`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject") between its points prior to
`.animate` and its points after applying `.animate` to it. This may
result in unexpected behavior when attempting to interpolate along paths,
or rotations.
If you want animations to consider the points between, consider using
[`ValueTracker`](https://docs.manim.community/en/stable/reference/manim.mobject.value_tracker.ValueTracker.html#manim.mobject.value_tracker.ValueTracker "manim.mobject.value_tracker.ValueTracker") with updaters instead.

_classmethod_ animation\_override\_for( _animation\_class_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/mobject/mobject.html#Mobject.animation_override_for) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject.animation_override_for "Link to this definition")

Returns the function defining a specific animation override for this class.

Parameters:

**animation\_class** ( _type_ _\[_ [_Animation_](https://docs.manim.community/en/stable/reference/manim.animation.animation.Animation.html#manim.animation.animation.Animation "manim.animation.animation.Animation") _\]_) – The animation class for which the override function should be returned.

Returns:

The function returning the override animation or `None` if no such animation
override is defined.

Return type:

Optional\[Callable\[\[ [Mobject](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject"), …\], [Animation](https://docs.manim.community/en/stable/reference/manim.animation.animation.Animation.html#manim.animation.animation.Animation "manim.animation.animation.Animation")\]\]

apply\_complex\_function( _function_, _\*\*kwargs_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/mobject/mobject.html#Mobject.apply_complex_function) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject.apply_complex_function "Link to this definition")

Applies a complex function to a [`Mobject`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject").
The x and y Point3Ds correspond to the real and imaginary parts respectively.

Example

Example: ApplyFuncExample [¶](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#applyfuncexample)

```
from manim import *

class ApplyFuncExample(Scene):
    def construct(self):
        circ = Circle().scale(1.5)
        circ_ref = circ.copy()
        circ.apply_complex_function(
            lambda x: np.exp(x*1j)
        )
        t = ValueTracker(0)
        circ.add_updater(
            lambda x: x.become(circ_ref.copy().apply_complex_function(
                lambda x: np.exp(x+t.get_value()*1j)
            )).set_color(BLUE)
        )
        self.add(circ_ref)
        self.play(TransformFromCopy(circ_ref, circ))
        self.play(t.animate.set_value(TAU), run_time=3)

```

Copy to clipboard

Make interactive

Parameters:

**function** ( _Callable_ _\[_ _\[_ _complex_ _\]_ _,_ _complex_ _\]_)

Return type:

Self

apply\_to\_family( _func_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/mobject/mobject.html#Mobject.apply_to_family) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject.apply_to_family "Link to this definition")

Apply a function to `self` and every submobject with points recursively.

Parameters:

**func** ( _Callable_ _\[_ _\[_ [_Mobject_](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject") _\]_ _,_ _None_ _\]_) – The function to apply to each mobject. `func` gets passed the respective
(sub)mobject as parameter.

Returns:

`self`

Return type:

[`Mobject`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject")

See also

`family_members_with_points()`

arrange( _direction=array(\[1.,0.,0.\])_, _buff=0.25_, _center=True_, _\*\*kwargs_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/mobject/mobject.html#Mobject.arrange) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject.arrange "Link to this definition")

Sorts [`Mobject`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject") next to each other on screen.

Examples

Example: Example [¶](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#example)

![../_images/Example-1.png](https://docs.manim.community/en/stable/_images/Example-1.png)

```
from manim import *

class Example(Scene):
    def construct(self):
        s1 = Square()
        s2 = Square()
        s3 = Square()
        s4 = Square()
        x = VGroup(s1, s2, s3, s4).set_x(0).arrange(buff=1.0)
        self.add(x)

```

Copy to clipboard

Make interactive

Parameters:

- **direction** ( [_Vector3D_](https://docs.manim.community/en/stable/reference/manim.typing.html#manim.typing.Vector3D "manim.typing.Vector3D"))

- **buff** ( _float_)

- **center** ( _bool_)


Return type:

Self

arrange\_in\_grid( _rows=None_, _cols=None_, _buff=0.25_, _cell\_alignment=array(\[0.,0.,0.\])_, _row\_alignments=None_, _col\_alignments=None_, _row\_heights=None_, _col\_widths=None_, _flow\_order='rd'_, _\*\*kwargs_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/mobject/mobject.html#Mobject.arrange_in_grid) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject.arrange_in_grid "Link to this definition")

Arrange submobjects in a grid.

Parameters:

- **rows** ( _int_ _\|_ _None_) – The number of rows in the grid.

- **cols** ( _int_ _\|_ _None_) – The number of columns in the grid.

- **buff** ( _float_ _\|_ _tuple_ _\[_ _float_ _,_ _float_ _\]_) – The gap between grid cells. To specify a different buffer in the horizontal and
vertical directions, a tuple of two values can be given - `(row, col)`.

- **cell\_alignment** ( [_Vector3D_](https://docs.manim.community/en/stable/reference/manim.typing.html#manim.typing.Vector3D "manim.typing.Vector3D")) – The way each submobject is aligned in its grid cell.

- **row\_alignments** ( _str_ _\|_ _None_) – The vertical alignment for each row (top to bottom). Accepts the following characters: `"u"` -
up, `"c"` \- center, `"d"` \- down.

- **col\_alignments** ( _str_ _\|_ _None_) – The horizontal alignment for each column (left to right). Accepts the following characters `"l"` \- left,
`"c"` \- center, `"r"` \- right.

- **row\_heights** ( _Iterable_ _\[_ _float_ _\|_ _None_ _\]_ _\|_ _None_) – Defines a list of heights for certain rows (top to bottom). If the list contains
`None`, the corresponding row will fit its height automatically based
on the highest element in that row.

- **col\_widths** ( _Iterable_ _\[_ _float_ _\|_ _None_ _\]_ _\|_ _None_) – Defines a list of widths for certain columns (left to right). If the list contains `None`, the
corresponding column will fit its width automatically based on the widest element in that column.

- **flow\_order** ( _str_) – The order in which submobjects fill the grid. Can be one of the following values:
“rd”, “dr”, “ld”, “dl”, “ru”, “ur”, “lu”, “ul”. (“rd” -> fill rightwards then downwards)


Returns:

`self`

Return type:

[`Mobject`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject")

Raises:

- **ValueError** – If `rows` and `cols` are too small to fit all submobjects.

- **ValueError** – If `cols`, `col_alignments` and `col_widths` or `rows`,
`row_alignments` and `row_heights` have mismatching sizes.


Notes

If only one of `cols` and `rows` is set implicitly, the other one will be chosen big
enough to fit all submobjects. If neither is set, they will be chosen to be about the same,
tending towards `cols` \> `rows` (simply because videos are wider than they are high).

If both `cell_alignment` and `row_alignments` / `col_alignments` are
defined, the latter has higher priority.

Examples

Example: ExampleBoxes [¶](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#exampleboxes)

![../_images/ExampleBoxes-1.png](https://docs.manim.community/en/stable/_images/ExampleBoxes-1.png)

```
from manim import *

class ExampleBoxes(Scene):
    def construct(self):
        boxes=VGroup(*[Square() for s in range(0,6)])
        boxes.arrange_in_grid(rows=2, buff=0.1)
        self.add(boxes)

```

Copy to clipboard

Make interactive

Example: ArrangeInGrid [¶](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#arrangeingrid)

![../_images/ArrangeInGrid-1.png](https://docs.manim.community/en/stable/_images/ArrangeInGrid-1.png)

```
from manim import *

class ArrangeInGrid(Scene):
    def construct(self):
        boxes = VGroup(*[\
            Rectangle(WHITE, 0.5, 0.5).add(Text(str(i+1)).scale(0.5))\
            for i in range(24)\
        ])
        self.add(boxes)

        boxes.arrange_in_grid(
            buff=(0.25,0.5),
            col_alignments="lccccr",
            row_alignments="uccd",
            col_widths=[1, *[None]*4, 1],
            row_heights=[1, None, None, 1],
            flow_order="dr"
        )

```

Copy to clipboard

Make interactive

arrange\_submobjects( _\*args_, _\*\*kwargs_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/mobject/mobject.html#Mobject.arrange_submobjects) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject.arrange_submobjects "Link to this definition")

Arrange the position of [`submobjects`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject.submobjects "manim.mobject.mobject.Mobject.submobjects") with a small buffer.

Examples

Example: ArrangeSumobjectsExample [¶](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#arrangesumobjectsexample)

![../_images/ArrangeSumobjectsExample-1.png](https://docs.manim.community/en/stable/_images/ArrangeSumobjectsExample-1.png)

```
from manim import *

class ArrangeSumobjectsExample(Scene):
    def construct(self):
        s= VGroup(*[Dot().shift(i*0.1*RIGHT*np.random.uniform(-1,1)+UP*np.random.uniform(-1,1)) for i in range(0,15)])
        s.shift(UP).set_color(BLUE)
        s2= s.copy().set_color(RED)
        s2.arrange_submobjects()
        s2.shift(DOWN)
        self.add(s,s2)

```

Copy to clipboard

Make interactive

Return type:

Self

become( _mobject_, _match\_height=False_, _match\_width=False_, _match\_depth=False_, _match\_center=False_, _stretch=False_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/mobject/mobject.html#Mobject.become) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject.become "Link to this definition")

Edit points, colors and submobjects to be identical
to another [`Mobject`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject")

Note

If both match\_height and match\_width are `True` then the transformed [`Mobject`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject")
will match the height first and then the width.

Parameters:

- **match\_height** ( _bool_) – Whether or not to preserve the height of the original
[`Mobject`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject").

- **match\_width** ( _bool_) – Whether or not to preserve the width of the original
[`Mobject`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject").

- **match\_depth** ( _bool_) – Whether or not to preserve the depth of the original
[`Mobject`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject").

- **match\_center** ( _bool_) – Whether or not to preserve the center of the original
[`Mobject`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject").

- **stretch** ( _bool_) – Whether or not to stretch the target mobject to match the
the proportions of the original [`Mobject`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject").

- **mobject** ( [_Mobject_](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject"))


Return type:

Self

Examples

Example: BecomeScene [¶](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#becomescene)

```
from manim import *

class BecomeScene(Scene):
    def construct(self):
        circ = Circle(fill_color=RED, fill_opacity=0.8)
        square = Square(fill_color=BLUE, fill_opacity=0.2)
        self.add(circ)
        self.wait(0.5)
        circ.become(square)
        self.wait(0.5)

```

Copy to clipboard

Make interactive

The following examples illustrate how mobject measurements
change when using the `match_...` and `stretch` arguments.
We start with a rectangle that is 2 units high and 4 units wide,
which we want to turn into a circle of radius 3:

```
>>> from manim import Rectangle, Circle
>>> import numpy as np
>>> rect = Rectangle(height=2, width=4)
>>> circ = Circle(radius=3)

```

Copy to clipboard

With `stretch=True`, the target circle is deformed to match
the proportions of the rectangle, which results in the target
mobject being an ellipse with height 2 and width 4. We can
check that the resulting points satisfy the ellipse equation
x2/a2+y2/b2=1 with a=4/2 and b=2/2
being the semi-axes:

```
>>> result = rect.copy().become(circ, stretch=True)
>>> result.height, result.width
(np.float64(2.0), np.float64(4.0))
>>> ellipse_points = np.array(result.get_anchors())
>>> ellipse_eq = np.sum(ellipse_points**2 * [1/4, 1, 0], axis=1)
>>> np.allclose(ellipse_eq, 1)
True

```

Copy to clipboard

With `match_height=True` and `match_width=True` the circle is
scaled such that the height or the width of the rectangle will
be preserved, respectively.
The points of the resulting mobject satisfy the circle equation
x2+y2=r2 for the corresponding radius r:

```
>>> result = rect.copy().become(circ, match_height=True)
>>> result.height, result.width
(np.float64(2.0), np.float64(2.0))
>>> circle_points = np.array(result.get_anchors())
>>> circle_eq = np.sum(circle_points**2, axis=1)
>>> np.allclose(circle_eq, 1)
True
>>> result = rect.copy().become(circ, match_width=True)
>>> result.height, result.width
(np.float64(4.0), np.float64(4.0))
>>> circle_points = np.array(result.get_anchors())
>>> circle_eq = np.sum(circle_points**2, axis=1)
>>> np.allclose(circle_eq, 2**2)
True

```

Copy to clipboard

With `match_center=True`, the resulting mobject is moved such that
its center is the same as the center of the original mobject:

```
>>> rect = rect.shift(np.array([0, 1, 0]))
>>> np.allclose(rect.get_center(), circ.get_center())
False
>>> result = rect.copy().become(circ, match_center=True)
>>> np.allclose(rect.get_center(), result.get_center())
True

```

Copy to clipboard

center() [\[source\]](https://docs.manim.community/en/stable/_modules/manim/mobject/mobject.html#Mobject.center) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject.center "Link to this definition")

Moves the center of the mobject to the center of the scene.

Returns:

The centered mobject.

Return type:

[`Mobject`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject")

clear\_updaters( _recursive=True_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/mobject/mobject.html#Mobject.clear_updaters) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject.clear_updaters "Link to this definition")

Remove every updater.

Parameters:

**recursive** ( _bool_) – Whether to recursively call `clear_updaters` on all submobjects.

Returns:

`self`

Return type:

[`Mobject`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject")

See also

[`remove_updater()`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject.remove_updater "manim.mobject.mobject.Mobject.remove_updater"), [`add_updater()`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject.add_updater "manim.mobject.mobject.Mobject.add_updater"), [`get_updaters()`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject.get_updaters "manim.mobject.mobject.Mobject.get_updaters")

copy() [\[source\]](https://docs.manim.community/en/stable/_modules/manim/mobject/mobject.html#Mobject.copy) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject.copy "Link to this definition")

Create and return an identical copy of the [`Mobject`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject") including all
[`submobjects`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject.submobjects "manim.mobject.mobject.Mobject.submobjects").

Returns:

The copy.

Return type:

[`Mobject`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject")

Note

The clone is initially not visible in the Scene, even if the original was.

_property_ depth _:float_ [¶](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject.depth "Link to this definition")

The depth of the mobject.

Return type:

`float`

See also

[`length_over_dim()`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject.length_over_dim "manim.mobject.mobject.Mobject.length_over_dim")

flip( _axis=array(\[0.,1.,0.\])_, _\*\*kwargs_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/mobject/mobject.html#Mobject.flip) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject.flip "Link to this definition")

Flips/Mirrors an mobject about its center.

Examples

Example: FlipExample [¶](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#flipexample)

![../_images/FlipExample-1.png](https://docs.manim.community/en/stable/_images/FlipExample-1.png)

```
from manim import *

class FlipExample(Scene):
    def construct(self):
        s= Line(LEFT, RIGHT+UP).shift(4*LEFT)
        self.add(s)
        s2= s.copy().flip()
        self.add(s2)

```

Copy to clipboard

Make interactive

Parameters:

**axis** ( [_Vector3D_](https://docs.manim.community/en/stable/reference/manim.typing.html#manim.typing.Vector3D "manim.typing.Vector3D"))

Return type:

Self

generate\_points() [\[source\]](https://docs.manim.community/en/stable/_modules/manim/mobject/mobject.html#Mobject.generate_points) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject.generate_points "Link to this definition")

Initializes [`points`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject.points "manim.mobject.mobject.Mobject.points") and therefore the shape.

Gets called upon creation. This is an empty method that can be implemented by
subclasses.

Return type:

object

get\_all\_points() [\[source\]](https://docs.manim.community/en/stable/_modules/manim/mobject/mobject.html#Mobject.get_all_points) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject.get_all_points "Link to this definition")

Return all points from this mobject and all submobjects.

May contain duplicates; the order is in a depth-first (pre-order)
traversal of the submobjects.

Return type:

[_Point3D\_Array_](https://docs.manim.community/en/stable/reference/manim.typing.html#manim.typing.Point3D_Array "manim.typing.Point3D_Array")

get\_bottom() [\[source\]](https://docs.manim.community/en/stable/_modules/manim/mobject/mobject.html#Mobject.get_bottom) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject.get_bottom "Link to this definition")

Get bottom Point3Ds of a box bounding the [`Mobject`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject")

Return type:

[_Point3D_](https://docs.manim.community/en/stable/reference/manim.typing.html#manim.typing.Point3D "manim.typing.Point3D")

get\_center() [\[source\]](https://docs.manim.community/en/stable/_modules/manim/mobject/mobject.html#Mobject.get_center) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject.get_center "Link to this definition")

Get center Point3Ds

Return type:

[_Point3D_](https://docs.manim.community/en/stable/reference/manim.typing.html#manim.typing.Point3D "manim.typing.Point3D")

get\_color() [\[source\]](https://docs.manim.community/en/stable/_modules/manim/mobject/mobject.html#Mobject.get_color) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject.get_color "Link to this definition")

Returns the color of the [`Mobject`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject")

Examples

```
>>> from manim import Square, RED
>>> Square(color=RED).get_color() == RED
True

```

Copy to clipboard

Return type:

[_ManimColor_](https://docs.manim.community/en/stable/reference/manim.utils.color.core.ManimColor.html#manim.utils.color.core.ManimColor "manim.utils.color.core.ManimColor")

get\_coord( _dim_, _direction=array(\[0.,0.,0.\])_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/mobject/mobject.html#Mobject.get_coord) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject.get_coord "Link to this definition")

Meant to generalize `get_x`, `get_y` and `get_z`

Parameters:

- **dim** ( _int_)

- **direction** ( [_Vector3D_](https://docs.manim.community/en/stable/reference/manim.typing.html#manim.typing.Vector3D "manim.typing.Vector3D"))


get\_corner( _direction_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/mobject/mobject.html#Mobject.get_corner) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject.get_corner "Link to this definition")

Get corner Point3Ds for certain direction.

Parameters:

**direction** ( [_Vector3D_](https://docs.manim.community/en/stable/reference/manim.typing.html#manim.typing.Vector3D "manim.typing.Vector3D"))

Return type:

[_Point3D_](https://docs.manim.community/en/stable/reference/manim.typing.html#manim.typing.Point3D "manim.typing.Point3D")

get\_critical\_point( _direction_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/mobject/mobject.html#Mobject.get_critical_point) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject.get_critical_point "Link to this definition")

Picture a box bounding the [`Mobject`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject"). Such a box has
9 ‘critical points’: 4 corners, 4 edge center, the
center. This returns one of them, along the given direction.

```
sample = Arc(start_angle=PI / 7, angle=PI / 5)

# These are all equivalent
max_y_1 = sample.get_top()[1]
max_y_2 = sample.get_critical_point(UP)[1]
max_y_3 = sample.get_extremum_along_dim(dim=1, key=1)

```

Copy to clipboard

Parameters:

**direction** ( [_Vector3D_](https://docs.manim.community/en/stable/reference/manim.typing.html#manim.typing.Vector3D "manim.typing.Vector3D"))

Return type:

[_Point3D_](https://docs.manim.community/en/stable/reference/manim.typing.html#manim.typing.Point3D "manim.typing.Point3D")

get\_edge\_center( _direction_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/mobject/mobject.html#Mobject.get_edge_center) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject.get_edge_center "Link to this definition")

Get edge Point3Ds for certain direction.

Parameters:

**direction** ( [_Vector3D_](https://docs.manim.community/en/stable/reference/manim.typing.html#manim.typing.Vector3D "manim.typing.Vector3D"))

Return type:

[_Point3D_](https://docs.manim.community/en/stable/reference/manim.typing.html#manim.typing.Point3D "manim.typing.Point3D")

get\_end() [\[source\]](https://docs.manim.community/en/stable/_modules/manim/mobject/mobject.html#Mobject.get_end) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject.get_end "Link to this definition")

Returns the point, where the stroke that surrounds the [`Mobject`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject") ends.

Return type:

[_Point3D_](https://docs.manim.community/en/stable/reference/manim.typing.html#manim.typing.Point3D "manim.typing.Point3D")

get\_left() [\[source\]](https://docs.manim.community/en/stable/_modules/manim/mobject/mobject.html#Mobject.get_left) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject.get_left "Link to this definition")

Get left Point3Ds of a box bounding the [`Mobject`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject")

Return type:

[_Point3D_](https://docs.manim.community/en/stable/reference/manim.typing.html#manim.typing.Point3D "manim.typing.Point3D")

get\_merged\_array( _array\_attr_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/mobject/mobject.html#Mobject.get_merged_array) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject.get_merged_array "Link to this definition")

Return all of a given attribute from this mobject and all submobjects.

May contain duplicates; the order is in a depth-first (pre-order)
traversal of the submobjects.

Parameters:

**array\_attr** ( _str_)

Return type:

_ndarray_

get\_midpoint() [\[source\]](https://docs.manim.community/en/stable/_modules/manim/mobject/mobject.html#Mobject.get_midpoint) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject.get_midpoint "Link to this definition")

Get Point3Ds of the middle of the path that forms the [`Mobject`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject").

Examples

Example: AngleMidPoint [¶](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#anglemidpoint)

![../_images/AngleMidPoint-1.png](https://docs.manim.community/en/stable/_images/AngleMidPoint-1.png)

```
from manim import *

class AngleMidPoint(Scene):
    def construct(self):
        line1 = Line(ORIGIN, 2*RIGHT)
        line2 = Line(ORIGIN, 2*RIGHT).rotate_about_origin(80*DEGREES)

        a = Angle(line1, line2, radius=1.5, other_angle=False)
        d = Dot(a.get_midpoint()).set_color(RED)

        self.add(line1, line2, a, d)
        self.wait()

```

Copy to clipboard

Make interactive

Return type:

[_Point3D_](https://docs.manim.community/en/stable/reference/manim.typing.html#manim.typing.Point3D "manim.typing.Point3D")

_static_ get\_mobject\_type\_class() [\[source\]](https://docs.manim.community/en/stable/_modules/manim/mobject/mobject.html#Mobject.get_mobject_type_class) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject.get_mobject_type_class "Link to this definition")

Return the base class of this mobject type.

Return type:

type\[ [_Mobject_](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject")\]

get\_nadir() [\[source\]](https://docs.manim.community/en/stable/_modules/manim/mobject/mobject.html#Mobject.get_nadir) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject.get_nadir "Link to this definition")

Get nadir (opposite the zenith) Point3Ds of a box bounding a 3D [`Mobject`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject").

Return type:

[_Point3D_](https://docs.manim.community/en/stable/reference/manim.typing.html#manim.typing.Point3D "manim.typing.Point3D")

get\_point\_mobject( _center=None_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/mobject/mobject.html#Mobject.get_point_mobject) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject.get_point_mobject "Link to this definition")

The simplest [`Mobject`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject") to be transformed to or from self.
Should by a point of the appropriate type

get\_right() [\[source\]](https://docs.manim.community/en/stable/_modules/manim/mobject/mobject.html#Mobject.get_right) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject.get_right "Link to this definition")

Get right Point3Ds of a box bounding the [`Mobject`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject")

Return type:

[_Point3D_](https://docs.manim.community/en/stable/reference/manim.typing.html#manim.typing.Point3D "manim.typing.Point3D")

get\_start() [\[source\]](https://docs.manim.community/en/stable/_modules/manim/mobject/mobject.html#Mobject.get_start) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject.get_start "Link to this definition")

Returns the point, where the stroke that surrounds the [`Mobject`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject") starts.

Return type:

[_Point3D_](https://docs.manim.community/en/stable/reference/manim.typing.html#manim.typing.Point3D "manim.typing.Point3D")

get\_start\_and\_end() [\[source\]](https://docs.manim.community/en/stable/_modules/manim/mobject/mobject.html#Mobject.get_start_and_end) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject.get_start_and_end "Link to this definition")

Returns starting and ending point of a stroke as a `tuple`.

Return type:

tuple\[ [_Point3D_](https://docs.manim.community/en/stable/reference/manim.typing.html#manim.typing.Point3D "manim.typing.Point3D"), [_Point3D_](https://docs.manim.community/en/stable/reference/manim.typing.html#manim.typing.Point3D "manim.typing.Point3D")\]

get\_time\_based\_updaters() [\[source\]](https://docs.manim.community/en/stable/_modules/manim/mobject/mobject.html#Mobject.get_time_based_updaters) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject.get_time_based_updaters "Link to this definition")

Return all updaters using the `dt` parameter.

The updaters use this parameter as the input for difference in time.

Returns:

The list of time based updaters.

Return type:

List\[ `Callable`\]

See also

[`get_updaters()`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject.get_updaters "manim.mobject.mobject.Mobject.get_updaters"), [`has_time_based_updater()`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject.has_time_based_updater "manim.mobject.mobject.Mobject.has_time_based_updater")

get\_top() [\[source\]](https://docs.manim.community/en/stable/_modules/manim/mobject/mobject.html#Mobject.get_top) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject.get_top "Link to this definition")

Get top Point3Ds of a box bounding the [`Mobject`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject")

Return type:

[_Point3D_](https://docs.manim.community/en/stable/reference/manim.typing.html#manim.typing.Point3D "manim.typing.Point3D")

get\_updaters() [\[source\]](https://docs.manim.community/en/stable/_modules/manim/mobject/mobject.html#Mobject.get_updaters) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject.get_updaters "Link to this definition")

Return all updaters.

Returns:

The list of updaters.

Return type:

List\[ `Callable`\]

See also

[`add_updater()`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject.add_updater "manim.mobject.mobject.Mobject.add_updater"), [`get_time_based_updaters()`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject.get_time_based_updaters "manim.mobject.mobject.Mobject.get_time_based_updaters")

get\_x( _direction=array(\[0.,0.,0.\])_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/mobject/mobject.html#Mobject.get_x) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject.get_x "Link to this definition")

Returns x Point3D of the center of the [`Mobject`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject") as `float`

Parameters:

**direction** ( [_Vector3D_](https://docs.manim.community/en/stable/reference/manim.typing.html#manim.typing.Vector3D "manim.typing.Vector3D"))

Return type:

float

get\_y( _direction=array(\[0.,0.,0.\])_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/mobject/mobject.html#Mobject.get_y) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject.get_y "Link to this definition")

Returns y Point3D of the center of the [`Mobject`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject") as `float`

Parameters:

**direction** ( [_Vector3D_](https://docs.manim.community/en/stable/reference/manim.typing.html#manim.typing.Vector3D "manim.typing.Vector3D"))

Return type:

float

get\_z( _direction=array(\[0.,0.,0.\])_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/mobject/mobject.html#Mobject.get_z) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject.get_z "Link to this definition")

Returns z Point3D of the center of the [`Mobject`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject") as `float`

Parameters:

**direction** ( [_Vector3D_](https://docs.manim.community/en/stable/reference/manim.typing.html#manim.typing.Vector3D "manim.typing.Vector3D"))

Return type:

float

get\_zenith() [\[source\]](https://docs.manim.community/en/stable/_modules/manim/mobject/mobject.html#Mobject.get_zenith) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject.get_zenith "Link to this definition")

Get zenith Point3Ds of a box bounding a 3D [`Mobject`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject").

Return type:

[_Point3D_](https://docs.manim.community/en/stable/reference/manim.typing.html#manim.typing.Point3D "manim.typing.Point3D")

has\_no\_points() [\[source\]](https://docs.manim.community/en/stable/_modules/manim/mobject/mobject.html#Mobject.has_no_points) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject.has_no_points "Link to this definition")

Check if [`Mobject`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject") _does not_ contains points.

Return type:

bool

has\_points() [\[source\]](https://docs.manim.community/en/stable/_modules/manim/mobject/mobject.html#Mobject.has_points) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject.has_points "Link to this definition")

Check if [`Mobject`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject") contains points.

Return type:

bool

has\_time\_based\_updater() [\[source\]](https://docs.manim.community/en/stable/_modules/manim/mobject/mobject.html#Mobject.has_time_based_updater) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject.has_time_based_updater "Link to this definition")

Test if `self` has a time based updater.

Returns:

`True` if at least one updater uses the `dt` parameter, `False`
otherwise.

Return type:

`bool`

See also

[`get_time_based_updaters()`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject.get_time_based_updaters "manim.mobject.mobject.Mobject.get_time_based_updaters")

_property_ height _:float_ [¶](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject.height "Link to this definition")

The height of the mobject.

Return type:

`float`

Examples

Example: HeightExample [¶](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#heightexample)

```
from manim import *

class HeightExample(Scene):
    def construct(self):
        decimal = DecimalNumber().to_edge(UP)
        rect = Rectangle(color=BLUE)
        rect_copy = rect.copy().set_stroke(GRAY, opacity=0.5)

        decimal.add_updater(lambda d: d.set_value(rect.height))

        self.add(rect_copy, rect, decimal)
        self.play(rect.animate.set(height=5))
        self.wait()

```

Copy to clipboard

Make interactive

See also

[`length_over_dim()`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject.length_over_dim "manim.mobject.mobject.Mobject.length_over_dim")

init\_colors() [\[source\]](https://docs.manim.community/en/stable/_modules/manim/mobject/mobject.html#Mobject.init_colors) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject.init_colors "Link to this definition")

Initializes the colors.

Gets called upon creation. This is an empty method that can be implemented by
subclasses.

Return type:

object

insert( _index_, _mobject_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/mobject/mobject.html#Mobject.insert) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject.insert "Link to this definition")

Inserts a mobject at a specific position into self.submobjects

Effectively just calls `self.submobjects.insert(index, mobject)`,
where `self.submobjects` is a list.

Highly adapted from `Mobject.add`.

Parameters:

- **index** ( _int_) – The index at which

- **mobject** ( [_Mobject_](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject")) – The mobject to be inserted.


Return type:

None

interpolate( _mobject1_, _mobject2_, _alpha_, _path\_func=<functioninterpolate>_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/mobject/mobject.html#Mobject.interpolate) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject.interpolate "Link to this definition")

Turns this [`Mobject`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject") into an interpolation between `mobject1`
and `mobject2`.

Examples

Example: DotInterpolation [¶](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#dotinterpolation)

![../_images/DotInterpolation-1.png](https://docs.manim.community/en/stable/_images/DotInterpolation-1.png)

```
from manim import *

class DotInterpolation(Scene):
    def construct(self):
        dotR = Dot(color=DARK_GREY)
        dotR.shift(2 * RIGHT)
        dotL = Dot(color=WHITE)
        dotL.shift(2 * LEFT)

        dotMiddle = VMobject().interpolate(dotL, dotR, alpha=0.3)

        self.add(dotL, dotR, dotMiddle)

```

Copy to clipboard

Make interactive

Parameters:

- **mobject1** ( [_Mobject_](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject"))

- **mobject2** ( [_Mobject_](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject"))

- **alpha** ( _float_)

- **path\_func** ( [_PathFuncType_](https://docs.manim.community/en/stable/reference/manim.typing.html#manim.typing.PathFuncType "manim.typing.PathFuncType"))


Return type:

Self

invert( _recursive=False_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/mobject/mobject.html#Mobject.invert) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject.invert "Link to this definition")

Inverts the list of [`submobjects`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject.submobjects "manim.mobject.mobject.Mobject.submobjects").

Parameters:

**recursive** ( _bool_) – If `True`, all submobject lists of this mobject’s family are inverted.

Return type:

None

Examples

Example: InvertSumobjectsExample [¶](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#invertsumobjectsexample)

```
from manim import *

class InvertSumobjectsExample(Scene):
    def construct(self):
        s = VGroup(*[Dot().shift(i*0.1*RIGHT) for i in range(-20,20)])
        s2 = s.copy()
        s2.invert()
        s2.shift(DOWN)
        self.play(Write(s), Write(s2))

```

Copy to clipboard

Make interactive

length\_over\_dim( _dim_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/mobject/mobject.html#Mobject.length_over_dim) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject.length_over_dim "Link to this definition")

Measure the length of an [`Mobject`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject") in a certain direction.

Parameters:

**dim** ( _int_)

Return type:

float

match\_color( _mobject_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/mobject/mobject.html#Mobject.match_color) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject.match_color "Link to this definition")

Match the color with the color of another [`Mobject`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject").

Parameters:

**mobject** ( [_Mobject_](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject"))

Return type:

Self

match\_coord( _mobject_, _dim_, _direction=array(\[0.,0.,0.\])_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/mobject/mobject.html#Mobject.match_coord) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject.match_coord "Link to this definition")

Match the Point3Ds with the Point3Ds of another [`Mobject`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject").

Parameters:

- **mobject** ( [_Mobject_](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject"))

- **dim** ( _int_)

- **direction** ( [_Vector3D_](https://docs.manim.community/en/stable/reference/manim.typing.html#manim.typing.Vector3D "manim.typing.Vector3D"))


Return type:

Self

match\_depth( _mobject_, _\*\*kwargs_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/mobject/mobject.html#Mobject.match_depth) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject.match_depth "Link to this definition")

Match the depth with the depth of another [`Mobject`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject").

Parameters:

**mobject** ( [_Mobject_](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject"))

Return type:

Self

match\_dim\_size( _mobject_, _dim_, _\*\*kwargs_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/mobject/mobject.html#Mobject.match_dim_size) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject.match_dim_size "Link to this definition")

Match the specified dimension with the dimension of another [`Mobject`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject").

Parameters:

- **mobject** ( [_Mobject_](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject"))

- **dim** ( _int_)


Return type:

Self

match\_height( _mobject_, _\*\*kwargs_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/mobject/mobject.html#Mobject.match_height) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject.match_height "Link to this definition")

Match the height with the height of another [`Mobject`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject").

Parameters:

**mobject** ( [_Mobject_](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject"))

Return type:

Self

match\_points( _mobject_, _copy\_submobjects=True_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/mobject/mobject.html#Mobject.match_points) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject.match_points "Link to this definition")

Edit points, positions, and submobjects to be identical
to another [`Mobject`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject"), while keeping the style unchanged.

Examples

Example: MatchPointsScene [¶](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#matchpointsscene)

```
from manim import *

class MatchPointsScene(Scene):
    def construct(self):
        circ = Circle(fill_color=RED, fill_opacity=0.8)
        square = Square(fill_color=BLUE, fill_opacity=0.2)
        self.add(circ)
        self.wait(0.5)
        self.play(circ.animate.match_points(square))
        self.wait(0.5)

```

Copy to clipboard

Make interactive

Parameters:

- **mobject** ( [_Mobject_](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject"))

- **copy\_submobjects** ( _bool_)


Return type:

Self

match\_updaters( _mobject_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/mobject/mobject.html#Mobject.match_updaters) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject.match_updaters "Link to this definition")

Match the updaters of the given mobject.

Parameters:

**mobject** ( [_Mobject_](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject")) – The mobject whose updaters get matched.

Returns:

`self`

Return type:

[`Mobject`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject")

Note

All updaters from submobjects are removed, but only updaters of the given
mobject are matched, not those of it’s submobjects.

See also

[`add_updater()`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject.add_updater "manim.mobject.mobject.Mobject.add_updater"), [`clear_updaters()`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject.clear_updaters "manim.mobject.mobject.Mobject.clear_updaters")

match\_width( _mobject_, _\*\*kwargs_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/mobject/mobject.html#Mobject.match_width) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject.match_width "Link to this definition")

Match the width with the width of another [`Mobject`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject").

Parameters:

**mobject** ( [_Mobject_](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject"))

Return type:

Self

match\_x( _mobject_, _direction=array(\[0.,0.,0.\])_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/mobject/mobject.html#Mobject.match_x) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject.match_x "Link to this definition")

Match x coord. to the x coord. of another [`Mobject`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject").

Parameters:

**mobject** ( [_Mobject_](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject"))

Return type:

Self

match\_y( _mobject_, _direction=array(\[0.,0.,0.\])_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/mobject/mobject.html#Mobject.match_y) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject.match_y "Link to this definition")

Match y coord. to the x coord. of another [`Mobject`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject").

Parameters:

**mobject** ( [_Mobject_](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject"))

Return type:

Self

match\_z( _mobject_, _direction=array(\[0.,0.,0.\])_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/mobject/mobject.html#Mobject.match_z) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject.match_z "Link to this definition")

Match z coord. to the x coord. of another [`Mobject`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject").

Parameters:

**mobject** ( [_Mobject_](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject"))

Return type:

Self

move\_to( _point\_or\_mobject_, _aligned\_edge=array(\[0.,0.,0.\])_, _coor\_mask=array(\[1,1,1\])_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/mobject/mobject.html#Mobject.move_to) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject.move_to "Link to this definition")

Move center of the [`Mobject`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject") to certain Point3D.

Parameters:

- **point\_or\_mobject** ( [_Point3DLike_](https://docs.manim.community/en/stable/reference/manim.typing.html#manim.typing.Point3DLike "manim.typing.Point3DLike") _\|_ [_Mobject_](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject"))

- **aligned\_edge** ( [_Vector3D_](https://docs.manim.community/en/stable/reference/manim.typing.html#manim.typing.Vector3D "manim.typing.Vector3D"))

- **coor\_mask** ( [_Vector3D_](https://docs.manim.community/en/stable/reference/manim.typing.html#manim.typing.Vector3D "manim.typing.Vector3D"))


Return type:

Self

next\_to( _mobject\_or\_point_, _direction=array(\[1.,0.,0.\])_, _buff=0.25_, _aligned\_edge=array(\[0.,0.,0.\])_, _submobject\_to\_align=None_, _index\_of\_submobject\_to\_align=None_, _coor\_mask=array(\[1,1,1\])_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/mobject/mobject.html#Mobject.next_to) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject.next_to "Link to this definition")

Move this [`Mobject`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject") next to another’s [`Mobject`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject") or Point3D.

Examples

Example: GeometricShapes [¶](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#geometricshapes)

![../_images/GeometricShapes-1.png](https://docs.manim.community/en/stable/_images/GeometricShapes-1.png)

```
from manim import *

class GeometricShapes(Scene):
    def construct(self):
        d = Dot()
        c = Circle()
        s = Square()
        t = Triangle()
        d.next_to(c, RIGHT)
        s.next_to(c, LEFT)
        t.next_to(c, DOWN)
        self.add(d, c, s, t)

```

Copy to clipboard

Make interactive

Parameters:

- **mobject\_or\_point** ( [_Mobject_](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject") _\|_ [_Point3DLike_](https://docs.manim.community/en/stable/reference/manim.typing.html#manim.typing.Point3DLike "manim.typing.Point3DLike"))

- **direction** ( [_Vector3D_](https://docs.manim.community/en/stable/reference/manim.typing.html#manim.typing.Vector3D "manim.typing.Vector3D"))

- **buff** ( _float_)

- **aligned\_edge** ( [_Vector3D_](https://docs.manim.community/en/stable/reference/manim.typing.html#manim.typing.Vector3D "manim.typing.Vector3D"))

- **submobject\_to\_align** ( [_Mobject_](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject") _\|_ _None_)

- **index\_of\_submobject\_to\_align** ( _int_ _\|_ _None_)

- **coor\_mask** ( [_Vector3D_](https://docs.manim.community/en/stable/reference/manim.typing.html#manim.typing.Vector3D "manim.typing.Vector3D"))


Return type:

Self

null\_point\_align( _mobject_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/mobject/mobject.html#Mobject.null_point_align) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject.null_point_align "Link to this definition")

If a [`Mobject`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject") with points is being aligned to
one without, treat both as groups, and push
the one with points into its own submobjects
list.

Returns:

`self`

Return type:

[`Mobject`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject")

Parameters:

**mobject** ( [_Mobject_](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject"))

reduce\_across\_dimension( _reduce\_func_, _dim_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/mobject/mobject.html#Mobject.reduce_across_dimension) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject.reduce_across_dimension "Link to this definition")

Find the min or max value from a dimension across all points in this and submobjects.

Parameters:

- **reduce\_func** ( _Callable_)

- **dim** ( _int_)


remove( _\*mobjects_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/mobject/mobject.html#Mobject.remove) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject.remove "Link to this definition")

Remove [`submobjects`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject.submobjects "manim.mobject.mobject.Mobject.submobjects").

The mobjects are removed from [`submobjects`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject.submobjects "manim.mobject.mobject.Mobject.submobjects"), if they exist.

Subclasses of mobject may implement `-` and `-=` dunder methods.

Parameters:

**mobjects** ( [_Mobject_](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject")) – The mobjects to remove.

Returns:

`self`

Return type:

[`Mobject`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject")

See also

[`add()`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject.add "manim.mobject.mobject.Mobject.add")

remove\_updater( _update\_function_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/mobject/mobject.html#Mobject.remove_updater) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject.remove_updater "Link to this definition")

Remove an updater.

If the same updater is applied multiple times, every instance gets removed.

Parameters:

**update\_function** ( [_Updater_](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.html#manim.mobject.mobject.Updater "manim.mobject.mobject.Updater")) – The update function to be removed.

Returns:

`self`

Return type:

[`Mobject`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject")

See also

[`clear_updaters()`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject.clear_updaters "manim.mobject.mobject.Mobject.clear_updaters"), [`add_updater()`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject.add_updater "manim.mobject.mobject.Mobject.add_updater"), [`get_updaters()`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject.get_updaters "manim.mobject.mobject.Mobject.get_updaters")

repeat( _count_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/mobject/mobject.html#Mobject.repeat) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject.repeat "Link to this definition")

This can make transition animations nicer

Parameters:

**count** ( _int_)

Return type:

Self

reset\_points() [\[source\]](https://docs.manim.community/en/stable/_modules/manim/mobject/mobject.html#Mobject.reset_points) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject.reset_points "Link to this definition")

Sets [`points`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject.points "manim.mobject.mobject.Mobject.points") to be an empty array.

Return type:

None

restore() [\[source\]](https://docs.manim.community/en/stable/_modules/manim/mobject/mobject.html#Mobject.restore) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject.restore "Link to this definition")

Restores the state that was previously saved with [`save_state()`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject.save_state "manim.mobject.mobject.Mobject.save_state").

Return type:

Self

resume\_updating( _recursive=True_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/mobject/mobject.html#Mobject.resume_updating) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject.resume_updating "Link to this definition")

Enable updating from updaters and animations.

Parameters:

**recursive** ( _bool_) – Whether to recursively enable updating on all submobjects.

Returns:

`self`

Return type:

[`Mobject`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject")

See also

[`suspend_updating()`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject.suspend_updating "manim.mobject.mobject.Mobject.suspend_updating"), [`add_updater()`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject.add_updater "manim.mobject.mobject.Mobject.add_updater")

rotate( _angle_, _axis=array(\[0.,0.,1.\])_, _about\_point=None_, _\*\*kwargs_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/mobject/mobject.html#Mobject.rotate) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject.rotate "Link to this definition")

Rotates the [`Mobject`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject") about a certain point.

Parameters:

- **angle** ( _float_)

- **axis** ( [_Vector3D_](https://docs.manim.community/en/stable/reference/manim.typing.html#manim.typing.Vector3D "manim.typing.Vector3D"))

- **about\_point** ( [_Point3DLike_](https://docs.manim.community/en/stable/reference/manim.typing.html#manim.typing.Point3DLike "manim.typing.Point3DLike") _\|_ _None_)


Return type:

Self

rotate\_about\_origin( _angle_, _axis=array(\[0.,0.,1.\])_, _axes=\[\]_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/mobject/mobject.html#Mobject.rotate_about_origin) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject.rotate_about_origin "Link to this definition")

Rotates the [`Mobject`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject") about the ORIGIN, which is at \[0,0,0\].

Parameters:

- **angle** ( _float_)

- **axis** ( [_Vector3D_](https://docs.manim.community/en/stable/reference/manim.typing.html#manim.typing.Vector3D "manim.typing.Vector3D"))


Return type:

Self

save\_image( _name=None_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/mobject/mobject.html#Mobject.save_image) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject.save_image "Link to this definition")

Saves an image of only this [`Mobject`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject") at its position to a png
file.

Parameters:

**name** ( _str_ _\|_ _None_)

Return type:

None

save\_state() [\[source\]](https://docs.manim.community/en/stable/_modules/manim/mobject/mobject.html#Mobject.save_state) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject.save_state "Link to this definition")

Save the current state (position, color & size). Can be restored with [`restore()`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject.restore "manim.mobject.mobject.Mobject.restore").

Return type:

Self

scale( _scale\_factor_, _\*\*kwargs_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/mobject/mobject.html#Mobject.scale) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject.scale "Link to this definition")

Scale the size by a factor.

Default behavior is to scale about the center of the mobject.

Parameters:

- **scale\_factor** ( _float_) – The scaling factor α. If 0<\|α\|<1, the mobject
will shrink, and for \|α\|>1 it will grow. Furthermore,
if α<0, the mobject is also flipped.

- **kwargs** – Additional keyword arguments passed to
`apply_points_function_about_point()`.


Returns:

`self`

Return type:

[`Mobject`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject")

Examples

Example: MobjectScaleExample [¶](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#mobjectscaleexample)

![../_images/MobjectScaleExample-1.png](https://docs.manim.community/en/stable/_images/MobjectScaleExample-1.png)

```
from manim import *

class MobjectScaleExample(Scene):
    def construct(self):
        f1 = Text("F")
        f2 = Text("F").scale(2)
        f3 = Text("F").scale(0.5)
        f4 = Text("F").scale(-1)

        vgroup = VGroup(f1, f2, f3, f4).arrange(6 * RIGHT)
        self.add(vgroup)

```

Copy to clipboard

Make interactive

See also

[`move_to()`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject.move_to "manim.mobject.mobject.Mobject.move_to")

scale\_to\_fit\_depth( _depth_, _\*\*kwargs_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/mobject/mobject.html#Mobject.scale_to_fit_depth) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject.scale_to_fit_depth "Link to this definition")

Scales the [`Mobject`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject") to fit a depth while keeping width/height proportional.

Parameters:

**depth** ( _float_)

Return type:

Self

scale\_to\_fit\_height( _height_, _\*\*kwargs_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/mobject/mobject.html#Mobject.scale_to_fit_height) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject.scale_to_fit_height "Link to this definition")

Scales the [`Mobject`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject") to fit a height while keeping width/depth proportional.

Returns:

`self`

Return type:

[`Mobject`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject")

Parameters:

**height** ( _float_)

Examples

```
>>> from manim import *
>>> sq = Square()
>>> sq.width
np.float64(2.0)
>>> sq.scale_to_fit_height(5)
Square
>>> sq.height
np.float64(5.0)
>>> sq.width
np.float64(5.0)

```

Copy to clipboard

scale\_to\_fit\_width( _width_, _\*\*kwargs_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/mobject/mobject.html#Mobject.scale_to_fit_width) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject.scale_to_fit_width "Link to this definition")

Scales the [`Mobject`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject") to fit a width while keeping height/depth proportional.

Returns:

`self`

Return type:

[`Mobject`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject")

Parameters:

**width** ( _float_)

Examples

```
>>> from manim import *
>>> sq = Square()
>>> sq.height
np.float64(2.0)
>>> sq.scale_to_fit_width(5)
Square
>>> sq.width
np.float64(5.0)
>>> sq.height
np.float64(5.0)

```

Copy to clipboard

set( _\*\*kwargs_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/mobject/mobject.html#Mobject.set) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject.set "Link to this definition")

Sets attributes.

I.e. `my_mobject.set(foo=1)` applies `my_mobject.foo = 1`.

This is a convenience to be used along with [`animate`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject.animate "manim.mobject.mobject.Mobject.animate") to
animate setting attributes.

In addition to this method, there is a compatibility
layer that allows `get_*` and `set_*` methods to
get and set generic attributes. For instance:

```
>>> mob = Mobject()
>>> mob.set_foo(0)
Mobject
>>> mob.get_foo()
0
>>> mob.foo
0

```

Copy to clipboard

This compatibility layer does not interfere with any
`get_*` or `set_*` methods that are explicitly
defined.

Warning

This compatibility layer is for backwards compatibility
and is not guaranteed to stay around. Where applicable,
please prefer getting/setting attributes normally or with
the [`set()`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject.set "manim.mobject.mobject.Mobject.set") method.

Parameters:

**\*\*kwargs** – The attributes and corresponding values to set.

Returns:

`self`

Return type:

[`Mobject`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject")

Examples

```
>>> mob = Mobject()
>>> mob.set(foo=0)
Mobject
>>> mob.foo
0

```

Copy to clipboard

set\_color( _color=ManimColor('#FFFF00')_, _family=True_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/mobject/mobject.html#Mobject.set_color) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject.set_color "Link to this definition")

Condition is function which takes in one arguments, (x, y, z).
Here it just recurses to submobjects, but in subclasses this
should be further implemented based on the the inner workings
of color

Parameters:

- **color** ( [_ParsableManimColor_](https://docs.manim.community/en/stable/reference/manim.utils.color.core.html#manim.utils.color.core.ParsableManimColor "manim.utils.color.core.ParsableManimColor"))

- **family** ( _bool_)


Return type:

Self

set\_color\_by\_gradient( _\*colors_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/mobject/mobject.html#Mobject.set_color_by_gradient) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject.set_color_by_gradient "Link to this definition")Parameters:

- **colors** ( [_ParsableManimColor_](https://docs.manim.community/en/stable/reference/manim.utils.color.core.html#manim.utils.color.core.ParsableManimColor "manim.utils.color.core.ParsableManimColor")) – The colors to use for the gradient. Use like set\_color\_by\_gradient(RED, BLUE, GREEN).

- **ManimColor.parse** **(** **color** **)** ( _self.color =_)

- **self** ( _return_)


Return type:

Self

_classmethod_ set\_default( _\*\*kwargs_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/mobject/mobject.html#Mobject.set_default) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject.set_default "Link to this definition")

Sets the default values of keyword arguments.

If this method is called without any additional keyword
arguments, the original default values of the initialization
method of this class are restored.

Parameters:

**kwargs** – Passing any keyword argument will update the default
values of the keyword arguments of the initialization
function of this class.

Return type:

None

Examples

```
>>> from manim import Square, GREEN
>>> Square.set_default(color=GREEN, fill_opacity=0.25)
>>> s = Square(); s.color, s.fill_opacity
(ManimColor('#83C167'), 0.25)
>>> Square.set_default()
>>> s = Square(); s.color, s.fill_opacity
(ManimColor('#FFFFFF'), 0.0)

```

Copy to clipboard

Example: ChangedDefaultTextcolor [¶](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#changeddefaulttextcolor)

![../_images/ChangedDefaultTextcolor-1.png](https://docs.manim.community/en/stable/_images/ChangedDefaultTextcolor-1.png)

```
from manim import *

config.background_color = WHITE

class ChangedDefaultTextcolor(Scene):
    def construct(self):
        Text.set_default(color=BLACK)
        self.add(Text("Changing default values is easy!"))

        # we revert the colour back to the default to prevent a bug in the docs.
        Text.set_default(color=WHITE)

```

Copy to clipboard

Make interactive

set\_x( _x_, _direction=array(\[0.,0.,0.\])_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/mobject/mobject.html#Mobject.set_x) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject.set_x "Link to this definition")

Set x value of the center of the [`Mobject`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject") ( `int` or `float`)

Parameters:

- **x** ( _float_)

- **direction** ( [_Vector3D_](https://docs.manim.community/en/stable/reference/manim.typing.html#manim.typing.Vector3D "manim.typing.Vector3D"))


Return type:

Self

set\_y( _y_, _direction=array(\[0.,0.,0.\])_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/mobject/mobject.html#Mobject.set_y) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject.set_y "Link to this definition")

Set y value of the center of the [`Mobject`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject") ( `int` or `float`)

Parameters:

- **y** ( _float_)

- **direction** ( [_Vector3D_](https://docs.manim.community/en/stable/reference/manim.typing.html#manim.typing.Vector3D "manim.typing.Vector3D"))


Return type:

Self

set\_z( _z_, _direction=array(\[0.,0.,0.\])_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/mobject/mobject.html#Mobject.set_z) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject.set_z "Link to this definition")

Set z value of the center of the [`Mobject`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject") ( `int` or `float`)

Parameters:

- **z** ( _float_)

- **direction** ( [_Vector3D_](https://docs.manim.community/en/stable/reference/manim.typing.html#manim.typing.Vector3D "manim.typing.Vector3D"))


Return type:

Self

set\_z\_index( _z\_index\_value_, _family=True_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/mobject/mobject.html#Mobject.set_z_index) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject.set_z_index "Link to this definition")

Sets the [`Mobject`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject")’s `z_index` to the value specified in z\_index\_value.

Parameters:

- **z\_index\_value** ( _float_) – The new value of `z_index` set.

- **family** ( _bool_) – If `True`, the `z_index` value of all submobjects is also set.


Returns:

The Mobject itself, after `z_index` is set. For chaining purposes. (Returns self.)

Return type:

[`Mobject`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject")

Examples

Example: SetZIndex [¶](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#setzindex)

![../_images/SetZIndex-1.png](https://docs.manim.community/en/stable/_images/SetZIndex-1.png)

```
from manim import *

class SetZIndex(Scene):
    def construct(self):
        text = Text('z_index = 3', color = PURE_RED).shift(UP).set_z_index(3)
        square = Square(2, fill_opacity=1).set_z_index(2)
        tex = Tex(r'zIndex = 1', color = PURE_BLUE).shift(DOWN).set_z_index(1)
        circle = Circle(radius = 1.7, color = GREEN, fill_opacity = 1) # z_index = 0

        # Displaying order is now defined by z_index values
        self.add(text)
        self.add(square)
        self.add(tex)
        self.add(circle)

```

Copy to clipboard

Make interactive

set\_z\_index\_by\_z\_Point3D() [\[source\]](https://docs.manim.community/en/stable/_modules/manim/mobject/mobject.html#Mobject.set_z_index_by_z_Point3D) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject.set_z_index_by_z_Point3D "Link to this definition")

Sets the [`Mobject`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject")’s z Point3D to the value of `z_index`.

Returns:

The Mobject itself, after `z_index` is set. (Returns self.)

Return type:

[`Mobject`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject")

shift( _\*vectors_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/mobject/mobject.html#Mobject.shift) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject.shift "Link to this definition")

Shift by the given vectors.

Parameters:

**vectors** ( [_Vector3D_](https://docs.manim.community/en/stable/reference/manim.typing.html#manim.typing.Vector3D "manim.typing.Vector3D")) – Vectors to shift by. If multiple vectors are given, they are added
together.

Returns:

`self`

Return type:

[`Mobject`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject")

See also

[`move_to()`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject.move_to "manim.mobject.mobject.Mobject.move_to")

shuffle( _recursive=False_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/mobject/mobject.html#Mobject.shuffle) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject.shuffle "Link to this definition")

Shuffles the list of [`submobjects`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject.submobjects "manim.mobject.mobject.Mobject.submobjects").

Parameters:

**recursive** ( _bool_)

Return type:

None

shuffle\_submobjects( _\*args_, _\*\*kwargs_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/mobject/mobject.html#Mobject.shuffle_submobjects) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject.shuffle_submobjects "Link to this definition")

Shuffles the order of [`submobjects`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject.submobjects "manim.mobject.mobject.Mobject.submobjects")

Examples

Example: ShuffleSubmobjectsExample [¶](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#shufflesubmobjectsexample)

```
from manim import *

class ShuffleSubmobjectsExample(Scene):
    def construct(self):
        s= VGroup(*[Dot().shift(i*0.1*RIGHT) for i in range(-20,20)])
        s2= s.copy()
        s2.shuffle_submobjects()
        s2.shift(DOWN)
        self.play(Write(s), Write(s2))

```

Copy to clipboard

Make interactive

Return type:

None

sort( _point\_to\_num\_func=<functionMobject.<lambda>>_, _submob\_func=None_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/mobject/mobject.html#Mobject.sort) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject.sort "Link to this definition")

Sorts the list of [`submobjects`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject.submobjects "manim.mobject.mobject.Mobject.submobjects") by a function defined by `submob_func`.

Parameters:

- **point\_to\_num\_func** ( _Callable_ _\[_ _\[_ [_Point3DLike_](https://docs.manim.community/en/stable/reference/manim.typing.html#manim.typing.Point3DLike "manim.typing.Point3DLike") _\]_ _,_ _float_ _\]_)

- **submob\_func** ( _Callable_ _\[_ _\[_ [_Mobject_](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject") _\]_ _,_ _Any_ _\]_ _\|_ _None_)


Return type:

Self

sort\_submobjects( _\*args_, _\*\*kwargs_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/mobject/mobject.html#Mobject.sort_submobjects) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject.sort_submobjects "Link to this definition")

Sort the [`submobjects`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject.submobjects "manim.mobject.mobject.Mobject.submobjects")

Return type:

Self

stretch\_to\_fit\_depth( _depth_, _\*\*kwargs_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/mobject/mobject.html#Mobject.stretch_to_fit_depth) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject.stretch_to_fit_depth "Link to this definition")

Stretches the [`Mobject`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject") to fit a depth, not keeping width/height proportional.

Parameters:

**depth** ( _float_)

Return type:

Self

stretch\_to\_fit\_height( _height_, _\*\*kwargs_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/mobject/mobject.html#Mobject.stretch_to_fit_height) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject.stretch_to_fit_height "Link to this definition")

Stretches the [`Mobject`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject") to fit a height, not keeping width/depth proportional.

Returns:

`self`

Return type:

[`Mobject`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject")

Parameters:

**height** ( _float_)

Examples

```
>>> from manim import *
>>> sq = Square()
>>> sq.width
np.float64(2.0)
>>> sq.stretch_to_fit_height(5)
Square
>>> sq.height
np.float64(5.0)
>>> sq.width
np.float64(2.0)

```

Copy to clipboard

stretch\_to\_fit\_width( _width_, _\*\*kwargs_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/mobject/mobject.html#Mobject.stretch_to_fit_width) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject.stretch_to_fit_width "Link to this definition")

Stretches the [`Mobject`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject") to fit a width, not keeping height/depth proportional.

Returns:

`self`

Return type:

[`Mobject`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject")

Parameters:

**width** ( _float_)

Examples

```
>>> from manim import *
>>> sq = Square()
>>> sq.height
np.float64(2.0)
>>> sq.stretch_to_fit_width(5)
Square
>>> sq.width
np.float64(5.0)
>>> sq.height
np.float64(2.0)

```

Copy to clipboard

suspend\_updating( _recursive=True_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/mobject/mobject.html#Mobject.suspend_updating) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject.suspend_updating "Link to this definition")

Disable updating from updaters and animations.

Parameters:

**recursive** ( _bool_) – Whether to recursively suspend updating on all submobjects.

Returns:

`self`

Return type:

[`Mobject`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject")

See also

[`resume_updating()`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject.resume_updating "manim.mobject.mobject.Mobject.resume_updating"), [`add_updater()`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject.add_updater "manim.mobject.mobject.Mobject.add_updater")

to\_corner( _corner=array(\[-1.,-1.,0.\])_, _buff=0.5_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/mobject/mobject.html#Mobject.to_corner) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject.to_corner "Link to this definition")

Moves this [`Mobject`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject") to the given corner of the screen.

Returns:

The newly positioned mobject.

Return type:

[`Mobject`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject")

Parameters:

- **corner** ( [_Vector3D_](https://docs.manim.community/en/stable/reference/manim.typing.html#manim.typing.Vector3D "manim.typing.Vector3D"))

- **buff** ( _float_)


Examples

Example: ToCornerExample [¶](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#tocornerexample)

![../_images/ToCornerExample-1.png](https://docs.manim.community/en/stable/_images/ToCornerExample-1.png)

```
from manim import *

class ToCornerExample(Scene):
    def construct(self):
        c = Circle()
        c.to_corner(UR)
        t = Tex("To the corner!")
        t2 = MathTex("x^3").shift(DOWN)
        self.add(c,t,t2)
        t.to_corner(DL, buff=0)
        t2.to_corner(UL, buff=1.5)

```

Copy to clipboard

Make interactive

to\_edge( _edge=array(\[-1.,0.,0.\])_, _buff=0.5_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/mobject/mobject.html#Mobject.to_edge) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject.to_edge "Link to this definition")

Moves this [`Mobject`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject") to the given edge of the screen,
without affecting its position in the other dimension.

Returns:

The newly positioned mobject.

Return type:

[`Mobject`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject")

Parameters:

- **edge** ( [_Vector3D_](https://docs.manim.community/en/stable/reference/manim.typing.html#manim.typing.Vector3D "manim.typing.Vector3D"))

- **buff** ( _float_)


Examples

Example: ToEdgeExample [¶](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#toedgeexample)

![../_images/ToEdgeExample-1.png](https://docs.manim.community/en/stable/_images/ToEdgeExample-1.png)

```
from manim import *

class ToEdgeExample(Scene):
    def construct(self):
        tex_top = Tex("I am at the top!")
        tex_top.to_edge(UP)
        tex_side = Tex("I am moving to the side!")
        c = Circle().shift(2*DOWN)
        self.add(tex_top, tex_side, c)
        tex_side.to_edge(LEFT)
        c.to_edge(RIGHT, buff=0)

```

Copy to clipboard

Make interactive

update( _dt=0_, _recursive=True_) [\[source\]](https://docs.manim.community/en/stable/_modules/manim/mobject/mobject.html#Mobject.update) [¶](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject.update "Link to this definition")

Apply all updaters.

Does nothing if updating is suspended.

Parameters:

- **dt** ( _float_) – The parameter `dt` to pass to the update functions. Usually this is the
time in seconds since the last call of `update`.

- **recursive** ( _bool_) – Whether to recursively update all submobjects.


Returns:

`self`

Return type:

[`Mobject`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject "manim.mobject.mobject.Mobject")

See also

[`add_updater()`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject.add_updater "manim.mobject.mobject.Mobject.add_updater"), [`get_updaters()`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject.get_updaters "manim.mobject.mobject.Mobject.get_updaters")

_property_ width _:float_ [¶](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject.width "Link to this definition")

The width of the mobject.

Return type:

`float`

Examples

Example: WidthExample [¶](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#widthexample)

```
from manim import *

class WidthExample(Scene):
    def construct(self):
        decimal = DecimalNumber().to_edge(UP)
        rect = Rectangle(color=BLUE)
        rect_copy = rect.copy().set_stroke(GRAY, opacity=0.5)

        decimal.add_updater(lambda d: d.set_value(rect.width))

        self.add(rect_copy, rect, decimal)
        self.play(rect.animate.set(width=7))
        self.wait()

```

Copy to clipboard

Make interactive

See also

[`length_over_dim()`](https://docs.manim.community/en/stable/reference/manim.mobject.mobject.Mobject.html#manim.mobject.mobject.Mobject.length_over_dim "manim.mobject.mobject.Mobject.length_over_dim")