# Path to Blender executable
# You can override this by setting BLENDER_EXE environment variable
# or passing it as an argument: just test-blender blender_exe=...

blender_exe := env_var_or_default('BLENDER_EXE', '/Applications/Blender.app/Contents/MacOS/Blender')

# Run E2E tests in Blender
test-blender:
    #!/usr/bin/env bash
    set -e

    export LOCAL_SITE_PACKAGES=$(python3 -c "import site; print(site.getsitepackages()[0])" 2>/dev/null || echo "")
    echo "Using Site Packages: $LOCAL_SITE_PACKAGES"

    for test_file in tests/blender/test_*.py; do
        echo "---------------------------------------------------"
        echo "Running: $test_file"

        "{{ blender_exe }}" --factory-startup -b \
            -P tests/blender/setup_dependencies.py \
            -P "$test_file" || exit 1
    done

    echo "✅ All tests passed!"
