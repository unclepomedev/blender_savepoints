# SPDX-License-Identifier: GPL-3.0-or-later

from pathlib import Path

import bpy


def _resize_image_file(image_path: str, max_dim: int = 360) -> None:
    """Resize the image file to save space."""
    if not Path(image_path).exists():
        return

    try:
        img = bpy.data.images.load(image_path)
        width, height = img.size

        if width > max_dim or height > max_dim:
            scale_factor = min(max_dim / width, max_dim / height)
            new_width = max(1, int(width * scale_factor))
            new_height = max(1, int(height * scale_factor))

            img.scale(new_width, new_height)
            img.save()

        bpy.data.images.remove(img)
    except Exception as e:
        print(f"Failed to resize thumbnail: {e}")


def capture_thumbnail(context: bpy.types.Context, filepath: str) -> None:
    """
    Capture a clean viewport render as a thumbnail.
    """
    path = Path(filepath)
    path.parent.mkdir(parents=True, exist_ok=True)

    # Background mode check
    if not context.window_manager.windows:
        return

    render = context.scene.render
    # Store old settings
    old_filepath = render.filepath

    try:
        # Use simple string for Blender API
        render.filepath = str(path)

        # OpenGL Render (Clean Viewport)
        bpy.ops.render.opengl(write_still=True)

        # Resize logic (To save disk space)
        _resize_image_file(str(path))

    except Exception as e:
        print(f"Thumbnail generation failed: {e}")
    finally:
        # Restore settings
        render.filepath = old_filepath
