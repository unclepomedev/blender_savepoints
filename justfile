# Path to Blender executable
# You can override this by setting BLENDER_EXE environment variable
# or passing it as an argument: just test-blender blender_exe=...
blender_exe := env_var_or_default('BLENDER_EXE', '/Applications/Blender.app/Contents/MacOS/Blender')

# Run E2E tests in Blender
test-blender:
    "{{blender_exe}}" --factory-startup -b -P tests/blender/test_in_blender.py

# Run Auto Save tests in Blender
test-autosave:
    "{{blender_exe}}" --factory-startup -b -P tests/blender/test_autosave.py
