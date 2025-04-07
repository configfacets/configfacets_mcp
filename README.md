# configfacets_mcp

Configfacets MCP Server

## Install

We recommend using [uv](https://docs.astral.sh/uv/) to manage your Python projects.

```
uv init <repository_name>
cd <repository_name>
```

Then add Configfacets MCP server to your project dependencies

```
uv add "configfacets-mcp"
```

Initialize your MCP server

coreconcepts.py

```
from configfacets.server import ConfigfacetsMCP

mcp_server = ConfigfacetsMCP(
    server="myserver"
    repository="configfacets/core-concepts",
    version="appconfigs",
    api_key="<your apikey>",
)
mcp_server.run()
```

## Build and Publish

```
uv build
uv publish
```

```
{
    "mcpServers": {
        "configfacets": {
            "command": "uv",
            "args": [
                "--directory",
                "<absolute path>/coreconcepts_mcp",
                "run",
                "coreconcepts.py"
            ]
        }
    }
}
```
