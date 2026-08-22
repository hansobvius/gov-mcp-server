import json
from typing import Any, Dict, List, Optional, Union
from src.config import mcp
from src.api.legislaturas.legislaturas_api import (
    get_legislaturas,
    get_legislatura_details,
)


def _json_response(data: Optional[Dict[str, Any]], default_empty_key: str = "dados") -> str:
    if data is not None:
        return json.dumps(data, ensure_ascii=False)
    return json.dumps({"error": "Nenhum resultado encontrado", default_empty_key: []}, ensure_ascii=False)


@mcp.tool()
async def get_legislaturas_tool(
    data: Optional[str] = None,
    pagina: int = 1,
    itens: int = 15,
    ordem: str = "DESC",
    ordenar_por: str = "id"
) -> str:
    """Consulta e lista os períodos de legislatura da Câmara dos Deputados (ex.: 57 = 2023-2027).

    Args:
        data: Data no formato AAAA-MM-DD para verificar a legislatura ativa nesse dia.
        pagina: Página de resultados (padrão: 1).
        itens: Quantidade de itens por página (máximo: 100, padrão: 15).
        ordem: Ordenação ("ASC" ou "DESC").
        ordenar_por: Campo de ordenação ("id", "dataInicio", "dataFim").
    """
    data_res = await get_legislaturas(
        data=data,
        pagina=pagina,
        itens=itens,
        ordem=ordem,
        ordenarPor=ordenar_por
    )
    return _json_response(data_res)


@mcp.tool()
async def get_legislatura_details_tool(legislatura_id: int) -> str:
    """Retorna dados detalhados, datas de início, fim e ano de eleição de uma determinada legislatura.

    Args:
        legislatura_id: Número identificador da legislatura (ex.: 57).
    """
    data = await get_legislatura_details(legislatura_id=legislatura_id)
    return _json_response(data)
