# Stream Vessel AI integrations

Public AI integrations for Stream Vessel: MCP configurations, plugins, skills, and examples for working with S3-compatible storage.

This repository starts with the [Stream Vessel plugin](plugins/streamvessel/README.md) for ChatGPT and Codex. The MCP server is hosted separately at https://mcp.streamvessel.com.

## Repository layout

- `plugins/streamvessel/`: plugin manifest, MCP configuration, documentation, and license.
- Additional skills and examples can be added as they become available.

## Create the public GitHub repository

Run from this repository with GitHub CLI authenticated as `isalexlog` and access to the organization:

```sh
gh repo create streamvessel/ai-integrations --public --source=. --remote=origin --description 'Public AI integrations for Stream Vessel: MCP configurations, plugins, skills, and examples for working with S3-compatible storage.'
git remote set-url origin git@github.com-isalexlog:streamvessel/ai-integrations.git
git push -u origin main
```

Repository creation requires GitHub API authentication. The SSH alias selects the personal account for pushes.

## License

[MIT](LICENSE). This license covers the files in this repository. The hosted service and backend retain their own terms and licenses.
