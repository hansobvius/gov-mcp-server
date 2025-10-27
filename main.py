#!/usr/bin/env python3
"""
MCP Server para buscar informações sobre o congresso brasileiro
Consolidated version with all functionality in a single file
"""

import json
import httpx
import sys
from typing import Any, Dict
from mcp.server.fastmcp import FastMCP

# Constants
URL_BASE_API = "https://dadosabertos.camara.leg.br/api/v2"

# Initialize MCP server
mcp = FastMCP("gov-mcp-server")


# API Functions
async def get_deputados_by_name(name: str) -> Dict[str, Any] | None:
    """Busca deputados pelo nome na API da Câmara dos Deputados"""
    async with httpx.AsyncClient() as client:
        try:
            params = {
                "nome": name,
                "ordem": "ASC",
                "ordenarPor": "nome"
            }
            response = await client.get(
                f"{URL_BASE_API}/deputados",
                params=params,
                timeout=30.0)

            response.raise_for_status()
            data = response.json()

            deputies_list = data.get('dados', [])
            if not deputies_list:
                return None  # Return empty result if no deputies found

            # Limit to first 5 deputies to avoid too many API calls
            limited_deputies = deputies_list[:5]
            
            # Get details for limited deputies found
            deputies_details = []
            for deputy in limited_deputies:
                deputy_id = deputy.get('id')
                if deputy_id:
                    try:
                        deputy_details = await get_deputy_details(deputy_id)
                        if deputy_details and 'dados' in deputy_details:
                            deputies_details.append(deputy_details['dados'])
                        else:
                            # If details not found, use basic info from search
                            deputies_details.append(deputy)
                    except Exception as e:
                        # If error getting details, use basic info
                        print(f"Warning: Could not get details for deputy {deputy_id}: {e}", file=sys.stderr)
                        deputies_details.append(deputy)
            
            # Return in the same format as the original API
            return {
                'dados': deputies_details,
                'links': data.get('links', []),
                'metadados': data.get('metadados', {})
            }
        except httpx.RequestError:
            return None


async def get_deputy_details(deputy_id: int) -> Dict[str, Any] | None:
    """Busca detalhes de um deputado específico pelo ID"""
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(f"{URL_BASE_API}/deputados/{deputy_id}", timeout=30.0)
            response.raise_for_status()
            return response.json()
        except httpx.RequestError:
            return None


# MCP Tools
@mcp.tool()
async def get_deputies_by_names_tool(name: str) -> str:
    """Busca deputies pelo nome.
    Args:
        name: Nome ou parte do nome do deputado (ex: eduardo)
    """
    data = await get_deputados_by_name(name=name)
    if data:
        # Return as JSON string
        return json.dumps(data, ensure_ascii=False)
    return json.dumps({"error": "No deputies found", "dados": []})


if __name__ == '__main__':
    mcp.run(transport='stdio')
