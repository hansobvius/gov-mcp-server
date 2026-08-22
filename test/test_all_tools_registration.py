import pytest
from src.config import mcp
import src.tools as tools
import main


@pytest.mark.asyncio
async def test_tools_registration():
    # Import main ensures all tools are registered on mcp
    assert mcp.name == "gov-mcp-server"
    
    tools_list = await mcp.list_tools()
    registered_tools = {t.name: t for t in tools_list}

    assert len(registered_tools) == 70, f"Expected 70 tools, found {len(registered_tools)}"
    print(f"\nTotal registered MCP tools: {len(registered_tools)}")

    # Check key tools from all modules
    expected_tools = [
        # Deputados
        "get_deputies_by_names_tool",
        "get_deputies_tool",
        "get_deputy_details_tool",
        "get_deputy_expenses_tool",
        "get_deputy_speeches_tool",
        "get_deputy_events_tool",
        "get_deputy_fronts_tool",
        "get_deputy_history_tool",
        "get_deputy_external_mandates_tool",
        "get_deputy_occupations_tool",
        "get_deputy_organs_tool",
        "get_deputy_professions_tool",
        "get_legislature_leaders_tool",
        "get_legislature_board_tool",
        # Proposições
        "get_propositions_by_id_tools",
        "get_propositions_tool",
        "get_proposition_details_tool",
        "get_proposition_authors_tool",
        "get_proposition_related_tool",
        "get_proposition_themes_tool",
        "get_proposition_tramitations_tool",
        "get_proposition_votings_tool",
        # Votações
        "get_votacoes_tool",
        "get_votacao_details_tool",
        "get_votacao_orientacoes_tool",
        "get_votacao_votos_tool",
        # Órgãos
        "get_orgaos_tool",
        "get_orgao_details_tool",
        "get_orgao_events_tool",
        "get_orgao_members_tool",
        "get_orgao_votings_tool",
        # Partidos e Blocos
        "get_partidos_tool",
        "get_partido_details_tool",
        "get_partido_lideres_tool",
        "get_partido_membros_tool",
        "get_blocos_tool",
        "get_bloco_details_tool",
        "get_bloco_partidos_tool",
        # Eventos
        "get_eventos_tool",
        "get_evento_details_tool",
        "get_evento_deputados_tool",
        "get_evento_orgaos_tool",
        "get_evento_pauta_tool",
        "get_evento_votacoes_tool",
        # Frentes e Grupos
        "get_frentes_tool",
        "get_frente_details_tool",
        "get_frente_membros_tool",
        "get_grupos_tool",
        "get_grupo_details_tool",
        "get_grupo_historico_tool",
        "get_grupo_membros_tool",
        # Legislaturas
        "get_legislaturas_tool",
        "get_legislatura_details_tool",
        # Referências
        "get_referencias_ufs_tool",
        "get_referencias_deputados_tool",
        "get_referencias_situacoes_deputado_tool",
        "get_referencias_tipos_profissao_tool",
        "get_referencias_tipos_despesa_tool",
        "get_referencias_proposicoes_tool",
        "get_referencias_tipos_proposicao_tool",
        "get_referencias_situacoes_proposicao_tool",
        "get_referencias_temas_proposicao_tool",
        "get_referencias_tipos_autor_tool",
        "get_referencias_tipos_tramitacao_tool",
        "get_referencias_eventos_tool",
        "get_referencias_tipos_evento_tool",
        "get_referencias_situacoes_evento_tool",
        "get_referencias_orgaos_tool",
        "get_referencias_tipos_orgao_tool",
        "get_referencias_situacoes_orgao_tool",
    ]

    for tool_name in expected_tools:
        assert tool_name in registered_tools, f"Tool '{tool_name}' was not registered on MCP server"
        assert tool_name in tools.TOOL_DESCRIPTIONS, f"Description for '{tool_name}' missing in TOOL_DESCRIPTIONS"
