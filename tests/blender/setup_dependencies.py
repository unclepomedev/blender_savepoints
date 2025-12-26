import os
import platform
import site
import sys
from pathlib import Path


def add_path(path_str):
    if path_str not in sys.path and os.path.exists(path_str):
        print(f"[Setup] Adding path: {path_str}")
        sys.path.insert(0, path_str)
        site.addsitedir(path_str)


# 1. Environment Variable
local_site_packages = os.environ.get('LOCAL_SITE_PACKAGES')
if local_site_packages:
    add_path(local_site_packages)
else:
    print("[Setup] Note: LOCAL_SITE_PACKAGES not set.")

# 2. Project Root .venv (CI/uv support)
# tests/blender/setup_dependencies.py -> Project Root
current_dir = Path(__file__).resolve().parent
project_root = current_dir.parents[1]
venv_path = project_root / ".venv"

if venv_path.exists():
    print(f"[Setup] Found .venv at: {venv_path}")
    site_packages_found = False

    if platform.system() == "Windows":
        # Windows: .venv/Lib/site-packages
        site_packages = venv_path / "Lib" / "site-packages"
        if site_packages.exists():
            add_path(str(site_packages))
            site_packages_found = True
    else:
        # Unix: .venv/lib/pythonX.X/site-packages
        lib_dir = venv_path / "lib"
        if lib_dir.exists():
            for child in lib_dir.iterdir():
                if child.is_dir() and child.name.startswith("python"):
                    site_packages = child / "site-packages"
                    if site_packages.exists():
                        add_path(str(site_packages))
                        site_packages_found = True

    if not site_packages_found:
        print("[Setup] Warning: .venv found but could not locate site-packages.")
