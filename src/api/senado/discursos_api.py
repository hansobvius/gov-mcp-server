from typing import Any, Dict, List, Optional, Union
from src.api.client import get_senado_request


async def get_senador_discursos(codigo: int) -> Optional[Dict[str, Any]]:
    """Lista discursos proferidos por um senador.
    
    Args:
        codigo: Código de identificação do senador.
    """
    return await get_senado_request(f"/senador/{codigo}/discursos")


async def get_senador_apartes(codigo: int) -> Optional[Dict[str, Any]]:
    """Lista apartes realizados por um senador em discursos de outros colegas.
    
    Args:
        codigo: Código de identificação do senador.
    """
    return await get_senado_request(f"/senador/{codigo}/apartes")


async def get_discurso_texto_integral(codigo_pronunciamento: int) -> Optional[Dict[str, Any]]:
    """Obtém o texto integral de um pronunciamento parlamentar.
    
    Args:
        codigo_pronunciamento: Código do pronunciamento.
    """
    return await get_senado_request(f"/discurso/texto-integral/{codigo_pronunciamento}")


async def get_plenario_discursos_periodo(data_inicio: str, data_fim: str) -> Optional[Dict[str, Any]]:
    """Lista os discursos de todos os parlamentares em plenário em um intervalo de datas.
    
    Args:
        data_inicio: Data inicial (AAAA-MM-DD).
        data_fim: Data final (AAAA-MM-DD).
    """
    return await get_senado_request(f"/plenario/lista/discursos/{data_inicio}/{data_fim}")


async def get_taquigrafia_notas(
    id_origem: int,
    tipo: str = "sessao"
) -> Optional[Dict[str, Any]]:
    """Obtém as notas taquigráficas de uma sessão plenária ou reunião.
    
    Args:
        id_origem: Identificador da sessão ou reunião.
        tipo: 'sessao' ou 'reuniao'. Padrão: 'sessao'.
    """
    return await get_senado_request(f"/taquigrafia/notas/{tipo}/{id_origem}")


async def get_taquigrafia_videos(
    id_origem: int,
    tipo: str = "sessao"
) -> Optional[Dict[str, Any]]:
    """Obtém as unidades descritivas e índices de vídeos de uma sessão ou reunião.
    
    Args:
        id_origem: Identificador da sessão ou reunião.
        tipo: 'sessao' ou 'reuniao'. Padrão: 'sessao'.
    """
    return await get_senado_request(f"/taquigrafia/videos/{tipo}/{id_origem}")
