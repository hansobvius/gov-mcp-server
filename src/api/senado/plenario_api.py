from typing import Any, Dict, List, Optional, Union
from src.api.client import get_senado_request


async def get_plenario_agenda_dia(data: str) -> Optional[Dict[str, Any]]:
    """Obtém a agenda do Plenário do Senado Federal para uma data específica.
    
    Args:
        data: Data no formato AAAA-MM-DD.
    """
    return await get_senado_request(f"/plenario/agenda/dia/{data}")


async def get_plenario_agenda_mes(ano_mes: str) -> Optional[Dict[str, Any]]:
    """Obtém a agenda do Plenário do Senado Federal para um mês de referência.
    
    Args:
        ano_mes: Mês no formato AAAA-MM.
    """
    return await get_senado_request(f"/plenario/agenda/mes/{ano_mes}")


async def get_plenario_agenda_cn(data: str) -> Optional[Dict[str, Any]]:
    """Obtém a agenda do Plenário do Congresso Nacional para uma data específica.
    
    Args:
        data: Data no formato AAAA-MM-DD.
    """
    return await get_senado_request(f"/plenario/agenda/cn/{data}")


async def get_plenario_encontro_detalhes(
    codigo: int,
    subrecurso: Optional[str] = None
) -> Optional[Dict[str, Any]]:
    """Obtém detalhes, pauta, resultado ou resumo de uma sessão plenária (encontro).
    
    Args:
        codigo: Código de identificação do encontro plenário.
        subrecurso: Sub-recurso opcional ('pauta', 'resultado', 'resumo').
    """
    if subrecurso:
        endpoint = f"/plenario/encontro/{codigo}/{subrecurso}"
    else:
        endpoint = f"/plenario/encontro/{codigo}"
    return await get_senado_request(endpoint)


async def get_plenario_resultado(data: str) -> Optional[Dict[str, Any]]:
    """Obtém o resultado consolidado das votações da Sessão Plenária do Senado.
    
    Args:
        data: Data da sessão (AAAA-MM-DD).
    """
    return await get_senado_request(f"/plenario/resultado/{data}")


async def get_plenario_resultado_cn(data: str) -> Optional[Dict[str, Any]]:
    """Obtém o resultado consolidado da Sessão Plenária do Congresso Nacional.
    
    Args:
        data: Data da sessão (AAAA-MM-DD).
    """
    return await get_senado_request(f"/plenario/resultado/cn/{data}")


async def get_plenario_resultado_veto(
    codigo: int,
    tipo: str = "veto"
) -> Optional[Dict[str, Any]]:
    """Obtém o resultado de votação nominal de vetos presidenciais.
    
    Args:
        codigo: Código numérico identificador.
        tipo: Tipo de apuração ('veto', 'dispositivo', 'materia').
    """
    endpoint = f"/plenario/resultado/{tipo}/{codigo}"
    return await get_senado_request(endpoint)


async def get_plenario_orientacao_bancada(
    data_sessao: str,
    data_fim: Optional[str] = None
) -> Optional[Dict[str, Any]]:
    """Obtém as orientações de bancada (Sim, Não, Liberado) para votação de matérias no painel.
    
    Args:
        data_sessao: Data da sessão (AAAA-MM-DD).
        data_fim: Data final caso seja consulta por período (opcional).
    """
    if data_fim:
        endpoint = f"/plenario/votacao/orientacaoBancada/{data_sessao}/{data_fim}"
    else:
        endpoint = f"/plenario/votacao/orientacaoBancada/{data_sessao}"
    return await get_senado_request(endpoint)
