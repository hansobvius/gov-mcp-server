import pytest
from src.api.eventos.eventos_api import get_eventos, get_evento_details


@pytest.mark.asyncio
async def test_eventos():
    res = await get_eventos(itens=5)
    assert res is not None
    assert "dados" in res
    assert len(res["dados"]) > 0
    
    first_id = res["dados"][0]["id"]
    det = await get_evento_details(first_id)
    assert det is not None
    assert "dados" in det
