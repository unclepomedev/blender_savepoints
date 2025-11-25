# SavePoints

SavePoints is a Blender add-on that helps you manage project versions easily. It allows you to create snapshots of your current work with automatic thumbnails, making it simple to browse and restore previous states.

## Features

- **Incremental Saves**: Automatically generates version IDs (v001, v002, etc.) for each save.
- **Visual Previews**: Captures a thumbnail of your viewport for every save point.
- **Notes**: Add custom notes to remember what changed in each version.
- **Easy Restore**: Browse your history in the UI and restore any version with a single click.

## Usage

1. **Installation**: Install the add-on zip file in Blender.
2. **Locate the Panel**: Open the 3D Viewport and find the **SavePoints** tab in the N-Panel.
3. **Save a Version**:
   - Click **Save Version**.
   - Enter a note (optional) and confirm.
   - A new version is created inside a hidden history folder next to your `.blend` file.
4. **Restore a Version**:
   - Select a version from the history list.
   - View the thumbnail and details.
   - Click **Checkout (Restore)** to open that version.