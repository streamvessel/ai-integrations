# Where the MCP server is listed

The hosted server is `https://mcp.streamvessel.com` (Streamable HTTP, OAuth). This file records every public catalog that lists it. Update it when a listing goes live or changes.

| Catalog | Status | Listing | How it is maintained |
|---|---|---|---|
| Claude Connectors Directory | Listed | | Anthropic review |
| Official MCP Registry | Pending | | `server.json` in this repo, published with `mcp-publisher` |
| GitHub MCP registry | Pending | | Reads the official registry |
| PulseMCP | Pending | | Reads the official registry; manual submissions paused |
| ChatGPT plugin directory | Pending | | Release ZIP from this repo, OpenAI submission portal |
| Smithery | Listed | [stream-vessel/sv-mcp](https://smithery.ai/servers/stream-vessel/sv-mcp) | Smithery account; it scans the live server |
| Glama | Listed | [com.streamvessel.mcp/stream-vessel](https://glama.ai/mcp/connectors/com.streamvessel.mcp/stream-vessel) | Glama account; connector form, claimed via domain or GitHub org |
| mcp.so | Pending | | Submit form, "Remote Server" |
| punkpeye/awesome-remote-mcp-servers | Pending | | Pull request |
| jaw9c/awesome-remote-mcp-servers | Pending | | Pull request |

## Publishing to the official registry

Bump `version` in `server.json` for every change; the registry never replaces a published version.

```sh
mcp-publisher login github   # account must be a public member of the streamvessel org
mcp-publisher publish
```
