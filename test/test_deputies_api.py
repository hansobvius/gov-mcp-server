import pytest
from src.api.deputies.deputies_api import (
    get_deputados,
    get_deputados_by_name,
    get_deputy_details,
    get_deputy_expenses,
    get_deputy_speeches,
)


@pytest.mark.asyncio
async def test_get_deputados_search():
    res = await get_deputados(nome="eduardo", itens=5)
    assert res is not None
    assert "dados" in res
    assert len(res["dados"]) > 0


@pytest.mark.asyncio
async def test_get_deputados_by_name_enriched():
    res = await get_deputados_by_name("eduardo")
    assert res is not None
    assert "dados" in res
    assert len(res["dados"]) > 0


@pytest.mark.asyncio
async def test_get_deputy_details():
    # Use standard known deputy ID
    res = await get_deputados(itens=1)
    assert res is not None and len(res["dados"]) > 0
    deputy_id = res["dados"][0]["id"]
    
    details = await get_deputy_details(deputy_id)
    assert details is not None
    assert "dados" in details
    assert "details" in details["dados"]
