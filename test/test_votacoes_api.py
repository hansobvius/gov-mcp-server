import pytest
from src.api.votacoes.votacoes_api import get_votacoes, get_votacao_details


@pytest.mark.asyncio
async def test_votacoes():
    res = await get_votacoes(itens=5)
    assert res is not None
    assert "dados" in res
    if len(res["dados"]) > 0:
        first_id = res["dados"][0]["id"]
        det = await get_votacao_details(first_id)
        assert det is not None
        assert "dados" in det
