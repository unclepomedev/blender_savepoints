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
  It has been released on Blender Extensions, so you can get it from [there](https://extensions.blender.org/add-ons/savepoints/).
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
      - A backup of the previous main file will be saved in the history folder (e.g., `.{YourFileName}_history/{YourFileName}.blend.123456.bak`).
5. **Auto Save**:
   - Configure auto-save settings directly in the panel.
   - Toggle on/off and set the interval (minimum 1 minute).
   - Auto-save overwrites a single "autosave" slot, so your history list doesn't get cluttered.
   - **Note**: Auto-save does not generate thumbnails to avoid rendering interruptions.

## ⚠️ Note

Thumbnails are skipped in no-GPU environments, but versioning remains fully functional. (Compatible with headless mode for automation and CI/CD workflows.)

### Known Limitations: Relative Paths

Because snapshots are saved in a subdirectory (`.{YourFileName}_history/vXXX/snapshot.blend_snapshot`), **external files linked with Relative Paths (e.g., `//Textures/image.png`) will appear as broken links** when you open a snapshot.

**Recommended Workflows:**
To avoid this issue, please use one of the following methods before saving versions:
1.  **Pack Resources (Recommended):** Go to `File > External Data > Pack Resources`. This embeds textures into the `.blend` file.
2.  **Use Absolute Paths:** Ensure your external links use absolute paths.

### ℹ️ Note regarding Asset Browser

Snapshots are saved with a custom `.blend_snapshot` extension. This prevents Blender from scanning them, ensuring **no duplicate assets appear in your Asset Browser**.

*For users upgrading from older versions: Legacy snapshots saved as standard `.blend` files may still cause duplication. You can safely delete them via the SavePoints panel to clean up your library.*

## ❓ FAQ / Troubleshooting

**Q: What if I uninstall the add-on? Can I still access my history?**
**A: Yes.** SavePoints does not use any proprietary format. The snapshot files (`.blend_snapshot`) are standard Blender files with a different extension.

**To manually recover a file without the add-on:**
1. Navigate to the hidden history folder next to your project file (named like `.{YourFileName}_history`).
2. Open the version folder you want to recover (e.g., `v005`).
3. **Copy** the snapshot file (`snapshot.blend_snapshot`) to another location (e.g., your Desktop).
4. **Rename** the extension from `.blend_snapshot` to `.blend`.
5. Open it normally in Blender.
