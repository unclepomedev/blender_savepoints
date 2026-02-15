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
from .ActionLayer import ActionLayer
from .ActionLayers import ActionLayers
from .ActionPoseMarkers import ActionPoseMarkers
from .ActionSlot import ActionSlot
from .ActionSlots import ActionSlots
from .AssetMetaData import AssetMetaData
from .IDOverrideLibrary import IDOverrideLibrary
from .ImagePreview import ImagePreview
from .Library import Library
from .LibraryWeakReference import LibraryWeakReference
from .TimelineMarker import TimelineMarker
class Action(ID):
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
    @property
    def is_empty(self) -> bool:
        """False when there is any Layer, Slot, or legacy F-Curve"""
        ...
    @property
    def is_action_legacy(self) -> bool:
        """Return whether this is a legacy Action. Legacy Actions have no layers or slots. An empty Action is considered as both a 'legacy' and a 'layered' Action. Since Blender 4.4 actions are automatically updated to layered actions, and thus this will only return True when the action is empty"""
        ...
    @property
    def is_action_layered(self) -> bool:
        """Return whether this is a layered Action. An empty Action is considered as both a 'legacy' and a 'layered' Action."""
        ...
    @property
    def slots(self) -> Annotated['ActionSlots', "is_animatable=False"]:
        """The list of slots in this Action"""
        ...
    @property
    def layers(self) -> Annotated['ActionLayers', "is_animatable=False"]:
        """The list of layers that make up this Action"""
        ...
    @property
    def pose_markers(self) -> Annotated['ActionPoseMarkers', "is_animatable=False"]:
        """Markers specific to this action, for labeling poses"""
        ...
    use_frame_range: Annotated[bool, "is_animatable=False"]
    """Manually specify the intended playback frame range for the action (this range is used by some tools, but does not affect animation evaluation)"""
    use_cyclic: Annotated[bool, "is_animatable=False"]
    """The action is intended to be used as a cycle looping over its manually set playback frame range (enabling this does not automatically make it loop)"""
    frame_start: Annotated[float, "subtype='TIME'", "unit='TIME'", "step=10.0", "precision=3", "is_animatable=False"]
    """The start frame of the manually set intended playback range"""
    frame_end: Annotated[float, "subtype='TIME'", "unit='TIME'", "step=10.0", "precision=3", "is_animatable=False"]
    """The end frame of the manually set intended playback range"""
    frame_range: Annotated[list[float], "subtype='XYZ'", "step=1.0", "precision=3"]
    """The intended playback frame range of this action, using the manually set range if available, or the combined frame range of all F-Curves within this action if not (assigning sets the manual frame range)"""
    @property
    def curve_frame_range(self) -> Annotated[list[float], "subtype='XYZ'", "step=1.0", "precision=3"]:
        """The combined frame range of all F-Curves within this action"""
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
    def deselect_keys(self, *args, **kwargs) -> Any: ...
    def fcurve_ensure_for_datablock(self, *args, **kwargs) -> Any: ...
    def flip_with_pose(self, *args, **kwargs) -> Any: ...