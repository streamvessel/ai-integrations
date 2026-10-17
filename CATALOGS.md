# Where the MCP server is listed

The hosted server is `https://mcp.streamvessel.com` (Streamable HTTP, OAuth). This file records every public catalog that lists it. Update it when a listing goes live or changes.

| Catalog | Status | Listing | How it is maintained |
|---|---|---|---|
| Claude Connectors Directory | Listed | | Anthropic review |
| Official MCP Registry | Listed | [io.github.streamvessel/streamvessel](https://registry.modelcontextprotocol.io/v0/servers?search=io.github.streamvessel/streamvessel) | `server.json` in this repo, published with `mcp-publisher` |
| GitHub MCP registry | Pending | | Reads the official registry |
| PulseMCP | Pending | | Reads the official registry; manual submissions paused |
| ChatGPT plugin directory | Deferred | | Release ZIP from this repo, OpenAI submission portal |
| Smithery | Listed | [stream-vessel/sv-mcp](https://smithery.ai/servers/stream-vessel/sv-mcp) | Smithery account; it scans the live server |
| Glama | Listed | [com.streamvessel.mcp/stream-vessel](https://glama.ai/mcp/connectors/com.streamvessel.mcp/stream-vessel) | Glama account; connector form, claimed via domain or GitHub org |
| mcp.so | Skipped | | Listing a remote server needs a paid submission |
| punkpeye/awesome-remote-mcp-servers | Pending | [PR #2061](https://github.com/punkpeye/awesome-remote-mcp-servers/pull/2061) | Pull request; needs the Glama connector badge and a star on the repo |
| jaw9c/awesome-remote-mcp-servers | Pending | [PR #1357](https://github.com/jaw9c/awesome-remote-mcp-servers/pull/1357) | Pull request |
| mcpservers.org | Submitted | | Free submit form, contact support@streamvessel.com; review within two weeks |
| MCP Market | Skipped | | Remote servers only get the paid listing |
| Cursor Directory | Listed | [stream-vessel](https://cursor.directory/plugins/stream-vessel) | Signed-in submission; verification requested |
| LobeHub | Skipped | | No working submission path |
| Docker MCP Catalog | Pending | [PR #5795](https://github.com/docker/mcp-registry/pull/5795) | Pull request to docker/mcp-registry; sign-in needs `https://mcp.docker.com/oauth/callback` allowed (sv-be #360) |
| Cline MCP Marketplace | Blocked | | Cline signs in through a per-server `vscode://` callback the allowlist does not accept |
| Goose extensions | Skipped | | Lists only locally installed servers |
| punkpeye/awesome-mcp-servers | Skipped | | Remote-only servers belong in awesome-remote-mcp-servers |

## Publishing to the official registry

Bump `version` in `server.json` for every change; the registry never replaces a published version.

```sh
mcp-publisher login github --token "$(gh auth token)"   # needs an owner of the streamvessel org; the device-flow login cannot see org roles (modelcontextprotocol/registry#1649)
mcp-publisher publish
```
