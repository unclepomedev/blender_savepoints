# SavePoints: Visual Version Control System

**SavePoints** allows you to manage project versions directly in the Blender N-Panel with automatic thumbnails. Stop guessing filenames and start seeing your history.

## Key Features
- **Visual History**: Automatically captures viewport thumbnails for every save.
- **Safe Restore**: Restoring a version automatically backs up the current state. No data loss.
- **Organized**: Saves are stored in a hidden sub-folder, keeping your project directory clean.
- **Snapshot Mode**: Preview old versions safely before overwriting.
- **Auto-Save**: Dedicated background auto-save that doesn't clutter your history list (thumbnails skipped for stability).

## ⚠️ Note

- In environments without a GPU, thumbnails will not be generated. Core functionality remains unaffected.

### Known Limitations: Relative Paths

Because snapshots are saved in a subdirectory (`.{YourFileName}_history/vXXX/snapshot.blend_snapshot`), **external files linked with Relative Paths (e.g., `//Textures/image.png`) will appear as broken links** when you open a snapshot.

**Recommended Workflows:**
To avoid this issue, please use one of the following methods before saving versions:
1.  **Pack Resources (Recommended):** Go to `File > External Data > Pack Resources`. This embeds textures into the `.blend` file.
2.  **Use Absolute Paths:** Ensure your external links use absolute paths.

### ℹ️ Note regarding Asset Browser

Snapshots are saved with a custom `.blend_snapshot` extension. This prevents Blender from scanning them, ensuring **no duplicate assets appear in your Asset Browser**.

*For users upgrading from older versions: Legacy snapshots saved as standard `.blend` files may still cause duplication. You can safely delete them via the SavePoints panel to clean up your library.*

### ℹ️ Note regarding Auto Save

To ensure stability and prevent viewport interference, **Auto-save no longer captures thumbnails**.

*For users upgrading from older versions: You may still see a leftover thumbnail on the "autosave" slot. This is harmless, but you can safely delete the entry via the panel to reset it.*