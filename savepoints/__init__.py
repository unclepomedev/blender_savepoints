# SPDX-License-Identifier: GPL-3.0-or-later

import bpy

from . import operators
from . import properties
from . import ui

classes = (
    properties.SavePointsVersion,
    properties.SavePointsSettings,
    operators.SAVEPOINTS_OT_commit,
    operators.SAVEPOINTS_OT_checkout,
    operators.SAVEPOINTS_OT_delete,
    operators.SAVEPOINTS_OT_refresh,
    ui.SAVEPOINTS_UL_version_list,
    ui.SAVEPOINTS_PT_main,
)


def register():
    for cls in classes:
        bpy.utils.register_class(cls)

    bpy.types.Scene.savepoints_settings = bpy.props.PointerProperty(type=properties.SavePointsSettings)


def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)

    del bpy.types.Scene.savepoints_settings


if __name__ == "__main__":
    register()
