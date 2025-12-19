# SavePoints

[![Blender Extensions](https://img.shields.io/badge/Blender_Extensions-Available-F5792A?logo=blender&logoColor=white)](https://extensions.blender.org/add-ons/savepoints/)
[![License](https://img.shields.io/github/license/unclepomedev/blender_savepoints)](https://github.com/unclepomedev/blender_savepoints/blob/main/LICENSE)
[![Release Blender Addon](https://github.com/unclepomedev/blender_savepoints/actions/workflows/release.yml/badge.svg)](https://github.com/unclepomedev/blender_savepoints/actions/workflows/release.yml)

<div align="center">
  <strong>
    <a href="#english">English</a> | 
    <a href="#japanese">日本語</a> | 
    <a href="#chinese">中文 (Simplified)</a>
  </strong>
</div>
<br>

<div id="english"></div>

---

SavePoints is a Blender add-on that helps you manage project versions easily. It allows you to create snapshots of your current work with automatic thumbnails, making it simple to browse and restore previous states.

![SavePoints UI Screenshot](resources/fig1.png)

## Features

- **Incremental Saves**: Automatically generates version IDs (v001, v002, etc.) for each save.
- **Visual Previews**: Captures a thumbnail of your viewport for every save point.
- **Detailed Info**: Displays object count and file size for each version.
- **Notes**: Add custom notes to remember what changed in each version.
- **Edit Notes**: Update notes for any version directly from the history list.
- **Easy Restore**: Browse your history in the UI and restore any version with a single click.
- **Rescue Assets**: Easily append objects from a specific version without opening the full snapshot.
- **Ghost Reference**: Overlay a previous version as a wireframe in the 3D viewport to visually compare changes without switching files.
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
     - `Ctrl + Alt (Opt) + S`: Standard Save (respects "Show Save Dialog" setting).
     - `Ctrl + Alt (Opt) + Shift + S`: Forced Quick Save (always skips dialog).
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
7. **Relinking History**:
   - If the history folder is missing (e.g., after moving the `.blend` file), a **Link Existing History Folder** button will appear.
   - Click it to select and reconnect an existing history folder.
8. **Export Project**:
   - Go to **File > Export > SavePoints Project (.zip)**.
   - This creates a zip file containing your current `.blend` file and its entire history folder.
   - Useful for backups or sharing the project with its version history.
9. **Tagging & Filtering**:
   - Click the tag icon on any version row to assign a tag (Stable, Milestone, etc.).
   - Use the filter dropdown at the top of the list to show only specific tags (e.g., only "Stable" versions).

## ⚠️ Note

Thumbnails are skipped in no-GPU environments, but versioning remains fully functional. (Compatible with headless mode for automation and CI/CD workflows.)

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

## Testing (for developers)

This repository includes an end-to-end (E2E) test script to verify the core functionality of the add-on in a headless Blender environment.

To run the tests:

```bash
just test-blender
```

> **Note**: 
> - Check and configure the `blender_exe` path in `justfile` to match your environment.
> - [Just](https://github.com/casey/just) is required to run the command.

This script verifies typical use cases and ensures the add-on fails safely (at least to the best of the developer's knowledge).

### CI Environment

In addition to local testing on macOS and Windows, these E2E tests are automatically executed on Windows and Linux (Blender 4.2, 4.5, and 5.0) via GitHub Actions.

<div id="japanese"></div>

---

SavePointsは、プロジェクトのバージョン管理をサポートするBlenderアドオンです。
現在の作業状態を、自動生成されるサムネイル付きのスナップショットとして保存し、いつでも簡単に閲覧・復元することができます。

## 主な機能

- **Incremental Saves**: v001, v002... といったバージョンIDを自動生成し保存します。
- **Visual Previews**: セーブポイントごとのビューポートの状態をサムネイル画像として記録します。
- **Detailed Info**: 各バージョンのオブジェクト数やファイルサイズを表示します。
- **Notes**: 各バージョンに「何を変更したか」の **Note**（メモ）を残せます。
- **Edit Notes**: 履歴リストから既存の **Note** を直接編集できます。
- **Easy Restore**: UI上の履歴リストから、ワンクリックで任意のバージョンを復元できます。
- **Rescue Assets**: 過去のファイル全体を開くことなく、特定のバージョンからオブジェクトだけを現在のシーンにインポート（アペンド）できます。
- **Ghost Reference**: 過去のバージョンをワイヤーフレームとして現在のビューポートに重ねて表示し、変更箇所を視覚的に比較できます。
- **Quick Save**: **Note** 入力ダイアログをスキップして即座に保存するオプションがあります。
- **Safe Recovery**: 過去のバージョンをメインファイルとして復元する際、元のファイルを自動的にバックアップします。
- **Auto Save**: 設定した間隔（デフォルト10分）で専用スロットに自動保存を行い、作業の消失を防ぎます。
- **Disk Management**: **Lock** されたバージョンを保護しつつ、古いバージョンを自動削除して履歴サイズを管理できます。
- **Version Protection**: 重要なバージョンを **Lock** することで、自動削除や誤削除を防ぎます。
- **Version Tagging**: バージョンに **Tag**（Stable, Milestone, Experiment, Bug）を付与し、履歴リストをフィルタリングできます。

## 使い方

1. **Installation**: アドオンのzipファイルをBlenderにインストールします。
   [Blender Extensions](https://extensions.blender.org/add-ons/savepoints/) からも入手可能です。
2. **Locate the Panel**: 3Dビューポートの **N-Panel** (サイドバー) にある **SavePoints** タブを開きます。
3. **Save a Version**:
   - **Save Version** ボタンをクリックするか、ショートカットを使用します：
     - `Ctrl + Alt (Opt) + S`: 通常セーブ (設定によりダイアログを表示)。
     - `Ctrl + Alt (Opt) + Shift + S`: 強制クイックセーブ (常にダイアログをスキップ)。
   - **Note** を入力（任意）して確定します。
   - *Tip*: 設定で **"Show Save Dialog"** をオフにすると、標準ショートカットでワンクリック保存が可能になります。
   - `.blend` ファイルと同じ場所に隠しフォルダが作成され、そこに履歴が保存されます。
4. **Restore a Version**:
   - 履歴リストからバージョンを選択します。
   - サムネイル、**Note**、オブジェクト数などを確認できます。
   - **Edit Note**: **Note** 横の鉛筆アイコンをクリックして内容を更新できます。
   - **Rescue Assets**: **Import** アイコンをクリックすると、そのバージョンに含まれるオブジェクトを選択して現在のシーンに追加できます（重いデータの場合は時間がかかることがあります）。
   - **Ghost Reference**: **Ghost** アイコンをクリックすると、そのバージョンのワイヤーフレームがビューポートに重なって表示されます。
   - **Checkout (Restore)** をクリックして、そのバージョンを開きます。
   - **Snapshot Mode** (ビューポートに赤い枠が表示されます) に入ります：
       - **Save as Parent**: このバージョンをメインファイルとして上書き保存します（復元）。
       - **Fork (Save as New)**: 全く新しいプロジェクトとして別名保存します。
       - **Return to Parent**: 変更を保存せずに元のファイルに戻ります。
       - ※復元前のメインファイルは履歴フォルダ内にバックアップされます（例: `.{YourFileName}_history/{YourFileName}.blend.123456.bak`）。
5. **Auto Save**:
   - パネル内でオン/オフと間隔（最短1分）を設定できます。
   - 自動保存は単一の「autosave」スロットを上書きするため、履歴リストを埋め尽くすことはありません。
   - **注**: 処理落ちを防ぐため、自動保存時にはサムネイルは生成されません。
6. **Disk Management & Protection**:
   - **Limit Versions**: Disk Management セクションで有効にすると、最新のN件（デフォルト50）のみを保持し、古いものを自動削除します。
   - **Lock Versions**: リストの **Lock** アイコン（鍵マーク）をクリックすると、そのバージョンは保護され、自動削除や手動削除の対象外になります。
7. **Relinking History**:
   - `.blend` ファイルを移動するなどして履歴フォルダが見つからない場合、**Link Existing History Folder** ボタンが表示されます。既存のフォルダを選択して再接続できます。
8. **Export Project**:
   - **File > Export > SavePoints Project (.zip)** を選択します。
   - 現在の `.blend` ファイルと履歴フォルダ一式をまとめたzipファイルを作成します。バックアップや共有に便利です。
9. **Tagging & Filtering**:
   - リストの **Tag** アイコンをクリックしてタグ（Stable, Milestoneなど）を付与できます。
   - リスト上部の **Filter** ドロップダウンで特定のタグのみを表示できます。

## ⚠️ Note

GPUがない環境ではサムネイル生成はスキップされますが、バージョン管理機能は問題なく動作します。（自動化やCI/CDなどのヘッドレスモードにも対応しています）

### ℹ️ Note regarding Asset Browser

スナップショットは `.blend_snapshot` という独自の拡張子で保存されます。これにより、Blenderがそれらをスキャン対象から除外し、**Asset Browser に重複したアセットが表示されるのを防ぎます**。

*古いバージョンからアップデートされた方へ: 以前の標準 `.blend` 形式で保存されたスナップショットが残っている場合、アセットが重複して表示されることがあります。SavePointsパネルからそれらを削除してライブラリを整理することをお勧めします。*

## ❓ FAQ / Troubleshooting

**Q: アドオンをアンインストールしたら、履歴データは消えますか？**
**A: いいえ、消えません。** SavePointsは独自のデータ形式を使用していません。スナップショットファイル（`.blend_snapshot`）は、拡張子が異なるだけの標準的なBlenderファイルです。

**アドオンなしで手動復元する方法:**
1. プロジェクトファイルの横にある隠し履歴フォルダ（`.{ファイル名}_history`）を開きます。
2. 復元したいバージョンのフォルダ（例: `v005`）を開きます。
3. スナップショットファイル（`snapshot.blend_snapshot`）を別の場所（デスクトップなど）にコピーします。
4. 拡張子を `.blend_snapshot` から `.blend` に書き換えます。
5. 通常通りBlenderで開きます。

<div id="chinese"></div>

---

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
     - `Ctrl + Alt (Opt) + S`: 标准保存 (遵循 "Show Save Dialog" 设置)。
     - `Ctrl + Alt (Opt) + Shift + S`: 强制快速保存 (总是跳过对话框)。
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
   - **Limit Versions**: 在 Disk Management 部分启用 "Limit Versions" 以自动仅保留最新的 N 个版本 (默认 50)，**不包括锁定的版本**。
   - **Lock Versions**: 点击版本旁边的 Lock 图标以保护它。锁定的版本永远不会被自动删除，除非解锁，否则无法手动删除。
7. **Relinking History**:
   - 如果历史文件夹丢失 (例如移动 `.blend` 文件后)，会出现 **Link Existing History Folder** 按钮。点击它以选择并重新连接现有的历史文件夹。
8. **Export Project**:
   - 转到 **File > Export > SavePoints Project (.zip)**。
   - 这将创建一个包含当前 `.blend` 文件及其整个历史文件夹的 zip 文件。
   - 适用于备份或分享带有版本历史的项目。
9. **Tagging & Filtering**:
   - 点击任何版本行上的 tag 图标以分配标签 (Stable, Milestone 等)。
   - 使用列表顶部的过滤器下拉菜单仅显示特定标签 (例如仅 "Stable" 版本)。

## ⚠️ Note

在无 GPU 环境中会跳过缩略图，但版本控制功能仍完全可用。(兼容用于自动化和 CI/CD 的 headless 模式。)

### ℹ️ Note regarding Asset Browser

快照使用自定义的 `.blend_snapshot` 扩展名保存。这可以防止 Blender 扫描它们，确保 **Asset Browser 中不会出现重复的资产**。

*对于从旧版本升级的用户: 保存为标准 `.blend` 文件的旧快照仍可能导致重复。您可以通过 SavePoints 面板安全地删除它们以清理库。*

## ❓ FAQ / Troubleshooting

**Q: 如果我卸载插件，我还能访问我的历史记录吗？**
**A: 可以。** SavePoints 不使用任何专有格式。快照文件 (`.blend_snapshot`) 是具有不同扩展名的标准 Blender 文件。

**在没有插件的情况下手动恢复文件:**
1. 导航到项目文件旁边的隐藏历史文件夹 (名称类似于 `.{YourFileName}_history`)。
2. 打开您要恢复的版本文件夹 (例如 `v005`)。
3. **复制** 快照文件 (`snapshot.blend_snapshot`) 到另一个位置 (例如您的桌面)。
4. 将扩展名从 `.blend_snapshot` **重命名** 为 `.blend`。
5. 在 Blender 中正常打开它。
