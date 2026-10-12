# Ferramentas MCP do Senado Federal
from .senadores_tools import (
    get_senadores_atuais_tool,
    get_senadores_afastados_tool,
    get_senadores_legislatura_tool,
    get_senador_detalhes_tool,
    get_senador_cargos_tool,
    get_senador_comissoes_tool,
    get_senador_filiacoes_tool,
    get_senador_historico_academico_tool,
    get_senador_licencas_tool,
    get_senador_mandatos_tool,
    get_senador_profissoes_tool,
)
from .comissoes_tools import (
    get_comissoes_tipos_colegiado_tool,
    get_comissoes_por_tipo_tool,
    get_colegiados_atividade_tool,
    get_comissoes_mistas_tool,
    get_comissao_detalhes_tool,
    get_comissao_agenda_tool,
    get_comissao_cpi_requerimentos_tool,
    get_comissao_reuniao_detalhes_tool,
    get_comissao_documento_ultima_reuniao_tool,
)
from .composicao_tools import (
    get_composicao_mesa_sf_tool,
    get_composicao_mesa_cn_tool,
    get_liderancas_tool,
    get_liderancas_tipos_tool,
    get_partidos_senado_tool,
    get_blocos_senado_tool,
    get_bloco_senado_detalhes_tool,
    get_composicao_comissao_tool,
    get_composicao_comissao_mista_atual_tool,
    get_composicao_comissao_mista_historica_tool,
)
from .processos_tools import (
    get_processos_senado_tool,
    get_processo_detalhes_senado_tool,
    get_processo_documentos_senado_tool,
    get_processo_emendas_senado_tool,
    get_processo_referencias_senado_tool,
)
from .plenario_votacoes_tools import (
    get_plenario_agenda_dia_tool,
    get_plenario_agenda_cn_tool,
    get_plenario_encontro_detalhes_tool,
    get_plenario_resultado_tool,
    get_plenario_resultado_veto_tool,
    get_plenario_orientacao_bancada_tool,
    get_votacoes_nominais_senado_tool,
    get_votacao_comissao_materia_tool,
    get_votacao_comissao_parlamentar_tool,
)
from .discursos_tools import (
    get_senador_discursos_tool,
    get_senador_apartes_tool,
    get_discurso_texto_integral_tool,
    get_plenario_discursos_periodo_tool,
    get_taquigrafia_notas_tool,
    get_taquigrafia_videos_tool,
)
from .legislacao_orcamento_tools import (
    get_legislacao_lista_senado_tool,
    get_legislacao_detalhes_senado_tool,
    get_legislacao_tipos_norma_tool,
    get_legislacao_termos_tool,
    get_orcamento_emendas_senado_tool,
    get_orcamento_oficios_senado_tool,
)

SENADO_TOOL_DESCRIPTIONS = {
    # Senadores
    "get_senadores_atuais_tool": "Lista senadores em exercício no Senado Federal com dados de contato, partido e UF.",
    "get_senadores_afastados_tool": "Lista senadores atualmente afastados do exercício do mandato e seus motivos.",
    "get_senadores_legislatura_tool": "Consulta senadores vinculados a uma legislatura ou intervalo de legislaturas.",
    "get_senador_detalhes_tool": "Obtém ficha cadastral completa, dados pessoais e mandato de um senador.",
    "get_senador_cargos_tool": "Lista todos os cargos ocupados por um senador em comissões e mesas.",
    "get_senador_comissoes_tool": "Lista comissões e colegiados dos quais o senador participa ou participou.",
    "get_senador_filiacoes_tool": "Histórico de filiações partidárias do senador.",
    "get_senador_historico_academico_tool": "Formação acadêmica e graduações declaradas pelo senador.",
    "get_senador_licencas_tool": "Histórico de licenças solicitadas pelo senador.",
    "get_senador_mandatos_tool": "Mandatos, titularidades e suplências exercidas pelo senador.",
    "get_senador_profissoes_tool": "Profissões e ocupações declaradas pelo senador.",
    # Comissões
    "get_comissoes_tipos_colegiado_tool": "Lista tipos de colegiado e comissões no Senado e Congresso.",
    "get_comissoes_por_tipo_tool": "Lista colegiados do Senado por tipo (Permanente, Temporaria, etc.).",
    "get_colegiados_atividade_tool": "Lista todas as comissões e colegiados em atividade no Congresso Nacional.",
    "get_comissoes_mistas_tool": "Lista comissões mistas atuais do Congresso Nacional.",
    "get_comissao_detalhes_tool": "Detalhes cadastrais, competência e contato de uma comissão do Senado.",
    "get_comissao_agenda_tool": "Agenda de reuniões e audiências de comissões por dia, período ou mês.",
    "get_comissao_cpi_requerimentos_tool": "Lista requerimentos apresentados no âmbito de uma CPI.",
    "get_comissao_reuniao_detalhes_tool": "Pauta, local e detalhes completos de uma reunião de comissão.",
    "get_comissao_documento_ultima_reuniao_tool": "Link para documento da última reunião de uma comissão.",
    # Composição
    "get_composicao_mesa_sf_tool": "Composição da Mesa Diretora do Senado Federal.",
    "get_composicao_mesa_cn_tool": "Composição da Mesa Diretora do Congresso Nacional.",
    "get_liderancas_tool": "Lideranças partidárias, de blocos e governo no Senado e Congresso.",
    "get_liderancas_tipos_tool": "Definições e tipos de lideranças legislativas.",
    "get_partidos_senado_tool": "Lista partidos políticos representados no Senado Federal.",
    "get_blocos_senado_tool": "Lista blocos partidários formados no Senado Federal.",
    "get_bloco_senado_detalhes_tool": "Detalhes e senadores membros de um bloco parlamentar.",
    "get_composicao_comissao_tool": "Composição e membros de uma comissão do Senado.",
    "get_composicao_comissao_mista_atual_tool": "Senadores e deputados integrantes de comissão mista do Congresso.",
    "get_composicao_comissao_mista_historica_tool": "Composição histórica resumida de comissão mista por período.",
    # Processos
    "get_processos_senado_tool": "Pesquisa processos legislativos no Senado Federal (rotas modernas /processo/).",
    "get_processo_detalhes_senado_tool": "Detalhes completos de processo legislativo (ementa, autores, relatorias).",
    "get_processo_documentos_senado_tool": "Documentos e pareceres vinculados a processos legislativos.",
    "get_processo_emendas_senado_tool": "Emendas apresentadas a processos legislativos no Senado.",
    "get_processo_referencias_senado_tool": "Tabelas de domínio do processo legislativo (assuntos, classes, siglas, etc.).",
    # Plenário e Votações
    "get_plenario_agenda_dia_tool": "Agenda do Plenário do Senado Federal por dia.",
    "get_plenario_agenda_cn_tool": "Agenda do Plenário do Congresso Nacional (sessão conjunta).",
    "get_plenario_encontro_detalhes_tool": "Detalhes, pauta ou resultado de sessão plenária (encontro).",
    "get_plenario_resultado_tool": "Resultado consolidado das deliberações em sessão plenária.",
    "get_plenario_resultado_veto_tool": "Resultado de votação nominal de Vetos Presidenciais no Congresso.",
    "get_plenario_orientacao_bancada_tool": "Orientações de bancada para votação em plenário.",
    "get_votacoes_nominais_senado_tool": "Votos nominais de senadores registrados no painel eletrônico.",
    "get_votacao_comissao_materia_tool": "Resultado de votações terminativas de matérias em comissões.",
    "get_votacao_comissao_parlamentar_tool": "Votos proferidos por parlamentar em comissões.",
    # Discursos
    "get_senador_discursos_tool": "Discursos e pronunciamentos oficiais proferidos por um senador.",
    "get_senador_apartes_tool": "Apartes e intervenções realizados por um senador.",
    "get_discurso_texto_integral_tool": "Texto integral transcrito de pronunciamento parlamentar.",
    "get_plenario_discursos_periodo_tool": "Discursos em plenário de todos os parlamentares em um período.",
    "get_taquigrafia_notas_tool": "Notas e transcrições taquigráficas de sessão plenária ou reunião.",
    "get_taquigrafia_videos_tool": "Índices e minutagem de vídeos de sessões e reuniões.",
    # Legislação e Orçamento
    "get_legislacao_lista_senado_tool": "Pesquisa normas jurídicas federais (leis, decretos, medidas provisórias).",
    "get_legislacao_detalhes_senado_tool": "Detalhes, ementa e texto integral de norma jurídica federal.",
    "get_legislacao_tipos_norma_tool": "Tabela de tipos de normas jurídicas catalogadas no Senado.",
    "get_legislacao_termos_tool": "Vocabulário controlado e termos de indexação de legislação.",
    "get_orcamento_emendas_senado_tool": "Emendas parlamentares ao Orçamento Geral da União (OGU).",
    "get_orcamento_oficios_senado_tool": "Ofícios de apoio e indicação de emendas orçamentárias (SEDOL).",
}

__all__ = list(SENADO_TOOL_DESCRIPTIONS.keys())
