# SPDX-License-Identifier: GPL-3.0-or-later

import bpy

def enable_gpu():
    try:
        preferences = bpy.context.preferences
        cycles_addon = preferences.addons.get('cycles')
        if not cycles_addon:
            print("Worker: Cycles addon not found in preferences (Factory Startup?). Skipping GPU.")
            return False

        cycles_prefs = cycles_addon.preferences
        device_types = ['METAL', 'OPTIX', 'CUDA', 'HIP', 'ONEAPI']

        for dtype in device_types:
            try:
                cycles_prefs.compute_device_type = dtype
                cycles_prefs.get_devices()
                active_devices = []
                for device in cycles_prefs.devices:
                    device.use = True
                    active_devices.append(device.name)

                if active_devices:
                    print(f"Worker: Activated GPU ({dtype}): {active_devices}")
                    return True
            except Exception:
                continue
        print("Worker: No compatible GPU found or failed to activate. Using CPU.")
        return False
    except Exception as e:
        print(f"Worker: GPU setup warning: {e}")
        return False
