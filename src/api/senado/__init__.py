# APIs do Senado Federal
from .senadores_api import (
    get_senadores_atuais,
    get_senadores_afastados,
    get_senadores_legislatura,
    get_senador_detalhes,
    get_senador_cargos,
    get_senador_comissoes,
    get_senador_filiacoes,
    get_senador_historico_academico,
    get_senador_licencas,
    get_senador_mandatos,
    get_senador_profissoes,
)
from .comissoes_api import (
    get_comissoes_tipos_colegiado,
    get_comissoes_por_tipo,
    get_colegiados_atividade,
    get_comissoes_mistas,
    get_comissao_detalhes,
    get_comissao_agenda,
    get_comissao_cpi_requerimentos,
    get_comissao_reuniao_detalhes,
    get_comissao_documento_ultima_reuniao,
)
from .composicao_api import (
    get_composicao_mesa_sf,
    get_composicao_mesa_cn,
    get_liderancas_tipos,
    get_liderancas_tipos_unidade,
    get_liderancas,
    get_partidos_senado,
    get_blocos_senado,
    get_bloco_senado_detalhes,
    get_composicao_comissao,
    get_composicao_comissao_mista_atual,
    get_composicao_comissao_mista_historica,
)
from .processos_api import (
    get_processos,
    get_processo_detalhes,
    get_processo_documentos,
    get_processo_emendas,
    get_processo_referencias,
)
from .plenario_api import (
    get_plenario_agenda_dia,
    get_plenario_agenda_mes,
    get_plenario_agenda_cn,
    get_plenario_encontro_detalhes,
    get_plenario_resultado,
    get_plenario_resultado_cn,
    get_plenario_resultado_veto,
    get_plenario_orientacao_bancada,
)
from .votacoes_api import (
    get_votacoes_nominais,
    get_votacao_comissao_materia,
    get_votacao_comissao_parlamentar,
)
from .discursos_api import (
    get_senador_discursos,
    get_senador_apartes,
    get_discurso_texto_integral,
    get_plenario_discursos_periodo,
    get_taquigrafia_notas,
    get_taquigrafia_videos,
)
from .legislacao_api import (
    get_legislacao_lista,
    get_legislacao_detalhes,
    get_legislacao_tipos_norma,
    get_legislacao_termos,
    get_legislacao_classes,
)
from .orcamento_api import (
    get_orcamento_emendas,
    get_orcamento_oficios,
)

__all__ = [
    # Senadores
    "get_senadores_atuais",
    "get_senadores_afastados",
    "get_senadores_legislatura",
    "get_senador_detalhes",
    "get_senador_cargos",
    "get_senador_comissoes",
    "get_senador_filiacoes",
    "get_senador_historico_academico",
    "get_senador_licencas",
    "get_senador_mandatos",
    "get_senador_profissoes",
    # Comissões
    "get_comissoes_tipos_colegiado",
    "get_comissoes_por_tipo",
    "get_colegiados_atividade",
    "get_comissoes_mistas",
    "get_comissao_detalhes",
    "get_comissao_agenda",
    "get_comissao_cpi_requerimentos",
    "get_comissao_reuniao_detalhes",
    "get_comissao_documento_ultima_reuniao",
    # Composição
    "get_composicao_mesa_sf",
    "get_composicao_mesa_cn",
    "get_liderancas_tipos",
    "get_liderancas_tipos_unidade",
    "get_liderancas",
    "get_partidos_senado",
    "get_blocos_senado",
    "get_bloco_senado_detalhes",
    "get_composicao_comissao",
    "get_composicao_comissao_mista_atual",
    "get_composicao_comissao_mista_historica",
    # Processos
    "get_processos",
    "get_processo_detalhes",
    "get_processo_documentos",
    "get_processo_emendas",
    "get_processo_referencias",
    # Plenário
    "get_plenario_agenda_dia",
    "get_plenario_agenda_mes",
    "get_plenario_agenda_cn",
    "get_plenario_encontro_detalhes",
    "get_plenario_resultado",
    "get_plenario_resultado_cn",
    "get_plenario_resultado_veto",
    "get_plenario_orientacao_bancada",
    # Votações
    "get_votacoes_nominais",
    "get_votacao_comissao_materia",
    "get_votacao_comissao_parlamentar",
    # Discursos
    "get_senador_discursos",
    "get_senador_apartes",
    "get_discurso_texto_integral",
    "get_plenario_discursos_periodo",
    "get_taquigrafia_notas",
    "get_taquigrafia_videos",
    # Legislação
    "get_legislacao_lista",
    "get_legislacao_detalhes",
    "get_legislacao_tipos_norma",
    "get_legislacao_termos",
    "get_legislacao_classes",
    # Orçamento
    "get_orcamento_emendas",
    "get_orcamento_oficios",
]
