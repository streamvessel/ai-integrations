# Stream Vessel plugin

Work with files and data across connected services in ChatGPT and Codex through [Stream Vessel](https://streamvessel.com). The plugin uses the hosted MCP server at `https://mcp.streamvessel.com` with OAuth authentication.

The bundled [skill](skills/streamvessel/SKILL.md) guides connection selection, file discovery and inspection, and file organization. Available operations depend on the service and granted access. Current MCP tools use connections, buckets, object keys, and prefixes.

## Package

- `plugin.json`: plugin identity and listing metadata.
- `mcp.json`: MCP endpoint and OAuth configuration.
- `skills/streamvessel/SKILL.md`: workflow instructions.
- `LICENSE`: MIT license.

## Test

Install the full plugin package to test the skill alongside the MCP tools. Adding only the custom MCP server tests the connection and tools.

Try listing connections, finding a file, sampling a large text file, and planning a folder move. Check partial results and permission failures. Use disposable files for write and deletion tests.

## Build

From the repository root:

```sh
python3 scripts/build_plugin.py
```

The ZIP preserves the skill directory and places the manifests at its root. Verify OAuth, listing details, and any required review information before uploading through the plugin submission portal. Publication follows approval.

## Release

Update the version in `plugin.json`, then open **Actions → Release Stream Vessel plugin → Run workflow** and choose the branch or tag to release. The workflow validates the package, builds the ZIP, and creates a GitHub release named `Stream Vessel <version>` with a `streamvessel-v<version>` tag and the ZIP attached.

Releases are drafts by default. Uncheck **Create a draft release for review** to publish the GitHub release immediately. Existing version tags are never replaced; use a new version for changes. Download the ZIP from the release for submission to the plugin directory. This workflow does not submit or publish the plugin to ChatGPT or Codex.

See the official [packaging guide](https://developers.openai.com/plugins/build/plugins) and [submission guide](https://developers.openai.com/plugins/deploy/submission).

## License

[MIT](LICENSE).
