# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated
from .bpy_prop_collection import bpy_prop_collection

from .bpy_struct import bpy_struct
from .BakeSettings import BakeSettings
from .CurveMapping import CurveMapping
from .FFmpegSettings import FFmpegSettings
from .ImageFormatSettings import ImageFormatSettings
from .RenderViews import RenderViews
from .SceneRenderView import SceneRenderView
class RenderSettings(bpy_struct):
    @property
    def image_settings(self) -> Annotated['ImageFormatSettings', "is_animatable=False"]:
        ...
    resolution_x: Annotated[int, "subtype='PIXEL'", "step=1", "is_animatable=False"]
    """Number of horizontal pixels in the rendered image"""
    resolution_y: Annotated[int, "subtype='PIXEL'", "step=1", "is_animatable=False"]
    """Number of vertical pixels in the rendered image"""
    resolution_percentage: Annotated[int, "subtype='PERCENTAGE'", "step=10", "is_animatable=False"]
    """Percentage scale for render resolution"""
    preview_pixel_size: Literal['AUTO', '1', '2', '4', '8']
    """Pixel size for viewport rendering"""
    pixel_aspect_x: Annotated[float, "step=10.0", "precision=3", "is_animatable=False"]
    """Horizontal aspect ratio - for anamorphic or non-square pixel output"""
    pixel_aspect_y: Annotated[float, "step=10.0", "precision=3", "is_animatable=False"]
    """Vertical aspect ratio - for anamorphic or non-square pixel output"""
    ppm_factor: Annotated[float, "step=2.0", "precision=2", "is_animatable=False"]
    """The pixel density meta-data written to supported image formats. This value is multiplied by the PPM-base which defines the unit (typically inches or meters)"""
    ppm_base: Annotated[float, "step=2.0", "precision=4", "is_animatable=False"]
    """The base unit for pixels per meter."""
    @property
    def ffmpeg(self) -> Annotated[Optional['FFmpegSettings'], "is_animatable=False"]:
        """FFmpeg related settings for the scene"""
        ...
    fps: Annotated[int, "step=1", "is_animatable=False"]
    """Framerate, expressed in frames per second"""
    fps_base: Annotated[float, "step=2.0", "precision=3", "is_animatable=False"]
    """Framerate base"""
    frame_map_old: Annotated[int, "step=1", "is_animatable=False"]
    """Old mapping value in frames"""
    frame_map_new: Annotated[int, "step=1", "is_animatable=False"]
    """How many frames the Map Old will last"""
    dither_intensity: Annotated[float, "step=0.10000000149011612", "precision=2"]
    """Amount of dithering noise added to the rendered image to break up banding"""
    filter_size: Annotated[float, "subtype='PIXEL'", "step=1.0", "precision=2"]
    """Width over which the reconstruction filter combines samples"""
    film_transparent: bool
    """World background is transparent, for compositing the render over another background"""
    use_freestyle: Annotated[bool, "is_animatable=False"]
    """Draw stylized strokes using Freestyle"""
    threads: Annotated[int, "step=1"]
    """Maximum number of CPU cores to use simultaneously while rendering (for multi-core/CPU systems)"""
    threads_mode: Literal['AUTO', 'FIXED']
    """Determine the amount of render threads used"""
    use_motion_blur: Annotated[bool, "is_animatable=False"]
    """Use multi-sampled 3D scene motion blur"""
    motion_blur_shutter: Annotated[float, "subtype='FACTOR'", "step=1.0", "precision=2"]
    """Time taken in frames between shutter open and close"""
    motion_blur_position: Literal['START', 'CENTER', 'END']
    """Offset for the shutter's time interval, allows to change the motion blur trails"""
    @property
    def motion_blur_shutter_curve(self) -> Annotated[Optional['CurveMapping'], "is_animatable=False"]:
        """Curve defining the shutter's openness over time"""
        ...
    hair_type: Literal['STRAND', 'STRIP', 'CYLINDER']
    """Curves shape type"""
    hair_subdiv: Annotated[int, "step=1"]
    """Additional subdivision along the curves"""
    use_high_quality_normals: bool
    """Use high quality tangent space at the cost of lower performance"""
    use_border: Annotated[bool, "is_animatable=False"]
    """Render a user-defined render region, within the frame size"""
    border_min_x: Annotated[float, "step=10.0", "precision=3", "is_animatable=False"]
    """Minimum X value for the render region"""
    border_min_y: Annotated[float, "step=10.0", "precision=3", "is_animatable=False"]
    """Minimum Y value for the render region"""
    border_max_x: Annotated[float, "step=10.0", "precision=3", "is_animatable=False"]
    """Maximum X value for the render region"""
    border_max_y: Annotated[float, "step=10.0", "precision=3", "is_animatable=False"]
    """Maximum Y value for the render region"""
    use_crop_to_border: Annotated[bool, "is_animatable=False"]
    """Crop the rendered frame to the defined render region size"""
    use_placeholder: Annotated[bool, "is_animatable=False"]
    """Create empty placeholder files while rendering frames (similar to Unix 'touch')"""
    use_overwrite: bool
    """Overwrite existing files while rendering"""
    use_compositing: Annotated[bool, "is_animatable=False"]
    """Process the render result through the compositing pipeline, if a compositing node group is assigned to the scene"""
    use_sequencer: Annotated[bool, "is_animatable=False"]
    """Process the render (and composited) result through the video sequence editor pipeline, if sequencer strips exist"""
    use_file_extension: Annotated[bool, "is_animatable=False"]
    """Add the file format extensions to the rendered file name (eg: filename + .jpg)"""
    @property
    def file_extension(self) -> Annotated[str, "is_animatable=False"]:
        """The file extension used for saving renders"""
        ...
    @property
    def is_movie_format(self) -> bool:
        """When true the format is a movie"""
        ...
    use_lock_interface: Annotated[bool, "is_animatable=False"]
    """Lock interface during rendering in favor of giving more memory to the renderer"""
    filepath: Annotated[str, "subtype='FILE_PATH'", "is_animatable=False"]
    """Directory/name to save animations, # characters define the position and padding of frame numbers"""
    use_render_cache: Annotated[bool, "is_animatable=False"]
    """Save render cache to EXR files (useful for heavy compositing, Note: affects indirectly rendered scenes)"""
    use_stamp_time: bool
    """Include the rendered frame timecode as HH:MM:SS.FF in image metadata"""
    use_stamp_date: bool
    """Include the current date in image/video metadata"""
    use_stamp_frame: bool
    """Include the frame number in image metadata"""
    use_stamp_frame_range: bool
    """Include the rendered frame range in image/video metadata"""
    use_stamp_camera: bool
    """Include the name of the active camera in image metadata"""
    use_stamp_lens: bool
    """Include the active camera's lens in image metadata"""
    use_stamp_scene: bool
    """Include the name of the active scene in image/video metadata"""
    use_stamp_note: bool
    """Include a custom note in image/video metadata"""
    use_stamp_marker: bool
    """Include the name of the last marker in image metadata"""
    use_stamp_filename: bool
    """Include the .blend filename in image/video metadata"""
    use_stamp_sequencer_strip: bool
    """Include the name of the foreground sequence strip in image metadata"""
    use_stamp_render_time: bool
    """Include the render time in image metadata"""
    stamp_note_text: Annotated[str, "is_animatable=False"]
    """Custom text to appear in the stamp note"""
    use_stamp: bool
    """Render the stamp info text in the rendered image"""
    use_stamp_labels: bool
    """Display stamp labels ("Camera" in front of camera name, etc.)"""
    metadata_input: Literal['SCENE', 'STRIPS']
    """Where to take the metadata from"""
    use_stamp_memory: bool
    """Include the peak memory usage in image metadata"""
    use_stamp_hostname: bool
    """Include the hostname of the machine that rendered the frame"""
    stamp_font_size: Annotated[int, "subtype='PIXEL'", "step=1"]
    """Size of the font used when rendering stamp text"""
    stamp_foreground: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]
    """Color to use for stamp text"""
    stamp_background: Annotated[list[float], "subtype='COLOR_GAMMA'", "step=10.0", "precision=3"]
    """Color to use behind stamp text"""
    sequencer_gl_preview: Literal['WIREFRAME', 'SOLID', 'MATERIAL', 'RENDERED']
    """Display method used in the sequencer view"""
    use_sequencer_override_scene_strip: bool
    """Use workbench render settings from the sequencer scene, instead of each individual scene used in the strip"""
    use_single_layer: Annotated[bool, "is_animatable=False"]
    """Only render the active layer. Only affects rendering from the interface, ignored for rendering from command line."""
    @property
    def views(self) -> Annotated['RenderViews', "is_animatable=False"]:
        ...
    @property
    def stereo_views(self) -> Annotated[bpy_prop_collection['SceneRenderView'], "is_animatable=False"]:
        ...
    use_multiview: bool
    """Use multiple views in the scene"""
    views_format: Annotated[Literal['STEREO_3D', 'MULTIVIEW'], "is_animatable=False"]
    engine: Annotated[Literal['BLENDER_EEVEE'], "is_animatable=False"]
    """Engine to use for rendering"""
    @property
    def has_multiple_engines(self) -> bool:
        """More than one rendering engine is available"""
        ...
    @property
    def use_spherical_stereo(self) -> bool:
        """Active render engine supports spherical stereo rendering"""
        ...
    use_simplify: bool
    """Enable simplification of scene for quicker preview renders"""
    simplify_subdivision: Annotated[int, "subtype='UNSIGNED'", "step=1"]
    """Global maximum subdivision level"""
    simplify_child_particles: Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]
    """Global child particles percentage"""
    simplify_subdivision_render: Annotated[int, "subtype='UNSIGNED'", "step=1"]
    """Global maximum subdivision level during rendering"""
    simplify_child_particles_render: Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]
    """Global child particles percentage during rendering"""
    simplify_volumes: Annotated[float, "subtype='FACTOR'", "step=10.0", "precision=3"]
    """Resolution percentage of volume objects in viewport"""
    use_simplify_normals: bool
    """Skip computing custom normals and face corner normals for displaying meshes in the viewport"""
    simplify_gpencil: bool
    """Simplify Grease Pencil drawing"""
    simplify_gpencil_onplay: bool
    """Simplify Grease Pencil only during animation playback"""
    simplify_gpencil_antialiasing: bool
    """Use Antialiasing to smooth stroke edges"""
    simplify_gpencil_view_fill: bool
    """Display fill strokes in the viewport"""
    simplify_gpencil_modifier: bool
    """Display modifiers"""
    simplify_gpencil_shader_fx: bool
    """Display Shader Effects"""
    simplify_gpencil_tint: bool
    """Display layer tint"""
    use_persistent_data: bool
    """Keep render data around for faster re-renders and animation renders, at the cost of increased memory usage"""
    line_thickness_mode: Literal['ABSOLUTE', 'RELATIVE']
    """Line thickness mode for Freestyle line drawing"""
    line_thickness: Annotated[float, "subtype='PIXEL'", "step=10.0", "precision=3"]
    """Line thickness in pixels"""
    @property
    def bake(self) -> Annotated['BakeSettings', "is_animatable=False"]:
        ...
    compositor_device: Literal['CPU', 'GPU']
    """Set how compositing is executed"""
    compositor_precision: Literal['AUTO', 'FULL']
    """The precision of compositor intermediate result"""
    compositor_denoise_device: Literal['AUTO', 'CPU', 'GPU']
    """The device to use to process the denoise nodes in the compositor"""
    compositor_denoise_preview_quality: Literal['HIGH', 'BALANCED', 'FAST']
    """The quality used by denoise nodes during viewport and interactive compositing if the nodes' quality option is set to Follow Scene"""
    compositor_denoise_final_quality: Literal['HIGH', 'BALANCED', 'FAST']
    """The quality used by denoise nodes during the compositing of final renders if the nodes' quality option is set to Follow Scene"""
    def frame_path(self, *args, **kwargs) -> Any: ...