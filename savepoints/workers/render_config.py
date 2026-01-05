# SPDX-License-Identifier: GPL-3.0-or-later

def apply_image_settings(render, settings):
    # A. Inherited settings
    src_img_settings = settings.get("image_settings", {})
    if src_img_settings:
        try:
            render.image_settings.file_format = src_img_settings.get("file_format", "PNG")
        except Exception:
            pass

        render.image_settings.color_mode = src_img_settings.get("color_mode", "RGBA")
        try:
            render.image_settings.color_depth = src_img_settings.get("color_depth", "8")
        except Exception:
            pass

        render.image_settings.compression = src_img_settings.get("compression", 15)
        render.image_settings.quality = src_img_settings.get("quality", 90)
        if "exr_codec" in src_img_settings:
            try:
                render.image_settings.exr_codec = src_img_settings["exr_codec"]
            except Exception:
                pass

    # B. Overrides
    fmt_override = settings.get("output_format_override", "SCENE")

    if fmt_override == 'PNG':
        render.image_settings.file_format = 'PNG'
    elif fmt_override == 'JPEG':
        render.image_settings.file_format = 'JPEG'
        render.image_settings.color_mode = 'RGB'

        if "jpeg_quality" in settings:
            render.image_settings.quality = settings["jpeg_quality"]
        elif "quality" in src_img_settings:
            render.image_settings.quality = src_img_settings["quality"]


def apply_render_settings(scene, render, settings):
    render.resolution_x = settings.get("resolution_x", 1920)
    render.resolution_y = settings.get("resolution_y", 1080)
    render.resolution_percentage = settings.get("resolution_percentage", 100)
    render.engine = settings.get("engine", 'CYCLES')

    if render.engine == 'CYCLES' and "samples" in settings:
        scene.cycles.samples = settings["samples"]
    elif render.engine in ['BLENDER_EEVEE', 'BLENDER_EEVEE_NEXT'] and "samples" in settings:
        if hasattr(scene.eevee, "taa_render_samples"):
            scene.eevee.taa_render_samples = settings["samples"]


def apply_ffmpeg_settings(render, settings):
    """
    Applies FFMPEG settings for video output.
    """
    ffmpeg = render.ffmpeg
    ffmpeg_settings = settings.get("ffmpeg", {})

    # Defaults matching the timelapse worker requirements
    ffmpeg.format = ffmpeg_settings.get("format", 'MPEG4')
    ffmpeg.codec = ffmpeg_settings.get("codec", 'H264')
    ffmpeg.constant_rate_factor = ffmpeg_settings.get("constant_rate_factor", 'HIGH')
    ffmpeg.audio_codec = ffmpeg_settings.get("audio_codec", 'NONE')
