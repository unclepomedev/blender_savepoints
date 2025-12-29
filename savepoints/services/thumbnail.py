# SPDX-License-Identifier: GPL-3.0-or-later

from pathlib import Path

import bpy

from ..ui_utils import find_3d_view_override


def _resize_image_file(image_path: str, max_dim: int = 360) -> None:
    """Resize the image file to save space."""
    path_obj = Path(image_path)

    # 1. Check existence and fallback logic
    if not path_obj.exists():
        # Fallback: check for other extensions or double extensions
        # This handles cases where Blender ignores the forced format or appends extension
        stem = path_obj.stem  # e.g. "thumbnail"
        parent = path_obj.parent

        # Priority: Double extension -> Common render formats
        candidates_exts = [".png", ".exr", ".jpg", ".jpeg", ".tga", ".tif", ".bmp"]
        found = None

        # Check double extension (thumbnail.png.png)
        double_ext = path_obj.with_name(path_obj.name + ".png")
        if double_ext.exists():
            found = double_ext

        # Check alternate extensions (thumbnail.exr, thumbnail.jpg ...)
        if not found:
            for ext in candidates_exts:
                candidate = parent / (stem + ext)
                if candidate.exists():
                    found = candidate
                    break

        if found:
            try:
                print(f"[SavePoints] Recovering thumbnail from: {found.name}")
                found.rename(path_obj)
            except OSError as e:
                print(f"[SavePoints] Failed to rename thumbnail candidate: {e}")
                return

    if not path_obj.exists():
        return

    try:
        img = bpy.data.images.load(image_path)
        width, height = img.size

        if width > max_dim or height > max_dim:
            scale_factor = min(max_dim / width, max_dim / height)
            new_width = max(1, int(width * scale_factor))
            new_height = max(1, int(height * scale_factor))

            img.scale(new_width, new_height)

        # Ensure format settings for the image object itself
        img.file_format = 'PNG'
        img.save()

        bpy.data.images.remove(img)
    except Exception as e:
        print(f"[SavePoints] Failed to resize/convert thumbnail: {e}")


def capture_thumbnail(context: bpy.types.Context, filepath: str) -> None:
    """
    Capture a clean viewport render as a thumbnail.
    """
    path = Path(filepath)
    path.parent.mkdir(parents=True, exist_ok=True)

    # Background mode check
    if not context.window_manager.windows:
        return

    # Locate a valid 3D Viewport
    override = find_3d_view_override(context)
    if not override:
        print("[SavePoints] Thumbnail skipped: No 3D Viewport found.")
        return

    render = context.scene.render
    # Store old settings
    old_filepath = render.filepath
    old_format = render.image_settings.file_format
    old_mode = render.image_settings.color_mode
    old_depth = render.image_settings.color_depth

    try:
        # Force PNG to ensure consistency
        render.image_settings.file_format = 'PNG'
        render.image_settings.color_mode = 'RGBA'
        render.image_settings.color_depth = '8'

        path_stem = path.with_suffix('')  # .../thumbnail
        render.filepath = str(path_stem)

        # OpenGL Render (Clean Viewport)
        # Use temp_override to ensure we render the correct viewport
        try:
            with context.temp_override(**override):
                bpy.ops.render.opengl(write_still=True)
        except AttributeError:
            # Fallback for older Blender versions if temp_override is missing (unlikely in 4.5)
            bpy.ops.render.opengl(override, write_still=True)
        except Exception as e:
            print(f"[SavePoints] OpenGL render failed: {e}")

        # Resize logic (To save disk space)
        _resize_image_file(str(path))

    except Exception as e:
        print(f"[SavePoints] Thumbnail generation failed: {e}")
    finally:
        # Restore settings
        render.filepath = old_filepath
        render.image_settings.file_format = old_format
        render.image_settings.color_mode = old_mode
        render.image_settings.color_depth = old_depth
