from typing import Any, Dict, List, Optional, Union
from src.api.client import get_request


async def get_legislaturas(
    id: Optional[Union[int, List[int], str]] = None,
    data: Optional[str] = None,
    pagina: Optional[int] = 1,
    itens: Optional[int] = 15,
    ordem: str = "DESC",
    ordenarPor: str = "id"
) -> Optional[Dict[str, Any]]:
    """Consulta e lista os períodos de mandatos e atividades legislativas da Câmara."""
    params = {
        "id": id,
        "data": data,
        "pagina": pagina,
        "itens": itens,
        "ordem": ordem,
        "ordenarPor": ordenarPor
    }
    return await get_request("/legislaturas", params=params)


async def get_legislatura_details(legislatura_id: int) -> Optional[Dict[str, Any]]:
    """Retorna dados detalhados e datas de início/fim de uma legislatura."""
    return await get_request(f"/legislaturas/{legislatura_id}")
