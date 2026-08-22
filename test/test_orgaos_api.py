import pytest
from src.api.orgaos.orgaos_api import get_orgaos, get_orgao_details


@pytest.mark.asyncio
async def test_orgaos():
    res = await get_orgaos(sigla="CCJC")
    assert res is not None
    assert "dados" in res
    assert len(res["dados"]) > 0
    
    orgao_id = res["dados"][0]["id"]
    det = await get_orgao_details(orgao_id)
    assert det is not None
    assert "dados" in det
