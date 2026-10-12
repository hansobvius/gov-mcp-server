# Government MCP Server (Congresso Nacional: Câmara dos Deputados & Senado Federal)

A Model Context Protocol (MCP) server that provides comprehensive access to open legislative data from the Brazilian National Congress: **Chamber of Deputies** ([Dados Abertos v2](https://dadosabertos.camara.leg.br/swagger/api.html)) and **Federal Senate** ([Dados Abertos v3](https://legis.senado.leg.br)).

## Overview

This project implements a bicameral MCP server allowing AI assistants (Claude Desktop, Google Antigravity, Cursor, ChatGPT, etc.) and agentic workflows to query, inspect, and analyze all open legislative data from Brazil's National Congress.

The server covers **126 MCP tools** organized into modular domains with full async support (`httpx`), robust error handling, parameter sanitation, and dual transport modes (`stdio` and `SSE`/`HTTP`).

---

## Architecture & Project Structure

```
gov-mcp-server/
├── Dockerfile                      # Container image definition
├── docker-compose.yml              # Multi-container/service configuration
├── requirements.txt                # Dependencies (FastMCP, httpx, uvicorn, etc.)
├── main.py                         # Server entry point (stdio / SSE / HTTP)
├── manifest.json                   # MCP server metadata
└── src/
    ├── config.py                   # FastMCP instance & global URLs
    ├── api/
    │   ├── client.py               # Centralized async HTTP client (Câmara & Senado)
    │   ├── api.py                  # Master API export module
    │   ├── camara/                 # Câmara dos Deputados API services
    │   │   ├── deputies/
    │   │   ├── propositions/
    │   │   ├── votacoes/
    │   │   ├── orgaos/
    │   │   ├── partidos/
    │   │   ├── blocos/
    │   │   ├── eventos/
    │   │   ├── frentes/
    │   │   ├── grupos/
    │   │   ├── legislaturas/
    │   │   └── referencias/
    │   └── senado/                 # Senado Federal API services
    │       ├── senadores_api.py
    │       ├── comissoes_api.py
    │       ├── composicao_api.py
    │       ├── processos_api.py
    │       ├── plenario_api.py
    │       ├── votacoes_api.py
    │       ├── discursos_api.py
    │       ├── legislacao_api.py
    │       └── orcamento_api.py
    └── tools/
        ├── __init__.py             # Public tools export & centralized descriptions
        ├── camara/                 # Câmara dos Deputados MCP tools
        │   ├── deputies_tools.py
        │   ├── proposition_tools.py
        │   ├── votacoes_tools.py
        │   ├── orgaos_tools.py
        │   ├── partidos_blocos_tools.py
        │   ├── eventos_tools.py
        │   ├── frentes_grupos_tools.py
        │   ├── legislaturas_tools.py
        │   └── referencias_tools.py
        └── senado/                 # Senado Federal MCP tools
            ├── senadores_tools.py
            ├── comissoes_tools.py
            ├── composicao_tools.py
            ├── processos_tools.py
            ├── plenario_votacoes_tools.py
            ├── discursos_tools.py
            └── legislacao_orcamento_tools.py
```

---

## Available MCP Tools by Domain

### A. Câmara dos Deputados (70 Tools)

#### 1. Deputados (Deputies)
- `get_deputies_tool`: Search and filter federal deputies by name, state (UF), party, legislature, gender, and date range.
- `get_deputies_by_names_tool`: Search deputies by name with enriched details.
- `get_deputy_details_tool`: Complete biographical and parliamentary information by deputy ID.
- `get_deputy_expenses_tool`: Parliamentary quota expenses (CEAP) filtered by year, month, legislature, and supplier CNPJ/CPF.
- `get_deputy_speeches_tool`: Official speeches and floor statements.
- `get_deputy_events_tool`: Events and hearings with deputy's participation.
- `get_deputy_fronts_tool`: Parliamentary fronts the deputy belongs to.
- `get_deputy_history_tool`: History of mandate status changes, leaves, and party switches.
- `get_deputy_external_mandates_tool`: Electoral history outside the Chamber (TSE data).
- `get_deputy_occupations_tool`: Professional occupations declared by the deputy.
- `get_deputy_organs_tool`: Committees and organs the deputy is/was a member of.
- `get_deputy_professions_tool`: Professions declared by the deputy.
- `get_legislature_leaders_tool`: Party leaders and representatives in a legislature.
- `get_legislature_board_tool`: Board of Directors (Mesa Diretora) in a legislature.

#### 2. Proposições (Legislative Proposals)
- `get_propositions_tool`: Search propositions (PL, PEC, MPV, PLP, etc.) with advanced filters (author, party, theme, status, keywords).
- `get_propositions_by_id_tools`: Retrieve propositions authored by a specific deputy ID.
- `get_proposition_details_tool`: Full details, summary/ementa, and text of a proposition.
- `get_proposition_authors_tool`: Authors and co-signers of a proposition.
- `get_proposition_related_tool`: Related and attached propositions.
- `get_proposition_themes_tool`: Thematic areas linked to the proposition.
- `get_proposition_tramitations_tool`: Full chronological history of legislative tramitation.
- `get_proposition_votings_tool`: Votings that occurred on a specific proposition.

#### 3. Votações (Votings & Deliberations)
- `get_votacoes_tool`: Search votings by period, proposition, event, or organ.
- `get_votacao_details_tool`: Voting outcome, summary, and official metadata.
- `get_votacao_orientacoes_tool`: Party bench and leadership voting recommendations.
- `get_votacao_votos_tool`: Roll-call nominal votes (Yes, No, Abstention, Obstruction) of each deputy.

#### 4. Órgãos e Comissões (Organs & Committees)
- `get_orgaos_tool`: Search permanent and special committees, CPIs, and councils.
- `get_orgao_details_tool`: Details, structure, and jurisdiction of an organ.
- `get_orgao_events_tool`: Public hearings and meetings held by an organ.
- `get_orgao_members_tool`: Titular and substitute members and leadership of an organ.
- `get_orgao_votings_tool`: Votings conducted within an organ.

#### 5. Partidos e Blocos Partidários (Parties & Blocs)
- `get_partidos_tool`: List political parties active in the Chamber.
- `get_partido_details_tool`: Party registration details and leadership.
- `get_partido_lideres_tool`: Party leaders and vice-leaders.
- `get_partido_membros_tool`: Deputies affiliated with a party over time.
- `get_blocos_tool`: List parliamentary blocs formed in a legislature.
- `get_bloco_details_tool`: Details of a parliamentary bloc.
- `get_bloco_partidos_tool`: Parties that compose a bloc.

#### 6. Eventos e Sessões (Events & Sessions)
- `get_eventos_tool`: Search scheduled and past committee meetings, public hearings, and floor sessions.
- `get_evento_details_tool`: Schedule, location, description, and status of an event.
- `get_evento_deputados_tool`: Deputies attending or invited to the event.
- `get_evento_orgaos_tool`: Organs organizing the event.
- `get_evento_pauta_tool`: Legislative matters scheduled on the agenda.
- `get_evento_votacoes_tool`: Votings held during the event.

#### 7. Frentes e Grupos Parlamentares (Fronts & Groups)
- `get_frentes_tool`: Search formally registered parliamentary fronts.
- `get_frente_details_tool`: Details and coordinator of a front.
- `get_frente_membros_tool`: Member deputies of a front.
- `get_grupos_tool`: Interparliamentary friendship and cooperation groups.
- `get_grupo_details_tool`: Details of an interparliamentary group.
- `get_grupo_historico_tool`: State changes and history of a group.
- `get_grupo_membros_tool`: Parliamentarians participating in a group.

#### 8. Legislaturas (Legislatures)
- `get_legislaturas_tool`: Periods of mandate and legislative activity (e.g. 57 = 2023–2027).
- `get_legislatura_details_tool`: Dates and election year of a legislature.

#### 9. Tabelas de Referência (Reference Data)
- `get_referencias_ufs_tool`: Official list of Brazilian States and Federal District.
- `get_referencias_deputados_tool`: Metadata and parameters for deputy searches.
- `get_referencias_situacoes_deputado_tool`: Valid parliamentary mandate statuses.
- `get_referencias_tipos_profissao_tool`: Catalog of professional activities.
- `get_referencias_tipos_despesa_tool`: CEAP reimbursable expense categories.
- `get_referencias_proposicoes_tool`: Parameters for proposition queries.
- `get_referencias_tipos_proposicao_tool`: Proposition acronyms and types (PL, PEC, MPV, etc.).
- `get_referencias_situacoes_proposicao_tool`: Proposition processing and tramitation statuses.
- `get_referencias_temas_proposicao_tool`: Thematic codes (Health, Economy, Education, etc.).
- `get_referencias_tipos_autor_tool`: Author entity types.
- `get_referencias_tipos_tramitacao_tool`: Tramitation step types.
- `get_referencias_eventos_tool`: Metadata and parameters for event queries.
- `get_referencias_tipos_evento_tool`: Event categories (Deliberative Meeting, Public Hearing, etc.).
- `get_referencias_situacoes_evento_tool`: Event statuses (Scheduled, Completed, Canceled).
- `get_referencias_orgaos_tool`: Parameters for organ queries.
- `get_referencias_tipos_orgao_tool`: Organ types across the Chamber.
- `get_referencias_situacoes_orgao_tool`: Organ operational statuses.

---

### B. Senado Federal & Congresso Nacional (56 Tools)

#### 1. Senadores (Senators)
- `get_senadores_atuais_tool`: Active senators in the Federal Senate with contact and party info.
- `get_senadores_afastados_tool`: Senators currently on leave/off-duty and leave rationale.
- `get_senadores_legislatura_tool`: Senators linked to a legislature or period of legislatures.
- `get_senador_detalhes_tool`: Full biographical, mandate, and contact record for a senator.
- `get_senador_cargos_tool`: Leadership and committee positions held by the senator.
- `get_senador_comissoes_tool`: Standing, special, and mixed committees the senator joined.
- `get_senador_filiacoes_tool`: Historical party affiliations across the senator's career.
- `get_senador_historico_academico_tool`: Academic background and degrees declared by the senator.
- `get_senador_licencas_tool`: Leaves of absence (medical, mission, personal interest).
- `get_senador_mandatos_tool`: Senate terms, titular mandates, and substitute appointments.
- `get_senador_profissoes_tool`: Professional occupations declared by the senator.

#### 2. Comissões e Colegiados (Committees & Collegiates)
- `get_comissoes_tipos_colegiado_tool`: Categories of committees in the Senate and Congress.
- `get_comissoes_por_tipo_tool`: Senate committees filtered by type (Permanent, Temporary, etc.).
- `get_colegiados_atividade_tool`: All active collegiate bodies in the National Congress.
- `get_comissoes_mistas_tool`: Current Joint Committees (Comissões Mistas - SF and CD).
- `get_comissao_detalhes_tool`: Committee jurisdiction, contacts, and legal mission.
- `get_comissao_agenda_tool`: Schedule of committee hearings and meetings by day, period, or month.
- `get_comissao_cpi_requerimentos_tool`: Official petitions and inquiries presented in a CPI.
- `get_comissao_reuniao_detalhes_tool`: Agenda, transcript, location, and details of a committee meeting.
- `get_comissao_documento_ultima_reuniao_tool`: Direct link to official documents from the last meeting.

#### 3. Composição, Lideranças e Blocos (Leadership & Blocs)
- `get_composicao_mesa_sf_tool`: Board of Directors of the Federal Senate (Mesa Diretora SF).
- `get_composicao_mesa_cn_tool`: Board of Directors of the National Congress (Mesa Diretora CN).
- `get_liderancas_tool`: Party, bloc, and government leadership posts in the Senate and Congress.
- `get_liderancas_tipos_tool`: Definitions and types of parliamentary leaderships.
- `get_partidos_senado_tool`: Political parties with representation in the Senate.
- `get_blocos_senado_tool`: Formed parliamentary blocs in the Senate.
- `get_bloco_senado_detalhes_tool`: Member parties and senators composing a bloc.
- `get_composicao_comissao_tool`: Committee composition (titular and substitute members).
- `get_composicao_comissao_mista_atual_tool`: Senators and deputies in a Joint Committee.
- `get_composicao_comissao_mista_historica_tool`: Historical composition of a Joint Committee over time.

#### 4. Processo Legislativo (Legislative Process - Modern /processo/ API)
- `get_processos_senado_tool`: Search bills, constitutional amendments, and decrees (PL, PEC, PDL, etc.).
- `get_processo_detalhes_senado_tool`: Deep details of a legislative process (summary, authors, rapporteurs).
- `get_processo_documentos_senado_tool`: Official documents, texts, and reports attached to a process.
- `get_processo_emendas_senado_tool`: Amendments submitted by parliamentarians to a bill.
- `get_processo_referencias_senado_tool`: Domain reference tables (subjects, classes, authors, statuses).

#### 5. Plenário e Votações (Floor Sessions & Deliberations)
- `get_plenario_agenda_dia_tool`: Senate floor schedule for a specific day.
- `get_plenario_agenda_cn_tool`: Joint Congress floor schedule for a specific day.
- `get_plenario_encontro_detalhes_tool`: Floor meeting details, agenda, decisions, or summary.
- `get_plenario_resultado_tool`: Consolidated voting results from Senate floor sessions.
- `get_plenario_resultado_veto_tool`: Presidential Veto roll-call results in Congress.
- `get_plenario_orientacao_bancada_tool`: Party bench voting instructions (Yes, No, Free).
- `get_votacoes_nominais_senado_tool`: Roll-call nominal votes recorded on the electronic voting board.
- `get_votacao_comissao_materia_tool`: Conclusive committee voting outcomes on specific bills.
- `get_votacao_comissao_parlamentar_tool`: Individual voting track record of a parliamentarian in committees.

#### 6. Discursos e Taquigrafia (Speeches & Transcripts)
- `get_senador_discursos_tool`: Official floor speeches and statements delivered by a senator.
- `get_senador_apartes_tool`: Interventions and floor remarks made by a senator during colleagues' speeches.
- `get_discurso_texto_integral_tool`: Full transcribed verbatim text of a speech.
- `get_plenario_discursos_periodo_tool`: All floor speeches delivered within a date interval.
- `get_taquigrafia_notas_tool`: Shorthand stenographic transcripts of floor sessions or meetings.
- `get_taquigrafia_videos_tool`: Video chapter marks and timing cues for meetings and sessions.

#### 7. Legislação e Orçamento (Legislation & Budget)
- `get_legislacao_lista_senado_tool`: Search Federal Brazilian laws, decrees, and provisional measures.
- `get_legislacao_detalhes_senado_tool`: Full details, summary, and text of a federal statute.
- `get_legislacao_tipos_norma_tool`: Catalog of federal legal norm classifications.
- `get_legislacao_termos_tool`: Controlled vocabulary and indexing thesaurus for legislation.
- `get_orcamento_emendas_senado_tool`: Batches of parliamentary budget amendments to the federal budget (OGU).
- `get_orcamento_oficios_senado_tool`: Official letters and notifications endorsing budget amendments (SEDOL).

---

## Installation & Running

### 1. Local Setup
```bash
# Clone and enter the project
git clone <repository-url>
cd gov-mcp-server

# Create virtual environment
python -m venv .venv
# Windows:
.venv\Scripts\activate
# Linux/macOS:
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### 2. Running
```bash
# Standard stdio mode (for Claude Desktop / Antigravity):
python main.py

# SSE / HTTP mode:
python main.py --http
```

### 3. Running Tests
```bash
pytest test/
```

---

## License

This project is licensed under the MIT License.
