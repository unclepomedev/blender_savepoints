# Path to Blender executable
# You can override this by setting BLENDER_EXE environment variable
# or passing it as an argument: just test-blender blender_exe=...
blender_exe := env_var_or_default('BLENDER_EXE', '/Applications/Blender.app/Contents/MacOS/Blender')

# Run E2E tests in Blender
test-blender:
    "{{blender_exe}}" --factory-startup -b -P tests/blender/test_in_blender.py
    "{{blender_exe}}" --factory-startup -b -P tests/blender/test_autosave_skip_thumb.py
    "{{blender_exe}}" --factory-startup -b -P tests/blender/test_extension_compatibility.py
    "{{blender_exe}}" --factory-startup -b -P tests/blender/test_retention_policy.py
    "{{blender_exe}}" --factory-startup -b -P tests/blender/test_missing_file_handling.py
    "{{blender_exe}}" --factory-startup -b -P tests/blender/test_link_history.py
    "{{blender_exe}}" --factory-startup -b -P tests/blender/test_link_history_validation.py
    "{{blender_exe}}" --factory-startup -b -P tests/blender/test_link_history_parent_update.py
    "{{blender_exe}}" --factory-startup -b -P tests/blender/test_export_zip.py
    "{{blender_exe}}" --factory-startup -b -P tests/blender/test_fork_version.py
    "{{blender_exe}}" --factory-startup -b -P tests/blender/test_quick_save_edit_note.py
    "{{blender_exe}}" --factory-startup -b -P tests/blender/test_remap_snapshot_paths.py
