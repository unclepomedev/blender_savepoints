# Introduction

**SavePoints** is a visual version control system designed specifically for Blender artists. It replaces the messy habit of "Save As..." with a clean, thumbnail-based history panel.

## Why SavePoints?

Standard incremental saves (e.g., `project_v01.blend`, `project_v02.blend`) have a major problem: **File names don't tell you what the project looks like.**

You often find yourself opening five different files just to find "that one version where the lighting was better." SavePoints solves this by attaching a **thumbnail** and a **note** to every save.

## Core Concepts

### 1. Visual History
Instead of browsing folders, you browse a list inside Blender. Every version shows:
* **Thumbnail**: Instantly recognize the state of your project.
* **Note**: "Fixed UVs", "Changed lighting", "Before applying modifiers".
* **Stats**: Vertex count and file size changes.

### 2. Non-Destructive Workflow
SavePoints keeps your main working file clean. All snapshots are stored in a hidden subfolder adjacent to your `.blend` file.
* **Autosave**: Runs silently in the background without freezing your UI.
* **Safe**: Restoring an old version automatically backs up your current state first.

### 3. "Time Travel" for Objects
Sometimes you don't want to revert the whole scene—you just want **that one chair** you deleted 3 hours ago.
* **Object Recovery**: You can append specific objects from *any* past snapshot directly into your current scene without opening the old file.

### 4. Automatic Timelapse
Since SavePoints captures a screenshot with every save, it can string them together into an MP4 video. This is perfect for sharing your "Work in Progress" on social media.

::: tip 💡 Did you know?
The timelapse feature uses your **current camera view** to render past versions. This means even if you moved the camera around while working, the final timelapse will be smooth and stable!
:::

## Getting Started

Ready to clean up your workflow?

* Go to the [Usage Guide](usage.md) to learn how to install and use the panel.
* Check the [FAQ](faq.md) for limitations and tips.
