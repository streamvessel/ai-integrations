# Stream Vessel plugin

Plugin package for ChatGPT and Codex, connecting to the hosted Stream Vessel MCP server at https://mcp.streamvessel.com.

Work with files and data across your connected services through Stream Vessel. The current MCP tools let you browse storage connections and buckets, find and read objects, inspect usage, and manage files. Available operations depend on the connected service and the access granted by the user.

## Package

- `plugin.json`: portable Agent Plugins manifest and OpenAI listing metadata.
- `mcp.json`: Streamable HTTP connection with OAuth authentication. OAuth endpoints and client registration are discovered from the server.
- [`skills/streamvessel/SKILL.md`](skills/streamvessel/SKILL.md): guidance for exploring connections, finding and inspecting files, and organizing files and data. Portable plugin packages discover this skill from the bundled `skills/` directory.

The server is deployed separately. This repository contains no server code or credentials.

## Test

In ChatGPT Plugins, add a custom MCP server named **Stream Vessel** with the URL `https://mcp.streamvessel.com` and OAuth authentication. Sign in to Stream Vessel and approve the desired access. Install it and test in a new Work chat.

Start with: "List my storage connections and the buckets on each." Test read-only and write access separately, including permission failures. Use disposable objects for any write or deletion tests.

To test the bundled skill, install the full plugin package rather than only adding the MCP server. Try finding a file by name, inspecting a large text file, and planning a folder move. Check that results identify partial searches and that destructive changes stay within the authorized scope.

## Build the submission ZIP

Run from the repository root:

```sh
mkdir -p dist
(cd plugins/streamvessel && zip -r ../../dist/streamvessel-plugin-0.2.0.zip plugin.json mcp.json LICENSE skills)
```

The archive puts both manifests and the license at its root and preserves the `skills/` directory. Before submission, verify OAuth discovery and connection, review the listing URLs and copy, and supply any additional branding and review information required by the portal.

Upload the ZIP through the plugin submission portal, connect the remote MCP server, resolve automated findings, and submit for review. Publication is a separate step after approval.

See the official [packaging guide](https://developers.openai.com/plugins/build/plugins) and [submission guide](https://developers.openai.com/plugins/deploy/submission).

## License

[MIT](LICENSE).

