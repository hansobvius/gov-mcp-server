# Tools package

# Deputados
from .deputies_tools import (
    get_deputies_by_names_tool,
    get_deputies_tool,
    get_deputy_details_tool,
    get_deputy_expenses_tool,
    get_deputy_speeches_tool,
    get_deputy_events_tool,
    get_deputy_fronts_tool,
    get_deputy_history_tool,
    get_deputy_external_mandates_tool,
    get_deputy_occupations_tool,
    get_deputy_organs_tool,
    get_deputy_professions_tool,
    get_legislature_leaders_tool,
    get_legislature_board_tool,
)

# Proposições
from .proposition_tools import (
    get_propositions_by_id_tools,
    get_propositions_tool,
    get_proposition_details_tool,
    get_proposition_authors_tool,
    get_proposition_related_tool,
    get_proposition_themes_tool,
    get_proposition_tramitations_tool,
    get_proposition_votings_tool,
)

# Votações
from .votacoes_tools import (
    get_votacoes_tool,
    get_votacao_details_tool,
    get_votacao_orientacoes_tool,
    get_votacao_votos_tool,
)

# Órgãos
from .orgaos_tools import (
    get_orgaos_tool,
    get_orgao_details_tool,
    get_orgao_events_tool,
    get_orgao_members_tool,
    get_orgao_votings_tool,
)

# Partidos e Blocos
from .partidos_blocos_tools import (
    get_partidos_tool,
    get_partido_details_tool,
    get_partido_lideres_tool,
    get_partido_membros_tool,
    get_blocos_tool,
    get_bloco_details_tool,
    get_bloco_partidos_tool,
)

# Eventos
from .eventos_tools import (
    get_eventos_tool,
    get_evento_details_tool,
    get_evento_deputados_tool,
    get_evento_orgaos_tool,
    get_evento_pauta_tool,
    get_evento_votacoes_tool,
)

# Frentes e Grupos
from .frentes_grupos_tools import (
    get_frentes_tool,
    get_frente_details_tool,
    get_frente_membros_tool,
    get_grupos_tool,
    get_grupo_details_tool,
    get_grupo_historico_tool,
    get_grupo_membros_tool,
)

# Legislaturas
from .legislaturas_tools import (
    get_legislaturas_tool,
    get_legislatura_details_tool,
)

# Referências
from .referencias_tools import (
    get_referencias_ufs_tool,
    get_referencias_deputados_tool,
    get_referencias_situacoes_deputado_tool,
    get_referencias_tipos_profissao_tool,
    get_referencias_tipos_despesa_tool,
    get_referencias_proposicoes_tool,
    get_referencias_tipos_proposicao_tool,
    get_referencias_situacoes_proposicao_tool,
    get_referencias_temas_proposicao_tool,
    get_referencias_tipos_autor_tool,
    get_referencias_tipos_tramitacao_tool,
    get_referencias_eventos_tool,
    get_referencias_tipos_evento_tool,
    get_referencias_situacoes_evento_tool,
    get_referencias_orgaos_tool,
    get_referencias_tipos_orgao_tool,
    get_referencias_situacoes_orgao_tool,
)

__all__ = [
    # Deputados
    "get_deputies_by_names_tool",
    "get_deputies_tool",
    "get_deputy_details_tool",
    "get_deputy_expenses_tool",
    "get_deputy_speeches_tool",
    "get_deputy_events_tool",
    "get_deputy_fronts_tool",
    "get_deputy_history_tool",
    "get_deputy_external_mandates_tool",
    "get_deputy_occupations_tool",
    "get_deputy_organs_tool",
    "get_deputy_professions_tool",
    "get_legislature_leaders_tool",
    "get_legislature_board_tool",
    # Proposições
    "get_propositions_by_id_tools",
    "get_propositions_tool",
    "get_proposition_details_tool",
    "get_proposition_authors_tool",
    "get_proposition_related_tool",
    "get_proposition_themes_tool",
    "get_proposition_tramitations_tool",
    "get_proposition_votings_tool",
    # Votações
    "get_votacoes_tool",
    "get_votacao_details_tool",
    "get_votacao_orientacoes_tool",
    "get_votacao_votos_tool",
    # Órgãos
    "get_orgaos_tool",
    "get_orgao_details_tool",
    "get_orgao_events_tool",
    "get_orgao_members_tool",
    "get_orgao_votings_tool",
    # Partidos e Blocos
    "get_partidos_tool",
    "get_partido_details_tool",
    "get_partido_lideres_tool",
    "get_partido_membros_tool",
    "get_blocos_tool",
    "get_bloco_details_tool",
    "get_bloco_partidos_tool",
    # Eventos
    "get_eventos_tool",
    "get_evento_details_tool",
    "get_evento_deputados_tool",
    "get_evento_orgaos_tool",
    "get_evento_pauta_tool",
    "get_evento_votacoes_tool",
    # Frentes e Grupos
    "get_frentes_tool",
    "get_frente_details_tool",
    "get_frente_membros_tool",
    "get_grupos_tool",
    "get_grupo_details_tool",
    "get_grupo_historico_tool",
    "get_grupo_membros_tool",
    # Legislaturas
    "get_legislaturas_tool",
    "get_legislatura_details_tool",
    # Referências
    "get_referencias_ufs_tool",
    "get_referencias_deputados_tool",
    "get_referencias_situacoes_deputado_tool",
    "get_referencias_tipos_profissao_tool",
    "get_referencias_tipos_despesa_tool",
    "get_referencias_proposicoes_tool",
    "get_referencias_tipos_proposicao_tool",
    "get_referencias_situacoes_proposicao_tool",
    "get_referencias_temas_proposicao_tool",
    "get_referencias_tipos_autor_tool",
    "get_referencias_tipos_tramitacao_tool",
    "get_referencias_eventos_tool",
    "get_referencias_tipos_evento_tool",
    "get_referencias_situacoes_evento_tool",
    "get_referencias_orgaos_tool",
    "get_referencias_tipos_orgao_tool",
    "get_referencias_situacoes_orgao_tool",
]

# Centralized descriptions for agents / UI help
TOOL_DESCRIPTIONS = {
    # Deputados
    "get_deputies_by_names_tool": "Busca deputados pelo nome ou fragmento e enriquece com detalhes cadastrais.",
    "get_deputies_tool": "Busca e lista deputados por nome, estado (UF), partido, legislatura, sexo e período.",
    "get_deputy_details_tool": "Recupera dados cadastrais, biografia e frentes de um deputado pelo ID.",
    "get_deputy_expenses_tool": "Consulta despesas e reembolsos da cota parlamentar (CEAP) de um deputado.",
    "get_deputy_speeches_tool": "Lista os discursos e pronunciamentos de um deputado em plenário ou eventos.",
    "get_deputy_events_tool": "Lista eventos e audiências com a participação prevista ou confirmada do deputado.",
    "get_deputy_fronts_tool": "Lista frentes parlamentares das quais o deputado é integrante.",
    "get_deputy_history_tool": "Histórico de mudanças e status no exercício do mandato parlamentar.",
    "get_deputy_external_mandates_tool": "Outros cargos eletivos exercidos pelo parlamentar fora da Câmara (TSE).",
    "get_deputy_occupations_tool": "Atividades e ocupações profissionais declaradas pelo deputado.",
    "get_deputy_organs_tool": "Órgãos e comissões que o deputado integra ou integrou.",
    "get_deputy_professions_tool": "Profissões declaradas pelo deputado.",
    "get_legislature_leaders_tool": "Líderes, vice-líderes e representantes partidários em uma legislatura.",
    "get_legislature_board_tool": "Composição da Mesa Diretora da Câmara em uma legislatura.",
    # Proposições
    "get_propositions_by_id_tools": "Recupera proposições apresentadas por um determinado autor (deputado).",
    "get_propositions_tool": "Busca proposições (PL, PEC, MPV) por tipo, número, ano, autor, partido, tema e palavras-chave.",
    "get_proposition_details_tool": "Recupera informações detalhadas, ementa e status de uma proposição.",
    "get_proposition_authors_tool": "Lista pessoas e entidades autoras ou signatárias de uma proposição.",
    "get_proposition_related_tool": "Lista proposições relacionadas ou apensadas a uma proposta.",
    "get_proposition_themes_tool": "Lista áreas temáticas vinculadas a uma proposição.",
    "get_proposition_tramitations_tool": "Histórico cronológico de tramitação e despachos de uma proposição.",
    "get_proposition_votings_tool": "Votações ocorridas sobre uma proposição legislativa específica.",
    # Votações
    "get_votacoes_tool": "Lista votações ocorridas na Câmara por período, proposição, evento ou órgão.",
    "get_votacao_details_tool": "Detalhes, aprovação/rejeição e dados oficiais de uma votação.",
    "get_votacao_orientacoes_tool": "Orientações de voto recomendadas pelas bancadas e lideranças.",
    "get_votacao_votos_tool": "Voto nominal (Sim/Não/Abstenção/Obstrução) de cada parlamentar em votação aberta.",
    # Órgãos
    "get_orgaos_tool": "Lista comissões, frentes e outros órgãos da estrutura legislativa da Câmara.",
    "get_orgao_details_tool": "Detalhes cadastrais, tipo e competência de um órgão da Câmara.",
    "get_orgao_events_tool": "Eventos e audiências públicas realizadas por um determinado órgão.",
    "get_orgao_members_tool": "Membros, titulares e suplentes componentes de um órgão legislativo.",
    "get_orgao_votings_tool": "Votações deliberadas em um órgão ou comissão temática.",
    # Partidos e Blocos
    "get_partidos_tool": "Lista de partidos políticos com representação na Câmara.",
    "get_partido_details_tool": "Detalhes cadastrais e liderança de um partido político.",
    "get_partido_lideres_tool": "Líderes e vice-líderes de um partido político.",
    "get_partido_membros_tool": "Deputados filiados a um partido em determinado período/legislatura.",
    "get_blocos_tool": "Lista blocos partidários formados em uma ou mais legislaturas.",
    "get_bloco_details_tool": "Detalhes de um bloco partidário específico.",
    "get_bloco_partidos_tool": "Lista os partidos que compõem um bloco partidário.",
    # Eventos
    "get_eventos_tool": "Busca eventos, reuniões e sessões deliberativas na Câmara.",
    "get_evento_details_tool": "Detalhes de um evento (horário, local, descrição e status).",
    "get_evento_deputados_tool": "Deputados participantes e convidados para o evento.",
    "get_evento_orgaos_tool": "Órgãos responsáveis pela organização do evento.",
    "get_evento_pauta_tool": "Lista de matérias e proposições pautadas no evento.",
    "get_evento_votacoes_tool": "Votações ocorridas durante o evento.",
    # Frentes e Grupos
    "get_frentes_tool": "Lista de frentes parlamentares registradas na Câmara.",
    "get_frente_details_tool": "Detalhes e coordenação de uma frente parlamentar.",
    "get_frente_membros_tool": "Deputados signatários e integrantes de uma frente parlamentar.",
    "get_grupos_tool": "Lista grupos parlamentares de cooperação internacional.",
    "get_grupo_details_tool": "Detalhes de um grupo parlamentar interparlamentar.",
    "get_grupo_historico_tool": "Histórico de alterações e variações de estado de um grupo.",
    "get_grupo_membros_tool": "Membros integrantes de um grupo interparlamentar.",
    # Legislaturas
    "get_legislaturas_tool": "Lista os períodos de legislatura da Câmara dos Deputados.",
    "get_legislatura_details_tool": "Detalhes, datas e informações de uma legislatura.",
    # Referências
    "get_referencias_ufs_tool": "Lista de siglas e nomes das Unidades da Federação (estados e DF).",
    "get_referencias_deputados_tool": "Valores válidos e metadados para parâmetros de deputados.",
    "get_referencias_situacoes_deputado_tool": "Situações possíveis de exercício do mandato parlamentar.",
    "get_referencias_tipos_profissao_tool": "Tabela de profissões e ocupações catalogadas.",
    "get_referencias_tipos_despesa_tool": "Tipos de despesa da cota parlamentar (CEAP).",
    "get_referencias_proposicoes_tool": "Metadados e parâmetros válidos para consulta de proposições.",
    "get_referencias_tipos_proposicao_tool": "Tipos e siglas de proposições existentes (PL, PEC, etc.).",
    "get_referencias_situacoes_proposicao_tool": "Estados e situações de tramitação de proposições.",
    "get_referencias_temas_proposicao_tool": "Áreas temáticas de proposições (Saúde, Economia, etc.).",
    "get_referencias_tipos_autor_tool": "Tipos de autores possíveis de proposições legislativas.",
    "get_referencias_tipos_tramitacao_tool": "Tipos regimentais de tramitação de proposições.",
    "get_referencias_eventos_tool": "Metadados e parâmetros válidos para consulta de eventos.",
    "get_referencias_tipos_evento_tool": "Tipos de eventos legislativos (Sessão, Audiência, etc.).",
    "get_referencias_situacoes_evento_tool": "Situações de eventos (Convocada, Realizada, Cancelada).",
    "get_referencias_orgaos_tool": "Metadados e parâmetros válidos para consulta de órgãos.",
    "get_referencias_tipos_orgao_tool": "Tipos de órgãos legislativos existentes na Câmara.",
    "get_referencias_situacoes_orgao_tool": "Situações de funcionamento de órgãos da Câmara.",
}
