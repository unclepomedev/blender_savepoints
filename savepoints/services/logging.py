# SPDX-License-Identifier: GPL-3.0-or-later

import bpy


def write_error_log(message, details):
    """
    Helper to write error details to a Blender text block.
    This manipulates bpy.data (Data Layer), not bpy.ops (UI Layer).
    """
    text_name = "SavePoints_Log.txt"
    text = bpy.data.texts.get(text_name)
    if not text:
        text = bpy.data.texts.new(text_name)

    text.clear()
    text.write(message + "\n\n")
    text.write(details)
