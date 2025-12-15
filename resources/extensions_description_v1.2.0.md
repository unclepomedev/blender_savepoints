# SavePoints: Visual Version Control System

**SavePoints** allows you to manage project versions directly in the Blender N-Panel with automatic thumbnails. Stop guessing filenames and start seeing your history.

## Key Features

- **Visual History**: Automatically captures viewport thumbnails and supports custom notes for every save.
- **Rescue Assets**: Easily append objects from a specific version without opening the full snapshot.
- **Ghost Reference**: Overlay a previous version as a wireframe in the 3D viewport to visually compare changes.
- **Disk Management**: Automatically deletes the oldest versions to maintain a manageable history size, while preserving locked versions.
- **Smart Organization**: Assign tags (Stable, Milestone, etc.) and filter your history instantly.
- **Safe Restore**: Restoring a version automatically backs up the current state. No data loss.
- **Snapshot Mode**: Preview old versions safely with a clear HUD overlay before overwriting.
- **Auto-Save**: Dedicated background auto-save that doesn't clutter your history list (thumbnails skipped for stability).

For detailed usage instructions, please check the links on the right (GitHub).

## ⚠️ Note

- In environments without a GPU, thumbnails will not be generated. Core functionality remains unaffected.

### ℹ️ Note regarding Asset Browser

Snapshots are saved with a custom `.blend_snapshot` extension. This prevents Blender from scanning them, ensuring **no duplicate assets appear in your Asset Browser**.

*For users upgrading from older versions: Legacy snapshots saved as standard `.blend` files may still cause duplication. You can safely delete them via the SavePoints panel to clean up your library.*

### ℹ️ Note regarding Auto Save

To ensure stability and prevent viewport interference, **Auto-save no longer captures thumbnails**.

*For users upgrading from older versions: You may still see a leftover thumbnail on the "autosave" slot. This is harmless, but you can safely delete the entry via the panel to reset it.*
