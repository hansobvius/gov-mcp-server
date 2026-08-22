# Government MCP Server (Câmara dos Deputados)

A Model Context Protocol (MCP) server that provides comprehensive access to the Brazilian Chamber of Deputies (Câmara dos Deputados) Open Data API ([Swagger v2](https://dadosabertos.camara.leg.br/swagger/api.html)).

## Overview

This project implements an MCP server allowing AI assistants (Claude Desktop, Google Antigravity, Cursor, ChatGPT, etc.) and agentic workflows to query, inspect, and analyze all open legislative data from the Brazilian Chamber of Deputies.

The server covers all 79 endpoints organized into modular domains with full async support (`httpx`), robust error handling, parameter sanitation, and dual transport modes (`stdio` and `SSE`/`HTTP`).

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
    ├── config.py                   # FastMCP instance & global settings
    ├── api/
    │   ├── client.py               # Centralized async HTTP client & parameter formatter
    │   ├── api.py                  # Master API export module
    │   ├── deputies/               # Deputies API services
    │   ├── propositions/           # Propositions API services
    │   ├── votacoes/               # Votings API services
    │   ├── orgaos/                 # Committees & Organs API services
    │   ├── partidos/               # Political Parties API services
    │   ├── blocos/                 # Parliamentary Blocs API services
    │   ├── eventos/                # Events & Sessions API services
    │   ├── frentes/                # Parliamentary Fronts API services
    │   ├── grupos/                 # Interparliamentary Groups API services
    │   ├── legislaturas/           # Legislatures API services
    │   └── referencias/            # Reference tables & lookup values
    └── tools/
        ├── __init__.py             # Public tools export & centralized descriptions
        ├── deputies_tools.py       # Deputies MCP tools
        ├── proposition_tools.py    # Propositions MCP tools
        ├── votacoes_tools.py       # Votings MCP tools
        ├── orgaos_tools.py         # Organs & Committees MCP tools
        ├── partidos_blocos_tools.py# Parties & Blocs MCP tools
        ├── eventos_tools.py        # Events MCP tools
        ├── frentes_grupos_tools.py # Fronts & Groups MCP tools
        ├── legislaturas_tools.py   # Legislatures MCP tools
        └── referencias_tools.py    # Reference tables MCP tools
```

---

## Available MCP Tools by Domain

### 1. Deputados (Deputies)
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

### 2. Proposições (Legislative Proposals)
- `get_propositions_tool`: Search propositions (PL, PEC, MPV, PLP, etc.) with advanced filters (author, party, theme, status, keywords).
- `get_propositions_by_id_tools`: Retrieve propositions authored by a specific deputy ID.
- `get_proposition_details_tool`: Full details, summary/ementa, and text of a proposition.
- `get_proposition_authors_tool`: Authors and co-signers of a proposition.
- `get_proposition_related_tool`: Related and attached propositions.
- `get_proposition_themes_tool`: Thematic areas linked to the proposition.
- `get_proposition_tramitations_tool`: Full chronological history of legislative tramitation.
- `get_proposition_votings_tool`: Votings that occurred on a specific proposition.

### 3. Votações (Votings & Deliberations)
- `get_votacoes_tool`: Search votings by period, proposition, event, or organ.
- `get_votacao_details_tool`: Voting outcome, summary, and official metadata.
- `get_votacao_orientacoes_tool`: Party bench and leadership voting recommendations.
- `get_votacao_votos_tool`: Roll-call nominal votes (Yes, No, Abstention, Obstruction) of each deputy.

### 4. Órgãos e Comissões (Organs & Committees)
- `get_orgaos_tool`: Search permanent and special committees, CPIs, and councils.
- `get_orgao_details_tool`: Details, structure, and jurisdiction of an organ.
- `get_orgao_events_tool`: Public hearings and meetings held by an organ.
- `get_orgao_members_tool`: Titular and substitute members and leadership of an organ.
- `get_orgao_votings_tool`: Votings conducted within an organ.

### 5. Partidos e Blocos Partidários (Parties & Blocs)
- `get_partidos_tool`: List political parties active in the Chamber.
- `get_partido_details_tool`: Party registration details and leadership.
- `get_partido_lideres_tool`: Party leaders and vice-leaders.
- `get_partido_membros_tool`: Deputies affiliated with a party over time.
- `get_blocos_tool`: List parliamentary blocs formed in a legislature.
- `get_bloco_details_tool`: Details of a parliamentary bloc.
- `get_bloco_partidos_tool`: Parties that compose a bloc.

### 6. Eventos e Sessões (Events & Sessions)
- `get_eventos_tool`: Search scheduled and past committee meetings, public hearings, and floor sessions.
- `get_evento_details_tool`: Schedule, location, description, and status of an event.
- `get_evento_deputados_tool`: Deputies attending or invited to the event.
- `get_evento_orgaos_tool`: Organs organizing the event.
- `get_evento_pauta_tool`: Legislative matters scheduled on the agenda.
- `get_evento_votacoes_tool`: Votings held during the event.

### 7. Frentes e Grupos Parlamentares (Fronts & Groups)
- `get_frentes_tool`: Search formally registered parliamentary fronts.
- `get_frente_details_tool`: Details and coordinator of a front.
- `get_frente_membros_tool`: Member deputies of a front.
- `get_grupos_tool`: Interparliamentary friendship and cooperation groups.
- `get_grupo_details_tool`: Details of an interparliamentary group.
- `get_grupo_historico_tool`: State changes and history of a group.
- `get_grupo_membros_tool`: Parliamentarians participating in a group.

### 8. Legislaturas (Legislatures)
- `get_legislaturas_tool`: Periods of mandate and legislative activity (e.g. 57 = 2023–2027).
- `get_legislatura_details_tool`: Dates and election year of a legislature.

### 9. Tabelas de Referência (Reference Data)
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
