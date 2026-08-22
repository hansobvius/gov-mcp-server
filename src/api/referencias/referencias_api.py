from typing import Any, Dict, List, Optional, Union
from src.api.client import get_request


async def get_referencias_deputados() -> Optional[Dict[str, Any]]:
    """Retorna valores válidos para parâmetros do endpoint /deputados."""
    return await get_request("/referencias/deputados")


async def get_referencias_situacoes_deputado() -> Optional[Dict[str, Any]]:
    """Retorna as possíveis situações de exercício parlamentar de um deputado."""
    return await get_request("/referencias/deputados/codSituacao")


async def get_referencias_tipos_profissao() -> Optional[Dict[str, Any]]:
    """Retorna os códigos e títulos de atividades profissionais usados na Câmara."""
    return await get_request("/referencias/deputados/codTipoProfissao")


async def get_referencias_ufs() -> Optional[Dict[str, Any]]:
    """Retorna as siglas e nomes dos estados e do Distrito Federal."""
    return await get_request("/referencias/uf")


async def get_referencias_tipos_despesa() -> Optional[Dict[str, Any]]:
    """Retorna os tipos de despesas da Cota para Exercício da Atividade Parlamentar."""
    return await get_request("/referencias/deputados/tipoDespesa")


async def get_referencias_eventos() -> Optional[Dict[str, Any]]:
    """Retorna valores válidos para parâmetros do endpoint /eventos."""
    return await get_request("/referencias/eventos")


async def get_referencias_situacoes_evento() -> Optional[Dict[str, Any]]:
    """Retorna as possíveis situações para eventos dos órgãos da Câmara."""
    return await get_request("/referencias/eventos/codSituacaoEvento")


async def get_referencias_tipos_evento() -> Optional[Dict[str, Any]]:
    """Retorna os tipos de eventos realizados na Câmara dos Deputados."""
    return await get_request("/referencias/eventos/codTipoEvento")


async def get_referencias_orgaos() -> Optional[Dict[str, Any]]:
    """Retorna valores válidos para parâmetros do endpoint /orgaos."""
    return await get_request("/referencias/orgaos")


async def get_referencias_situacoes_orgao() -> Optional[Dict[str, Any]]:
    """Retorna as situações em que os órgãos da Câmara podem se encontrar."""
    return await get_request("/referencias/orgaos/codSituacao")


async def get_referencias_tipos_orgao() -> Optional[Dict[str, Any]]:
    """Retorna os tipos de órgãos existentes na Câmara."""
    return await get_request("/referencias/orgaos/codTipoOrgao")


async def get_referencias_proposicoes() -> Optional[Dict[str, Any]]:
    """Retorna valores válidos para parâmetros do endpoint /proposicoes."""
    return await get_request("/referencias/proposicoes")


async def get_referencias_situacoes_proposicao() -> Optional[Dict[str, Any]]:
    """Retorna os possíveis estados de tramitação de uma proposição."""
    return await get_request("/referencias/proposicoes/codSituacao")


async def get_referencias_temas_proposicao() -> Optional[Dict[str, Any]]:
    """Retorna os códigos e descrições dos temas de proposições."""
    return await get_request("/referencias/proposicoes/codTema")


async def get_referencias_tipos_autor() -> Optional[Dict[str, Any]]:
    """Retorna os tipos de entidades que podem ser autoras de proposições."""
    return await get_request("/referencias/proposicoes/codTipoAutor")


async def get_referencias_tipos_tramitacao() -> Optional[Dict[str, Any]]:
    """Retorna os tipos de tramitação de proposições."""
    return await get_request("/referencias/proposicoes/codTipoTramitacao")


async def get_referencias_tipos_proposicao() -> Optional[Dict[str, Any]]:
    """Retorna as siglas e descrições dos tipos de proposições existentes na Câmara."""
    return await get_request("/referencias/proposicoes/siglaTipo")
