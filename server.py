import requests
from datetime import datetime
from typing import Union, Literal, List
from mcp.server import FastMCP
from pydantic import Field
from typing import Annotated
from mcp.server.fastmcp import FastMCP
from fastmcp import FastMCP, Context


import os
from dotenv import load_dotenv
load_dotenv()
nbot_api_key = os.getenv("NBOT_API_KEY")

mcp = FastMCP('nbot_search')

@mcp.tool()
def nbot_search(query: Annotated[str, Field(description='query to search for nbot answer')],
                     zipcode: Annotated[Union[str, None], Field(description='zipcode of the user is doing the search')] = None,
                time_sensitive: Annotated[Union[bool, None], Field(description='time sensitive answer or not')] = None):
    '''Search with nbot for news results'''
    url = 'http://agentsdk.ai/mcp/search'
    headers = {'X-Origin-ID': 'mcp', 'X-API-Key': nbot_api_key}
    payload = {
        'query': query,
        'zipcode': zipcode,
        'time_sensitive': time_sensitive
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()


if __name__ == '__main__':
    import sys
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 9997
    mcp.run(transport="stdio")
