from typing import Any, Dict, List, Optional, Union
from src.api.client import get_senado_request


async def get_comissoes_tipos_colegiado() -> Optional[Dict[str, Any]]:
    """Obtém a lista de tipos de colegiado do Senado e Congresso."""
    return await get_senado_request("/comissao/lista/tiposColegiado")


async def get_comissoes_por_tipo(tipo: str) -> Optional[Dict[str, Any]]:
    """Lista de colegiados do Senado Federal por tipo (ex.: Permanente, Temporaria).
    
    Args:
        tipo: Tipo do colegiado.
    """
    return await get_senado_request(f"/comissao/lista/{tipo}")


async def get_colegiados_atividade() -> Optional[Dict[str, Any]]:
    """Obtém a lista geral de colegiados em atividade no Congresso Nacional."""
    return await get_senado_request("/comissao/lista/colegiados")


async def get_comissoes_mistas() -> Optional[Dict[str, Any]]:
    """Obtém a lista de comissões mistas atuais do Congresso Nacional."""
    return await get_senado_request("/comissao/lista/mistas")


async def get_comissao_detalhes(codigo: Union[int, str]) -> Optional[Dict[str, Any]]:
    """Obtém os detalhes cadastrais e finalidade de um colegiado/comissão.
    
    Args:
        codigo: Código ou sigla identificadora da comissão (ex.: CAE, CCJ ou código numérico).
    """
    return await get_senado_request(f"/comissao/{codigo}")


async def get_comissao_agenda(
    data_referencia: Optional[str] = None,
    data_inicio: Optional[str] = None,
    data_fim: Optional[str] = None,
    mes_referencia: Optional[str] = None
) -> Optional[Dict[str, Any]]:
    """Consulta a agenda de reuniões de comissão por data específica, período ou mês.
    
    Args:
        data_referencia: Data específica no formato AAAA-MM-DD.
        data_inicio: Data de início do período no formato AAAA-MM-DD.
        data_fim: Data de término do período no formato AAAA-MM-DD.
        mes_referencia: Mês no formato AAAA-MM.
    """
    if data_inicio and data_fim:
        endpoint = f"/comissao/agenda/{data_inicio}/{data_fim}"
    elif mes_referencia:
        endpoint = f"/comissao/agenda/mes/{mes_referencia}"
    elif data_referencia:
        endpoint = f"/comissao/agenda/{data_referencia}"
    else:
        endpoint = "/comissao/agenda"
    return await get_senado_request(endpoint)


async def get_comissao_cpi_requerimentos(comissao: Union[int, str]) -> Optional[Dict[str, Any]]:
    """Lista requerimentos de uma CPI (Comissão Parlamentar de Inquérito).
    
    Args:
        comissao: Sigla ou código da CPI.
    """
    return await get_senado_request(f"/comissao/cpi/{comissao}/requerimentos")


async def get_comissao_reuniao_detalhes(codigo_reuniao: int) -> Optional[Dict[str, Any]]:
    """Obtém informações detalhadas, pauta e local de uma reunião de comissão.
    
    Args:
        codigo_reuniao: Identificador numérico da reunião.
    """
    return await get_senado_request(f"/comissao/reuniao/{codigo_reuniao}")


async def get_comissao_documento_ultima_reuniao(sigla: str, tipo_documento: str) -> Optional[Dict[str, Any]]:
    """Obtém o link para documento da última reunião de uma comissão.
    
    Args:
        sigla: Sigla da comissão (ex.: CCJ).
        tipo_documento: Tipo de documento desejado.
    """
    return await get_senado_request(f"/comissao/reuniao/{sigla}/documento/{tipo_documento}")
