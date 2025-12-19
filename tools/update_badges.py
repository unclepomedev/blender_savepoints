import os
import re


def main():
    base_path = "artifacts"

    print("Checking artifacts for badge updates...")
    if not os.path.exists(base_path):
        print(f"Artifacts directory '{base_path}' not found.")
        return

    detected_versions = set()
    for item in os.listdir(base_path):
        if item.startswith("success-"):
            parts = item.split("-")
            if len(parts) >= 3:
                detected_versions.add(parts[-1])

    sorted_versions = sorted(list(detected_versions), key=lambda v: [int(x) for x in v.split('.') if x.isdigit()])

    badges = []
    for ver in sorted_versions:
        linux_key = f"success-Linux-{ver}"
        win_key = f"success-Windows-{ver}"

        linux_path = os.path.join(base_path, linux_key)
        win_path = os.path.join(base_path, win_key)

        linux_ok = os.path.exists(linux_path)
        win_ok = os.path.exists(win_path)

        print(f"Version {ver}: Linux={linux_ok}, Windows={win_ok}")

        if linux_ok and win_ok:
            short_ver = ".".join(ver.split(".")[:2])
            badge = f"[![Blender {short_ver}](https://img.shields.io/badge/Blender-{short_ver}-green?logo=blender&logoColor=white)](https://www.blender.org/download/)"
            badges.append(badge)

    if not badges:
        print("No successful versions found. Badges will be cleared.")
        badge_str = ""
    else:
        badge_str = " ".join(badges)

    readme_path = "README.md"
    if not os.path.exists(readme_path):
        print(f"{readme_path} not found.")
        return

    with open(readme_path, "r", encoding="utf-8") as f:
        content = f.read()

    start_marker = "<!-- BLENDER_BADGES_START -->"
    end_marker = "<!-- BLENDER_BADGES_END -->"

    pattern = re.compile(f"({re.escape(start_marker)}).*?({re.escape(end_marker)})", re.DOTALL)

    if pattern.search(content):
        print("Found badge markers. Updating content.")
        new_content = pattern.sub(f"\\1\n{badge_str}\n\\2", content)

        with open(readme_path, "w", encoding="utf-8") as f:
            f.write(new_content)
        print("README.md updated.")
    else:
        print("Badge markers not found in README.md.")


if __name__ == "__main__":
    main()