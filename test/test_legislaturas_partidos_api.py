import pytest
from src.api.legislaturas.legislaturas_api import get_legislaturas, get_legislatura_details
from src.api.partidos.partidos_api import get_partidos
from src.api.blocos.blocos_api import get_blocos


@pytest.mark.asyncio
async def test_legislaturas():
    res = await get_legislaturas(itens=5)
    assert res is not None
    assert "dados" in res
    assert len(res["dados"]) > 0
    # Test details for legislatura 57
    det = await get_legislatura_details(57)
    assert det is not None
    assert "dados" in det
    assert det["dados"].get("id") == 57


@pytest.mark.asyncio
async def test_partidos():
    res = await get_partidos(sigla="PT")
    assert res is not None
    assert "dados" in res
    assert len(res["dados"]) > 0


@pytest.mark.asyncio
async def test_blocos():
    res = await get_blocos(idLegislatura=57)
    assert res is not None
    assert "dados" in res
