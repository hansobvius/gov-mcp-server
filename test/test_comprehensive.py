#!/usr/bin/env python3
"""
Comprehensive test suite for the Brazilian Government MCP Server
"""
import asyncio
import sys
import os
import json
import pytest

# Add project root to path so we can import modules
project_root = os.path.join(os.path.dirname(__file__), '..')
sys.path.insert(0, project_root)

from src.config import mcp
from src.api.client import get_request
from src.api.deputies.deputies_api import get_deputados, get_deputy_details
from src.api.propositions.propositions_api import get_proposicoes
from src.api.votacoes.votacoes_api import get_votacoes
from src.api.orgaos.orgaos_api import get_orgaos
from src.api.partidos.partidos_api import get_partidos
from src.api.eventos.eventos_api import get_eventos
from src.api.frentes.frentes_api import get_frentes
from src.api.grupos.grupos_api import get_grupos
from src.api.legislaturas.legislaturas_api import get_legislaturas
from src.api.referencias.referencias_api import get_referencias_ufs
import main


@pytest.mark.asyncio
async def test_all_modules_connectivity():
    """Test connectivity and basic response structure across all domains."""
    checks = [
        ("Deputados", get_deputados(itens=2)),
        ("Proposicoes", get_proposicoes(itens=2)),
        ("Votacoes", get_votacoes(itens=2)),
        ("Orgaos", get_orgaos(itens=2)),
        ("Partidos", get_partidos(itens=2)),
        ("Eventos", get_eventos(itens=2)),
        ("Frentes", get_frentes(itens=2)),
        ("Grupos", get_grupos(itens=2)),
        ("Legislaturas", get_legislaturas(itens=2)),
        ("Referencias", get_referencias_ufs()),
    ]
    for name, coro in checks:
        res = await coro
        assert res is not None, f"Module {name} failed to fetch data"
        assert "dados" in res, f"Module {name} missing 'dados' key"
        assert len(res["dados"]) > 0, f"Module {name} returned empty 'dados'"


@pytest.mark.asyncio
async def test_fastmcp_tools_completeness():
    """Verify all 70 MCP tools are registered and ready."""
    tools = await mcp.list_tools()
    assert len(tools) == 70, f"Expected 70 tools, found {len(tools)}"


def test_manifest_validation():
    """Validate manifest.json schema and metadata."""
    manifest_path = os.path.join(os.path.dirname(__file__), '..', 'manifest.json')
    with open(manifest_path, 'r', encoding='utf-8') as f:
        manifest = json.load(f)
    assert manifest.get("name") == "gov-mcp-server"
