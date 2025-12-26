import os
import sys
from pathlib import Path

# Get the local site-packages path from environment variable
local_site_packages = os.environ.get('LOCAL_SITE_PACKAGES')

if local_site_packages:
    if local_site_packages not in sys.path:
        print(f"[Setup] Adding local site-packages to sys.path: {local_site_packages}")
        sys.path.append(local_site_packages)
else:
    print("[Setup] Warning: LOCAL_SITE_PACKAGES environment variable not set.")

# Add project root .venv site-packages if exists (for CI/uv support)
# We assume this script is at tests/blender/setup_dependencies.py
current_dir = Path(__file__).resolve().parent
project_root = current_dir.parents[1]
venv_path = project_root / ".venv"

if venv_path.exists():
    print(f"[Setup] Found .venv at: {venv_path}")
    site_packages_found = False

    # Windows
    if sys.platform == "win32":
        site_packages = venv_path / "Lib" / "site-packages"
        if site_packages.exists():
            if str(site_packages) not in sys.path:
                sys.path.append(str(site_packages))
                print(f"[Setup] Adding .venv site-packages: {site_packages}")
                site_packages_found = True
    else:
        # Unix/Linux/macOS
        lib_dir = venv_path / "lib"
        if lib_dir.exists():
            for child in lib_dir.iterdir():
                if child.is_dir() and child.name.startswith("python"):
                    site_packages = child / "site-packages"
                    if site_packages.exists():
                        if str(site_packages) not in sys.path:
                            sys.path.append(str(site_packages))
                            print(f"[Setup] Adding .venv site-packages: {site_packages}")
                            site_packages_found = True
                        # Assuming only one python version in venv, but we can iterate all

    if not site_packages_found:
        print("[Setup] Warning: .venv found but could not locate site-packages.")
