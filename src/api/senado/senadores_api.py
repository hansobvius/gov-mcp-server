from typing import Any, Dict, List, Optional, Union
from src.api.client import get_senado_request


async def get_senadores_atuais() -> Optional[Dict[str, Any]]:
    """Obtém a lista de senadores em exercício no Senado Federal."""
    return await get_senado_request("/senador/lista/atual")


async def get_senadores_afastados() -> Optional[Dict[str, Any]]:
    """Obtém a lista de senadores atualmente afastados do exercício do mandato."""
    return await get_senado_request("/senador/afastados")


async def get_senadores_legislatura(
    legislatura: int,
    legislatura_fim: Optional[int] = None
) -> Optional[Dict[str, Any]]:
    """Obtém a lista de senadores por legislatura ou intervalo de legislaturas.
    
    Args:
        legislatura: Número da legislatura inicial (ex.: 57 para 2023-2027).
        legislatura_fim: Número da legislatura final (opcional).
    """
    if legislatura_fim:
        endpoint = f"/senador/lista/legislatura/{legislatura}/{legislatura_fim}"
    else:
        endpoint = f"/senador/lista/legislatura/{legislatura}"
    return await get_senado_request(endpoint)


async def get_senador_detalhes(codigo: int) -> Optional[Dict[str, Any]]:
    """Obtém a ficha completa de informações e dados cadastrais de um senador.
    
    Args:
        codigo: Código de identificação do senador.
    """
    return await get_senado_request(f"/senador/{codigo}")


async def get_senador_cargos(codigo: int) -> Optional[Dict[str, Any]]:
    """Lista os cargos ocupados pelo parlamentar no Senado e Congresso.
    
    Args:
        codigo: Código de identificação do senador.
    """
    return await get_senado_request(f"/senador/{codigo}/cargos")


async def get_senador_comissoes(codigo: int) -> Optional[Dict[str, Any]]:
    """Lista as comissões e colegiados dos quais o senador é ou foi integrante.
    
    Args:
        codigo: Código de identificação do senador.
    """
    return await get_senado_request(f"/senador/{codigo}/comissoes")


async def get_senador_filiacoes(codigo: int) -> Optional[Dict[str, Any]]:
    """Obtém o histórico de filiações partidárias do senador.
    
    Args:
        codigo: Código de identificação do senador.
    """
    return await get_senado_request(f"/senador/{codigo}/filiacoes")


async def get_senador_historico_academico(codigo: int) -> Optional[Dict[str, Any]]:
    """Obtém o histórico acadêmico e formação do senador.
    
    Args:
        codigo: Código de identificação do senador.
    """
    return await get_senado_request(f"/senador/{codigo}/historicoAcademico")


async def get_senador_licencas(codigo: int) -> Optional[Dict[str, Any]]:
    """Obtém o histórico de licenças solicitadas pelo senador.
    
    Args:
        codigo: Código de identificação do senador.
    """
    return await get_senado_request(f"/senador/{codigo}/licencas")


async def get_senador_mandatos(codigo: int) -> Optional[Dict[str, Any]]:
    """Obtém os mandatos e suplências exercidas pelo senador.
    
    Args:
        codigo: Código de identificação do senador.
    """
    return await get_senado_request(f"/senador/{codigo}/mandatos")


async def get_senador_profissoes(codigo: int) -> Optional[Dict[str, Any]]:
    """Obtém as profissões declaradas pelo senador.
    
    Args:
        codigo: Código de identificação do senador.
    """
    return await get_senado_request(f"/senador/{codigo}/profissao")
