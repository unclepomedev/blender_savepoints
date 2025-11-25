# SPDX-License-Identifier: GPL-3.0-or-later

import bpy
from bpy.app.handlers import persistent

from . import operators
from . import properties
from . import ui
from . import utils

classes = (
    properties.SavePointsVersion,
    properties.SavePointsSettings,
    operators.SAVEPOINTS_OT_commit,
    operators.SAVEPOINTS_OT_checkout,
    operators.SAVEPOINTS_OT_restore,
    operators.SAVEPOINTS_OT_delete,
    operators.SAVEPOINTS_OT_refresh,
    ui.SAVEPOINTS_UL_version_list,
    ui.SAVEPOINTS_PT_main,
)


@persistent
def load_handler(dummy):
    """Sync history when file is loaded."""
    if bpy.context.scene:
        utils.sync_history_to_props(bpy.context)


def register():
    utils.register_previews()
    for cls in classes:
        bpy.utils.register_class(cls)

    bpy.types.Scene.savepoints_settings = bpy.props.PointerProperty(type=properties.SavePointsSettings)
    bpy.app.handlers.load_post.append(load_handler)


def unregister():
    if load_handler in bpy.app.handlers.load_post:
        bpy.app.handlers.load_post.remove(load_handler)

    utils.unregister_previews()
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)

    del bpy.types.Scene.savepoints_settings


if __name__ == "__main__":
    register()
