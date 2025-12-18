from pathlib import Path

from savepoints.services.storage import get_history_dir


class SecurityError(ValueError):
    pass


def validate_filename(name: str):
    if not name or ".." in name or "/" in name or "\\" in name:
        raise SecurityError(f"Invalid filename format: '{name}'")


def get_safe_version_dir(version_id: str, must_exist: bool = True) -> Path:
    history_dir_str = get_history_dir()
    if not history_dir_str:
        raise FileNotFoundError("History directory not found")

    history_dir = Path(history_dir_str).resolve()

    validate_filename(version_id)
    target_dir = (history_dir / version_id).resolve()

    if history_dir not in target_dir.parents:
        raise SecurityError(f"Path traversal detected for version ID '{version_id}'")

    if must_exist and not target_dir.exists():
        raise FileNotFoundError(f"Version directory not found: {version_id}")

    return target_dir
