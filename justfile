# Path to Blender executable
# You can override this by setting BLENDER_EXE environment variable
# or passing it as an argument: just test-blender blender_exe=...

blender_exe := env_var_or_default('BLENDER_EXE', '/Applications/Blender.app/Contents/MacOS/Blender')

# Run E2E tests in Blender
test-blender:
    #!/usr/bin/env bash
    set -e

    for test_file in tests/blender/test_*.py; do
        echo "---------------------------------------------------"
        echo "Running: $test_file"
        "{{ blender_exe }}" --factory-startup -b -P "$test_file"
    done

    echo "✅ All tests passed!"
