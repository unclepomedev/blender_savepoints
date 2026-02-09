## ⚠️ Note

### Batch Rendering Limitations
To ensure maximum stability, the batch renderer runs in **Factory Startup Mode**.
- **Supported**: Geometry, Shaders, Modifiers, Geometry Nodes.
- **Not Supported**: Third-party add-ons that generate geometry specifically at render-time (e.g., some scattering tools) will not be loaded.
- **GPU Support**: The renderer attempts to auto-detect and use your saved System Preferences (CUDA/OptiX/Metal) even in factory mode.

### Object History Limitations
The Object History feature relies on lightweight metadata (Vertex Count, Bounding Box, and Transform Matrix) for instant feedback rather than full geometry analysis.
- **Internal Deformations**: Changes that do not alter the bounding box or vertex count (e.g., sculpting on a fixed mesh) will not appear as "Modified" in the default list. **Use the "Show All Versions" toggle** to find these snapshots.
- **Renaming**: History tracking relies on object names. Renaming an object will disconnect it from its past history.
- **Scope**: Changes to Materials, Modifiers, or Custom Properties are not tracked in this view.

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
