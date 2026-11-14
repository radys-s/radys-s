"""Rewrite the activity block in README.md from public GitHub data."""

import json
import os
import re
import urllib.request
from pathlib import Path

USER = "radys-s"
README = Path(__file__).resolve().parent.parent / "README.md"
START, END = "<!-- activity:start -->", "<!-- activity:end -->"


def get(path: str) -> list[dict]:
    request = urllib.request.Request(f"https://api.github.com{path}")
    request.add_header("Accept", "application/vnd.github+json")
    if token := os.environ.get("GITHUB_TOKEN"):
        request.add_header("Authorization", f"Bearer {token}")
    with urllib.request.urlopen(request, timeout=30) as response:
        return json.load(response)


def main() -> None:
    repos = [
        r
        for r in get(f"/users/{USER}/repos?type=owner&sort=pushed&per_page=100")
        if not (r["fork"] or r["archived"] or r["private"]) and r["name"] != USER
    ]
    releases = []
    for repo in repos:
        for release in get(f"/repos/{USER}/{repo['name']}/releases?per_page=1"):
            if not release["draft"]:
                releases.append((release["published_at"], repo["name"], release))

    lines = ["### latest releases", ""]
    for published, name, release in sorted(releases, reverse=True)[:5]:
        tag = " (pre-release)" if release["prerelease"] else ""
        lines.append(
            f"- **{name}** [{release['name'] or release['tag_name']}]({release['html_url']})"
            f"{tag} · {published[:10]}"
        )
    lines += ["", "### recently worked on", ""]
    for repo in repos[:5]:
        description = f" · {repo['description']}" if repo["description"] else ""
        lines.append(f"- [{repo['name']}]({repo['html_url']}){description}")

    text = README.read_text(encoding="utf-8")
    block = f"{START}\n" + "\n".join(lines) + f"\n{END}"
    new = re.sub(re.escape(START) + ".*?" + re.escape(END), lambda _: block, text, flags=re.S)
    if START not in text:
        raise SystemExit("README has no activity markers")
    README.write_text(new, encoding="utf-8")


if __name__ == "__main__":
    main()
