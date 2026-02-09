# SPDX-License-Identifier: GPL-3.0-or-later

import json
import os
import sys

import bpy
import addon_utils


def run_export(json_path: str, output_dir: str, file_prefix: str):
    try:
        with open(json_path, "r", encoding="utf-8") as f:
            settings = json.load(f)
    except Exception as ex:
        print(f"Failed to load settings: {ex}")
        sys.exit(1)

    try:
        addon_utils.enable("io_scene_gltf2", default_set=False)
    except Exception as ex:
        print(f"Error: Failed to enable glTF2 addon: {ex}")
        sys.exit(1)

    target_objects = set(settings.get("target_objects", []))

    for obj in bpy.context.selected_objects:
        obj.select_set(False)

    found_objects = []
    missing_objects = []

    for obj in bpy.data.objects:
        if obj.name in target_objects:
            obj.select_set(True)
            found_objects.append(obj.name)

    for name in target_objects:
        if name not in found_objects:
            missing_objects.append(name)

    if missing_objects:
        print(
            f"Warning: The following objects were not found in this version: {', '.join(missing_objects)}"
        )

    if not found_objects:
        print("Error: No matching objects found to export.")
        sys.exit(1)

    os.makedirs(output_dir, exist_ok=True)

    output_file = os.path.join(output_dir, f"{file_prefix}.glb")
    print(f"Exporting to {output_file}...")

    try:
        bpy.ops.export_scene.gltf(
            filepath=output_file, use_selection=True, export_format="GLB"
        )
        print("Export Finished Successfully.")
    except Exception as ex:
        print(f"Export Failed: {ex}")
        sys.exit(1)


if __name__ == "__main__":
    try:
        argv = sys.argv
        if "--" in argv:
            args = argv[argv.index("--") + 1 :]
            if len(args) >= 3:
                # args[0]: settings_json_path
                # args[1]: output_dir
                # args[2]: file_prefix (filename without extension)
                run_export(args[0], args[1], args[2])
            else:
                print("Worker Error: Missing arguments.")
                sys.exit(1)
        else:
            print("Worker Error: No arguments separator '--' found.")
            sys.exit(1)
    except Exception as e:
        print(f"Worker Global Error: {e}")
        sys.exit(1)
