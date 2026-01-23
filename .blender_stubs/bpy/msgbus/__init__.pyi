# Blender Probe Generated Stub for Blender 5.1.0 Alpha
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name

import typing
from typing import Any, Callable

def subscribe_rna(key: Any, owner: Any, args: Any, notify: Callable[[tuple], None], options: set[str] | None = None) -> None: ...
def publish_rna(key: Any) -> None: ...
def clear_by_owner(owner: Any) -> None: ...