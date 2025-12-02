# SavePoints

SavePoints is a Blender add-on that helps you manage project versions easily. It allows you to create snapshots of your current work with automatic thumbnails, making it simple to browse and restore previous states.

## Features

- **Incremental Saves**: Automatically generates version IDs (v001, v002, etc.) for each save.
- **Visual Previews**: Captures a thumbnail of your viewport for every save point.
- **Detailed Info**: Displays object count and file size for each version.
- **Notes**: Add custom notes to remember what changed in each version.
- **Easy Restore**: Browse your history in the UI and restore any version with a single click.
- **Safe Recovery**: Overwrite the main project file with a previous version safely. The original file is automatically backed up in the history folder.
- **Auto Save**: Automatically saves your work to a dedicated slot at configurable intervals (default 10 min), ensuring you never lose progress.

## Usage

1. **Installation**: Install the add-on zip file in Blender.
2. **Locate the Panel**: Open the 3D Viewport and find the **SavePoints** tab in the N-Panel.
3. **Save a Version**:
   - Click **Save Version**.
   - Enter a note (optional) and confirm.
   - A new version is created inside a hidden history folder next to your `.blend` file.
4. **Restore a Version**:
   - Select a version from the history list.
   - View the thumbnail, note, object count, and file size.
   - Click **Checkout (Restore)** to open that version.
   - You are now in **Snapshot Mode**.
       - To restore this version as the main file, click **Save as Parent**.
       - To return to your original file without saving changes, click **Return to Parent**.
       - A backup of the previous main file will be saved in the history folder (e.g., `.Project_history/Project.blend.123456.bak`).

5. **Auto Save**:
   - Configure auto-save settings directly in the panel.
   - Toggle on/off and set the interval (minimum 1 minute).
   - Auto-save overwrites a single "autosave" slot, so your history list doesn't get cluttered.

## Testing

This repository includes an end-to-end (E2E) test script to verify the core functionality of the add-on in a headless Blender environment.

To run the tests:

```bash
just test-blender
```

> **Note**: 
> - Check and configure the `blender_exe` path in `justfile` to match your environment.
> - [Just](https://github.com/casey/just) is required to run the command.

This script tests:
- Committing a new version.
- Checking out a version.
- Restoring a snapshot to the parent file (with backup).
