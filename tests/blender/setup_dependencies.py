import os
import sys

# Get the local site-packages path from environment variable
local_site_packages = os.environ.get('LOCAL_SITE_PACKAGES')

if local_site_packages:
    if local_site_packages not in sys.path:
        print(f"[Setup] Adding local site-packages to sys.path: {local_site_packages}")
        sys.path.append(local_site_packages)
else:
    print("[Setup] Warning: LOCAL_SITE_PACKAGES environment variable not set.")
