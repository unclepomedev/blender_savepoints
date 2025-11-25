import shutil
import tomllib
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ADDON_DIR = ROOT / "savepoints"
DIST_DIR = ROOT / "dist"


def get_version():
    manifest = tomllib.loads((ADDON_DIR / "blender_manifest.toml").read_text("utf-8"))
    return manifest["version"]


def main():
    version = get_version()
    DIST_DIR.mkdir(exist_ok=True)
    out_base = DIST_DIR / f"savepoints-{version}"
    if out_base.exists():
        shutil.rmtree(out_base)
    shutil.make_archive(str(out_base), "zip", root_dir=ROOT, base_dir=ADDON_DIR.name)
    print(f"Built: {out_base}.zip")


if __name__ == "__main__":
    main()
