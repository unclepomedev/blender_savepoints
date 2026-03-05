# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.types.Scene.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated

from .ID import ID
from .AnimData import AnimData
from .Annotation import Annotation
from .AssetMetaData import AssetMetaData
from .Collection import Collection
from .ColorManagedDisplaySettings import ColorManagedDisplaySettings
from .ColorManagedSequencerColorspaceSettings import ColorManagedSequencerColorspaceSettings
from .ColorManagedViewSettings import ColorManagedViewSettings
from .DisplaySafeAreas import DisplaySafeAreas
from .IDOverrideLibrary import IDOverrideLibrary
from .ImagePreview import ImagePreview
from .KeyingSet import KeyingSet
from .KeyingSets import KeyingSets
from .KeyingSetsAll import KeyingSetsAll
from .Library import Library
from .LibraryWeakReference import LibraryWeakReference
from .MovieClip import MovieClip
from .NodeTree import NodeTree
from .Object import Object
from .RenderSettings import RenderSettings
from .RigidBodyWorld import RigidBodyWorld
from .SceneDisplay import SceneDisplay
from .SceneEEVEE import SceneEEVEE
from .SceneGpencil import SceneGpencil
from .SceneHydra import SceneHydra
from .SceneObjects import SceneObjects
from .SequenceEditor import SequenceEditor
from .TimelineMarker import TimelineMarker
from .TimelineMarkers import TimelineMarkers
from .ToolSettings import ToolSettings
from .TransformOrientationSlot import TransformOrientationSlot
from .UnitSettings import UnitSettings
from .View3DCursor import View3DCursor
from .ViewLayer import ViewLayer
from .ViewLayers import ViewLayers
from .World import World
from .bpy_prop_collection import bpy_prop_collection
from warnings import deprecated

class Scene(ID):

    @property
    def name(self) -> Annotated[str, "is_animatable=False"]:
        """Unique data-block ID name (within a same type and library)"""
        ...
    @name.setter
    def name(self, value: Annotated[str, "is_animatable=False"]):
        ...
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
    @property
    def use_fake_user(self) -> bool:
        """Save this data-block even if it has no users"""
        ...
    @use_fake_user.setter
    def use_fake_user(self, value: bool):
        ...
    @property
    def use_extra_user(self) -> bool:
        """Indicates whether an extra user is set or not (mainly for internal/debug usages)"""
        ...
    @use_extra_user.setter
    def use_extra_user(self, value: bool):
        ...
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
    @property
    def is_runtime_data(self) -> bool:
        """This data-block is runtime data, i.e. it won't be saved in .blend file. Note that e.g. evaluated IDs are always runtime, so this value is only editable for data-blocks in Main data-base."""
        ...
    @is_runtime_data.setter
    def is_runtime_data(self, value: bool):
        ...
    @property
    def is_editable(self) -> bool:
        """This data-block is editable in the user interface. Linked data-blocks are not editable, except if they were loaded as editable assets."""
        ...
    @property
    def tag(self) -> bool:
        """Tools can use this to tag data for their own purposes (initial state is undefined)"""
        ...
    @tag.setter
    def tag(self, value: bool):
        ...
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
    @property
    def asset_data(self) -> Annotated[Optional['AssetMetaData'], "is_animatable=False"]:
        """Additional data for an asset data-block"""
        ...
    @asset_data.setter
    def asset_data(self, value: Annotated[Optional['AssetMetaData'], "is_animatable=False"]):
        ...
    @property
    def override_library(self) -> Annotated[Optional['IDOverrideLibrary'], "is_animatable=False"]:
        """Library override data"""
        ...
    @property
    def preview(self) -> Annotated[Optional['ImagePreview'], "is_animatable=False"]:
        """Preview image and icon of this data-block (always None if not supported for this type of data)"""
        ...
    @property
    def camera(self) -> Annotated[Optional['Object'], "is_animatable=False"]:
        """Active camera, used for rendering the scene"""
        ...
    @camera.setter
    def camera(self, value: Annotated[Optional['Object'], "is_animatable=False"]):
        ...
    @property
    def background_set(self) -> Annotated[Optional['Scene'], "is_animatable=False"]:
        """Background set scene"""
        ...
    @background_set.setter
    def background_set(self, value: Annotated[Optional['Scene'], "is_animatable=False"]):
        ...
    @property
    def world(self) -> Annotated[Optional['World'], "is_animatable=False"]:
        """World used for rendering the scene"""
        ...
    @world.setter
    def world(self, value: Annotated[Optional['World'], "is_animatable=False"]):
        ...
    @property
    def objects(self) -> Annotated['SceneObjects', "is_animatable=False"]:

        ...
    @property
    def frame_current(self) -> Annotated[int, "subtype='TIME'", "unit='TIME'", "step=1", "is_animatable=False"]:
        """Current frame, to update animation data from Python frame_set() instead"""
        ...
    @frame_current.setter
    def frame_current(self, value: Annotated[int, "subtype='TIME'", "unit='TIME'", "step=1", "is_animatable=False"]):
        ...
    @property
    def frame_subframe(self) -> Annotated[float, "subtype='TIME'", "unit='TIME'", "step=0.009999999776482582", "precision=2", "is_animatable=False"]:

        ...
    @frame_subframe.setter
    def frame_subframe(self, value: Annotated[float, "subtype='TIME'", "unit='TIME'", "step=0.009999999776482582", "precision=2", "is_animatable=False"]):
        ...
    @property
    def frame_float(self) -> Annotated[float, "subtype='TIME'", "unit='TIME'", "step=0.10000000149011612", "precision=2", "is_animatable=False"]:

        ...
    @frame_float.setter
    def frame_float(self, value: Annotated[float, "subtype='TIME'", "unit='TIME'", "step=0.10000000149011612", "precision=2", "is_animatable=False"]):
        ...
    @property
    def frame_start(self) -> Annotated[int, "subtype='TIME'", "unit='TIME'", "step=1", "is_animatable=False"]:
        """First frame of the playback/rendering range"""
        ...
    @frame_start.setter
    def frame_start(self, value: Annotated[int, "subtype='TIME'", "unit='TIME'", "step=1", "is_animatable=False"]):
        ...
    @property
    def frame_end(self) -> Annotated[int, "subtype='TIME'", "unit='TIME'", "step=1", "is_animatable=False"]:
        """Final frame of the playback/rendering range"""
        ...
    @frame_end.setter
    def frame_end(self, value: Annotated[int, "subtype='TIME'", "unit='TIME'", "step=1", "is_animatable=False"]):
        ...
    @property
    def frame_step(self) -> Annotated[int, "subtype='TIME'", "unit='TIME'", "step=1", "is_animatable=False"]:
        """Number of frames to skip forward while rendering/playing back each frame"""
        ...
    @frame_step.setter
    def frame_step(self, value: Annotated[int, "subtype='TIME'", "unit='TIME'", "step=1", "is_animatable=False"]):
        ...
    @property
    def time_jump_unit(self) -> Annotated[Literal['FRAME', 'SECOND'], "is_animatable=False"]:
        """Which unit to use for time jumps in the timeline"""
        ...
    @time_jump_unit.setter
    def time_jump_unit(self, value: Annotated[Literal['FRAME', 'SECOND'], "is_animatable=False"]):
        ...
    @property
    def time_jump_delta(self) -> Annotated[float, "subtype='TIME'", "unit='TIME'", "step=10.0", "precision=3", "is_animatable=False"]:
        """Number of frames or seconds to jump forward or backward"""
        ...
    @time_jump_delta.setter
    def time_jump_delta(self, value: Annotated[float, "subtype='TIME'", "unit='TIME'", "step=10.0", "precision=3", "is_animatable=False"]):
        ...
    @property
    def frame_current_final(self) -> Annotated[float, "subtype='TIME'", "unit='TIME'", "step=10.0", "precision=3", "is_animatable=False"]:
        """Current frame with subframe and time remapping applied"""
        ...
    @property
    def lock_frame_selection_to_range(self) -> Annotated[bool, "is_animatable=False"]:
        """Don't allow frame to be selected with mouse outside of frame range"""
        ...
    @lock_frame_selection_to_range.setter
    def lock_frame_selection_to_range(self, value: Annotated[bool, "is_animatable=False"]):
        ...
    @property
    def use_preview_range(self) -> Annotated[bool, "is_animatable=False"]:
        """Use an alternative start/end frame range for animation playback and view renders"""
        ...
    @use_preview_range.setter
    def use_preview_range(self, value: Annotated[bool, "is_animatable=False"]):
        ...
    @property
    def frame_preview_start(self) -> Annotated[int, "subtype='TIME'", "unit='TIME'", "step=1", "is_animatable=False"]:
        """Alternative start frame for UI playback"""
        ...
    @frame_preview_start.setter
    def frame_preview_start(self, value: Annotated[int, "subtype='TIME'", "unit='TIME'", "step=1", "is_animatable=False"]):
        ...
    @property
    def frame_preview_end(self) -> Annotated[int, "subtype='TIME'", "unit='TIME'", "step=1", "is_animatable=False"]:
        """Alternative end frame for UI playback"""
        ...
    @frame_preview_end.setter
    def frame_preview_end(self, value: Annotated[int, "subtype='TIME'", "unit='TIME'", "step=1", "is_animatable=False"]):
        ...
    @property
    def show_subframe(self) -> Annotated[bool, "is_animatable=False"]:
        """Display and allow setting fractional frame values for the current frame"""
        ...
    @show_subframe.setter
    def show_subframe(self, value: Annotated[bool, "is_animatable=False"]):
        ...
    @property
    def show_keys_from_selected_only(self) -> bool:
        """Only include channels relating to selected objects and data"""
        ...
    @show_keys_from_selected_only.setter
    def show_keys_from_selected_only(self, value: bool):
        ...
    @property
    def use_stamp_note(self) -> Annotated[str, "is_animatable=False"]:
        """User defined note for the render stamping"""
        ...
    @use_stamp_note.setter
    def use_stamp_note(self, value: Annotated[str, "is_animatable=False"]):
        ...
    @property
    def animation_data(self) -> Annotated[Optional['AnimData'], "is_animatable=False"]:
        """Animation data for this data-block"""
        ...
    @property
    def is_nla_tweakmode(self) -> bool:
        """Whether there is any action referenced by NLA being edited (strictly read-only)"""
        ...
    @property
    def use_custom_simulation_range(self) -> Annotated[bool, "is_animatable=False"]:
        """Use a simulation range that is different from the scene range for simulation nodes that don't override the frame range themselves"""
        ...
    @use_custom_simulation_range.setter
    def use_custom_simulation_range(self, value: Annotated[bool, "is_animatable=False"]):
        ...
    @property
    def simulation_frame_start(self) -> Annotated[int, "step=1", "is_animatable=False"]:
        """Frame at which simulations start"""
        ...
    @simulation_frame_start.setter
    def simulation_frame_start(self, value: Annotated[int, "step=1", "is_animatable=False"]):
        ...
    @property
    def simulation_frame_end(self) -> Annotated[int, "step=1", "is_animatable=False"]:
        """Frame at which simulations end"""
        ...
    @simulation_frame_end.setter
    def simulation_frame_end(self, value: Annotated[int, "step=1", "is_animatable=False"]):
        ...
    @property
    def sync_mode(self) -> Literal['NONE', 'FRAME_DROP', 'AUDIO_SYNC']:
        """How to sync playback"""
        ...
    @sync_mode.setter
    def sync_mode(self, value: Literal['NONE', 'FRAME_DROP', 'AUDIO_SYNC']):
        ...
    @property
    def compositing_node_group(self) -> Annotated[Optional['NodeTree'], "is_animatable=False"]:
        """Compositor Nodes"""
        ...
    @compositing_node_group.setter
    def compositing_node_group(self, value: Annotated[Optional['NodeTree'], "is_animatable=False"]):
        ...
    @deprecated('Deprecated in 5.0.0, Removal in 6.0.0')
    @property
    def use_nodes(self) -> bool:
        """Enable the compositing node group."""
        ...
    @deprecated('Deprecated in 5.0.0, Removal in 6.0.0')
    @use_nodes.setter
    def use_nodes(self, value: bool):
        ...
    @property
    def sequence_editor(self) -> Annotated[Optional['SequenceEditor'], "is_animatable=False"]:

        ...
    @property
    def keying_sets(self) -> Annotated['KeyingSets', "is_animatable=False"]:
        """Absolute Keying Sets for this Scene"""
        ...
    @property
    def keying_sets_all(self) -> Annotated['KeyingSetsAll', "is_animatable=False"]:
        """All Keying Sets available for use (Builtins and Absolute Keying Sets for this Scene)"""
        ...
    @property
    def rigidbody_world(self) -> Annotated[Optional['RigidBodyWorld'], "is_animatable=False"]:

        ...
    @property
    def tool_settings(self) -> Annotated['ToolSettings', "is_animatable=False"]:

        ...
    @property
    def unit_settings(self) -> Annotated['UnitSettings', "is_animatable=False"]:
        """Unit editing settings"""
        ...
    @property
    def gravity(self) -> Annotated[list[float], "subtype='ACCELERATION'", "unit='ACCELERATION'", "step=1.0", "precision=2"]:
        """Constant acceleration in a given direction"""
        ...
    @gravity.setter
    def gravity(self, value: Annotated[list[float], "subtype='ACCELERATION'", "unit='ACCELERATION'", "step=1.0", "precision=2"]):
        ...
    @property
    def use_gravity(self) -> bool:
        """Use global gravity for all dynamics"""
        ...
    @use_gravity.setter
    def use_gravity(self, value: bool):
        ...
    @property
    def render(self) -> Annotated['RenderSettings', "is_animatable=False"]:

        ...
    @property
    def safe_areas(self) -> Annotated['DisplaySafeAreas', "is_animatable=False"]:

        ...
    @property
    def timeline_markers(self) -> Annotated['TimelineMarkers', "is_animatable=False"]:
        """Markers used in all timelines for the current scene"""
        ...
    @property
    def transform_orientation_slots(self) -> Annotated[bpy_prop_collection['TransformOrientationSlot'], "is_animatable=False"]:

        ...
    @property
    def cursor(self) -> Annotated['View3DCursor', "is_animatable=False"]:

        ...
    @property
    def use_audio(self) -> bool:
        """Play back of audio from Sequence Editor, otherwise mute audio"""
        ...
    @use_audio.setter
    def use_audio(self, value: bool):
        ...
    @property
    def use_audio_scrub(self) -> bool:
        """Play audio from Sequence Editor while scrubbing"""
        ...
    @use_audio_scrub.setter
    def use_audio_scrub(self, value: bool):
        ...
    @property
    def audio_doppler_speed(self) -> Annotated[float, "step=10.0", "precision=3", "is_animatable=False"]:
        """Speed of sound for Doppler effect calculation"""
        ...
    @audio_doppler_speed.setter
    def audio_doppler_speed(self, value: Annotated[float, "step=10.0", "precision=3", "is_animatable=False"]):
        ...
    @property
    def audio_doppler_factor(self) -> Annotated[float, "step=10.0", "precision=3", "is_animatable=False"]:
        """Pitch factor for Doppler effect calculation"""
        ...
    @audio_doppler_factor.setter
    def audio_doppler_factor(self, value: Annotated[float, "step=10.0", "precision=3", "is_animatable=False"]):
        ...
    @property
    def audio_distance_model(self) -> Annotated[Literal['NONE', 'INVERSE', 'INVERSE_CLAMPED', 'LINEAR', 'LINEAR_CLAMPED', 'EXPONENT', 'EXPONENT_CLAMPED'], "is_animatable=False"]:
        """Distance model for distance attenuation calculation"""
        ...
    @audio_distance_model.setter
    def audio_distance_model(self, value: Annotated[Literal['NONE', 'INVERSE', 'INVERSE_CLAMPED', 'LINEAR', 'LINEAR_CLAMPED', 'EXPONENT', 'EXPONENT_CLAMPED'], "is_animatable=False"]):
        ...
    @property
    def audio_volume(self) -> Annotated[float, "step=10.0", "precision=3"]:
        """Audio volume"""
        ...
    @audio_volume.setter
    def audio_volume(self, value: Annotated[float, "step=10.0", "precision=3"]):
        ...
    @property
    def annotation(self) -> Annotated[Optional['Annotation'], "is_animatable=False"]:
        """Data-block used for annotations in the 3D view"""
        ...
    @annotation.setter
    def annotation(self, value: Annotated[Optional['Annotation'], "is_animatable=False"]):
        ...
    @property
    def active_clip(self) -> Annotated[Optional['MovieClip'], "is_animatable=False"]:
        """Active Movie Clip that can be used by motion tracking constraints or as a camera's background image"""
        ...
    @active_clip.setter
    def active_clip(self, value: Annotated[Optional['MovieClip'], "is_animatable=False"]):
        ...
    @property
    def view_settings(self) -> Annotated[Optional['ColorManagedViewSettings'], "is_animatable=False"]:
        """Color management settings applied on image before saving"""
        ...
    @property
    def display_settings(self) -> Annotated[Optional['ColorManagedDisplaySettings'], "is_animatable=False"]:
        """Settings of device saved image would be displayed on"""
        ...
    @property
    def sequencer_colorspace_settings(self) -> Annotated[Optional['ColorManagedSequencerColorspaceSettings'], "is_animatable=False"]:
        """Settings of color space sequencer is working in"""
        ...
    @property
    def view_layers(self) -> Annotated['ViewLayers', "is_animatable=False"]:

        ...
    @property
    def collection(self) -> Annotated['Collection', "is_animatable=False"]:
        """Scene root collection that owns all the objects and other collections instantiated in the scene"""
        ...
    @property
    def display(self) -> Annotated[Optional['SceneDisplay'], "is_animatable=False"]:
        """Scene display settings for 3D viewport"""
        ...
    @property
    def eevee(self) -> Annotated[Optional['SceneEEVEE'], "is_animatable=False"]:
        """EEVEE settings for the scene"""
        ...
    @property
    def grease_pencil_settings(self) -> Annotated[Optional['SceneGpencil'], "is_animatable=False"]:
        """Grease Pencil settings for the scene"""
        ...
    @property
    def hydra(self) -> Annotated[Optional['SceneHydra'], "is_animatable=False"]:
        """Hydra settings for the scene"""
        ...
    @property
    def cycles(self) -> Annotated[Optional['CyclesRenderSettings'], "is_animatable=False"]:
        """Cycles render settings"""
        ...
    @property
    def cycles_curves(self) -> Annotated[Optional['CyclesCurveRenderSettings'], "is_animatable=False"]:
        """Cycles curves rendering settings"""
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
    def update_render_engine(self, *args, **kwargs) -> Any: ...
    def statistics(self, *args, **kwargs) -> Any: ...
    def frame_set(self, *args, **kwargs) -> Any: ...
    def uvedit_aspect(self, *args, **kwargs) -> Any: ...
    def ray_cast(self, *args, **kwargs) -> Any: ...
    def sequence_editor_create(self, *args, **kwargs) -> Any: ...
    def sequence_editor_clear(self, *args, **kwargs) -> Any: ...