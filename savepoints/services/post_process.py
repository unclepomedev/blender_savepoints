# SPDX-License-Identifier: GPL-3.0-or-later

import os
import subprocess
import sys

import bpy

FRAMES_PER_IMAGE = 6


def _escape_for_applescript(text):
    return text.replace('\\', '\\\\').replace('"', '\\"')


def _escape_for_powershell(text):
    # Escape backtick first, then dollar sign and double quote
    return text.replace('`', '``').replace('$', '`$').replace('"', '`"')


def send_os_notification(title, message):
    """
    Send OS-native notification without external dependencies.
    """
    try:
        if sys.platform == "darwin":  # macOS
            safe_title = _escape_for_applescript(title)
            safe_message = _escape_for_applescript(message)
            script = f'display notification "{safe_message}" with title "{safe_title}" sound name "default"'
            subprocess.run(["osascript", "-e", script], check=False)

        elif sys.platform == "win32":  # Windows
            safe_title = _escape_for_powershell(title)
            safe_message = _escape_for_powershell(message)
            ps_script = f"""
            [reflection.assembly]::loadwithpartialname("System.Windows.Forms");
            $icon = [system.windows.forms.notifyicon]::new();
            $icon.icon = [system.drawing.icon]::extractassociatedicon((Get-Process -id $pid).Path);
            $icon.visible = $true;
            $icon.showballoontip(3000, "{safe_title}", "{safe_message}", [system.windows.forms.tooltipicon]::Info);
            start-sleep -m 3000; 
            $icon.dispose();
            """
            creation_flags = getattr(subprocess, 'CREATE_NO_WINDOW', 0x08000000)
            subprocess.run(["powershell", "-Command", ps_script], creationflags=creation_flags, check=False)

        elif sys.platform.startswith("linux"):  # Linux
            subprocess.run(["notify-send", title, message], check=False)

    except Exception as e:
        print(f"[SavePoints] Notification failed: {e}")


def open_folder_platform_independent(directory_path):
    """
    Opens the directory in the OS default file explorer.
    """
    if not os.path.exists(directory_path):
        return False

    try:
        bpy.ops.wm.path_open(filepath=directory_path)
        return True
    except Exception as e:
        print(f"Failed to open folder: {e}")
        return False


def create_vse_timelapse(directory_path, scene_name_suffix="_Timelapse"):
    """
    Creates a new Scene, imports rendered images into VSE.
    Returns the scene name if successful, None otherwise.
    """
    if not os.path.exists(directory_path):
        return None

    # 1. collect and sort image files
    valid_exts = {'.png', '.jpg', '.jpeg', '.exr', '.tif', '.tiff', '.webp', '.tga', '.bmp'}
    files = [
        f for f in os.listdir(directory_path)
        if os.path.splitext(f)[1].lower() in valid_exts
    ]

    files.sort()

    if not files:
        print("No images found to create timelapse.")
        return None

    # 2. get current file name and determine scene name
    clean_path = directory_path.rstrip(os.sep)
    base_name = os.path.basename(clean_path)
    if not base_name:
        base_name = "render"
    scene_name = f"{base_name}{scene_name_suffix}"

    new_scene = bpy.data.scenes.new(name=scene_name)

    # 3. scene setup
    current_scene = bpy.context.scene
    new_scene.render.resolution_x = current_scene.render.resolution_x
    new_scene.render.resolution_y = current_scene.render.resolution_y
    new_scene.render.fps = current_scene.render.fps
    new_scene.render.fps_base = current_scene.render.fps_base

    # 4. VSE setup
    if not new_scene.sequence_editor:
        new_scene.sequence_editor_create()

    seq = new_scene.sequence_editor

    if hasattr(seq, 'strips'):
        strips_collection = seq.strips
    else:
        strips_collection = seq.sequences

    try:
        current_frame = 1

        for i, f_name in enumerate(files):
            f_path = os.path.join(directory_path, f_name)

            strip = strips_collection.new_image(
                name=f"Timelapse_Image_{i}",
                filepath=f_path,
                channel=1,
                frame_start=current_frame,
            )
            strip.frame_final_duration = FRAMES_PER_IMAGE
            current_frame += FRAMES_PER_IMAGE

        new_scene.frame_end = current_frame - 1

        return new_scene.name

    except Exception as e:
        print(f"SavePoints Error creating VSE strip: {e}")
        import traceback
        traceback.print_exc()
        return None


def launch_timelapse_mp4_generation(input_dir, output_file, fps, burn_in, burn_in_pos):
    """
    Launches the timelapse worker script in a background process to generate an MP4.
    """
    worker_script = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "workers", "timelapse_worker.py"))

    if not os.path.exists(worker_script):
        print(f"[SavePoints] Error: Timelapse worker not found at {worker_script}")
        return False

    cmd = [
        bpy.app.binary_path,
        "-b",
        "--factory-startup",
        "-P", worker_script,
        "--",
        input_dir,
        output_file,
        str(fps),
        str(int(burn_in)),
        str(burn_in_pos)
    ]

    # Prevent command prompt window on Windows
    startupinfo = None
    if sys.platform == 'win32':
        startupinfo = subprocess.STARTUPINFO()
        startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW

    try:
        # Use startupinfo for Windows, close_fds for POSIX
        subprocess.Popen(
            cmd,
            startupinfo=startupinfo,
            close_fds=(os.name == 'posix')
        )
        print("[SavePoints] MP4 generation started in background...")
        return True
    except Exception as e:
        print(f"[SavePoints] Failed to start MP4 generation: {e}")
        return False
