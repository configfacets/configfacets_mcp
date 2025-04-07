from configfacets.server import ConfigfacetsMCP

mcp_server = ConfigfacetsMCP(
    server="myserver",
    repository="configfacets/core-concepts",
    version="appconfigs",
    api_key="<your api key>",
)
mcp_server.run()
