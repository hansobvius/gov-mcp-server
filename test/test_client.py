import pytest
from src.api.client import format_params, get_request


def test_format_params_empty():
    assert format_params(None) == {}
    assert format_params({}) == {}


def test_format_params_lists_and_filtering():
    params = {
        "id": [1, 2, 3],
        "nome": "eduardo",
        "siglaUf": ("SP", "RJ"),
        "vazio": None,
        "bool_val": True,
        "int_zero": 0
    }
    formatted = format_params(params)
    assert formatted["id"] == "1,2,3"
    assert formatted["nome"] == "eduardo"
    assert formatted["siglaUf"] == "SP,RJ"
    assert "vazio" not in formatted
    assert formatted["bool_val"] == "true"
    assert formatted["int_zero"] == 0


@pytest.mark.asyncio
async def test_get_request_live():
    # Test simple live endpoint
    res = await get_request("/referencias/uf")
    assert res is not None
    assert "dados" in res
    assert len(res["dados"]) >= 27
