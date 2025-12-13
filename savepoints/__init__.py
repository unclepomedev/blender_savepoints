# SPDX-License-Identifier: GPL-3.0-or-later

import time

import bpy
from bpy.app.handlers import persistent

from . import operators
from . import properties
from . import ui
from . import ui_utils

classes = (
    properties.SavePointsVersion,
    properties.SavePointsSettings,
    operators.SAVEPOINTS_OT_commit,
    operators.SAVEPOINTS_OT_checkout,
    operators.SAVEPOINTS_OT_restore,
    operators.SAVEPOINTS_OT_open_parent,
    operators.SAVEPOINTS_OT_delete,
    operators.SAVEPOINTS_OT_refresh,
    ui.SAVEPOINTS_UL_version_list,
    ui.SAVEPOINTS_PT_main,
)


@persistent
def load_handler(dummy):
    """Sync history when file is loaded."""
    if bpy.context.scene:
        ui_utils.sync_history_to_props(bpy.context)
        # Reset autosave timer
        if hasattr(bpy.context.scene, "savepoints_settings"):
            bpy.context.scene.savepoints_settings.last_autosave_timestamp = str(time.time())


def register():
    ui_utils.register_previews()
    for cls in classes:
        bpy.utils.register_class(cls)

    bpy.types.Scene.savepoints_settings = bpy.props.PointerProperty(type=properties.SavePointsSettings)
    bpy.app.handlers.load_post.append(load_handler)

    bpy.app.handlers.render_init.append(operators.render_init_handler)
    bpy.app.handlers.render_complete.append(operators.render_complete_handler)
    bpy.app.handlers.render_cancel.append(operators.render_cancel_handler)

    if not bpy.app.timers.is_registered(operators.autosave_timer):
        bpy.app.timers.register(operators.autosave_timer, first_interval=10.0, persistent=True)


def unregister():
    if bpy.app.timers.is_registered(operators.autosave_timer):
        bpy.app.timers.unregister(operators.autosave_timer)

    if load_handler in bpy.app.handlers.load_post:
        bpy.app.handlers.load_post.remove(load_handler)

    if operators.render_init_handler in bpy.app.handlers.render_init:
        bpy.app.handlers.render_init.remove(operators.render_init_handler)
    if operators.render_complete_handler in bpy.app.handlers.render_complete:
        bpy.app.handlers.render_complete.remove(operators.render_complete_handler)
    if operators.render_cancel_handler in bpy.app.handlers.render_cancel:
        bpy.app.handlers.render_cancel.remove(operators.render_cancel_handler)

    ui_utils.unregister_previews()
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)

    del bpy.types.Scene.savepoints_settings


if __name__ == "__main__":
    register()
