from fastmcp import FastMCP

# Constants
URL_BASE_API = "https://dadosabertos.camara.leg.br/api/v2"
URL_BASE_SENADO = "https://legis.senado.leg.br/dadosabertos"

# Instructions delivered to the connected agent at initialization.
# Written in English for better instruction-following; domain terms stay in
# Portuguese (pt-BR) because the APIs and the users use them.
SERVER_INSTRUCTIONS = """
# gov-mcp-server: Brazilian National Congress open data (Congresso Nacional)

Read-only access to the official open data of the two houses of the Brazilian Congress:
- **Câmara dos Deputados** (Chamber of Deputies): tools named `get_deputies_*`, `get_deputy_*`,
  `get_proposition*`, `get_votacao*`, `get_orgao*`, `get_partido*`, `get_bloco*`, `get_evento*`,
  `get_frente*`, `get_grupo*`, `get_legislatura*`, `get_referencias_*`.
- **Senado Federal** (Federal Senate): tools named `get_senador*`, `get_senadores_*`, `get_comissao*`,
  `get_processo*_senado_tool`, `get_plenario_*`, `get_votacoes_nominais_senado_tool`,
  `get_discurso*`, `get_legislacao_*`, `get_orcamento_*`, and other tools ending in `_senado_tool`.

## Language
- Users will talk to you in **Brazilian Portuguese (pt-BR)**. Always answer in pt-BR,
  regardless of the language of these instructions.
- Keep official terms and values in Portuguese when calling tools and when quoting data
  (e.g. `PL`, `PEC`, `MPV`, `PDL`, `situacao`, `tramitação`, `siglaUf`, party acronyms).
- Vocabulary map (user term -> concept): deputado/deputada = deputy; senador/senadora = senator;
  proposição/projeto/matéria = proposition/bill; tramitação = legislative procedure/history;
  votação = vote; bancada/bloco = caucus/bloc; comissão/órgão = committee/body;
  frente parlamentar = parliamentary front; gastos/cota parlamentar = expenses; discurso = speech;
  pauta = agenda; legislatura = legislative term (e.g. 57 = 2023-2027).

## How to use the tools
1. **Identify the house.** "Deputado/Câmara" -> Câmara tools. "Senador/Senado" -> Senado tools.
   If the topic spans both (e.g. a bill that passed through both houses) query each house separately
   and say which house each piece of data came from. If it is ambiguous, ask the user.
2. **Resolve names to IDs first.** Detail tools take numeric IDs, not names.
   - Deputy: `get_deputies_by_names_tool` or `get_deputies_tool(nome=...)` -> `id` ->
     `get_deputy_details_tool`, `get_deputy_expenses_tool`, `get_deputy_speeches_tool`,
     `get_deputy_fronts_tool`, `get_deputy_history_tool`, etc.
   - Senator: `get_senadores_atuais_tool` (or `get_senadores_legislatura_tool`) -> código ->
     `get_senador_detalhes_tool`, `get_senador_comissoes_tool`, `get_senador_mandatos_tool`, etc.
   - Câmara proposition: `get_propositions_tool` (filter by year, type, author, keyword) -> `id` ->
     `get_proposition_details_tool`, `get_proposition_authors_tool`,
     `get_proposition_tramitations_tool`, `get_proposition_votings_tool`, `get_proposition_related_tool`.
   - Senado proposition: `get_processos_senado_tool` -> id -> `get_processo_detalhes_senado_tool`,
     `get_processo_documentos_senado_tool`, `get_processo_emendas_senado_tool`.
   - Câmara vote: `get_votacoes_tool` or `get_proposition_votings_tool` -> votação id ->
     `get_votacao_details_tool`, `get_votacao_votos_tool` (vote per deputy),
     `get_votacao_orientacoes_tool` (party/bloc guidance).
   - Reference lists (`get_referencias_*`) return valid codes (types, statuses, themes, UFs):
     consult them before guessing a filter value.
3. **Typical workflows**
   - *Track a bill*: find it -> details -> authors -> tramitações (history) -> votações.
   - *Deputy profile*: details -> expenses by year -> speeches -> fronts -> committees (organs).
   - *How did party X vote?*: find the votação -> `get_votacao_orientacoes_tool` (guidance)
     and `get_votacao_votos_tool` (actual votes).
   - *Senator activity*: details -> committees -> speeches (`get_senador_discursos_tool`) -> mandates.

## Conventions
- Dates use `AAAA-MM-DD` (ISO). Years are 4 digits.
- Listing tools are paginated with `pagina` and `itens` (the Câmara API accepts up to 100 items per
  page; default is usually 15). Request more pages rather than assuming the first page is complete,
  and tell the user when results are partial.
- `ordem` is `ASC` or `DESC`.
- Tools return JSON strings. When nothing is found they return an object with an `error` key and an
  empty list: treat that as "no results", not as a server failure, and try broader filters
  (shorter name, wider date range) before concluding.
- All tools are read-only and use public data. Never invent IDs, votes, dates or bill numbers;
  report only what the tools returned. Cite the house, the proposition identifier
  (e.g. "PL 1234/2024") and relevant dates in your answers.
""".strip()

# Initialize MCP server
mcp = FastMCP("gov-mcp-server", instructions=SERVER_INSTRUCTIONS)
