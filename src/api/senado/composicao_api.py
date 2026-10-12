from typing import Any, Dict, List, Optional, Union
from src.api.client import get_senado_request


async def get_composicao_mesa_sf() -> Optional[Dict[str, Any]]:
    """Obtém a composição da Mesa Diretora do Senado Federal."""
    return await get_senado_request("/composicao/mesaSF")


async def get_composicao_mesa_cn() -> Optional[Dict[str, Any]]:
    """Obtém a composição da Mesa Diretora do Congresso Nacional."""
    return await get_senado_request("/composicao/mesaCN")


async def get_liderancas_tipos() -> Optional[Dict[str, Any]]:
    """Lista os tipos de lideranças do Senado e Congresso."""
    return await get_senado_request("/composicao/lideranca/tipos")


async def get_liderancas_tipos_unidade() -> Optional[Dict[str, Any]]:
    """Lista os tipos de unidade de lideranças."""
    return await get_senado_request("/composicao/lideranca/tipos-unidade")


async def get_liderancas() -> Optional[Dict[str, Any]]:
    """Obtém as lideranças atuais no Senado Federal e Congresso Nacional."""
    return await get_senado_request("/composicao/lideranca")


async def get_partidos_senado() -> Optional[Dict[str, Any]]:
    """Lista os partidos políticos com representação no Senado (em atividade e extintos)."""
    return await get_senado_request("/composicao/lista/partidos")


async def get_blocos_senado() -> Optional[Dict[str, Any]]:
    """Lista os blocos parlamentares constituídos no Senado Federal."""
    return await get_senado_request("/composicao/lista/blocos")


async def get_bloco_senado_detalhes(codigo: int) -> Optional[Dict[str, Any]]:
    """Obtém a composição detalhada e membros de um bloco parlamentar do Senado.
    
    Args:
        codigo: Código de identificação do bloco.
    """
    return await get_senado_request(f"/composicao/bloco/{codigo}")


async def get_composicao_comissao(codigo: Union[int, str]) -> Optional[Dict[str, Any]]:
    """Obtém a última composição e membros titulares/suplentes de uma comissão do Senado.
    
    Args:
        codigo: Código ou sigla da comissão.
    """
    return await get_senado_request(f"/composicao/comissao/{codigo}")


async def get_composicao_comissao_mista_atual(codigo: Union[int, str]) -> Optional[Dict[str, Any]]:
    """Obtém a composição atual de uma comissão mista do Congresso Nacional.
    
    Args:
        codigo: Código da comissão mista.
    """
    return await get_senado_request(f"/composicao/comissao/atual/mista/{codigo}")


async def get_composicao_comissao_mista_historica(
    codigo: Union[int, str],
    data_inicio: str,
    data_fim: str
) -> Optional[Dict[str, Any]]:
    """Obtém a composição resumida histórica de uma comissão mista por período.
    
    Args:
        codigo: Código da comissão mista.
        data_inicio: Data inicial (AAAA-MM-DD).
        data_fim: Data final (AAAA-MM-DD).
    """
    return await get_senado_request(f"/composicao/comissao/resumida/mista/{codigo}/{data_inicio}/{data_fim}")
