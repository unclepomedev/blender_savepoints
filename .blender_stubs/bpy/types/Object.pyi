# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.Object.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .ID import ID
from .AnimData import AnimData
from .AnimViz import AnimViz
from .AssetMetaData import AssetMetaData
from .Collection import Collection
from .CollisionSettings import CollisionSettings
from .Constraint import Constraint
from .FieldSettings import FieldSettings
from .IDOverrideLibrary import IDOverrideLibrary
from .ImagePreview import ImagePreview
from .ImageUser import ImageUser
from .Library import Library
from .LibraryWeakReference import LibraryWeakReference
from .Material import Material
from .MaterialSlot import MaterialSlot
from .Modifier import Modifier
from .MotionPath import MotionPath
from .ObjectConstraints import ObjectConstraints
from .ObjectDisplay import ObjectDisplay
from .ObjectLightLinking import ObjectLightLinking
from .ObjectLineArt import ObjectLineArt
from .ObjectModifiers import ObjectModifiers
from .ObjectShaderFx import ObjectShaderFx
from .ParticleSystem import ParticleSystem
from .ParticleSystems import ParticleSystems
from .Pose import Pose
from .RigidBodyConstraint import RigidBodyConstraint
from .RigidBodyObject import RigidBodyObject
from .ShaderFx import ShaderFx
from .ShapeKey import ShapeKey
from .SoftBodySettings import SoftBodySettings
from .VertexGroup import VertexGroup
from .VertexGroups import VertexGroups
from .bpy_prop_collection import bpy_prop_collection

class Object(ID):

    name: Annotated[str, "is_animatable=False"]
    """Unique data-block ID name (within a same type and library)"""
    @property
    def name_full(self) -> Annotated[str, "is_animatable=False"]:
        """Unique data-block ID name, including library one if any"""
        ...
    @property
    def id_type(self) -> Literal['ACTION', 'ARMATURE', 'BRUSH', 'CACHEFILE', 'CAMERA', 'COLLECTION', 'CURVE', 'CURVES', 'FONT', 'GREASEPENCIL', 'GREASEPENCIL_V3', 'IMAGE', 'KEY', 'LATTICE', 'LIBRARY', 'LIGHT', 'LIGHT_PROBE', 'LINESTYLE', 'MASK', 'MATERIAL', 'MESH', 'META', 'MOVIECLIP', 'NODETREE', 'OBJECT', 'PAINTCURVE', 'PALETTE', 'PARTICLE', 'POINTCLOUD', 'SCENE', 'SCREEN', 'SOUND', 'SPEAKER', 'TEXT', 'TEXTURE', 'VOLUME', 'WINDOWMANAGER', 'WORKSPACE', 'WORLD']:
        """Type identifier of this data-block"""
        ...
    @property
    def session_uid(self) -> Annotated[int, "step=1"]:
        """A session-wide unique identifier for the data block that remains the same across renames and internal reallocations, unchanged when reloading the file"""
        ...
    @property
    def is_evaluated(self) -> bool:
        """Whether this ID is runtime-only, evaluated data-block, or actual data from .blend file"""
        ...
    @property
    def original(self) -> Annotated[Optional['ID'], "is_animatable=False"]:
        """Actual data-block from .blend file (Main database) that generated that evaluated one"""
        ...
    @property
    def users(self) -> Annotated[int, "subtype='UNSIGNED'", "step=1"]:
        """Number of times this data-block is referenced"""
        ...
    use_fake_user: bool
    """Save this data-block even if it has no users"""
    use_extra_user: bool
    """Indicates whether an extra user is set or not (mainly for internal/debug usages)"""
    @property
    def is_embedded_data(self) -> bool:
        """This data-block is not an independent one, but is actually a sub-data of another ID (typical example: root node trees or master collections)"""
        ...
    @property
    def is_linked_packed(self) -> bool:
        """This data-block is linked and packed into the .blend file"""
        ...
    @property
    def is_missing(self) -> bool:
        """This data-block is a place-holder for missing linked data (i.e. it is [an override of] a linked data that could not be found anymore)"""
        ...
    is_runtime_data: bool
    """This data-block is runtime data, i.e. it won't be saved in .blend file. Note that e.g. evaluated IDs are always runtime, so this value is only editable for data-blocks in Main data-base."""
    @property
    def is_editable(self) -> bool:
        """This data-block is editable in the user interface. Linked data-blocks are not editable, except if they were loaded as editable assets."""
        ...
    tag: bool
    """Tools can use this to tag data for their own purposes (initial state is undefined)"""
    @property
    def is_library_indirect(self) -> bool:
        """Is this ID block linked indirectly"""
        ...
    @property
    def library(self) -> Annotated[Optional['Library'], "is_animatable=False"]:
        """Library file the data-block is linked from"""
        ...
    @property
    def library_weak_reference(self) -> Annotated[Optional['LibraryWeakReference'], "is_animatable=False"]:
        """Weak reference to a data-block in another library .blend file (used to re-use already appended data instead of appending new copies)"""
        ...
    asset_data: Annotated[Optional['AssetMetaData'], "is_animatable=False"]
    """Additional data for an asset data-block"""
    @property
    def override_library(self) -> Annotated[Optional['IDOverrideLibrary'], "is_animatable=False"]:
        """Library override data"""
        ...
    @property
    def preview(self) -> Annotated[Optional['ImagePreview'], "is_animatable=False"]:
        """Preview image and icon of this data-block (always None if not supported for this type of data)"""
        ...
    data: Annotated[Optional['ID'], "is_animatable=False"]
    """Object data"""
    @property
    def type(self) -> Literal['MESH', 'CURVE', 'SURFACE', 'META', 'FONT', 'CURVES', 'POINTCLOUD', 'VOLUME', 'GREASEPENCIL', 'ARMATURE', 'LATTICE', 'EMPTY', 'LIGHT', 'LIGHT_PROBE', 'CAMERA', 'SPEAKER']:
        """Type of object"""
        ...
    @property
    def mode(self) -> Literal['OBJECT', 'EDIT', 'POSE', 'SCULPT', 'VERTEX_PAINT', 'WEIGHT_PAINT', 'TEXTURE_PAINT', 'PARTICLE_EDIT', 'EDIT_GPENCIL', 'SCULPT_GREASE_PENCIL', 'PAINT_GREASE_PENCIL', 'WEIGHT_GREASE_PENCIL', 'VERTEX_GREASE_PENCIL', 'SCULPT_CURVES']:
        """Object interaction mode"""
        ...
    @property
    def bound_box(self) -> Annotated[list[float], "step=10.0", "precision=3"]:
        """Object's bounding box in object-space coordinates, all values are -1.0 when not available"""
        ...
    parent: Annotated[Optional['Object'], "is_animatable=False"]
    """Parent object"""
    parent_type: Literal['OBJECT', 'ARMATURE', 'LATTICE', 'VERTEX', 'VERTEX_3', 'BONE']
    """Type of parent relation"""
    parent_vertices: Annotated[list[int], "subtype='UNSIGNED'", "step=1"]
    """Indices of vertices in case of a vertex parenting relation"""
    parent_bone: Annotated[str, "is_animatable=False"]
    """Name of parent bone in case of a bone parenting relation"""
    use_parent_final_indices: bool
    """Use the final evaluated indices rather than the original mesh indices"""
    use_camera_lock_parent: bool
    """View Lock 3D viewport camera transformation affects the object's parent instead"""
    track_axis: Literal['POS_X', 'POS_Y', 'POS_Z', 'NEG_X', 'NEG_Y', 'NEG_Z']
    """Axis that points in the 'forward' direction (applies to Instance Vertices when Align to Vertex Normal is enabled)"""
    up_axis: Literal['X', 'Y', 'Z']
    """Axis that points in the upward direction (applies to Instance Vertices when Align to Vertex Normal is enabled)"""
    @property
    def material_slots(self) -> Annotated[bpy_prop_collection['MaterialSlot'], "is_animatable=False"]:
        """Material slots in the object"""
        ...
    active_material: Annotated[Optional['Material'], "is_animatable=False"]
    """Active material being displayed"""
    active_material_index: Annotated[int, "subtype='UNSIGNED'", "step=1", "is_animatable=False"]
    """Index of active material slot"""
    location: Annotated[list[float], "subtype='TRANSLATION'", "unit='LENGTH'", "step=1.0", "precision=5"]
    """Location of the object"""
    rotation_quaternion: Annotated[list[float], "subtype='QUATERNION'", "step=10.0", "precision=3"]
    """Rotation in Quaternions"""
    rotation_axis_angle: Annotated[list[float], "subtype='AXISANGLE'", "step=10.0", "precision=3"]
    """Angle of Rotation for Axis-Angle rotation representation"""
    rotation_euler: Annotated[list[float], "subtype='EULER'", "unit='ROTATION'", "step=100.0", "precision=5"]
    """Rotation in Eulers"""
    rotation_mode: Literal['QUATERNION', 'XYZ', 'XZY', 'YXZ', 'YZX', 'ZXY', 'ZYX', 'AXIS_ANGLE']
    """The kind of rotation to apply, values from other rotation modes are not used"""
    scale: Annotated[list[float], "subtype='XYZ'", "step=1.0", "precision=3"]
    """Scaling of the object"""
    dimensions: Annotated[list[float], "subtype='XYZ_LENGTH'", "unit='LENGTH'", "step=1.0", "precision=5", "is_animatable=False"]
    """Absolute bounding box dimensions of the object.
Warning: Assigning to it or its members multiple consecutive times will not work correctly, as this needs up-to-date evaluated data"""
    delta_location: Annotated[list[float], "subtype='TRANSLATION'", "unit='LENGTH'", "step=1.0", "precision=5"]
    """Extra translation added to the location of the object"""
    delta_rotation_euler: Annotated[list[float], "subtype='EULER'", "unit='ROTATION'", "step=100.0", "precision=5"]
    """Extra rotation added to the rotation of the object (when using Euler rotations)"""
    delta_rotation_quaternion: Annotated[list[float], "subtype='QUATERNION'", "step=10.0", "precision=3"]
    """Extra rotation added to the rotation of the object (when using Quaternion rotations)"""
    delta_scale: Annotated[list[float], "subtype='XYZ'", "step=1.0", "precision=3"]
    """Extra scaling added to the scale of the object"""
    lock_location: list[bool]
    """Lock editing of location when transforming"""
    lock_rotation: list[bool]
    """Lock editing of rotation when transforming"""
    lock_rotation_w: bool
    """Lock editing of 'angle' component of four-component rotations when transforming"""
    lock_rotations_4d: bool
    """Lock editing of four component rotations by components (instead of as Eulers)"""
    lock_scale: list[bool]
    """Lock editing of scale when transforming"""
    matrix_world: Annotated[list[float], "subtype='MATRIX'", "step=10.0", "precision=3", "is_animatable=False"]
    """Worldspace transformation matrix"""
    matrix_local: Annotated[list[float], "subtype='MATRIX'", "step=10.0", "precision=3", "is_animatable=False"]
    """Parent relative transformation matrix.
Warning: Only takes into account object parenting, so e.g. in case of bone parenting you get a matrix relative to the Armature object, not to the actual parent bone"""
    matrix_basis: Annotated[list[float], "subtype='MATRIX'", "step=10.0", "precision=3", "is_animatable=False"]
    """Matrix access to location, rotation and scale (including deltas), before constraints and parenting are applied"""
    matrix_parent_inverse: Annotated[list[float], "subtype='MATRIX'", "step=10.0", "precision=3"]
    """Inverse of object's parent matrix at time of parenting"""
    @property
    def modifiers(self) -> Annotated['ObjectModifiers', "is_animatable=False"]:
        """Modifiers affecting the geometric data of the object"""
        ...
    @property
    def shader_effects(self) -> Annotated['ObjectShaderFx', "is_animatable=False"]:
        """Effects affecting display of object"""
        ...
    @property
    def constraints(self) -> Annotated['ObjectConstraints', "is_animatable=False"]:
        """Constraints affecting the transformation of the object"""
        ...
    @property
    def vertex_groups(self) -> Annotated['VertexGroups', "is_animatable=False"]:
        """Vertex groups of the object"""
        ...
    empty_display_type: Literal['PLAIN_AXES', 'ARROWS', 'SINGLE_ARROW', 'CIRCLE', 'CUBE', 'SPHERE', 'CONE', 'IMAGE']
    """Viewport display style for empties"""
    empty_display_size: Annotated[float, "subtype='DISTANCE'", "unit='LENGTH'", "step=1.0", "precision=2"]
    """Size of display for empties in the viewport"""
    empty_image_offset: Annotated[list[float], "step=0.10000000149011612", "precision=2"]
    """Origin offset distance"""
    @property
    def image_user(self) -> Annotated['ImageUser', "is_animatable=False"]:
        """Parameters defining which layer, pass and frame of the image is displayed"""
        ...
    empty_image_depth: Literal['DEFAULT', 'FRONT', 'BACK']
    """Determine which other objects will occlude the image"""
    show_empty_image_perspective: bool
    """Display image in perspective mode"""
    show_empty_image_orthographic: bool
    """Display image in orthographic mode"""
    show_empty_image_only_axis_aligned: bool
    """Only display the image when it is aligned with the view axis"""
    use_empty_image_alpha: bool
    """Use alpha blending instead of alpha test (can produce sorting artifacts)"""
    empty_image_side: Literal['DOUBLE_SIDED', 'FRONT', 'BACK']
    """Show front/back side"""
    add_rest_position_attribute: bool
    """Add a "rest_position" attribute that is a copy of the position attribute before shape keys and modifiers are evaluated"""
    pass_index: Annotated[int, "subtype='UNSIGNED'", "step=1"]
    """Index number for the "Object Index" render pass"""
    color: Annotated[list[float], "subtype='COLOR'", "step=10.0", "precision=3"]
    """Object color and alpha, used when the Object Color mode is enabled"""
    @property
    def field(self) -> Annotated[Optional['FieldSettings'], "is_animatable=False"]:
        """Settings for using the object as a field in physics simulation"""
        ...
    @property
    def collision(self) -> Annotated[Optional['CollisionSettings'], "is_animatable=False"]:
        """Settings for using the object as a collider in physics simulation"""
        ...
    @property
    def soft_body(self) -> Annotated[Optional['SoftBodySettings'], "is_animatable=False"]:
        """Settings for soft body simulation"""
        ...
    @property
    def particle_systems(self) -> Annotated['ParticleSystems', "is_animatable=False"]:
        """Particle systems emitted from the object"""
        ...
    @property
    def rigid_body(self) -> Annotated[Optional['RigidBodyObject'], "is_animatable=False"]:
        """Settings for rigid body simulation"""
        ...
    @property
    def rigid_body_constraint(self) -> Annotated[Optional['RigidBodyConstraint'], "is_animatable=False"]:
        """Constraint constraining rigid bodies"""
        ...
    use_simulation_cache: Annotated[bool, "is_animatable=False"]
    """Cache frames during simulation nodes playback"""
    hide_viewport: bool
    """Globally disable in viewports"""
    hide_select: Annotated[bool, "is_animatable=False"]
    """Disable selection in viewport"""
    hide_render: bool
    """Globally disable in renders"""
    hide_probe_volume: bool
    """Globally disable in volume probes"""
    hide_probe_sphere: bool
    """Globally disable in spherical light probes"""
    hide_probe_plane: bool
    """Globally disable in planar light probes"""
    hide_surface_pick: bool
    """Disable surface influence during selection, snapping and depth-picking operators. Usually used to avoid semi-transparent objects to affect scene navigation"""
    show_instancer_for_render: bool
    """Make instancer visible when rendering"""
    show_instancer_for_viewport: bool
    """Make instancer visible in the viewport"""
    visible_camera: bool
    """Object visibility to camera rays"""
    visible_diffuse: bool
    """Object visibility to diffuse rays"""
    visible_glossy: bool
    """Object visibility to glossy rays"""
    visible_transmission: bool
    """Object visibility to transmission rays"""
    visible_volume_scatter: bool
    """Object visibility to volume scattering rays"""
    visible_shadow: bool
    """Object visibility to shadow rays"""
    is_holdout: bool
    """Render objects as a holdout or matte, creating a hole in the image with zero alpha, to fill out in compositing with real footage or another render"""
    is_shadow_catcher: bool
    """Only render shadows and reflections on this object, for compositing renders into real footage. Objects with this setting are considered to already exist in the footage, objects without it are synthetic objects being composited into it."""
    instance_type: Literal['NONE', 'VERTS', 'FACES', 'COLLECTION']
    """If not None, object instancing method to use"""
    use_instance_vertices_rotation: bool
    """Rotate instance according to vertex normal"""
    use_instance_faces_scale: bool
    """Scale instance based on face size"""
    instance_faces_scale: Annotated[float, "step=10.0", "precision=3"]
    """Scale the face instance objects"""
    instance_collection: Annotated[Optional['Collection'], "is_animatable=False"]
    """Instance an existing collection"""
    @property
    def is_instancer(self) -> bool:

        ...
    display_type: Literal['BOUNDS', 'WIRE', 'SOLID', 'TEXTURED']
    """How to display object in viewport"""
    show_bounds: bool
    """Display the object's bounds"""
    display_bounds_type: Literal['BOX', 'SPHERE', 'CYLINDER', 'CONE', 'CAPSULE']
    """Object boundary display type"""
    show_name: bool
    """Display the object's name"""
    show_axis: bool
    """Display the object's origin and axes"""
    show_texture_space: bool
    """Display the object's texture space"""
    show_wire: bool
    """Display the object's wireframe over solid shading"""
    show_all_edges: bool
    """Display all edges for mesh objects"""
    use_grease_pencil_lights: bool
    """Lights affect Grease Pencil object"""
    show_transparent: bool
    """Display material transparency in the object"""
    show_in_front: bool
    """Make the object display in front of others"""
    @property
    def pose(self) -> Annotated[Optional['Pose'], "is_animatable=False"]:
        """Current pose for armatures"""
        ...
    show_only_shape_key: bool
    """Only show the active shape key at full value"""
    use_shape_key_edit_mode: bool
    """Display shape keys in edit mode (for meshes only)"""
    @property
    def active_shape_key(self) -> Annotated[Optional['ShapeKey'], "is_animatable=False"]:
        """Current shape key"""
        ...
    active_shape_key_index: Annotated[int, "step=1", "is_animatable=False"]
    """Current shape key index"""
    @property
    def use_dynamic_topology_sculpting(self) -> bool:

        ...
    @property
    def is_from_instancer(self) -> bool:
        """Object comes from a instancer"""
        ...
    @property
    def is_from_set(self) -> bool:
        """Object comes from a background set"""
        ...
    @property
    def display(self) -> Annotated['ObjectDisplay', "is_animatable=False"]:
        """Object display settings for 3D viewport"""
        ...
    @property
    def lineart(self) -> Annotated[Optional['ObjectLineArt'], "is_animatable=False"]:
        """Line Art settings for the object"""
        ...
    use_mesh_mirror_x: bool
    """Enable mesh symmetry in the X axis"""
    use_mesh_mirror_y: bool
    """Enable mesh symmetry in the Y axis"""
    use_mesh_mirror_z: bool
    """Enable mesh symmetry in the Z axis"""
    lightgroup: Annotated[str, "is_animatable=False"]
    """Lightgroup that the object belongs to"""
    @property
    def light_linking(self) -> Annotated['ObjectLightLinking', "is_animatable=False"]:
        """Light linking settings"""
        ...
    shadow_terminator_normal_offset: Annotated[float, "subtype='DISTANCE'", "unit='LENGTH'", "step=0.009999999776482582", "precision=4"]
    """Offset rays from the surface to reduce shadow terminator artifact on low poly geometry. Only affect triangles that are affected by the geometry offset"""
    shadow_terminator_geometry_offset: Annotated[float, "subtype='FACTOR'", "step=1.0", "precision=2"]
    """Offset rays from the surface to reduce shadow terminator artifact on low poly geometry. Only affects triangles at grazing angles to light"""
    shadow_terminator_shading_offset: Annotated[float, "subtype='FACTOR'", "step=1.0", "precision=2"]
    """Push the shadow terminator towards the light to hide artifacts on low poly geometry"""
    @property
    def animation_data(self) -> Annotated[Optional['AnimData'], "is_animatable=False"]:
        """Animation data for this data-block"""
        ...
    @property
    def animation_visualization(self) -> Annotated['AnimViz', "is_animatable=False"]:
        """Animation data for this data-block"""
        ...
    @property
    def motion_path(self) -> Annotated[Optional['MotionPath'], "is_animatable=False"]:
        """Motion Path for this element"""
        ...
    @property
    def selection_sets(self) -> Annotated[bpy_prop_collection['SelectionSet'], "is_animatable=False"]:
        """List of groups of bones for easy selection"""
        ...
    active_selection_set: Annotated[int, "step=1"]
    """Index of the currently active selection set"""
    @property
    def cycles(self) -> Annotated[Optional['CyclesObjectSettings'], "is_animatable=False"]:
        """Cycles object settings"""
        ...
    def bl_system_properties_get(self, *args, **kwargs) -> Any: ...
    def rename(self, *args, **kwargs) -> Any: ...
    def evaluated_get(self, *args, **kwargs) -> Any: ...
    def copy(self, *args, **kwargs) -> Any: ...
    def asset_mark(self, *args, **kwargs) -> Any: ...
    def asset_clear(self, *args, **kwargs) -> Any: ...
    def asset_generate_preview(self, *args, **kwargs) -> Any: ...
    def override_create(self, *args, **kwargs) -> Any: ...
    def override_hierarchy_create(self, *args, **kwargs) -> Any: ...
    def user_clear(self, *args, **kwargs) -> Any: ...
    def user_remap(self, *args, **kwargs) -> Any: ...
    def make_local(self, *args, **kwargs) -> Any: ...
    def user_of_id(self, *args, **kwargs) -> Any: ...
    def animation_data_create(self, *args, **kwargs) -> Any: ...
    def animation_data_clear(self, *args, **kwargs) -> Any: ...
    def update_tag(self, *args, **kwargs) -> Any: ...
    def preview_ensure(self, *args, **kwargs) -> Any: ...
    def select_get(self, *args, **kwargs) -> Any: ...
    def select_set(self, *args, **kwargs) -> Any: ...
    def hide_get(self, *args, **kwargs) -> Any: ...
    def hide_set(self, *args, **kwargs) -> Any: ...
    def visible_get(self, *args, **kwargs) -> Any: ...
    def holdout_get(self, *args, **kwargs) -> Any: ...
    def indirect_only_get(self, *args, **kwargs) -> Any: ...
    def local_view_get(self, *args, **kwargs) -> Any: ...
    def local_view_set(self, *args, **kwargs) -> Any: ...
    def visible_in_viewport_get(self, *args, **kwargs) -> Any: ...
    def convert_space(self, *args, **kwargs) -> Any: ...
    def calc_matrix_camera(self, *args, **kwargs) -> Any: ...
    def camera_fit_coords(self, *args, **kwargs) -> Any: ...
    def crazyspace_eval(self, *args, **kwargs) -> Any: ...
    def crazyspace_displacement_to_deformed(self, *args, **kwargs) -> Any: ...
    def crazyspace_displacement_to_original(self, *args, **kwargs) -> Any: ...
    def crazyspace_eval_clear(self, *args, **kwargs) -> Any: ...
    def to_mesh(self, *args, **kwargs) -> Any: ...
    def to_mesh_clear(self, *args, **kwargs) -> Any: ...
    def to_curve(self, *args, **kwargs) -> Any: ...
    def to_curve_clear(self, *args, **kwargs) -> Any: ...
    def find_armature(self, *args, **kwargs) -> Any: ...
    def shape_key_add(self, *args, **kwargs) -> Any: ...
    def shape_key_remove(self, *args, **kwargs) -> Any: ...
    def shape_key_clear(self, *args, **kwargs) -> Any: ...
    def ray_cast(self, *args, **kwargs) -> Any: ...
    def closest_point_on_mesh(self, *args, **kwargs) -> Any: ...
    def is_modified(self, *args, **kwargs) -> Any: ...
    def is_deform_modified(self, *args, **kwargs) -> Any: ...
    def update_from_editmode(self, *args, **kwargs) -> Any: ...
    def cache_release(self, *args, **kwargs) -> Any: ...
    # --- Injected Methods ---
    def select_set(self, state: bool) -> None: ...
    def select_get(self) -> bool: ...
    def hide_set(self, state: bool) -> None: ...
    def hide_get(self) -> bool: ...
    def hide_viewport_set(self, state: bool) -> None: ...
    def hide_render_set(self, state: bool) -> None: ...
    def temp_override(self, window=None, area=None, region=None, **kwargs) -> Any: ...