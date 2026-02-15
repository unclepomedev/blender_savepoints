# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated
from .bpy_prop_collection import bpy_prop_collection

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
class Scene(ID):
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
    camera: Annotated[Optional['Object'], "is_animatable=False"]
    """Active camera, used for rendering the scene"""
    background_set: Annotated[Optional['Scene'], "is_animatable=False"]
    """Background set scene"""
    world: Annotated[Optional['World'], "is_animatable=False"]
    """World used for rendering the scene"""
    @property
    def objects(self) -> Annotated['SceneObjects', "is_animatable=False"]:
        ...
    frame_current: Annotated[int, "subtype='TIME'", "unit='TIME'", "step=1", "is_animatable=False"]
    """Current frame, to update animation data from Python frame_set() instead"""
    frame_subframe: Annotated[float, "subtype='TIME'", "unit='TIME'", "step=0.009999999776482582", "precision=2", "is_animatable=False"]
    frame_float: Annotated[float, "subtype='TIME'", "unit='TIME'", "step=0.10000000149011612", "precision=2", "is_animatable=False"]
    frame_start: Annotated[int, "subtype='TIME'", "unit='TIME'", "step=1", "is_animatable=False"]
    """First frame of the playback/rendering range"""
    frame_end: Annotated[int, "subtype='TIME'", "unit='TIME'", "step=1", "is_animatable=False"]
    """Final frame of the playback/rendering range"""
    frame_step: Annotated[int, "subtype='TIME'", "unit='TIME'", "step=1", "is_animatable=False"]
    """Number of frames to skip forward while rendering/playing back each frame"""
    time_jump_unit: Annotated[Literal['FRAME', 'SECOND'], "is_animatable=False"]
    """Which unit to use for time jumps in the timeline"""
    time_jump_delta: Annotated[float, "subtype='TIME'", "unit='TIME'", "step=10.0", "precision=3", "is_animatable=False"]
    """Number of frames or seconds to jump forward or backward"""
    @property
    def frame_current_final(self) -> Annotated[float, "subtype='TIME'", "unit='TIME'", "step=10.0", "precision=3", "is_animatable=False"]:
        """Current frame with subframe and time remapping applied"""
        ...
    lock_frame_selection_to_range: Annotated[bool, "is_animatable=False"]
    """Don't allow frame to be selected with mouse outside of frame range"""
    use_preview_range: Annotated[bool, "is_animatable=False"]
    """Use an alternative start/end frame range for animation playback and view renders"""
    frame_preview_start: Annotated[int, "subtype='TIME'", "unit='TIME'", "step=1", "is_animatable=False"]
    """Alternative start frame for UI playback"""
    frame_preview_end: Annotated[int, "subtype='TIME'", "unit='TIME'", "step=1", "is_animatable=False"]
    """Alternative end frame for UI playback"""
    show_subframe: Annotated[bool, "is_animatable=False"]
    """Display and allow setting fractional frame values for the current frame"""
    show_keys_from_selected_only: bool
    """Only include channels relating to selected objects and data"""
    use_stamp_note: Annotated[str, "is_animatable=False"]
    """User defined note for the render stamping"""
    @property
    def animation_data(self) -> Annotated[Optional['AnimData'], "is_animatable=False"]:
        """Animation data for this data-block"""
        ...
    @property
    def is_nla_tweakmode(self) -> bool:
        """Whether there is any action referenced by NLA being edited (strictly read-only)"""
        ...
    use_custom_simulation_range: Annotated[bool, "is_animatable=False"]
    """Use a simulation range that is different from the scene range for simulation nodes that don't override the frame range themselves"""
    simulation_frame_start: Annotated[int, "step=1", "is_animatable=False"]
    """Frame at which simulations start"""
    simulation_frame_end: Annotated[int, "step=1", "is_animatable=False"]
    """Frame at which simulations end"""
    sync_mode: Literal['NONE', 'FRAME_DROP', 'AUDIO_SYNC']
    """How to sync playback"""
    compositing_node_group: Annotated[Optional['NodeTree'], "is_animatable=False"]
    """Compositor Nodes"""
    use_nodes: bool
    """Enable the compositing node group."""
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
    gravity: Annotated[list[float], "subtype='ACCELERATION'", "unit='ACCELERATION'", "step=1.0", "precision=2"]
    """Constant acceleration in a given direction"""
    use_gravity: bool
    """Use global gravity for all dynamics"""
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
    use_audio: bool
    """Play back of audio from Sequence Editor, otherwise mute audio"""
    use_audio_scrub: bool
    """Play audio from Sequence Editor while scrubbing"""
    audio_doppler_speed: Annotated[float, "step=10.0", "precision=3", "is_animatable=False"]
    """Speed of sound for Doppler effect calculation"""
    audio_doppler_factor: Annotated[float, "step=10.0", "precision=3", "is_animatable=False"]
    """Pitch factor for Doppler effect calculation"""
    audio_distance_model: Annotated[Literal['NONE', 'INVERSE', 'INVERSE_CLAMPED', 'LINEAR', 'LINEAR_CLAMPED', 'EXPONENT', 'EXPONENT_CLAMPED'], "is_animatable=False"]
    """Distance model for distance attenuation calculation"""
    audio_volume: Annotated[float, "step=10.0", "precision=3"]
    """Audio volume"""
    annotation: Annotated[Optional['Annotation'], "is_animatable=False"]
    """Data-block used for annotations in the 3D view"""
    active_clip: Annotated[Optional['MovieClip'], "is_animatable=False"]
    """Active Movie Clip that can be used by motion tracking constraints or as a camera's background image"""
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