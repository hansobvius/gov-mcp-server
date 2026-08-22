import pytest
from src.api.referencias.referencias_api import (
    get_referencias_ufs,
    get_referencias_deputados,
    get_referencias_proposicoes,
    get_referencias_eventos,
    get_referencias_orgaos,
    get_referencias_tipos_despesa,
    get_referencias_tipos_proposicao,
)


@pytest.mark.asyncio
async def test_referencias_ufs():
    res = await get_referencias_ufs()
    assert res is not None
    assert "dados" in res
    siglas = [item.get("sigla") for item in res["dados"]]
    assert "SP" in siglas
    assert "RJ" in siglas
    assert "DF" in siglas


@pytest.mark.asyncio
async def test_referencias_tipos_despesa():
    res = await get_referencias_tipos_despesa()
    assert res is not None
    assert "dados" in res
    assert len(res["dados"]) > 0


@pytest.mark.asyncio
async def test_referencias_tipos_proposicao():
    res = await get_referencias_tipos_proposicao()
    assert res is not None
    assert "dados" in res
    siglas = [item.get("sigla") for item in res["dados"]]
    assert "PL" in siglas
    assert "PEC" in siglas
