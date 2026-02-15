# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.SpaceView3D.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .Space import Space
from .Object import Object
from .RegionView3D import RegionView3D
from .View3DOverlay import View3DOverlay
from .View3DShading import View3DShading
from .bpy_prop_collection import bpy_prop_collection

class SpaceView3D(Space):

    @property
    def type(self) -> Literal['EMPTY', 'VIEW_3D', 'IMAGE_EDITOR', 'NODE_EDITOR', 'SEQUENCE_EDITOR', 'CLIP_EDITOR', 'DOPESHEET_EDITOR', 'GRAPH_EDITOR', 'NLA_EDITOR', 'TEXT_EDITOR', 'CONSOLE', 'INFO', 'TOPBAR', 'STATUSBAR', 'OUTLINER', 'PROPERTIES', 'FILE_BROWSER', 'SPREADSHEET', 'PREFERENCES']:
        """Space data type"""
        ...
    show_locked_time: bool
    """Synchronize the visible timeline range with other time-based editors"""
    show_region_header: bool

    show_region_tool_header: bool

    show_region_toolbar: bool

    show_region_ui: bool

    show_region_hud: bool

    show_region_asset_shelf: bool
    """Display a region with assets that may currently be relevant (such as brushes in paint modes, or poses in Pose Mode)"""
    camera: Annotated[Optional['Object'], "is_animatable=False"]
    """Active camera used in this view (when unlocked from the scene's active camera)"""
    use_render_border: Annotated[bool, "is_animatable=False"]
    """Use a region within the frame size for rendered viewport (when not viewing through the camera)"""
    render_border_min_x: Annotated[float, "step=10.0", "precision=3"]
    """Minimum X value for the render region"""
    render_border_min_y: Annotated[float, "step=10.0", "precision=3"]
    """Minimum Y value for the render region"""
    render_border_max_x: Annotated[float, "step=10.0", "precision=3"]
    """Maximum X value for the render region"""
    render_border_max_y: Annotated[float, "step=10.0", "precision=3"]
    """Maximum Y value for the render region"""
    lock_object: Annotated[Optional['Object'], "is_animatable=False"]
    """3D View center is locked to this object's position"""
    lock_bone: Annotated[str, "is_animatable=False"]
    """3D View center is locked to this bone's position"""
    lock_cursor: bool
    """3D View center is locked to the cursor's position"""
    @property
    def local_view(self) -> Annotated[Optional['SpaceView3D'], "is_animatable=False"]:
        """Display an isolated subset of objects, apart from the scene visibility"""
        ...
    lens: Annotated[float, "subtype=''", "unit='CAMERA'", "step=10.0", "precision=3"]
    """Viewport lens angle"""
    clip_start: Annotated[float, "subtype='DISTANCE'", "unit='LENGTH'", "step=10.0", "precision=3"]
    """3D View near clipping distance (perspective view only)"""
    clip_end: Annotated[float, "subtype='DISTANCE'", "unit='LENGTH'", "step=10.0", "precision=3"]
    """3D View far clipping distance"""
    lock_camera: bool
    """Enable view navigation within the camera view"""
    show_gizmo: bool
    """Show gizmos of all types"""
    show_gizmo_navigate: bool
    """Viewport navigation gizmo"""
    show_gizmo_context: bool
    """Context sensitive gizmos for the active item"""
    show_gizmo_modifier: bool
    """Gizmos for the active modifier"""
    show_gizmo_tool: bool
    """Active tool gizmo"""
    show_gizmo_object_translate: bool
    """Gizmo to adjust location"""
    show_gizmo_object_rotate: bool
    """Gizmo to adjust rotation"""
    show_gizmo_object_scale: bool
    """Gizmo to adjust scale"""
    show_gizmo_empty_image: bool
    """Gizmo to adjust image size and position"""
    show_gizmo_empty_force_field: bool
    """Gizmo to adjust the force field"""
    show_gizmo_light_size: bool
    """Gizmo to adjust spot and area size"""
    show_gizmo_light_look_at: bool
    """Gizmo to adjust the direction of the light"""
    show_gizmo_camera_lens: bool
    """Gizmo to adjust camera focal length or orthographic scale"""
    show_gizmo_camera_dof_distance: bool
    """Gizmo to adjust camera focus distance (depends on limits display)"""
    use_local_camera: bool
    """Use a local camera in this view, rather than scene's active camera"""
    @property
    def region_3d(self) -> Annotated[Optional['RegionView3D'], "is_animatable=False"]:
        """3D region for this space. When the space is in quad view, the camera region"""
        ...
    @property
    def region_quadviews(self) -> Annotated[bpy_prop_collection['RegionView3D'], "is_animatable=False"]:
        """3D regions (the third one defines quad view settings, the fourth one is same as 'region_3d')"""
        ...
    show_reconstruction: bool
    """Display reconstruction data from active movie clip"""
    tracks_display_size: Annotated[float, "step=1.0", "precision=3"]
    """Display size of tracks from reconstructed data"""
    tracks_display_type: Literal['PLAIN_AXES', 'ARROWS', 'SINGLE_ARROW', 'CIRCLE', 'CUBE', 'SPHERE', 'CONE']
    """Viewport display style for tracks"""
    show_camera_path: bool
    """Show reconstructed camera path"""
    show_bundle_names: bool
    """Show names for reconstructed tracks objects"""
    use_local_collections: bool
    """Display a different set of collections in this viewport"""
    @property
    def stereo_3d_eye(self) -> Literal['LEFT_EYE', 'RIGHT_EYE']:
        """Current stereo eye being displayed"""
        ...
    stereo_3d_camera: Literal['LEFT', 'RIGHT', 'S3D']

    show_stereo_3d_cameras: bool
    """Show the left and right cameras"""
    show_stereo_3d_convergence_plane: bool
    """Show the stereo 3D convergence plane"""
    stereo_3d_convergence_plane_alpha: Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]
    """Opacity (alpha) of the convergence plane"""
    show_stereo_3d_volume: bool
    """Show the stereo 3D frustum volume"""
    stereo_3d_volume_alpha: Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]
    """Opacity (alpha) of the cameras' frustum volume"""
    mirror_xr_session: bool
    """Synchronize the viewer perspective of virtual reality sessions with this 3D viewport"""
    show_object_viewport_mesh: bool
    """Show mesh objects"""
    show_object_viewport_curve: bool
    """Show curves"""
    show_object_viewport_surf: bool
    """Show surfaces"""
    show_object_viewport_meta: bool
    """Show metaballs"""
    show_object_viewport_font: bool
    """Show text objects"""
    show_object_viewport_curves: bool
    """Show hair curves"""
    show_object_viewport_pointcloud: bool
    """Show point clouds"""
    show_object_viewport_volume: bool
    """Show volumes"""
    show_object_viewport_armature: bool
    """Show armatures"""
    show_object_viewport_lattice: bool
    """Show lattices"""
    show_object_viewport_empty: bool
    """Show empties"""
    show_object_viewport_grease_pencil: bool
    """Show Grease Pencil objects"""
    show_object_viewport_camera: bool
    """Show cameras"""
    show_object_viewport_light: bool
    """Show lights"""
    show_object_viewport_speaker: bool
    """Show speakers"""
    show_object_viewport_light_probe: bool
    """Show light probes"""
    show_object_select_mesh: bool
    """Allow selection of mesh objects"""
    show_object_select_curve: bool
    """Allow selection of curves"""
    show_object_select_surf: bool
    """Allow selection of surfaces"""
    show_object_select_meta: bool
    """Allow selection of metaballs"""
    show_object_select_font: bool
    """Allow selection of text objects"""
    show_object_select_curves: bool
    """Allow selection of hair curves"""
    show_object_select_pointcloud: bool
    """Allow selection of point clouds"""
    show_object_select_volume: bool
    """Allow selection of volumes"""
    show_object_select_armature: bool
    """Allow selection of armatures"""
    show_object_select_lattice: bool
    """Allow selection of lattices"""
    show_object_select_empty: bool
    """Allow selection of empties"""
    show_object_select_grease_pencil: bool
    """Allow selection of Grease Pencil objects"""
    show_object_select_camera: bool
    """Allow selection of cameras"""
    show_object_select_light: bool
    """Allow selection of lights"""
    show_object_select_speaker: bool
    """Allow selection of speakers"""
    show_object_select_light_probe: bool
    """Allow selection of light probes"""
    @property
    def icon_from_show_object_viewport(self) -> Annotated[int, "step=1"]:

        ...
    show_viewer: bool
    """Display non-final geometry from viewer nodes"""
    @property
    def shading(self) -> Annotated['View3DShading', "is_animatable=False"]:
        """Settings for shading in the 3D viewport"""
        ...
    @property
    def overlay(self) -> Annotated['View3DOverlay', "is_animatable=False"]:
        """Settings for display of overlays in the 3D viewport"""
        ...
    # --- Injected Methods ---
    @classmethod
    def draw_handler_add(cls, callback: Callable, args: tuple, region_type: str, draw_type: str) -> object: ...
    @classmethod
    def draw_handler_remove(cls, handler: object, region_type: str) -> None: ...