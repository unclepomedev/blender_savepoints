import bpy
import sys

print("-" * 30)
print(f"Blender Version: {bpy.app.version_string}")
print("Testing API Fix: Setting media_type='VIDEO' before file_format='FFMPEG'")

settings = bpy.context.scene.render.image_settings

try:
    print("Attempting to set media_type -> 'VIDEO'...")
    settings.media_type = 'VIDEO'
    print("  OK: media_type set successfully.")
except AttributeError:
    print("  NOTE: 'media_type' property does not exist in this version.")
except TypeError as e:
    print(f"  ERROR: Failed to set media_type. Details: {e}")

try:
    print("Attempting to set file_format -> 'FFMPEG'...")
    settings.file_format = 'FFMPEG'
    print("\nSUCCESS: FFMPEG format set! The fix works.")
except TypeError as e:
    print(f"\nFAILURE: Still cannot set FFMPEG. Details: {e}")

    rna_enum = settings.bl_rna.properties['file_format'].enum_items
    available = [item.identifier for item in rna_enum]
    print(f"Available formats: {available}")
    sys.exit(1)

# blender --factory-startup -b -P tools/debug/test_ffmpeg.py