# Stream Vessel plugin

Plugin package for ChatGPT and Codex, connecting to the hosted Stream Vessel MCP server at https://mcp.streamvessel.com.

Browse storage connections and buckets, find and read objects, inspect storage usage, and manage objects in S3-compatible storage. Available operations depend on the access granted by the user.

## Package

- `plugin.json`: portable Agent Plugins manifest and OpenAI listing metadata.
- `mcp.json`: Streamable HTTP connection with OAuth authentication. OAuth endpoints and client registration are discovered from the server.

The server is deployed separately. This repository contains no server code or credentials.

## Test

In ChatGPT Plugins, add a custom MCP server named **Stream Vessel** with the URL `https://mcp.streamvessel.com` and OAuth authentication. Sign in to Stream Vessel and approve the desired access. Install it and test in a new Work chat.

Start with: "List my storage connections and the buckets on each." Test read-only and write access separately, including permission failures. Use disposable objects for any write or deletion tests.

## Build the submission ZIP

Run from the repository root:

```sh
mkdir -p dist
zip -j dist/streamvessel-plugin-0.1.0.zip plugins/streamvessel/plugin.json plugins/streamvessel/mcp.json plugins/streamvessel/LICENSE
```

The archive puts both manifests and the license at its root. Before submission, verify OAuth discovery and connection, review the listing URLs and copy, and supply any additional branding and review information required by the portal.

Upload the ZIP through the plugin submission portal, connect the remote MCP server, resolve automated findings, and submit for review. Publication is a separate step after approval.

See the official [packaging guide](https://developers.openai.com/plugins/build/plugins) and [submission guide](https://developers.openai.com/plugins/deploy/submission).

## License

[MIT](LICENSE).

