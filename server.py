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
rapid_api_key = os.getenv("RAPID_API_KEY")

__rapidapi_url__ = 'https://rapidapi.com/particle-media-particle-media-default/api/aigeon-web-search'

mcp = FastMCP('nbot_search')

@mcp.tool()
def nbot_search(query: Annotated[str, Field(description='Search query for nbot answer.')],
                     zipcode: Annotated[Union[str, None], Field(description='The zipcode of the user doing the search.')] = None,
                time_sensitive: Annotated[Union[bool, None], Field(description='The query is time sensitive or not.')] = None):
    '''Search with nbot for news results'''
    url = 'https://aigeon-web-search.p.rapidapi.com/aigeon_search'
    headers = {'x-rapidapi-host': 'aigeon-web-search.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'query': query,
        'zipcode': zipcode,
        'time_sensitive': time_sensitive
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.post(url, headers=headers, json=payload)
    return response.json()


if __name__ == '__main__':
    import sys
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 9997
    mcp.run(transport="stdio")
