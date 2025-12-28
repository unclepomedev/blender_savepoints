import bpy
import sys

try:
    bpy.context.scene.render.image_settings.file_format = 'FFMPEG'
    print("SUCCESS: FFMPEG is available.")
except TypeError:
    print("FAILURE: FFMPEG is NOT available in factory mode.")
    sys.exit(1)

# blender --factory-startup -b -P tools/debug/test_ffmpeg.py