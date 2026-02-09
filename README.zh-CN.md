<div align="center">
  <strong>
    <a href="README.md">English</a> | 
    <a href="README.ja.md">日本語</a> | 
    中文 (Simplified)
  </strong>
</div>
<br>

<div id="chinese"></div>

---

**保存是为了恢复。**

SavePoints 是一个版本控制系统，它为快速恢复提供了可视化的用户体验，同时还具有延时摄影功能，让保存变得更有趣。

## Why SavePoints?

- **📸 Visual Versioning**: 通过自动缩略图确切查看每个版本的样子。
- **🎬 Timelapse**: 使用**当前相机角度**批量渲染历史记录。创建作品的演变视频。
- **⚡ Shortcuts**: 在记录和速度之间选择。使用快捷键保存并添加备注，或立即强制保存（添加 `Shift`）以跳过对话框。
- **👻 Ghost Overlay**: 在视口中以线框形式叠加以前的版本，以便即时比较更改。
- **📦 Retrieve Objects**: 需要 3 小时前删除的模型吗？无需打开文件即可从任何快照追加对象。（右键单击任何对象以检查其特定时间线。）
- **🏷️ Tags**: 将版本标记为 "Stable" 或 "Milestone" 以保持历史记录井井有条。
- **🛡️ Safe & Clean**: 自动保存在后台运行，不会弄乱您的列表。恢复版本会自动备份您的当前状态——零数据丢失。

## Table of Contents

- [使用方法 (Usage)](#使用方法-usage)
- [注意事项 (Note)](#-注意事项-note)
  - [批量渲染限制](#批量渲染限制)
  - [对象历史记录限制 (Object History Limitations)](#对象历史记录限制-object-history-limitations)
  - [一般注意事项](#一般注意事项)
- [FAQ / 故障排除](#-faq--故障排除)

## 使用方法 (Usage)

1.  **Installation (安装)**: 在 Blender 中安装插件 zip 文件。
    它已在 Blender Extensions 上发布，因此您可以从 [那里](https://extensions.blender.org/add-ons/savepoints/) 获取。
2.  **Locate the Panel (找到面板)**: 打开 3D 视口并在 N-Panel (侧边栏) 中找到 **SavePoints** 选项卡。
3.  **Save a Version (保存版本)**:
    * 点击 **Save Version** 或使用快捷键：
        * `Ctrl/Cmd + Alt (Opt) + S`: 标准保存 (遵循 "Show Save Dialog" 设置)。
        * `Ctrl/Cmd + Alt (Opt) + Shift + S`: 强制快速保存 (总是跳过对话框)。
    * 输入备注 (可选) 并确认。
    * *提示*: 在设置中禁用 **"Show Save Dialog"** 可使用标准快捷键一键保存。
    * 新版本将创建在 `.blend` 文件旁边的隐藏历史文件夹中。
4.  **Restore a Version (恢复版本)**:
    * 从历史列表中选择一个版本。
    * 查看缩略图、备注、对象数量和文件大小。
    * **Edit Note**: 点击备注旁边的铅笔图标以更新它。
    * **Retrieve Objects**: 点击 Import 图标以浏览并将该版本中的对象追加 (append) 到当前场景。
    * **Ghost Reference**: 点击 Ghost 图标以在视口中切换该版本的线框叠加。用于比较更改。
    * 点击 **Checkout (Restore)** 打开该版本。
    * 您现在处于 **Snapshot Mode (快照模式)** (视口中显示红色边框)：
        * **Save as Parent**: 将此版本恢复为主文件（覆盖原文件）。
        * **Fork (Save as New)**: 将此快照另存为一个全新的项目。
          * **选项**: 您可以在弹窗中启用 **"Detach from Library"**。这会将所有链接数据（对象、材质）转换为本地数据并清除资产标记，确保新文件完全独立，不会污染您的资产浏览器。
        * **Return to Parent**: 返回原始文件而不保存更改。
        * 之前的主文件备份将保存在历史文件夹中 (例如 `.{YourFileName}_history/{YourFileName}.blend.123456.bak`)。
5.  **Auto Save (自动保存)**:
    * 直接在面板中配置自动保存设置。
    * 开启/关闭并设置间隔 (最少 1 分钟)。
    * 自动保存会覆盖单个 "autosave" 插槽，因此您的历史列表不会变得混乱。
    * **注意**: 自动保存不会生成缩略图以避免渲染中断。
    * **Safety Mode (安全模式)**: 为防止崩溃和中断，当您处于交互模式（例如雕刻、权重绘制）或正在渲染时，自动保存将被 **跳过**。保存操作会被推迟，并在您退出这些模式后立即自动执行。
6.  **Disk Management & Protection (磁盘管理与保护)**:
    * **Snapshot Compression**: 在常规设置中默认启用。保持开启以节省磁盘空间；如果您优先考虑最大保存速度而不是文件大小，请将其关闭。
    * **Limit Versions**: 在 Disk Management 部分启用 "Limit Versions" 以自动仅保留最新的 N 个版本 (默认 50)，**不包括锁定的版本**。
    * **Lock Versions**: 点击版本旁边的 Lock 图标以保护它。锁定的版本永远不会被自动删除；除非解锁，否则无法手动删除。
    * 保存新版本或刷新列表时，会自动触发旧版本的清理操作。
7.  **Relinking History (重新链接历史记录)**:
    * 如果历史文件夹丢失 (例如移动 `.blend` 文件后)，会出现 **Link Existing History Folder** 按钮。
    * 点击它以选择并重新连接现有的历史文件夹。
    * **请注意：选中的源文件夹将被移动到当前位置，并从原始路径中删除。**
8.  **Export Project (导出项目)**:
    * 转到 **File > Export > SavePoints Project (.zip)**。
    * 这将创建一个包含当前 `.blend` 文件及其整个历史文件夹的 zip 文件。
    * 适用于备份或分享带有版本历史的项目。
9.  **Tagging & Filtering (标签与筛选)**:
    * 点击任何版本行上的 tag 图标以分配标签 (Stable, Milestone 等)。
    * 使用列表顶部的过滤器下拉菜单仅显示特定标签 (例如仅 "Stable" 版本)。
10. **Batch Rendering & Timelapse (批量渲染与延时摄影)**:
    * **进入批量模式**: 勾选历史列表右上角的复选框。
    * **选择版本**: 勾选要渲染的版本。（结合使用过滤器和 "Select All" 可以快速选择所有 "Stable" 版本）。
    * **配置输出**: 选择 **SCENE**（使用当前渲染设置）、**PNG** 或 **JPEG**。
    * **开始渲染**: 点击 **Batch Render Selected**。
        * *注意*: 渲染器会将您**当前场景的摄像机、世界环境和渲染设置**应用到过去的版本。
        * **延时摄影设置**: 在对话框中勾选 **Create Timelapse MP4** 以生成视频文件。启用 **Burn-in Version ID** 可以将版本名称 (例如 v001) 叠加在视频上，并可选择其角落位置。
        * **试运行 (Dry Run)**: 勾选 **"Dry Run"** 以渲染快速低质量预览（25% 分辨率，1 个采样）。
        * **即时最终渲染**: 按住 `Shift` + 点击按钮以**跳过对话框**并立即使用当前设置开始最终渲染。
        * **取消**: 在处理过程中随时按 `ESC` 键中止。
    * **自动延时摄影**: 完成后，会自动创建一个名为 `..._Timelapse` 的新场景，其中所有图像都已导入视频序列编辑器 (VSE) 以便立即播放。
    * **输出位置**: 文件保存在 `//renders_batch/{BlendName}_{Timestamp}/`。
11. **Object History (对象历史)**:
    - 在 3D 视图中右键单击任何对象，然后选择 **Show Object History**。
    - 弹出窗口将列出检测到的更改：**Created** (创建)、**Moved** (移动)、**Minor** (形状更改) 或 **Major** (顶点数更改)。
    - **Show All Versions**: 开启列表右上角的开关，即可列出包含该对象的所有快照（显示为 **Record**），即使未检测到更改。这对于查看雕刻等内部变形非常有用。
    - **点击条目** 以将该特定版本的形状作为 **Ghost** (线框) 叠加在当前视图中。
12. **Background GLB Export (后台 GLB 导出)**:
    - *Note*: 此功能是可选的。请在插件首选项中启用 **"Enable Background GLB Export"** 以解锁此功能。
    - **选择目标对象**: 在当前场景中选择对象。SavePoints 使用它们的 **名称** 来识别需要从过去版本中导出的对象。
    - **选择版本**: 单击列表中的某个版本。
    - **导出**:
        - 在版本详细信息面板（Checkout 按钮下方）中设置 **Export Path (导出路径)**。
        - 点击 **Export GLB**。
    - 导出在后台运行，您可以继续工作。
    - **错误日志**: 如果导出失败，日志将输出到 Blender 文本编辑器中的 **`SavePoints_Log.txt`**。
13. **Post-Save Command (保存后命令)**:
    - *注意*: 此功能为可选功能。请在插件首选项 > Automation 中启用 **"Enable Post-Save Command"**。
    - **自动化**: 在创建快照后立即在后台执行 Shell 命令。
    - **集成**: 支持动态占位符（例如 `{version}`、`{note}`），可与资产管理流程（例如 `dvc push`、云同步或 NAS 备份）无缝集成。
    - **错误日志**: 如果命令失败，日志将输出到 Blender 文本编辑器中的 **`SavePoints_Log.txt`**。

## ⚠️ 注意事项 (Note)

### 批量渲染限制
为了确保最大的稳定性，批量渲染器在 **出厂启动模式 (Factory Startup Mode)** 下运行。
- **支持**: 几何体、着色器、修改器、几何节点。
- **不支持**: 不会加载在渲染时专门生成几何体的第三方插件（例如某些散布工具）。
- **GPU 支持**: 即使在出厂模式下，渲染器也会尝试自动检测并使用您保存的系统首选项 (CUDA/OptiX/Metal)。

### 对象历史记录限制 (Object History Limitations)
对象历史记录功能依赖于轻量级元数据（顶点数、边界框和变换矩阵）以提供即时反馈，而非进行完整的几何分析。
- **内部变形**: 不改变整体边界框或顶点数的网格更改（例如雕刻）默认不会被检测到。如需查看此类更改，请启用 **"Show All Versions"** 开关。
- **重命名**: 历史记录追踪依赖于对象名称。重命名对象将切断其与过去历史记录的链接。
- **检测范围**: 此视图不追踪材质、修改器或自定义属性的更改。

### 一般注意事项
- 在无 GPU 环境中会跳过缩略图，但版本控制功能仍然完全可用。
- **资产浏览器**: 快照使用自定义的 `.blend_snapshot` 扩展名保存。这可以防止 Blender 扫描它们，确保 **您的资产浏览器中不会出现重复的资产**。

*对于从旧版本升级的用户：保存为标准 `.blend` 文件的旧快照仍可能导致重复。您可以放心地通过 SavePoints 面板删除它们以清理库。*

## ❓ FAQ / 故障排除

**Q: 如果我卸载插件，我还能访问我的历史记录吗？**
**A: 可以。** SavePoints 不使用任何专有格式。快照文件 (`.blend_snapshot`) 是具有不同扩展名的标准 Blender 文件。

**在没有插件的情况下手动恢复文件:**
1. 导航到项目文件旁边的隐藏历史文件夹 (名称类似于 `.{YourFileName}_history`)。
2. 打开您要恢复的版本文件夹 (例如 `v005`)。
3. **复制** 快照文件 (`snapshot.blend_snapshot`) 到另一个位置 (例如您的桌面)。
4. 将扩展名从 `.blend_snapshot` **重命名** 为 `.blend`。
5. 在 Blender 中正常打开它。
