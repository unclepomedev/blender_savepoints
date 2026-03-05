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
    @property
    def show_locked_time(self) -> bool:
        """Synchronize the visible timeline range with other time-based editors"""
        ...
    @show_locked_time.setter
    def show_locked_time(self, value: bool) -> None:
        ...
    @property
    def show_region_header(self) -> bool:

        ...
    @show_region_header.setter
    def show_region_header(self, value: bool) -> None:
        ...
    @property
    def show_region_tool_header(self) -> bool:

        ...
    @show_region_tool_header.setter
    def show_region_tool_header(self, value: bool) -> None:
        ...
    @property
    def show_region_toolbar(self) -> bool:

        ...
    @show_region_toolbar.setter
    def show_region_toolbar(self, value: bool) -> None:
        ...
    @property
    def show_region_ui(self) -> bool:

        ...
    @show_region_ui.setter
    def show_region_ui(self, value: bool) -> None:
        ...
    @property
    def show_region_hud(self) -> bool:

        ...
    @show_region_hud.setter
    def show_region_hud(self, value: bool) -> None:
        ...
    @property
    def show_region_asset_shelf(self) -> bool:
        """Display a region with assets that may currently be relevant (such as brushes in paint modes, or poses in Pose Mode)"""
        ...
    @show_region_asset_shelf.setter
    def show_region_asset_shelf(self, value: bool) -> None:
        ...
    @property
    def camera(self) -> Annotated[Optional['Object'], "is_animatable=False"]:
        """Active camera used in this view (when unlocked from the scene's active camera)"""
        ...
    @camera.setter
    def camera(self, value: Annotated[Optional['Object'], "is_animatable=False"]) -> None:
        ...
    @property
    def use_render_border(self) -> Annotated[bool, "is_animatable=False"]:
        """Use a region within the frame size for rendered viewport (when not viewing through the camera)"""
        ...
    @use_render_border.setter
    def use_render_border(self, value: Annotated[bool, "is_animatable=False"]) -> None:
        ...
    @property
    def render_border_min_x(self) -> Annotated[float, "step=10.0", "precision=3"]:
        """Minimum X value for the render region"""
        ...
    @render_border_min_x.setter
    def render_border_min_x(self, value: Annotated[float, "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def render_border_min_y(self) -> Annotated[float, "step=10.0", "precision=3"]:
        """Minimum Y value for the render region"""
        ...
    @render_border_min_y.setter
    def render_border_min_y(self, value: Annotated[float, "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def render_border_max_x(self) -> Annotated[float, "step=10.0", "precision=3"]:
        """Maximum X value for the render region"""
        ...
    @render_border_max_x.setter
    def render_border_max_x(self, value: Annotated[float, "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def render_border_max_y(self) -> Annotated[float, "step=10.0", "precision=3"]:
        """Maximum Y value for the render region"""
        ...
    @render_border_max_y.setter
    def render_border_max_y(self, value: Annotated[float, "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def lock_object(self) -> Annotated[Optional['Object'], "is_animatable=False"]:
        """3D View center is locked to this object's position"""
        ...
    @lock_object.setter
    def lock_object(self, value: Annotated[Optional['Object'], "is_animatable=False"]) -> None:
        ...
    @property
    def lock_bone(self) -> Annotated[str, "is_animatable=False"]:
        """3D View center is locked to this bone's position"""
        ...
    @lock_bone.setter
    def lock_bone(self, value: Annotated[str, "is_animatable=False"]) -> None:
        ...
    @property
    def lock_cursor(self) -> bool:
        """3D View center is locked to the cursor's position"""
        ...
    @lock_cursor.setter
    def lock_cursor(self, value: bool) -> None:
        ...
    @property
    def local_view(self) -> Annotated[Optional['SpaceView3D'], "is_animatable=False"]:
        """Display an isolated subset of objects, apart from the scene visibility"""
        ...
    @property
    def lens(self) -> Annotated[float, "subtype=''", "unit='CAMERA'", "step=10.0", "precision=3"]:
        """Viewport lens angle"""
        ...
    @lens.setter
    def lens(self, value: Annotated[float, "subtype=''", "unit='CAMERA'", "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def clip_start(self) -> Annotated[float, "subtype='DISTANCE'", "unit='LENGTH'", "step=10.0", "precision=3"]:
        """3D View near clipping distance (perspective view only)"""
        ...
    @clip_start.setter
    def clip_start(self, value: Annotated[float, "subtype='DISTANCE'", "unit='LENGTH'", "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def clip_end(self) -> Annotated[float, "subtype='DISTANCE'", "unit='LENGTH'", "step=10.0", "precision=3"]:
        """3D View far clipping distance"""
        ...
    @clip_end.setter
    def clip_end(self, value: Annotated[float, "subtype='DISTANCE'", "unit='LENGTH'", "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def lock_camera(self) -> bool:
        """Enable view navigation within the camera view"""
        ...
    @lock_camera.setter
    def lock_camera(self, value: bool) -> None:
        ...
    @property
    def show_gizmo(self) -> bool:
        """Show gizmos of all types"""
        ...
    @show_gizmo.setter
    def show_gizmo(self, value: bool) -> None:
        ...
    @property
    def show_gizmo_navigate(self) -> bool:
        """Viewport navigation gizmo"""
        ...
    @show_gizmo_navigate.setter
    def show_gizmo_navigate(self, value: bool) -> None:
        ...
    @property
    def show_gizmo_context(self) -> bool:
        """Context sensitive gizmos for the active item"""
        ...
    @show_gizmo_context.setter
    def show_gizmo_context(self, value: bool) -> None:
        ...
    @property
    def show_gizmo_modifier(self) -> bool:
        """Gizmos for the active modifier"""
        ...
    @show_gizmo_modifier.setter
    def show_gizmo_modifier(self, value: bool) -> None:
        ...
    @property
    def show_gizmo_tool(self) -> bool:
        """Active tool gizmo"""
        ...
    @show_gizmo_tool.setter
    def show_gizmo_tool(self, value: bool) -> None:
        ...
    @property
    def show_gizmo_object_translate(self) -> bool:
        """Gizmo to adjust location"""
        ...
    @show_gizmo_object_translate.setter
    def show_gizmo_object_translate(self, value: bool) -> None:
        ...
    @property
    def show_gizmo_object_rotate(self) -> bool:
        """Gizmo to adjust rotation"""
        ...
    @show_gizmo_object_rotate.setter
    def show_gizmo_object_rotate(self, value: bool) -> None:
        ...
    @property
    def show_gizmo_object_scale(self) -> bool:
        """Gizmo to adjust scale"""
        ...
    @show_gizmo_object_scale.setter
    def show_gizmo_object_scale(self, value: bool) -> None:
        ...
    @property
    def show_gizmo_empty_image(self) -> bool:
        """Gizmo to adjust image size and position"""
        ...
    @show_gizmo_empty_image.setter
    def show_gizmo_empty_image(self, value: bool) -> None:
        ...
    @property
    def show_gizmo_empty_force_field(self) -> bool:
        """Gizmo to adjust the force field"""
        ...
    @show_gizmo_empty_force_field.setter
    def show_gizmo_empty_force_field(self, value: bool) -> None:
        ...
    @property
    def show_gizmo_light_size(self) -> bool:
        """Gizmo to adjust spot and area size"""
        ...
    @show_gizmo_light_size.setter
    def show_gizmo_light_size(self, value: bool) -> None:
        ...
    @property
    def show_gizmo_light_look_at(self) -> bool:
        """Gizmo to adjust the direction of the light"""
        ...
    @show_gizmo_light_look_at.setter
    def show_gizmo_light_look_at(self, value: bool) -> None:
        ...
    @property
    def show_gizmo_camera_lens(self) -> bool:
        """Gizmo to adjust camera focal length or orthographic scale"""
        ...
    @show_gizmo_camera_lens.setter
    def show_gizmo_camera_lens(self, value: bool) -> None:
        ...
    @property
    def show_gizmo_camera_dof_distance(self) -> bool:
        """Gizmo to adjust camera focus distance (depends on limits display)"""
        ...
    @show_gizmo_camera_dof_distance.setter
    def show_gizmo_camera_dof_distance(self, value: bool) -> None:
        ...
    @property
    def use_local_camera(self) -> bool:
        """Use a local camera in this view, rather than scene's active camera"""
        ...
    @use_local_camera.setter
    def use_local_camera(self, value: bool) -> None:
        ...
    @property
    def region_3d(self) -> Annotated[Optional['RegionView3D'], "is_animatable=False"]:
        """3D region for this space. When the space is in quad view, the camera region"""
        ...
    @property
    def region_quadviews(self) -> Annotated[bpy_prop_collection['RegionView3D'], "is_animatable=False"]:
        """3D regions (the third one defines quad view settings, the fourth one is same as 'region_3d')"""
        ...
    @property
    def show_reconstruction(self) -> bool:
        """Display reconstruction data from active movie clip"""
        ...
    @show_reconstruction.setter
    def show_reconstruction(self, value: bool) -> None:
        ...
    @property
    def tracks_display_size(self) -> Annotated[float, "step=1.0", "precision=3"]:
        """Display size of tracks from reconstructed data"""
        ...
    @tracks_display_size.setter
    def tracks_display_size(self, value: Annotated[float, "step=1.0", "precision=3"]) -> None:
        ...
    @property
    def tracks_display_type(self) -> Literal['PLAIN_AXES', 'ARROWS', 'SINGLE_ARROW', 'CIRCLE', 'CUBE', 'SPHERE', 'CONE']:
        """Viewport display style for tracks"""
        ...
    @tracks_display_type.setter
    def tracks_display_type(self, value: Literal['PLAIN_AXES', 'ARROWS', 'SINGLE_ARROW', 'CIRCLE', 'CUBE', 'SPHERE', 'CONE']) -> None:
        ...
    @property
    def show_camera_path(self) -> bool:
        """Show reconstructed camera path"""
        ...
    @show_camera_path.setter
    def show_camera_path(self, value: bool) -> None:
        ...
    @property
    def show_bundle_names(self) -> bool:
        """Show names for reconstructed tracks objects"""
        ...
    @show_bundle_names.setter
    def show_bundle_names(self, value: bool) -> None:
        ...
    @property
    def use_local_collections(self) -> bool:
        """Display a different set of collections in this viewport"""
        ...
    @use_local_collections.setter
    def use_local_collections(self, value: bool) -> None:
        ...
    @property
    def stereo_3d_eye(self) -> Literal['LEFT_EYE', 'RIGHT_EYE']:
        """Current stereo eye being displayed"""
        ...
    @property
    def stereo_3d_camera(self) -> Literal['LEFT', 'RIGHT', 'S3D']:

        ...
    @stereo_3d_camera.setter
    def stereo_3d_camera(self, value: Literal['LEFT', 'RIGHT', 'S3D']) -> None:
        ...
    @property
    def show_stereo_3d_cameras(self) -> bool:
        """Show the left and right cameras"""
        ...
    @show_stereo_3d_cameras.setter
    def show_stereo_3d_cameras(self, value: bool) -> None:
        ...
    @property
    def show_stereo_3d_convergence_plane(self) -> bool:
        """Show the stereo 3D convergence plane"""
        ...
    @show_stereo_3d_convergence_plane.setter
    def show_stereo_3d_convergence_plane(self, value: bool) -> None:
        ...
    @property
    def stereo_3d_convergence_plane_alpha(self) -> Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]:
        """Opacity (alpha) of the convergence plane"""
        ...
    @stereo_3d_convergence_plane_alpha.setter
    def stereo_3d_convergence_plane_alpha(self, value: Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def show_stereo_3d_volume(self) -> bool:
        """Show the stereo 3D frustum volume"""
        ...
    @show_stereo_3d_volume.setter
    def show_stereo_3d_volume(self, value: bool) -> None:
        ...
    @property
    def stereo_3d_volume_alpha(self) -> Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]:
        """Opacity (alpha) of the cameras' frustum volume"""
        ...
    @stereo_3d_volume_alpha.setter
    def stereo_3d_volume_alpha(self, value: Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def mirror_xr_session(self) -> bool:
        """Synchronize the viewer perspective of virtual reality sessions with this 3D viewport"""
        ...
    @mirror_xr_session.setter
    def mirror_xr_session(self, value: bool) -> None:
        ...
    @property
    def show_object_viewport_mesh(self) -> bool:
        """Show mesh objects"""
        ...
    @show_object_viewport_mesh.setter
    def show_object_viewport_mesh(self, value: bool) -> None:
        ...
    @property
    def show_object_viewport_curve(self) -> bool:
        """Show curves"""
        ...
    @show_object_viewport_curve.setter
    def show_object_viewport_curve(self, value: bool) -> None:
        ...
    @property
    def show_object_viewport_surf(self) -> bool:
        """Show surfaces"""
        ...
    @show_object_viewport_surf.setter
    def show_object_viewport_surf(self, value: bool) -> None:
        ...
    @property
    def show_object_viewport_meta(self) -> bool:
        """Show metaballs"""
        ...
    @show_object_viewport_meta.setter
    def show_object_viewport_meta(self, value: bool) -> None:
        ...
    @property
    def show_object_viewport_font(self) -> bool:
        """Show text objects"""
        ...
    @show_object_viewport_font.setter
    def show_object_viewport_font(self, value: bool) -> None:
        ...
    @property
    def show_object_viewport_curves(self) -> bool:
        """Show hair curves"""
        ...
    @show_object_viewport_curves.setter
    def show_object_viewport_curves(self, value: bool) -> None:
        ...
    @property
    def show_object_viewport_pointcloud(self) -> bool:
        """Show point clouds"""
        ...
    @show_object_viewport_pointcloud.setter
    def show_object_viewport_pointcloud(self, value: bool) -> None:
        ...
    @property
    def show_object_viewport_volume(self) -> bool:
        """Show volumes"""
        ...
    @show_object_viewport_volume.setter
    def show_object_viewport_volume(self, value: bool) -> None:
        ...
    @property
    def show_object_viewport_armature(self) -> bool:
        """Show armatures"""
        ...
    @show_object_viewport_armature.setter
    def show_object_viewport_armature(self, value: bool) -> None:
        ...
    @property
    def show_object_viewport_lattice(self) -> bool:
        """Show lattices"""
        ...
    @show_object_viewport_lattice.setter
    def show_object_viewport_lattice(self, value: bool) -> None:
        ...
    @property
    def show_object_viewport_empty(self) -> bool:
        """Show empties"""
        ...
    @show_object_viewport_empty.setter
    def show_object_viewport_empty(self, value: bool) -> None:
        ...
    @property
    def show_object_viewport_grease_pencil(self) -> bool:
        """Show Grease Pencil objects"""
        ...
    @show_object_viewport_grease_pencil.setter
    def show_object_viewport_grease_pencil(self, value: bool) -> None:
        ...
    @property
    def show_object_viewport_camera(self) -> bool:
        """Show cameras"""
        ...
    @show_object_viewport_camera.setter
    def show_object_viewport_camera(self, value: bool) -> None:
        ...
    @property
    def show_object_viewport_light(self) -> bool:
        """Show lights"""
        ...
    @show_object_viewport_light.setter
    def show_object_viewport_light(self, value: bool) -> None:
        ...
    @property
    def show_object_viewport_speaker(self) -> bool:
        """Show speakers"""
        ...
    @show_object_viewport_speaker.setter
    def show_object_viewport_speaker(self, value: bool) -> None:
        ...
    @property
    def show_object_viewport_light_probe(self) -> bool:
        """Show light probes"""
        ...
    @show_object_viewport_light_probe.setter
    def show_object_viewport_light_probe(self, value: bool) -> None:
        ...
    @property
    def show_object_select_mesh(self) -> bool:
        """Allow selection of mesh objects"""
        ...
    @show_object_select_mesh.setter
    def show_object_select_mesh(self, value: bool) -> None:
        ...
    @property
    def show_object_select_curve(self) -> bool:
        """Allow selection of curves"""
        ...
    @show_object_select_curve.setter
    def show_object_select_curve(self, value: bool) -> None:
        ...
    @property
    def show_object_select_surf(self) -> bool:
        """Allow selection of surfaces"""
        ...
    @show_object_select_surf.setter
    def show_object_select_surf(self, value: bool) -> None:
        ...
    @property
    def show_object_select_meta(self) -> bool:
        """Allow selection of metaballs"""
        ...
    @show_object_select_meta.setter
    def show_object_select_meta(self, value: bool) -> None:
        ...
    @property
    def show_object_select_font(self) -> bool:
        """Allow selection of text objects"""
        ...
    @show_object_select_font.setter
    def show_object_select_font(self, value: bool) -> None:
        ...
    @property
    def show_object_select_curves(self) -> bool:
        """Allow selection of hair curves"""
        ...
    @show_object_select_curves.setter
    def show_object_select_curves(self, value: bool) -> None:
        ...
    @property
    def show_object_select_pointcloud(self) -> bool:
        """Allow selection of point clouds"""
        ...
    @show_object_select_pointcloud.setter
    def show_object_select_pointcloud(self, value: bool) -> None:
        ...
    @property
    def show_object_select_volume(self) -> bool:
        """Allow selection of volumes"""
        ...
    @show_object_select_volume.setter
    def show_object_select_volume(self, value: bool) -> None:
        ...
    @property
    def show_object_select_armature(self) -> bool:
        """Allow selection of armatures"""
        ...
    @show_object_select_armature.setter
    def show_object_select_armature(self, value: bool) -> None:
        ...
    @property
    def show_object_select_lattice(self) -> bool:
        """Allow selection of lattices"""
        ...
    @show_object_select_lattice.setter
    def show_object_select_lattice(self, value: bool) -> None:
        ...
    @property
    def show_object_select_empty(self) -> bool:
        """Allow selection of empties"""
        ...
    @show_object_select_empty.setter
    def show_object_select_empty(self, value: bool) -> None:
        ...
    @property
    def show_object_select_grease_pencil(self) -> bool:
        """Allow selection of Grease Pencil objects"""
        ...
    @show_object_select_grease_pencil.setter
    def show_object_select_grease_pencil(self, value: bool) -> None:
        ...
    @property
    def show_object_select_camera(self) -> bool:
        """Allow selection of cameras"""
        ...
    @show_object_select_camera.setter
    def show_object_select_camera(self, value: bool) -> None:
        ...
    @property
    def show_object_select_light(self) -> bool:
        """Allow selection of lights"""
        ...
    @show_object_select_light.setter
    def show_object_select_light(self, value: bool) -> None:
        ...
    @property
    def show_object_select_speaker(self) -> bool:
        """Allow selection of speakers"""
        ...
    @show_object_select_speaker.setter
    def show_object_select_speaker(self, value: bool) -> None:
        ...
    @property
    def show_object_select_light_probe(self) -> bool:
        """Allow selection of light probes"""
        ...
    @show_object_select_light_probe.setter
    def show_object_select_light_probe(self, value: bool) -> None:
        ...
    @property
    def icon_from_show_object_viewport(self) -> Annotated[int, "step=1"]:

        ...
    @property
    def show_viewer(self) -> bool:
        """Display non-final geometry from viewer nodes"""
        ...
    @show_viewer.setter
    def show_viewer(self, value: bool) -> None:
        ...
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