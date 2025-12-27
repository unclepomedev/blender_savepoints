SavePoints is a Blender add-on that helps you manage project versions easily. It allows you to create snapshots of your current work with automatic thumbnails, making it simple to browse and restore previous states.

## Features

- **Incremental Saves**: Automatically generates version IDs (v001, v002, etc.) for each save.
- **Visual Previews**: Captures a thumbnail of your viewport for every save point.
- **Detailed Info**: Displays object count and file size for each version.
- **Notes**: Add custom notes to remember what changed in each version.
- **Edit Notes**: Update notes for any version directly from the history list.
- **Easy Restore**: Browse your history in the UI and restore any version with a single click.
- **Rescue Assets**: Easily append objects from a specific version without opening the full snapshot.
- **Ghost Reference**: Overlay a previous version as a wireframe in the 3D viewport to visually compare changes without switching files.
- **Batch Timelapse**: **(New!)** Automatically render multiple versions to create an evolution timelapse.
- **Context-Aware Rendering**: **(New!)** Applies your **current** camera position, lighting, and render settings to **past** snapshots. This ensures perfect alignment for timelapses, regardless of how the camera moved during the project.
- **Quick Save**: Option to skip the note dialog for instant saving.
- **Safe Recovery**: Overwrite the main project file with a previous version safely. The original file is automatically backed up in the history folder.
- **Auto Save**: Automatically saves your work to a dedicated slot at configurable intervals (default 10 min), ensuring you never lose progress.
- **Disk Management**: Automatically deletes the oldest versions to maintain a manageable history size, while preserving locked versions.
- **Version Protection**: Lock specific versions to prevent them from being auto-deleted or accidentally removed.
- **Version Tagging**: Assign tags (Stable, Milestone, Experiment, Bug) to versions and filter the history list to find important snapshots instantly.

## Usage

1. **Installation**: Install the add-on zip file in Blender.
   It has been released on Blender Extensions, so you can get it from [there](https://extensions.blender.org/add-ons/savepoints/).
2. **Locate the Panel**: Open the 3D Viewport and find the **SavePoints** tab in the N-Panel.
3. **Save a Version**:
   - Click **Save Version** or use shortcuts:
     - `Ctrl/Cmd + Alt (Opt) + S`: Standard Save (respects "Show Save Dialog" setting).
     - `Ctrl/Cmd + Alt (Opt) + Shift + S`: Forced Quick Save (always skips dialog).
   - Enter a note (optional) and confirm.
   - *Tip*: Disable **"Show Save Dialog"** in settings for one-click saving with the standard shortcut.
   - A new version is created inside a hidden history folder next to your `.blend` file.
4. **Restore a Version**:
   - Select a version from the history list.
   - View the thumbnail, note, object count, and file size.
   - **Edit Note**: Click the pencil icon next to the note to update it.
   - **Rescue Assets**: Click the Import icon to browse and append objects from this version into your current scene.
   - **Ghost Reference**: Click the Ghost icon to toggle a wireframe overlay of this version in the viewport. Useful for comparing changes.
   - Click **Checkout (Restore)** to open that version.
   - You are now in **Snapshot Mode** (indicated by a red border in the viewport).
       - To restore this version as the main file, click **Save as Parent**.
       - To save this snapshot as an entirely separate project, click **Fork (Save as New)**.
       - To return to your original file without saving changes, click **Return to Parent**.
       - A backup of the previous main file will be saved in the history folder (e.g., `.{YourFileName}_history/{YourFileName}.blend.123456.bak`).
5. **Auto Save**:
   - Configure auto-save settings directly in the panel.
   - Toggle on/off and set the interval (minimum 1 minute).
   - Auto-save overwrites a single "autosave" slot, so your history list doesn't get cluttered.
   - **Note**: Auto-save does not generate thumbnails to avoid rendering interruptions.
6. **Disk Management & Protection**:
   - **Limit Versions**: Enable "Limit Versions" in the Disk Management section to automatically keep only the latest N versions (default 50) excluding locked versions.
   - **Lock Versions**: Click the Lock icon next to a version to protect it. Locked versions are never auto-deleted and cannot be manually deleted unless unlocked.
   - Pruning is triggered automatically when a new version is saved or when the list is refreshed.
7. **Relinking History**:
   - If the history folder is missing (e.g., after moving the `.blend` file), a **Link Existing History Folder** button will appear.
   - Click it to select and reconnect an existing history folder.
   - **Note that the selected source folder will be moved to the current location and deleted from the original path.**
8. **Export Project**:
   - Go to **File > Export > SavePoints Project (.zip)**.
   - This creates a zip file containing your current `.blend` file and its entire history folder.
   - Useful for backups or sharing the project with its version history.
9. **Tagging & Filtering**:
   - Click the tag icon on any version row to assign a tag (Stable, Milestone, etc.).
   - Use the filter dropdown at the top of the list to show only specific tags (e.g., only "Stable" versions).
10. **Batch Rendering & Timelapse**:
    - **Enter Batch Mode**: Toggle the checkbox at the top right of the history list.
    - **Select Versions**: Check the boxes for the versions you want to render. (Use "Select All" combined with filters to quickly select all "Stable" versions).
    - **Configure Output**: Choose **SCENE** (uses current render settings), **PNG**, or **JPEG**.
    - **Start Render**: Click **Batch Render Selected**.
      - *Note*: The renderer applies your **current scene's camera, world, and render settings** to the past versions.
      - **Dry Run (Preview)**: Click normally to open the dialog, then check **"Dry Run"** to render a quick low-quality preview (25% resolution, 1 sample).
      - **Instant Final Render**: Hold `Shift` + Click the button to **skip the dialog** and immediately start the final render.
      - **Cancel**: Press `ESC` at any time to abort the process.
    - **Auto-Timelapse**: When finished, a new scene named `..._Timelapse` is created with all images imported into the Video Sequence Editor (VSE) for immediate playback.
    - **Output Location**: Files are saved in `//renders_batch/{BlendName}_{Timestamp}/`.

## ⚠️ Note

### Batch Rendering Limitations
To ensure maximum stability, the batch renderer runs in **Factory Startup Mode**.
- **Supported**: Geometry, Shaders, Modifiers, Geometry Nodes.
- **Not Supported**: Third-party add-ons that generate geometry specifically at render-time (e.g., some scattering tools) will not be loaded.
- **GPU Support**: The renderer attempts to auto-detect and use your saved System Preferences (CUDA/OptiX/Metal) even in factory mode.

### General Notes
- Thumbnails are skipped in no-GPU environments, but versioning remains fully functional.
- **Asset Browser**: Snapshots are saved with a custom `.blend_snapshot` extension. This prevents Blender from scanning them, ensuring **no duplicate assets appear in your Asset Browser**.

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
