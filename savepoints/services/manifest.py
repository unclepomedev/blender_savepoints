# SPDX-License-Identifier: GPL-3.0-or-later

import json
import uuid
from pathlib import Path
from typing import Any

from .storage import (
    get_manifest_path,
    get_project_path,
    get_history_dir_for_path,
    MANIFEST_NAME,
)

SCHEMA_VERSION = 1


def load_manifest(create_if_missing: bool = True) -> dict[str, Any]:
    """
    Load and return the savepoints manifest for the current project.

    Reads manifest.json from the project's history directory, validates that the file contains a JSON object, and backfills missing fields: `schema_version`, `project_uuid`, `parent_file`, and `versions` (ensuring `versions` is a list). If any backfilled fields are added the manifest is persisted. If the manifest file is missing or cannot be read/parsed, a default manifest with `parent_file`, empty `versions`, `schema_version`, and a new `project_uuid` is returned. Errors encountered while loading are printed.

    Args:
        create_if_missing (bool): If True, creates the default manifest on disk if it is missing.

    Returns:
        manifest (dict): Manifest object containing at least the keys:
            - `parent_file` (str): path to the parent .blend file
            - `versions` (list): list of version entries
            - `schema_version` (int): manifest schema version
            - `project_uuid` (str): stable UUID for the project
    """
    path_str = get_manifest_path()
    if path_str:
        path = Path(path_str)
        if path.exists():
            try:
                with path.open('r', encoding='utf-8') as f:
                    data = json.load(f)

                    if not isinstance(data, dict):
                        raise ValueError("Manifest JSON must be an object")

                    mutated = _backfill(data)

                    # Optional: persist backfilled fields so UUID stabilizes after first load
                    if mutated:
                        save_manifest(data)

                    return data
            except Exception as e:
                print(f"Error loading manifest: {e}")
    default_manifest = {
        "parent_file": get_project_path(),
        "versions": [],
        "schema_version": SCHEMA_VERSION,
        "project_uuid": str(uuid.uuid4()),
    }
    if create_if_missing:
        save_manifest(default_manifest)
    return default_manifest


def _backfill(data):
    mutated = False
    if "schema_version" not in data:
        data["schema_version"] = SCHEMA_VERSION
        mutated = True
    if "project_uuid" not in data:
        data["project_uuid"] = str(uuid.uuid4())
        mutated = True
    if "parent_file" not in data:
        data["parent_file"] = get_project_path()
        mutated = True
    if "versions" not in data or not isinstance(data["versions"], list):
        data["versions"] = []
        mutated = True
    return mutated


def save_manifest(data: dict[str, Any]) -> None:
    """
    Write the given manifest dictionary to the project's manifest.json inside the history directory.

    Parameters:
        data (dict[str, Any]): Manifest data to persist. Will be serialized as pretty-printed JSON with UTF-8 encoding.

    Notes:
        - Creates parent directories for the manifest file if they do not exist.
        - Errors encountered while writing are caught and printed; the function does not raise.
    """
    path_str = get_manifest_path()
    if path_str:
        save_manifest_to_path(Path(path_str), data)


def save_manifest_to_path(manifest_path: Path, data: dict[str, Any]) -> None:
    """
    Write the given manifest dictionary to the specified path.

    Parameters:
        manifest_path (Path): Path to the manifest file.
        data (dict[str, Any]): Manifest data to persist.
    """
    try:
        manifest_path.parent.mkdir(parents=True, exist_ok=True)
        with manifest_path.open('w', encoding='utf-8') as f:
            json.dump(data, f, indent=4, ensure_ascii=False)
    except Exception as e:
        print(f"Error saving manifest: {e}")


def create_default_manifest_data(parent_file_path: str) -> dict[str, Any]:
    """Create a default manifest dictionary."""
    return {
        "parent_file": parent_file_path,
        "versions": [],
        "schema_version": SCHEMA_VERSION,
        "project_uuid": str(uuid.uuid4()),
    }


def initialize_history_for_path(target_path: Path) -> None:
    """
    Initialize the history directory and manifest for a given target path.

    Args:
        target_path (Path): Path to the target blend file.
    """
    try:
        new_history_dir_str = get_history_dir_for_path(str(target_path))
        if new_history_dir_str:
            new_history_dir = Path(new_history_dir_str)
            new_history_dir.mkdir(parents=True, exist_ok=True)

            # Create default manifest
            manifest_path = new_history_dir / MANIFEST_NAME
            if not manifest_path.exists():
                default_manifest = create_default_manifest_data(str(target_path))
                save_manifest_to_path(manifest_path, default_manifest)
    except Exception as e:
        print(f"Warning: History initialization failed: {e}")
