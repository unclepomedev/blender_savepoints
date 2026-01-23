# Blender Probe Generated Stub for Blender 5.1.0 Alpha
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name

import typing
from typing import Any, Union, Sequence, TypeVar, Generic, Optional, Callable, Iterator

T = TypeVar('T')

class bpy_prop_collection(Sequence[T], Generic[T]):
    def values(self) -> list[T]: ...
    def items(self) -> list[tuple[str, T]]: ...
    def get(self, key: Union[str, Any], default: T = None) -> Optional[T]: ...
    def __getitem__(self, key: Union[str, int]) -> T: ...
    def __iter__(self) -> Iterator[T]: ...
    def __len__(self) -> int: ...
    def __contains__(self, key: Union[str, Any]) -> bool: ...

    # --- Generic fallbacks (Injected via Blender Probe) ---

    def new(self, name: str = '', *args, **kwargs) -> T:
        """
        Create a new item in this collection.

        **⚠️ Warning (Stub)**:
        This is a generic fallback method provided by the IDE plugin.
        Not all collections support creating new items (e.g., read-only collections).
        Please verify if this specific collection supports `new()` in the Blender API docs.
        """
        ...

    def remove(self, value: T, do_unlink: bool = True, do_id_user: bool = True, do_ui_user: bool = True) -> None:
        """
        Remove an item from this collection.

        **⚠️ Warning (Stub)**:
        This is a generic fallback method provided by the IDE plugin.
        Read-only collections do not support removal.
        """
        ...

    def clear(self) -> None:
        """
        Clear all items from this collection.

        **⚠️ Warning (Stub)**:
        This is a generic fallback method. Most Blender collections do not support `clear()`.
        """
        ...

    def load(self, filepath: str, link: bool = False, relative: bool = False, assets: bool = False) -> Any:
        """
        Load data from an external blend file (Context Manager).

        **Note**:
        This method is typically available on `bpy.data.libraries`, `bpy.data.images`, etc.
        """
        ...

    # For collection.objects.link/unlink
    def link(self, item: T) -> None:
        """
        Add a data-block to this collection (e.g., Objects, Collections).

        **⚠️ Warning (Stub)**:
        Valid mainly for `bpy.data.objects` or `collection.children`.
        """
        ...

    def unlink(self, item: T) -> None:
        """
        Remove a data-block from this collection.

        **⚠️ Warning (Stub)**:
        Valid mainly for `bpy.data.objects` or `collection.children`.
        """
        ...