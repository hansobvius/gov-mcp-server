import pytest
from src.api.propositions.propositions_api import (
    get_proposicoes,
    get_propositions_by_id,
    get_proposition_details,
    get_proposition_authors,
    get_proposition_themes,
)


@pytest.mark.asyncio
async def test_get_proposicoes():
    res = await get_proposicoes(siglaTipo="PL", ano=2024, itens=5)
    assert res is not None
    assert "dados" in res
    assert len(res["dados"]) > 0


@pytest.mark.asyncio
async def test_get_proposition_details():
    res = await get_proposicoes(siglaTipo="PL", ano=2024, itens=1)
    assert res is not None and len(res["dados"]) > 0
    prop_id = res["dados"][0]["id"]
    
    details = await get_proposition_details(prop_id)
    assert details is not None
    assert "dados" in details
    assert details["dados"].get("id") == prop_id


@pytest.mark.asyncio
async def test_get_proposition_authors():
    res = await get_proposicoes(siglaTipo="PL", ano=2024, itens=1)
    assert res is not None and len(res["dados"]) > 0
    prop_id = res["dados"][0]["id"]
    
    authors = await get_proposition_authors(prop_id)
    assert authors is not None
    assert "dados" in authors
