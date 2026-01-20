# install blup first

# Run E2E tests in Blender
test-blender version='':
    #!/usr/bin/env bash
    set -e

    export LOCAL_SITE_PACKAGES=$(python3 -c "import site; print(site.getsitepackages()[0])" 2>/dev/null || echo "")
    echo "Using Site Packages: $LOCAL_SITE_PACKAGES"

    if [ -z "{{version}}" ]; then
        BLUP_CMD="blup run"
    else
        BLUP_CMD="blup run {{version}}"
    fi
    echo "Running tests with command: $BLUP_CMD"

    for test_file in tests/blender/test_*.py; do
        echo "---------------------------------------------------"
        echo "Running: $test_file"

        $BLUP_CMD -- --factory-startup -b \
            -P tests/blender/setup_dependencies.py \
            -P "$test_file" || exit 1
    done

    echo "✅ All tests passed!"
