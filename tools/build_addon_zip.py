import os
import tomllib
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ADDON_DIR = ROOT / "savepoints"
DIST_DIR = ROOT / "dist"

# Files/Folders to exclude
EXCLUDE_FILES = {".DS_Store"}
EXCLUDE_DIRS = {"__pycache__"}
EXCLUDE_EXTENSIONS = {".pyc"}


def get_version():
    manifest = tomllib.loads((ADDON_DIR / "blender_manifest.toml").read_text("utf-8"))
    return manifest["version"]


def is_excluded(path: Path) -> bool:
    if path.name in EXCLUDE_FILES:
        return True
    if path.suffix in EXCLUDE_EXTENSIONS:
        return True
    return False


def main():
    version = get_version()
    DIST_DIR.mkdir(exist_ok=True)

    zip_filename = f"savepoints_v{version}.zip"
    zip_path = DIST_DIR / zip_filename

    if zip_path.exists():
        zip_path.unlink()

    print(f"Building: {zip_path}")

    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as zf:
        for root, dirs, files in os.walk(ADDON_DIR):
            # Filter directories in-place to skip walking into excluded ones
            dirs[:] = [d for d in dirs if d not in EXCLUDE_DIRS]

            for file in files:
                file_path = Path(root) / file

                if is_excluded(file_path):
                    continue

                # Archive name should preserve the "savepoints" root folder
                # relative_to(ROOT) gives "savepoints/..."
                arcname = file_path.relative_to(ROOT)

                zf.write(file_path, arcname)
                # print(f"  Adding: {arcname}")

    print(f"Built successfully: {zip_path}")


if __name__ == "__main__":
    main()
