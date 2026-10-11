"""Validate and package the Stream Vessel plugin using the Python standard library."""

import argparse
import json
import os
from pathlib import Path
import re
import zipfile


def build(plugin: Path, output: Path) -> dict[str, str]:
    manifest = json.loads((plugin / "plugin.json").read_text())
    mcp = json.loads((plugin / "mcp.json").read_text())
    version = manifest.get("version", "")
    if not re.fullmatch(r"(0|[1-9]\d*)\.(0|[1-9]\d*)\.(0|[1-9]\d*)", version):
        raise ValueError("Plugin version must be a stable version such as 0.2.1")
    if manifest.get("name") != "streamvessel" or manifest.get("license") != "MIT":
        raise ValueError("Expected the streamvessel plugin with an MIT license")
    if not manifest.get("description", "").strip():
        raise ValueError("Plugin description is required")
    server = mcp["mcpServers"]["streamvessel"]
    if server.get("type") != "streamable-http" or server.get("url") != "https://mcp.streamvessel.com":
        raise ValueError("Unexpected MCP transport or endpoint")
    if server["extensions"]["com.openai"]["auth"].get("type") != "oauth":
        raise ValueError("OAuth authentication is required")

    files = [plugin / name for name in ("plugin.json", "mcp.json", "LICENSE")]
    skills = sorted((plugin / "skills").glob("*/SKILL.md"))
    if not skills:
        raise ValueError("At least one bundled skill is required")
    for skill in skills:
        text = skill.read_text()
        frontmatter = re.match(r"\A---\n(.*?)\n---\n", text, re.DOTALL)
        if not frontmatter:
            raise ValueError(f"Missing skill frontmatter: {skill}")
        fields = dict(re.findall(r"^(name|description):\s*(.+)$", frontmatter[1], re.MULTILINE))
        if fields.get("name") != skill.parent.name or not fields.get("description", "").strip():
            raise ValueError(f"Invalid skill name or description: {skill}")
    files.extend(sorted(path for path in (plugin / "skills").rglob("*") if path.is_file()))
    for path in files:
        if path.is_symlink() or not path.is_file():
            raise ValueError(f"Package files must be regular files: {path}")

    output.mkdir(parents=True, exist_ok=True)
    archive = output / f"streamvessel-plugin-{version}.zip"
    with zipfile.ZipFile(archive, "w", zipfile.ZIP_DEFLATED) as package:
        for path in files:
            package.write(path, path.relative_to(plugin).as_posix())
    return {"version": version, "tag": f"streamvessel-v{version}", "archive": str(archive)}


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--plugin", type=Path, default=Path("plugins/streamvessel"))
    parser.add_argument("--output", type=Path, default=Path("dist"))
    args = parser.parse_args()
    result = build(args.plugin, args.output)
    if os.environ.get("GITHUB_OUTPUT"):
        with open(os.environ["GITHUB_OUTPUT"], "a") as outputs:
            for key, value in result.items():
                outputs.write(f"{key}={value}\n")
    print(f"Built {result['archive']}")
