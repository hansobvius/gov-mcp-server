import pytest
from unittest.mock import AsyncMock, patch, MagicMock
from src.api.client import get_senado_request, format_params


def test_senado_format_params():
    params = {
        "codigo": 12345,
        "tipos": ["Permanente", "Temporaria"],
        "ativo": True,
        "nulo": None
    }
    formatted = format_params(params)
    assert formatted["codigo"] == 12345
    assert formatted["tipos"] == "Permanente,Temporaria"
    assert formatted["ativo"] == "true"
    assert "nulo" not in formatted


@pytest.mark.asyncio
async def test_get_senado_request_success():
    mock_response = MagicMock()
    mock_response.json.return_value = {"dados": [{"codigo": 1, "nome": "Teste"}]}
    mock_response.raise_for_status = MagicMock()

    mock_client = AsyncMock()
    mock_client.get.return_value = mock_response

    with patch("httpx.AsyncClient") as mock_client_cls:
        mock_client_cls.return_value.__aenter__.return_value = mock_client
        res = await get_senado_request("/senador/lista/atual")

        assert res is not None
        assert "dados" in res
        mock_client.get.assert_called_once()
        args, kwargs = mock_client.get.call_args
        assert "senador/lista/atual" in args[0]
        assert kwargs["headers"]["Accept"] == "application/json"


@pytest.mark.asyncio
async def test_get_senado_request_strips_dadosabertos_prefix():
    mock_response = MagicMock()
    mock_response.json.return_value = {"Colegiado": {}}
    mock_response.raise_for_status = MagicMock()

    mock_client = AsyncMock()
    mock_client.get.return_value = mock_response

    with patch("httpx.AsyncClient") as mock_client_cls:
        mock_client_cls.return_value.__aenter__.return_value = mock_client
        res = await get_senado_request("/dadosabertos/comissao/lista/colegiados")

        assert res is not None
        args, _ = mock_client.get.call_args
        assert args[0] == "https://legis.senado.leg.br/dadosabertos/comissao/lista/colegiados"


@pytest.mark.asyncio
async def test_get_senado_request_error_returns_none():
    mock_client = AsyncMock()
    mock_client.get.side_effect = Exception("Connection error")

    with patch("httpx.AsyncClient") as mock_client_cls:
        mock_client_cls.return_value.__aenter__.return_value = mock_client
        res = await get_senado_request("/endpoint_invalido")
        assert res is None
