# Path to Blender executable
# macOS
blender_exe := '/Applications/Blender.app/Contents/MacOS/Blender'
# Windows
# blender_exe := 'C:\Program Files\Blender Foundation\Blender 4.2\blender.exe'
# Linux
# blender_exe := '/usr/bin/blender'

# Run E2E tests in Blender
test-blender:
    "{{blender_exe}}" --factory-startup -b -P tests/blender/test_in_blender.py
