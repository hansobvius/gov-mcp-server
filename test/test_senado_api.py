import pytest
from unittest.mock import AsyncMock, patch

from src.api.senado.senadores_api import (
    get_senadores_atuais,
    get_senadores_afastados,
    get_senadores_legislatura,
    get_senador_detalhes,
)
from src.api.senado.comissoes_api import (
    get_comissoes_tipos_colegiado,
    get_comissoes_por_tipo,
    get_colegiados_atividade,
    get_comissao_detalhes,
)
from src.api.senado.composicao_api import (
    get_composicao_mesa_sf,
    get_composicao_mesa_cn,
    get_liderancas,
    get_partidos_senado,
    get_blocos_senado,
)
from src.api.senado.processos_api import (
    get_processos,
    get_processo_detalhes,
    get_processo_documentos,
    get_processo_referencias,
)
from src.api.senado.plenario_api import (
    get_plenario_agenda_dia,
    get_plenario_resultado,
    get_plenario_orientacao_bancada,
)
from src.api.senado.votacoes_api import (
    get_votacoes_nominais,
    get_votacao_comissao_materia,
)
from src.api.senado.discursos_api import (
    get_senador_discursos,
    get_discurso_texto_integral,
)
from src.api.senado.legislacao_api import (
    get_legislacao_lista,
    get_legislacao_detalhes,
)
from src.api.senado.orcamento_api import (
    get_orcamento_emendas,
    get_orcamento_oficios,
)


@pytest.mark.asyncio
async def test_senadores_api():
    with patch("src.api.senado.senadores_api.get_senado_request", new_callable=AsyncMock) as mock_get:
        mock_get.return_value = {"ListaParlamentarEmExercicio": {}}
        res = await get_senadores_atuais()
        assert res is not None
        mock_get.assert_called_with("/senador/lista/atual")

        await get_senadores_afastados()
        mock_get.assert_called_with("/senador/afastados")

        await get_senadores_legislatura(57)
        mock_get.assert_called_with("/senador/lista/legislatura/57")

        await get_senadores_legislatura(56, 57)
        mock_get.assert_called_with("/senador/lista/legislatura/56/57")

        await get_senador_detalhes(5988)
        mock_get.assert_called_with("/senador/5988")


@pytest.mark.asyncio
async def test_comissoes_api():
    with patch("src.api.senado.comissoes_api.get_senado_request", new_callable=AsyncMock) as mock_get:
        mock_get.return_value = {"Colegiados": []}
        await get_comissoes_tipos_colegiado()
        mock_get.assert_called_with("/comissao/lista/tiposColegiado")

        await get_comissoes_por_tipo("Permanente")
        mock_get.assert_called_with("/comissao/lista/Permanente")

        await get_colegiados_atividade()
        mock_get.assert_called_with("/comissao/lista/colegiados")

        await get_comissao_detalhes("CCJ")
        mock_get.assert_called_with("/comissao/CCJ")


@pytest.mark.asyncio
async def test_composicao_api():
    with patch("src.api.senado.composicao_api.get_senado_request", new_callable=AsyncMock) as mock_get:
        mock_get.return_value = {"Mesa": []}
        await get_composicao_mesa_sf()
        mock_get.assert_called_with("/composicao/mesaSF")

        await get_composicao_mesa_cn()
        mock_get.assert_called_with("/composicao/mesaCN")

        await get_liderancas()
        mock_get.assert_called_with("/composicao/lideranca")

        await get_partidos_senado()
        mock_get.assert_called_with("/composicao/lista/partidos")

        await get_blocos_senado()
        mock_get.assert_called_with("/composicao/lista/blocos")


@pytest.mark.asyncio
async def test_processos_api():
    with patch("src.api.senado.processos_api.get_senado_request", new_callable=AsyncMock) as mock_get:
        mock_get.return_value = {"Processos": []}
        await get_processos(sigla="PL", ano=2024)
        args, kwargs = mock_get.call_args
        assert args[0] == "/processo"
        assert kwargs["params"]["sigla"] == "PL"
        assert kwargs["params"]["ano"] == 2024

        await get_processo_detalhes(123456)
        mock_get.assert_called_with("/processo/123456")

        await get_processo_documentos(processo_id=123456)
        args, kwargs = mock_get.call_args
        assert args[0] == "/processo/documento"
        assert kwargs["params"]["idProcesso"] == 123456

        await get_processo_referencias("assuntos")
        mock_get.assert_called_with("/processo/assuntos")


@pytest.mark.asyncio
async def test_plenario_and_votacoes_api():
    with patch("src.api.senado.plenario_api.get_senado_request", new_callable=AsyncMock) as mock_get:
        mock_get.return_value = {"Resultado": {}}
        await get_plenario_agenda_dia("2024-05-10")
        mock_get.assert_called_with("/plenario/agenda/dia/2024-05-10")

        await get_plenario_resultado("2024-05-10")
        mock_get.assert_called_with("/plenario/resultado/2024-05-10")

        await get_plenario_orientacao_bancada("2024-05-10")
        mock_get.assert_called_with("/plenario/votacao/orientacaoBancada/2024-05-10")

    with patch("src.api.senado.votacoes_api.get_senado_request", new_callable=AsyncMock) as mock_get:
        mock_get.return_value = {"Votacao": {}}
        await get_votacoes_nominais(codigo_materia=123)
        args, kwargs = mock_get.call_args
        assert args[0] == "/votacao"
        assert kwargs["params"]["codigoMateria"] == 123

        await get_votacao_comissao_materia("PL", 100, 2024)
        mock_get.assert_called_with("/votacaoComissao/materia/PL/100/2024")


@pytest.mark.asyncio
async def test_discursos_legislacao_orcamento_api():
    with patch("src.api.senado.discursos_api.get_senado_request", new_callable=AsyncMock) as mock_get:
        mock_get.return_value = {"Discursos": {}}
        await get_senador_discursos(5988)
        mock_get.assert_called_with("/senador/5988/discursos")

        await get_discurso_texto_integral(999)
        mock_get.assert_called_with("/discurso/texto-integral/999")

    with patch("src.api.senado.legislacao_api.get_senado_request", new_callable=AsyncMock) as mock_get:
        mock_get.return_value = {"Normas": {}}
        await get_legislacao_lista(tipo="LEI", ano=2024)
        args, kwargs = mock_get.call_args
        assert args[0] == "/legislacao/lista"
        assert kwargs["params"]["tipo"] == "LEI"

        await get_legislacao_detalhes(12345)
        mock_get.assert_called_with("/legislacao/12345")

    with patch("src.api.senado.orcamento_api.get_senado_request", new_callable=AsyncMock) as mock_get:
        mock_get.return_value = {"Emendas": {}}
        await get_orcamento_emendas(ano=2024)
        args, kwargs = mock_get.call_args
        assert args[0] == "/orcamento/lista"
        assert kwargs["params"]["ano"] == 2024

        await get_orcamento_oficios("SEDOL123")
        mock_get.assert_called_with("/orcamento/oficios/SEDOL123")
