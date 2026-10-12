from typing import Any, Dict, List, Optional, Union
from src.api.client import get_senado_request


async def get_votacoes_nominais(
    id_sessao: Optional[int] = None,
    codigo_materia: Optional[int] = None,
    codigo_parlamentar: Optional[int] = None,
    sigla_partido: Optional[str] = None
) -> Optional[Dict[str, Any]]:
    """Consulta os votos nominais de parlamentares no painel eletrônico do Plenário.
    
    Args:
        id_sessao: Identificador da sessão plenária.
        codigo_materia: Código da matéria votada.
        codigo_parlamentar: Código do parlamentar.
        sigla_partido: Sigla do partido político.
    """
    params = {
        "idSessao": id_sessao,
        "codigoMateria": codigo_materia,
        "codigoParlamentar": codigo_parlamentar,
        "siglaPartido": sigla_partido,
    }
    return await get_senado_request("/votacao", params=params)


async def get_votacao_comissao_materia(
    sigla: str,
    numero: int,
    ano: int
) -> Optional[Dict[str, Any]]:
    """Consulta votações de matérias deliberadas em comissões (sem ir a plenário).
    
    Args:
        sigla: Sigla da matéria (ex.: PL, PDL).
        numero: Número da matéria.
        ano: Ano da matéria.
    """
    return await get_senado_request(f"/votacaoComissao/materia/{sigla}/{numero}/{ano}")


async def get_votacao_comissao_parlamentar(codigo_parlamentar: int) -> Optional[Dict[str, Any]]:
    """Consulta o histórico de votações de um parlamentar em comissões do Senado.
    
    Args:
        codigo_parlamentar: Código do parlamentar.
    """
    return await get_senado_request(f"/votacaoComissao/parlamentar/{codigo_parlamentar}")
