# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.RenderSettings.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .bpy_struct import bpy_struct
from .BakeSettings import BakeSettings
from .CurveMapping import CurveMapping
from .FFmpegSettings import FFmpegSettings
from .ImageFormatSettings import ImageFormatSettings
from .RenderViews import RenderViews
from .SceneRenderView import SceneRenderView
from .bpy_prop_collection import bpy_prop_collection

class RenderSettings(bpy_struct):

    @property
    def image_settings(self) -> Annotated['ImageFormatSettings', "is_animatable=False"]:

        ...
    @property
    def resolution_x(self) -> Annotated[int, "subtype='PIXEL'", "step=1", "is_animatable=False"]:
        """Number of horizontal pixels in the rendered image"""
        ...
    @resolution_x.setter
    def resolution_x(self, value: Annotated[int, "subtype='PIXEL'", "step=1", "is_animatable=False"]) -> None:
        ...
    @property
    def resolution_y(self) -> Annotated[int, "subtype='PIXEL'", "step=1", "is_animatable=False"]:
        """Number of vertical pixels in the rendered image"""
        ...
    @resolution_y.setter
    def resolution_y(self, value: Annotated[int, "subtype='PIXEL'", "step=1", "is_animatable=False"]) -> None:
        ...
    @property
    def resolution_percentage(self) -> Annotated[int, "subtype='PERCENTAGE'", "step=10", "is_animatable=False"]:
        """Percentage scale for render resolution"""
        ...
    @resolution_percentage.setter
    def resolution_percentage(self, value: Annotated[int, "subtype='PERCENTAGE'", "step=10", "is_animatable=False"]) -> None:
        ...
    @property
    def preview_pixel_size(self) -> Literal['AUTO', '1', '2', '4', '8']:
        """Pixel size for viewport rendering"""
        ...
    @preview_pixel_size.setter
    def preview_pixel_size(self, value: Literal['AUTO', '1', '2', '4', '8']) -> None:
        ...
    @property
    def pixel_aspect_x(self) -> Annotated[float, "step=10.0", "precision=3", "is_animatable=False"]:
        """Horizontal aspect ratio - for anamorphic or non-square pixel output"""
        ...
    @pixel_aspect_x.setter
    def pixel_aspect_x(self, value: Annotated[float, "step=10.0", "precision=3", "is_animatable=False"]) -> None:
        ...
    @property
    def pixel_aspect_y(self) -> Annotated[float, "step=10.0", "precision=3", "is_animatable=False"]:
        """Vertical aspect ratio - for anamorphic or non-square pixel output"""
        ...
    @pixel_aspect_y.setter
    def pixel_aspect_y(self, value: Annotated[float, "step=10.0", "precision=3", "is_animatable=False"]) -> None:
        ...
    @property
    def ppm_factor(self) -> Annotated[float, "step=2.0", "precision=2", "is_animatable=False"]:
        """The pixel density meta-data written to supported image formats. This value is multiplied by the PPM-base which defines the unit (typically inches or meters)"""
        ...
    @ppm_factor.setter
    def ppm_factor(self, value: Annotated[float, "step=2.0", "precision=2", "is_animatable=False"]) -> None:
        ...
    @property
    def ppm_base(self) -> Annotated[float, "step=2.0", "precision=4", "is_animatable=False"]:
        """The base unit for pixels per meter."""
        ...
    @ppm_base.setter
    def ppm_base(self, value: Annotated[float, "step=2.0", "precision=4", "is_animatable=False"]) -> None:
        ...
    @property
    def ffmpeg(self) -> Annotated[Optional['FFmpegSettings'], "is_animatable=False"]:
        """FFmpeg related settings for the scene"""
        ...
    @property
    def fps(self) -> Annotated[int, "step=1", "is_animatable=False"]:
        """Framerate, expressed in frames per second"""
        ...
    @fps.setter
    def fps(self, value: Annotated[int, "step=1", "is_animatable=False"]) -> None:
        ...
    @property
    def fps_base(self) -> Annotated[float, "step=2.0", "precision=3", "is_animatable=False"]:
        """Framerate base"""
        ...
    @fps_base.setter
    def fps_base(self, value: Annotated[float, "step=2.0", "precision=3", "is_animatable=False"]) -> None:
        ...
    @property
    def frame_map_old(self) -> Annotated[int, "step=1", "is_animatable=False"]:
        """Old mapping value in frames"""
        ...
    @frame_map_old.setter
    def frame_map_old(self, value: Annotated[int, "step=1", "is_animatable=False"]) -> None:
        ...
    @property
    def frame_map_new(self) -> Annotated[int, "step=1", "is_animatable=False"]:
        """How many frames the Map Old will last"""
        ...
    @frame_map_new.setter
    def frame_map_new(self, value: Annotated[int, "step=1", "is_animatable=False"]) -> None:
        ...
    @property
    def dither_intensity(self) -> Annotated[float, "step=0.10000000149011612", "precision=2"]:
        """Amount of dithering noise added to the rendered image to break up banding"""
        ...
    @dither_intensity.setter
    def dither_intensity(self, value: Annotated[float, "step=0.10000000149011612", "precision=2"]) -> None:
        ...
    @property
    def filter_size(self) -> Annotated[float, "subtype='PIXEL'", "step=1.0", "precision=2"]:
        """Width over which the reconstruction filter combines samples"""
        ...
    @filter_size.setter
    def filter_size(self, value: Annotated[float, "subtype='PIXEL'", "step=1.0", "precision=2"]) -> None:
        ...
    @property
    def film_transparent(self) -> bool:
        """World background is transparent, for compositing the render over another background"""
        ...
    @film_transparent.setter
    def film_transparent(self, value: bool) -> None:
        ...
    @property
    def use_freestyle(self) -> Annotated[bool, "is_animatable=False"]:
        """Draw stylized strokes using Freestyle"""
        ...
    @use_freestyle.setter
    def use_freestyle(self, value: Annotated[bool, "is_animatable=False"]) -> None:
        ...
    @property
    def threads(self) -> Annotated[int, "step=1"]:
        """Maximum number of CPU cores to use simultaneously while rendering (for multi-core/CPU systems)"""
        ...
    @threads.setter
    def threads(self, value: Annotated[int, "step=1"]) -> None:
        ...
    @property
    def threads_mode(self) -> Literal['AUTO', 'FIXED']:
        """Determine the amount of render threads used"""
        ...
    @threads_mode.setter
    def threads_mode(self, value: Literal['AUTO', 'FIXED']) -> None:
        ...
    @property
    def use_motion_blur(self) -> Annotated[bool, "is_animatable=False"]:
        """Use multi-sampled 3D scene motion blur"""
        ...
    @use_motion_blur.setter
    def use_motion_blur(self, value: Annotated[bool, "is_animatable=False"]) -> None:
        ...
    @property
    def motion_blur_shutter(self) -> Annotated[float, "subtype='FACTOR'", "step=1.0", "precision=2"]:
        """Time taken in frames between shutter open and close"""
        ...
    @motion_blur_shutter.setter
    def motion_blur_shutter(self, value: Annotated[float, "subtype='FACTOR'", "step=1.0", "precision=2"]) -> None:
        ...
    @property
    def motion_blur_position(self) -> Literal['START', 'CENTER', 'END']:
        """Offset for the shutter's time interval, allows to change the motion blur trails"""
        ...
    @motion_blur_position.setter
    def motion_blur_position(self, value: Literal['START', 'CENTER', 'END']) -> None:
        ...
    @property
    def motion_blur_shutter_curve(self) -> Annotated[Optional['CurveMapping'], "is_animatable=False"]:
        """Curve defining the shutter's openness over time"""
        ...
    @property
    def hair_type(self) -> Literal['STRAND', 'STRIP', 'CYLINDER']:
        """Curves shape type"""
        ...
    @hair_type.setter
    def hair_type(self, value: Literal['STRAND', 'STRIP', 'CYLINDER']) -> None:
        ...
    @property
    def hair_subdiv(self) -> Annotated[int, "step=1"]:
        """Additional subdivision along the curves"""
        ...
    @hair_subdiv.setter
    def hair_subdiv(self, value: Annotated[int, "step=1"]) -> None:
        ...
    @property
    def use_high_quality_normals(self) -> bool:
        """Use high quality tangent space at the cost of lower performance"""
        ...
    @use_high_quality_normals.setter
    def use_high_quality_normals(self, value: bool) -> None:
        ...
    @property
    def use_border(self) -> Annotated[bool, "is_animatable=False"]:
        """Render a user-defined render region, within the frame size"""
        ...
    @use_border.setter
    def use_border(self, value: Annotated[bool, "is_animatable=False"]) -> None:
        ...
    @property
    def border_min_x(self) -> Annotated[float, "step=10.0", "precision=3", "is_animatable=False"]:
        """Minimum X value for the render region"""
        ...
    @border_min_x.setter
    def border_min_x(self, value: Annotated[float, "step=10.0", "precision=3", "is_animatable=False"]) -> None:
        ...
    @property
    def border_min_y(self) -> Annotated[float, "step=10.0", "precision=3", "is_animatable=False"]:
        """Minimum Y value for the render region"""
        ...
    @border_min_y.setter
    def border_min_y(self, value: Annotated[float, "step=10.0", "precision=3", "is_animatable=False"]) -> None:
        ...
    @property
    def border_max_x(self) -> Annotated[float, "step=10.0", "precision=3", "is_animatable=False"]:
        """Maximum X value for the render region"""
        ...
    @border_max_x.setter
    def border_max_x(self, value: Annotated[float, "step=10.0", "precision=3", "is_animatable=False"]) -> None:
        ...
    @property
    def border_max_y(self) -> Annotated[float, "step=10.0", "precision=3", "is_animatable=False"]:
        """Maximum Y value for the render region"""
        ...
    @border_max_y.setter
    def border_max_y(self, value: Annotated[float, "step=10.0", "precision=3", "is_animatable=False"]) -> None:
        ...
    @property
    def use_crop_to_border(self) -> Annotated[bool, "is_animatable=False"]:
        """Crop the rendered frame to the defined render region size"""
        ...
    @use_crop_to_border.setter
    def use_crop_to_border(self, value: Annotated[bool, "is_animatable=False"]) -> None:
        ...
    @property
    def use_placeholder(self) -> Annotated[bool, "is_animatable=False"]:
        """Create empty placeholder files while rendering frames (similar to Unix 'touch')"""
        ...
    @use_placeholder.setter
    def use_placeholder(self, value: Annotated[bool, "is_animatable=False"]) -> None:
        ...
    @property
    def use_overwrite(self) -> bool:
        """Overwrite existing files while rendering"""
        ...
    @use_overwrite.setter
    def use_overwrite(self, value: bool) -> None:
        ...
    @property
    def use_compositing(self) -> Annotated[bool, "is_animatable=False"]:
        """Process the render result through the compositing pipeline, if a compositing node group is assigned to the scene"""
        ...
    @use_compositing.setter
    def use_compositing(self, value: Annotated[bool, "is_animatable=False"]) -> None:
        ...
    @property
    def use_sequencer(self) -> Annotated[bool, "is_animatable=False"]:
        """Process the render (and composited) result through the video sequence editor pipeline, if sequencer strips exist"""
        ...
    @use_sequencer.setter
    def use_sequencer(self, value: Annotated[bool, "is_animatable=False"]) -> None:
        ...
    @property
    def use_file_extension(self) -> Annotated[bool, "is_animatable=False"]:
        """Add the file format extensions to the rendered file name (eg: filename + .jpg)"""
        ...
    @use_file_extension.setter
    def use_file_extension(self, value: Annotated[bool, "is_animatable=False"]) -> None:
        ...
    @property
    def file_extension(self) -> Annotated[str, "is_animatable=False"]:
        """The file extension used for saving renders"""
        ...
    @property
    def is_movie_format(self) -> bool:
        """When true the format is a movie"""
        ...
    @property
    def use_lock_interface(self) -> Annotated[bool, "is_animatable=False"]:
        """Lock interface during rendering in favor of giving more memory to the renderer"""
        ...
    @use_lock_interface.setter
    def use_lock_interface(self, value: Annotated[bool, "is_animatable=False"]) -> None:
        ...
    @property
    def filepath(self) -> Annotated[str, "subtype='FILE_PATH'", "is_animatable=False"]:
        """Directory/name to save animations, # characters define the position and padding of frame numbers"""
        ...
    @filepath.setter
    def filepath(self, value: Annotated[str, "subtype='FILE_PATH'", "is_animatable=False"]) -> None:
        ...
    @property
    def use_render_cache(self) -> Annotated[bool, "is_animatable=False"]:
        """Save render cache to EXR files (useful for heavy compositing, Note: affects indirectly rendered scenes)"""
        ...
    @use_render_cache.setter
    def use_render_cache(self, value: Annotated[bool, "is_animatable=False"]) -> None:
        ...
    @property
    def use_stamp_time(self) -> bool:
        """Include the rendered frame timecode as HH:MM:SS.FF in image metadata"""
        ...
    @use_stamp_time.setter
    def use_stamp_time(self, value: bool) -> None:
        ...
    @property
    def use_stamp_date(self) -> bool:
        """Include the current date in image/video metadata"""
        ...
    @use_stamp_date.setter
    def use_stamp_date(self, value: bool) -> None:
        ...
    @property
    def use_stamp_frame(self) -> bool:
        """Include the frame number in image metadata"""
        ...
    @use_stamp_frame.setter
    def use_stamp_frame(self, value: bool) -> None:
        ...
    @property
    def use_stamp_frame_range(self) -> bool:
        """Include the rendered frame range in image/video metadata"""
        ...
    @use_stamp_frame_range.setter
    def use_stamp_frame_range(self, value: bool) -> None:
        ...
    @property
    def use_stamp_camera(self) -> bool:
        """Include the name of the active camera in image metadata"""
        ...
    @use_stamp_camera.setter
    def use_stamp_camera(self, value: bool) -> None:
        ...
    @property
    def use_stamp_lens(self) -> bool:
        """Include the active camera's lens in image metadata"""
        ...
    @use_stamp_lens.setter
    def use_stamp_lens(self, value: bool) -> None:
        ...
    @property
    def use_stamp_scene(self) -> bool:
        """Include the name of the active scene in image/video metadata"""
        ...
    @use_stamp_scene.setter
    def use_stamp_scene(self, value: bool) -> None:
        ...
    @property
    def use_stamp_note(self) -> bool:
        """Include a custom note in image/video metadata"""
        ...
    @use_stamp_note.setter
    def use_stamp_note(self, value: bool) -> None:
        ...
    @property
    def use_stamp_marker(self) -> bool:
        """Include the name of the last marker in image metadata"""
        ...
    @use_stamp_marker.setter
    def use_stamp_marker(self, value: bool) -> None:
        ...
    @property
    def use_stamp_filename(self) -> bool:
        """Include the .blend filename in image/video metadata"""
        ...
    @use_stamp_filename.setter
    def use_stamp_filename(self, value: bool) -> None:
        ...
    @property
    def use_stamp_sequencer_strip(self) -> bool:
        """Include the name of the foreground sequence strip in image metadata"""
        ...
    @use_stamp_sequencer_strip.setter
    def use_stamp_sequencer_strip(self, value: bool) -> None:
        ...
    @property
    def use_stamp_render_time(self) -> bool:
        """Include the render time in image metadata"""
        ...
    @use_stamp_render_time.setter
    def use_stamp_render_time(self, value: bool) -> None:
        ...
    @property
    def stamp_note_text(self) -> Annotated[str, "is_animatable=False"]:
        """Custom text to appear in the stamp note"""
        ...
    @stamp_note_text.setter
    def stamp_note_text(self, value: Annotated[str, "is_animatable=False"]) -> None:
        ...
    @property
    def use_stamp(self) -> bool:
        """Render the stamp info text in the rendered image"""
        ...
    @use_stamp.setter
    def use_stamp(self, value: bool) -> None:
        ...
    @property
    def use_stamp_labels(self) -> bool:
        """Display stamp labels ("Camera" in front of camera name, etc.)"""
        ...
    @use_stamp_labels.setter
    def use_stamp_labels(self, value: bool) -> None:
        ...
    @property
    def metadata_input(self) -> Literal['SCENE', 'STRIPS']:
        """Where to take the metadata from"""
        ...
    @metadata_input.setter
    def metadata_input(self, value: Literal['SCENE', 'STRIPS']) -> None:
        ...
    @property
    def use_stamp_memory(self) -> bool:
        """Include the peak memory usage in image metadata"""
        ...
    @use_stamp_memory.setter
    def use_stamp_memory(self, value: bool) -> None:
        ...
    @property
    def use_stamp_hostname(self) -> bool:
        """Include the hostname of the machine that rendered the frame"""
        ...
    @use_stamp_hostname.setter
    def use_stamp_hostname(self, value: bool) -> None:
        ...
    @property
    def stamp_font_size(self) -> Annotated[int, "subtype='PIXEL'", "step=1"]:
        """Size of the font used when rendering stamp text"""
        ...
    @stamp_font_size.setter
    def stamp_font_size(self, value: Annotated[int, "subtype='PIXEL'", "step=1"]) -> None:
        ...
    @property
    def stamp_foreground(self) -> Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]:
        """Color to use for stamp text"""
        ...
    @stamp_foreground.setter
    def stamp_foreground(self, value: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def stamp_background(self) -> Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]:
        """Color to use behind stamp text"""
        ...
    @stamp_background.setter
    def stamp_background(self, value: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def sequencer_gl_preview(self) -> Literal['WIREFRAME', 'SOLID', 'MATERIAL', 'RENDERED']:
        """Display method used in the sequencer view"""
        ...
    @sequencer_gl_preview.setter
    def sequencer_gl_preview(self, value: Literal['WIREFRAME', 'SOLID', 'MATERIAL', 'RENDERED']) -> None:
        ...
    @property
    def use_sequencer_override_scene_strip(self) -> bool:
        """Use workbench render settings from the sequencer scene, instead of each individual scene used in the strip"""
        ...
    @use_sequencer_override_scene_strip.setter
    def use_sequencer_override_scene_strip(self, value: bool) -> None:
        ...
    @property
    def use_single_layer(self) -> Annotated[bool, "is_animatable=False"]:
        """Only render the active layer. Only affects rendering from the interface, ignored for rendering from command line."""
        ...
    @use_single_layer.setter
    def use_single_layer(self, value: Annotated[bool, "is_animatable=False"]) -> None:
        ...
    @property
    def views(self) -> Annotated['RenderViews', "is_animatable=False"]:

        ...
    @property
    def stereo_views(self) -> Annotated[bpy_prop_collection['SceneRenderView'], "is_animatable=False"]:

        ...
    @property
    def use_multiview(self) -> bool:
        """Use multiple views in the scene"""
        ...
    @use_multiview.setter
    def use_multiview(self, value: bool) -> None:
        ...
    @property
    def views_format(self) -> Annotated[Literal['STEREO_3D', 'MULTIVIEW'], "is_animatable=False"]:

        ...
    @views_format.setter
    def views_format(self, value: Annotated[Literal['STEREO_3D', 'MULTIVIEW'], "is_animatable=False"]) -> None:
        ...
    @property
    def engine(self) -> Annotated[Literal['BLENDER_EEVEE'], "is_animatable=False"]:
        """Engine to use for rendering"""
        ...
    @engine.setter
    def engine(self, value: Annotated[Literal['BLENDER_EEVEE'], "is_animatable=False"]) -> None:
        ...
    @property
    def has_multiple_engines(self) -> bool:
        """More than one rendering engine is available"""
        ...
    @property
    def use_spherical_stereo(self) -> bool:
        """Active render engine supports spherical stereo rendering"""
        ...
    @property
    def use_simplify(self) -> bool:
        """Enable simplification of scene for quicker preview renders"""
        ...
    @use_simplify.setter
    def use_simplify(self, value: bool) -> None:
        ...
    @property
    def simplify_subdivision(self) -> Annotated[int, "subtype='UNSIGNED'", "step=1"]:
        """Global maximum subdivision level"""
        ...
    @simplify_subdivision.setter
    def simplify_subdivision(self, value: Annotated[int, "subtype='UNSIGNED'", "step=1"]) -> None:
        ...
    @property
    def simplify_child_particles(self) -> Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]:
        """Global child particles percentage"""
        ...
    @simplify_child_particles.setter
    def simplify_child_particles(self, value: Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def simplify_subdivision_render(self) -> Annotated[int, "subtype='UNSIGNED'", "step=1"]:
        """Global maximum subdivision level during rendering"""
        ...
    @simplify_subdivision_render.setter
    def simplify_subdivision_render(self, value: Annotated[int, "subtype='UNSIGNED'", "step=1"]) -> None:
        ...
    @property
    def simplify_child_particles_render(self) -> Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]:
        """Global child particles percentage during rendering"""
        ...
    @simplify_child_particles_render.setter
    def simplify_child_particles_render(self, value: Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def simplify_volumes(self) -> Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]:
        """Resolution percentage of volume objects in viewport"""
        ...
    @simplify_volumes.setter
    def simplify_volumes(self, value: Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def use_simplify_normals(self) -> bool:
        """Skip computing custom normals and face corner normals for displaying meshes in the viewport"""
        ...
    @use_simplify_normals.setter
    def use_simplify_normals(self, value: bool) -> None:
        ...
    @property
    def simplify_gpencil(self) -> bool:
        """Simplify Grease Pencil drawing"""
        ...
    @simplify_gpencil.setter
    def simplify_gpencil(self, value: bool) -> None:
        ...
    @property
    def simplify_gpencil_onplay(self) -> bool:
        """Simplify Grease Pencil only during animation playback"""
        ...
    @simplify_gpencil_onplay.setter
    def simplify_gpencil_onplay(self, value: bool) -> None:
        ...
    @property
    def simplify_gpencil_antialiasing(self) -> bool:
        """Use Antialiasing to smooth stroke edges"""
        ...
    @simplify_gpencil_antialiasing.setter
    def simplify_gpencil_antialiasing(self, value: bool) -> None:
        ...
    @property
    def simplify_gpencil_view_fill(self) -> bool:
        """Display fill strokes in the viewport"""
        ...
    @simplify_gpencil_view_fill.setter
    def simplify_gpencil_view_fill(self, value: bool) -> None:
        ...
    @property
    def simplify_gpencil_modifier(self) -> bool:
        """Display modifiers"""
        ...
    @simplify_gpencil_modifier.setter
    def simplify_gpencil_modifier(self, value: bool) -> None:
        ...
    @property
    def simplify_gpencil_shader_fx(self) -> bool:
        """Display Shader Effects"""
        ...
    @simplify_gpencil_shader_fx.setter
    def simplify_gpencil_shader_fx(self, value: bool) -> None:
        ...
    @property
    def simplify_gpencil_tint(self) -> bool:
        """Display layer tint"""
        ...
    @simplify_gpencil_tint.setter
    def simplify_gpencil_tint(self, value: bool) -> None:
        ...
    @property
    def use_persistent_data(self) -> bool:
        """Keep render data around for faster re-renders and animation renders, at the cost of increased memory usage"""
        ...
    @use_persistent_data.setter
    def use_persistent_data(self, value: bool) -> None:
        ...
    @property
    def line_thickness_mode(self) -> Literal['ABSOLUTE', 'RELATIVE']:
        """Line thickness mode for Freestyle line drawing"""
        ...
    @line_thickness_mode.setter
    def line_thickness_mode(self, value: Literal['ABSOLUTE', 'RELATIVE']) -> None:
        ...
    @property
    def line_thickness(self) -> Annotated[float, "subtype='PIXEL'", "step=10.0", "precision=3"]:
        """Line thickness in pixels"""
        ...
    @line_thickness.setter
    def line_thickness(self, value: Annotated[float, "subtype='PIXEL'", "step=10.0", "precision=3"]) -> None:
        ...
    @property
    def bake(self) -> Annotated['BakeSettings', "is_animatable=False"]:

        ...
    @property
    def compositor_device(self) -> Literal['CPU', 'GPU']:
        """Set how compositing is executed"""
        ...
    @compositor_device.setter
    def compositor_device(self, value: Literal['CPU', 'GPU']) -> None:
        ...
    @property
    def compositor_precision(self) -> Literal['AUTO', 'FULL']:
        """The precision of compositor intermediate result"""
        ...
    @compositor_precision.setter
    def compositor_precision(self, value: Literal['AUTO', 'FULL']) -> None:
        ...
    @property
    def compositor_denoise_device(self) -> Literal['AUTO', 'CPU', 'GPU']:
        """The device to use to process the denoise nodes in the compositor"""
        ...
    @compositor_denoise_device.setter
    def compositor_denoise_device(self, value: Literal['AUTO', 'CPU', 'GPU']) -> None:
        ...
    @property
    def compositor_denoise_preview_quality(self) -> Literal['HIGH', 'BALANCED', 'FAST']:
        """The quality used by denoise nodes during viewport and interactive compositing if the nodes' quality option is set to Follow Scene"""
        ...
    @compositor_denoise_preview_quality.setter
    def compositor_denoise_preview_quality(self, value: Literal['HIGH', 'BALANCED', 'FAST']) -> None:
        ...
    @property
    def compositor_denoise_final_quality(self) -> Literal['HIGH', 'BALANCED', 'FAST']:
        """The quality used by denoise nodes during the compositing of final renders if the nodes' quality option is set to Follow Scene"""
        ...
    @compositor_denoise_final_quality.setter
    def compositor_denoise_final_quality(self, value: Literal['HIGH', 'BALANCED', 'FAST']) -> None:
        ...
    def frame_path(self, *args, **kwargs) -> Any: ...