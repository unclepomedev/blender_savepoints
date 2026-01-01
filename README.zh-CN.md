SavePoints 是一款 Blender 插件，可以帮助您轻松管理项目版本。它允许您为当前工作创建带有自动缩略图的快照，使浏览和恢复以前的状态变得简单。

## Features

- **Incremental Saves**: 每次保存自动生成版本 ID (v001, v002 等)。
- **Visual Previews**: 为每个保存点捕获视口缩略图。
- **Detailed Info**: 显示每个版本的对象数量和文件大小。
- **Notes**: 添加自定义备注以记录每个版本的更改。
- **Edit Notes**: 直接从历史列表中更新任何版本的备注。
- **Easy Restore**: 在 UI 中浏览历史记录，单击即可恢复任何版本。
- **Rescue Assets**: 轻松从特定版本追加 (append) 对象，无需打开完整的快照。
- **Ghost Reference**: 在 3D 视口中以线框形式叠加以前的版本，以便在不切换文件的情况下直观地比较更改。
- **Batch Timelapse**: **(New!)** 自动渲染多个版本以创建演变过程的延时摄影，并支持叠加版本 ID。
- **Context-Aware Rendering**: **(New!)** 将您**当前**的摄像机设置（位置、镜头、移位）、世界环境、色彩管理（AgX/Filmic）以及渲染设置应用于**过去**的快照。
  <br>*(注意：合成节点仍保持快照时的原样。)*
- **Snapshot Compression**: **(New!)** 压缩快照文件的选项。这允许您以稍长的保存时间为代价，显著减小文件大小。（默认：**已启用**）
- **Quick Save**: 跳过备注对话框以立即保存的选项。
- **Safe Recovery**: 安全地用以前的版本覆盖主项目文件。原始文件会自动备份在历史文件夹中。
- **Auto Save**: 按可配置的时间间隔（默认为 10 分钟）自动将您的工作保存到专用插槽，确保您永远不会丢失进度。
- **Disk Management**: 自动删除最旧的版本以保持可管理的历史记录大小，同时保留锁定的版本。
- **Version Protection**: 锁定特定版本以防止它们被自动删除或意外移除。
- **Version Tagging**: 为版本分配标签 (Stable, Milestone, Experiment, Bug) 并筛选历史列表以立即找到重要的快照。

## Usage

1. **Installation**: 在 Blender 中安装插件 zip 文件。
   它已在 Blender Extensions 上发布，因此您可以从 [那里](https://extensions.blender.org/add-ons/savepoints/) 获取。
2. **Locate the Panel**: 打开 3D 视口并在 N-Panel (侧边栏) 中找到 **SavePoints** 选项卡。
3. **Save a Version**:
   - 点击 **Save Version** 或使用快捷键：
     - `Ctrl/Cmd + Alt (Opt) + S`: 标准保存 (遵循 "Show Save Dialog" 设置)。
     - `Ctrl/Cmd + Alt (Opt) + Shift + S`: 强制快速保存 (总是跳过对话框)。
   - 输入备注 (可选) 并确认。
   - *提示*: 在设置中禁用 **"Show Save Dialog"** 可使用标准快捷键一键保存。
   - 新版本将创建在 `.blend` 文件旁边的隐藏历史文件夹中。
4. **Restore a Version**:
   - 从历史列表中选择一个版本。
   - 查看缩略图、备注、对象数量和文件大小。
   - **Edit Note**: 点击备注旁边的铅笔图标以更新它。
   - **Rescue Assets**: 点击 Import 图标以浏览并将该版本中的对象追加 (append) 到当前场景。
   - **Ghost Reference**: 点击 Ghost 图标以在视口中切换该版本的线框叠加。用于比较更改。
   - 点击 **Checkout (Restore)** 打开该版本。
   - 您现在处于 **Snapshot Mode** (视口中显示红色边框)：
       - **Save as Parent**: 将此版本恢复为主文件。
       - **Fork (Save as New)**: 将此快照另存为一个全新的项目。
       - **Return to Parent**: 返回原始文件而不保存更改。
       - 之前的主文件备份将保存在历史文件夹中 (例如 `.{YourFileName}_history/{YourFileName}.blend.123456.bak`)。
5. **Auto Save**:
   - 直接在面板中配置自动保存设置。
   - 开启/关闭并设置间隔 (最少 1 分钟)。
   - 自动保存会覆盖单个 "autosave" 插槽，因此您的历史列表不会变得混乱。
   - **注意**: 自动保存不会生成缩略图以避免渲染中断。
6. **Disk Management & Protection**:
   - **Snapshot Compression**: 在常规设置中默认启用。保持开启以节省磁盘空间，或者如果您优先考虑最大保存速度而不是文件大小，请将其关闭。
   - **Limit Versions**: 在 Disk Management 部分启用 "Limit Versions" 以自动仅保留最新的 N 个版本 (默认 50)，**不包括锁定的版本**。
   - **Lock Versions**: 点击版本旁边的 Lock 图标以保护它。锁定的版本永远不会被自动删除，除非解锁，否则无法手动删除。
   - 保存新版本或刷新列表时，会自动触发旧版本的清理操作。
7. **Relinking History**:
   - 如果历史文件夹丢失 (例如移动 `.blend` 文件后)，会出现 **Link Existing History Folder** 按钮。点击它以选择并重新连接现有的历史文件夹。
   - **请注意：选中的源文件夹将被移动到当前位置，并从原始路径中删除。**
8. **Export Project**:
   - 转到 **File > Export > SavePoints Project (.zip)**。
   - 这将创建一个包含当前 `.blend` 文件及其整个历史文件夹的 zip 文件。
   - 适用于备份或分享带有版本历史的项目。
9. **Tagging & Filtering**:
   - 点击任何版本行上的 tag 图标以分配标签 (Stable, Milestone 等)。
   - 使用列表顶部的过滤器下拉菜单仅显示特定标签 (例如仅 "Stable" 版本)。
10. **Batch Rendering & Timelapse**:
    - **进入批量模式**: 切换历史列表右上角的复选框。
    - **选择版本**: 勾选要渲染的版本。（结合使用过滤器和 "Select All" 可以快速选择所有 "Stable" 版本）。
    - **配置输出**: 选择 **SCENE**（使用当前渲染设置）、**PNG** 或 **JPEG**。
    - **开始渲染**: 点击 **Batch Render Selected**。
      - *注意*: 渲染器会将您**当前场景的摄像机、世界环境和渲染设置**应用到过去的版本。
      - **延时摄影设置**: 在对话框中勾选 **Create Timelapse MP4** 以生成视频文件。启用 **Burn-in Version ID** 可以将版本名称 (例如 v001) 叠加在视频上，并可选择其角落位置。
      - **试运行 (Dry Run)**: 勾选 **"Dry Run"** 以渲染快速低质量预览（25% 分辨率，1 个采样）。
      - **即时最终渲染**: 按住 `Shift` + 点击按钮以**跳过对话框**并立即使用当前设置开始最终渲染。
      - **取消**: 在处理过程中随时按 `ESC` 键中止。
    - **自动延时摄影**: 完成后，会自动创建一个名为 `..._Timelapse` 的新场景，其中所有图像都已导入视频序列编辑器 (VSE) 以便立即播放。
    - **输出位置**: 文件保存在 `//renders_batch/{BlendName}_{Timestamp}/`。

## ⚠️ 注意事项 (Note)

### 批量渲染限制
为了确保最大的稳定性，批量渲染器在 **出厂启动模式 (Factory Startup Mode)** 下运行。
- **支持**: 几何体、着色器、修改器、几何节点。
- **不支持**: 不会加载在渲染时专门生成几何体的第三方插件（例如某些散布工具）。
- **GPU 支持**: 即使在出厂模式下，渲染器也会尝试自动检测并使用您保存的系统首选项 (CUDA/OptiX/Metal)。

### 一般注意事项
- 在无 GPU 环境中会跳过缩略图，但版本控制功能仍然完全可用。
- **资产浏览器**: 快照使用自定义的 `.blend_snapshot` 扩展名保存。这可以防止 Blender 扫描它们，确保 **您的资产浏览器中不会出现重复的资产**。

*对于从旧版本升级的用户：保存为标准 `.blend` 文件的旧快照仍可能导致重复。您可以放心地通过 SavePoints 面板删除它们以清理库。*

## ❓ FAQ / Troubleshooting

**Q: 如果我卸载插件，我还能访问我的历史记录吗？**
**A: 可以。** SavePoints 不使用任何专有格式。快照文件 (`.blend_snapshot`) 是具有不同扩展名的标准 Blender 文件。

**在没有插件的情况下手动恢复文件:**
1. 导航到项目文件旁边的隐藏历史文件夹 (名称类似于 `.{YourFileName}_history`)。
2. 打开您要恢复的版本文件夹 (例如 `v005`)。
3. **复制** 快照文件 (`snapshot.blend_snapshot`) 到另一个位置 (例如您的桌面)。
4. 将扩展名从 `.blend_snapshot` **重命名** 为 `.blend`。
5. 在 Blender 中正常打开它。
