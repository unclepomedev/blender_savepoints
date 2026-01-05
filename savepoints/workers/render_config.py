# SPDX-License-Identifier: GPL-3.0-or-later

def apply_image_settings(render, settings):
    # A. Inherited settings
    src_img_settings = settings.get("image_settings", {})
    if src_img_settings:
        # File Format
        try:
            render.image_settings.file_format = src_img_settings.get("file_format", "PNG")
        except Exception as e:
            print(f"Worker Warning: Failed to set image_settings.file_format: {e}")

        # Color Mode
        try:
            render.image_settings.color_mode = src_img_settings.get("color_mode", "RGBA")
        except Exception as e:
            print(f"Worker Warning: Failed to set image_settings.color_mode: {e}")

        # Color Depth
        try:
            render.image_settings.color_depth = src_img_settings.get("color_depth", "8")
        except Exception as e:
            print(f"Worker Warning: Failed to set image_settings.color_depth: {e}")

        # Compression
        try:
            render.image_settings.compression = src_img_settings.get("compression", 15)
        except Exception as e:
            print(f"Worker Warning: Failed to set image_settings.compression: {e}")

        # Quality
        try:
            render.image_settings.quality = src_img_settings.get("quality", 90)
        except Exception as e:
            print(f"Worker Warning: Failed to set image_settings.quality: {e}")

        # EXR Codec (Specific logic)
        if "exr_codec" in src_img_settings:
            try:
                render.image_settings.exr_codec = src_img_settings["exr_codec"]
            except Exception as e:
                print(f"Worker Warning: Failed to set image_settings.exr_codec: {e}")

    # B. Overrides (Format Override logic)
    fmt_override = settings.get("output_format_override", "SCENE")

    if fmt_override == 'PNG':
        try:
            render.image_settings.file_format = 'PNG'
        except Exception as e:
            print(f"Worker Warning: Failed to override format to PNG: {e}")

    elif fmt_override == 'JPEG':
        try:
            render.image_settings.file_format = 'JPEG'
            render.image_settings.color_mode = 'RGB'

            if "jpeg_quality" in settings:
                render.image_settings.quality = settings["jpeg_quality"]
            elif "quality" in src_img_settings:
                render.image_settings.quality = src_img_settings["quality"]
        except Exception as e:
            print(f"Worker Warning: Failed to override format to JPEG: {e}")


def apply_render_settings(scene, render, settings):
    # Basic settings usually don't fail, but safe to wrap if paranoia is high.
    # Typically resolution/engine are stable properties.
    render.resolution_x = settings.get("resolution_x", 1920)
    render.resolution_y = settings.get("resolution_y", 1080)
    render.resolution_percentage = settings.get("resolution_percentage", 100)

    try:
        render.engine = settings.get("engine", 'CYCLES')
    except Exception as e:
        print(f"Worker Warning: Failed to set render engine: {e}")

    if render.engine == 'CYCLES' and "samples" in settings:
        try:
            scene.cycles.samples = settings["samples"]
        except Exception as e:
            print(f"Worker Warning: Failed to set Cycles samples: {e}")

    elif render.engine in ['BLENDER_EEVEE', 'BLENDER_EEVEE_NEXT'] and "samples" in settings:
        try:
            if hasattr(scene.eevee, "taa_render_samples"):
                scene.eevee.taa_render_samples = settings["samples"]
        except Exception as e:
            print(f"Worker Warning: Failed to set Eevee samples: {e}")


def apply_ffmpeg_settings(render, settings):
    """
    Applies FFMPEG settings.
    FFmpeg enum values can vary between Blender versions.
    """
    ffmpeg_data = settings.get("ffmpeg", {})
    if not ffmpeg_data:
        return

    # format
    try:
        render.ffmpeg.format = ffmpeg_data.get("format", 'MPEG4')
    except Exception as e:
        print(f"Worker Warning: Failed to set ffmpeg.format: {e}")

    # codec
    try:
        render.ffmpeg.codec = ffmpeg_data.get("codec", 'H264')
    except Exception as e:
        print(f"Worker Warning: Failed to set ffmpeg.codec: {e}")

    # constant_rate_factor (CRF)
    try:
        render.ffmpeg.constant_rate_factor = ffmpeg_data.get("constant_rate_factor", 'HIGH')
    except Exception as e:
        print(f"Worker Warning: Failed to set ffmpeg.constant_rate_factor: {e}")

    # audio_codec
    try:
        render.ffmpeg.audio_codec = ffmpeg_data.get("audio_codec", 'NONE')
    except Exception as e:
        print(f"Worker Warning: Failed to set ffmpeg.audio_codec: {e}")
