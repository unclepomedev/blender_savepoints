# Blender Probe Generated Stub for Blender 5.0.1
# noinspection PyPep8Naming
# noinspection PyUnresolvedReferences
# noqa: N801
# pylint: disable=invalid-name


"""
Online Documentation:
https://docs.blender.org/api/current/bpy.app.html
"""

import sys
import typing
from typing import Any, Optional, Union, Sequence, Callable, Iterator, Literal, Annotated


alembic: Any
autoexec_fail = False
autoexec_fail_message = ''
autoexec_fail_quiet = False
background = True
binary_path = '/Users/xxx/Library/Application Support/blup/versions/5.0.1/Blender.app/Contents/MacOS/Blender'
build_branch: Any
build_cflags: Any
build_commit_date: Any
build_commit_time: Any
build_commit_timestamp = 1765816573
build_cxxflags: Any
build_date: Any
build_hash: Any
build_linkflags: Any
build_options: Any
build_platform: Any
build_system: Any
build_time: Any
build_type: Any
def count(value, /) -> Any:
    """Return number of occurrences of value.

    Online Documentation:
    https://docs.blender.org/api/current/bpy.app.html"""
    ...

debug = False
debug_depsgraph = False
debug_depsgraph_build = False
debug_depsgraph_eval = False
debug_depsgraph_pretty = False
debug_depsgraph_tag = False
debug_depsgraph_time = False
debug_events = False
debug_freestyle = False
debug_handlers = False
debug_io = False
debug_python = False
debug_simdata = False
debug_value = 0
debug_wm = False
driver_namespace: Any
factory_startup = True
ffmpeg: Any
handlers: Any
def help_text(*args, **kwargs) -> Any:
    """.. staticmethod:: help_text(*, all=False)

   Return the help text as a string.

   :arg all: Return all arguments, even those which aren't available for the current platform.
   :type all: bool
   :return: Help text.
   :rtype: str


    Online Documentation:
    https://docs.blender.org/api/current/bpy.app.html"""
    ...

def index(value, start=0, stop=9223372036854775807, /) -> Any:
    """Return first index of value.

Raises ValueError if the value is not present.

    Online Documentation:
    https://docs.blender.org/api/current/bpy.app.html"""
    ...

def is_job_running(*args, **kwargs) -> Any:
    """.. staticmethod:: is_job_running(job_type)

   Check whether a job of the given type is running.

   :arg job_type: job type in :ref:`rna_enum_wm_job_type_items`.
   :type job_type: str
   :return: Whether a job of the given type is currently running.
   :rtype: bool


    Online Documentation:
    https://docs.blender.org/api/current/bpy.app.html"""
    ...

def memory_usage_undo(*args, **kwargs) -> Any:
    """.. staticmethod:: memory_usage_undo()

   Get undo memory usage information.

   :return: Memory usage of the undo stack in bytes.
   :rtype: int


    Online Documentation:
    https://docs.blender.org/api/current/bpy.app.html"""
    ...

module = False
n_fields = 34
n_sequence_fields = 34
n_unnamed_fields = 0
ocio: Any
oiio: Any
online_access = False
online_access_override = False
opensubdiv: Any
openvdb: Any
portable = False
python_args: Any
render_icon_size = 32
render_preview_size = 128
sdl: Any
tempdir = '/var/folders/zn/vrqg3hq9059c8w8ht1pmpycm0000gn/T/blender_Fglqtw/'
translations: Any
usd: Any
use_event_simulate = False
use_userpref_skip_save_on_exit = True
version: Any
version_cycle = 'release'
version_file: Any
version_string = '5.0.1'
from . import handlers as handlers
# Documentation: https://docs.blender.org/api/current/bpy.app.handlers.html
from . import icons as icons
# Documentation: https://docs.blender.org/api/current/bpy.app.icons.html
from . import timers as timers
# Documentation: https://docs.blender.org/api/current/bpy.app.timers.html
from . import translations as translations
# Documentation: https://docs.blender.org/api/current/bpy.app.translations.html