# SPDX-License-Identifier: GPL-3.0-or-later

import json
import os
import tempfile
import bpy
from .batch_executor import BatchRenderExecutor
from .logging import write_error_log


def get_export_worker_script_path():
    """
    Returns the absolute path to the export worker script file.
    """
    # savepoints/services/../workers/export_worker.py
    return os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..", "workers", "export_worker.py")
    )


def create_glb_export_executor(version, object_names, output_dir_raw):
    """
    Prepares the temporary settings and output directory,
    then initializes and returns a BatchRenderExecutor for GLB export.

    Args:
        version: The version object (from settings.versions).
        object_names (list[str]): List of object names to export.
        output_dir_raw (str): The output path string (can be relative //).

    Returns:
        BatchRenderExecutor: The configured executor instance.

    Raises:
        ValueError: If object_names is empty.
        OSError: If directories cannot be created or files written.
    """
    if not object_names:
        raise ValueError("No objects selected for export.")

    export_settings = {"target_objects": object_names}

    temp_dir = tempfile.mkdtemp(prefix="savepoints_export_")
    settings_path = os.path.join(temp_dir, "export_settings.json")

    with open(settings_path, "w", encoding="utf-8") as f:
        json.dump(export_settings, f, indent=4)

    if not output_dir_raw:
        output_dir_raw = "//"

    output_dir = bpy.path.abspath(output_dir_raw)
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    worker_script = get_export_worker_script_path()

    blend_name = "untitled"
    if bpy.data.filepath:
        blend_name = os.path.splitext(os.path.basename(bpy.data.filepath))[0]

    executor = BatchRenderExecutor(
        tasks=[version],
        temp_dir=temp_dir,
        output_dir=output_dir,
        settings_path=settings_path,
        worker_script_path=worker_script,
        blender_bin=bpy.app.binary_path,
        output_suffix="",  # No suffix, worker adds .glb
        filename_override=blend_name,
    )

    return executor


def process_export_failure(status):
    """
    Handles export failure by reading the worker log and writing it to the SavePoints log.
    """
    log_content = "Log file not found."
    log_path = status.get("log_path")
    if log_path and os.path.exists(log_path):
        try:
            with open(log_path, "r", encoding="utf-8") as f:
                log_content = f.read()
        except Exception as e:
            log_content = f"Failed to read log file: {e}"

    write_error_log(
        f"Export failed for version {status['version_id']}",
        f"Return Code: {status.get('return_code')}\n\nWorker Output:\n{log_content}",
    )
