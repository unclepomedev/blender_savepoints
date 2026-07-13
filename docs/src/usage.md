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
   - **Retrieve Objects**: Click the Import icon to browse and append objects from this version into your current scene.
   - **Ghost Reference**: Click the Ghost icon to toggle a wireframe overlay of this version in the viewport. Useful for comparing changes.
   - Click **Checkout (Restore)** to open that version.
   - You are now in **Snapshot Mode** (indicated by a red border in the viewport).
       - To restore this version as the main file, click **Save as Parent**.
       - To save this snapshot as an entirely separate project, click **Fork (Save as New)**.
         - **Option**: You can enable **"Detach from Library"** in the popup. This converts all linked data (objects, materials) into local data and clears asset marks, ensuring the new file is fully independent and does not pollute your Asset Browser.
       - To return to your original file without saving changes, click **Return to Parent**.
       - A backup of the previous main file will be saved in the history folder (e.g., `.{YourFileName}_history/{YourFileName}.blend.123456.bak`).
5. **Auto Save**:
   - Configure auto-save settings directly in the panel.
   - Toggle on/off and set the interval (minimum 1 minute).
   - Auto-save overwrites a single "autosave" slot, so your history list doesn't get cluttered.
   - **Note**: Auto-save does not generate thumbnails to avoid rendering interruptions.
   - **Safety**: Auto-save is delayed while a blocking interactive operation (such as an active brush stroke or transform) or rendering is running. It retries shortly after the operation finishes; simply staying in Sculpt, Weight Paint, or Edit Mode does not block saving.
6. **Disk Management & Protection**:
   - **Snapshot Compression**: Enabled by default in the General settings. Keep this ON to save disk space, or turn it OFF if you prioritize maximum save speed over file size.
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
      - **Timelapse Settings**: In the dialog, check **Create Timelapse MP4** to generate a video file. You can enable **Burn-in Version ID** to overlay the version name (e.g., "v001") on the video and choose its corner position.
      - **Dry Run (Preview)**: Check **"Dry Run"** to render a quick low-quality preview (25% resolution, 1 sample).
      - **Instant Final Render**: Hold `Shift` + Click the button to **skip the dialog** and immediately start the final render (uses current settings).
      - **Cancel**: Press `ESC` at any time to abort the process.
    - **Auto-Timelapse**: When finished, a new scene named `..._Timelapse` is created with all images imported into the Video Sequence Editor (VSE) for immediate playback.
    - **Output Location**: Files are saved in `//renders_batch/{BlendName}_{Timestamp}/`.
11. **Object History**:
    - Right-click any object in the 3D View and select **Show Object History**.
    - A popup lists detected changes: **Created**, **Moved**, **Minor** (Shape), or **Major** (Vertex Count).
    - **Show All Versions**: Enable this toggle to list *every* snapshot containing the object, even if no changes were detected (marked as **Record**). This ensures you can access internal changes like sculpting or subtle deformations.
    - **Click an entry** to overlay a Ghost Reference of that specific version.
