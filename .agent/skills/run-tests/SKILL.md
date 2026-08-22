---
name: run-tests
description: >-
  Executa os testes do projeto localizados em `test/` de forma interativa, permitindo ao usuário escolher entre rodar todos os testes ou selecionar testes específicos através de uma checklist com múltipla escolha. Use sempre que o usuário solicitar executar testes, rodar testes, rodar a suíte de testes, testar a aplicação, testar APIs ou componentes MCP.
---

# Execução Interativa de Testes

Esta skill instrui o agente sobre como proceder sempre que o usuário solicitar a execução de testes no projeto `gov-mcp-server`.

## Mapeamento de Testes Disponíveis

| Arquivo de Teste | Descrição / Cobertura |
| :--- | :--- |
| `test/test_deputies_api.py` | Testes da API de Deputados (busca por nome, detalhes, despesas, discursos) |
| `test/test_proposition_api.py` | Testes da API de Proposições (busca, detalhes, autores, votações, tramitações) |
| `test/test_votacoes_api.py` | Testes da API de Votações (listagem de votações, detalhes, votos, orientações) |
| `test/test_eventos_api.py` | Testes da API de Eventos (busca de eventos, pauta, deputados participantes) |
| `test/test_orgaos_api.py` | Testes da API de Órgãos (busca de órgãos, detalhes, membros, eventos) |
| `test/test_legislaturas_partidos_api.py` | Testes de Partidos, Blocos Partidários e Legislaturas |
| `test/test_referencias_api.py` | Testes das Tabelas de Referências e Domínios (UFs, tipos de despesa, etc.) |
| `test/test_all_tools_registration.py` | Validação do registro e contagem de todas as 70 ferramentas MCP |
| `test/test_mcp_server.py` | Testes de inicialização do servidor FastMCP e chamada básica de tools |
| `test/test_comprehensive.py` | Suíte de testes abrangente (imports, manifesto, conectividade e integração) |
| `test/test_client.py` | Testes de execução via cliente FastMCP |

---

## Fluxo de Execução Obrigatório

Quando o usuário solicitar a execução de testes, o agente **NÃO** deve executar comandos diretamente sem antes perguntar a preferência do usuário. Siga estritamente o fluxo abaixo:

### Passo 1: Perguntar se deseja executar TODOS ou ESPECÍFICOS

Utilize a ferramenta `ask_question` para apresentar a seguinte pergunta:

```json
{
  "questions": [
    {
      "question": "Como você deseja executar os testes do projeto?",
      "options": [
        "(Recomendado) Executar todos os testes do projeto",
        "Selecionar testes específicos da lista"
      ],
      "is_multi_select": false
    }
  ],
  "toolSummary": "Seleção do modo de teste",
  "toolAction": "Perguntando modo de execução dos testes"
}
```

---

### Passo 2A: Se o usuário escolher "Executar todos os testes do projeto"

1. Execute a suíte de testes completa a partir da raiz do projeto usando o ambiente virtual (`.venv`) ou o comando `pytest`:
   ```bash
   pytest test/ -v
   ```
   *(ou `.\.venv\Scripts\pytest test/ -v` / `python -m pytest test/ -v`)*

2. Analise a saída e apresente um resumo claro ao usuário contendo:
   - Total de testes executados
   - Quantidade de testes aprovados (`PASSED`)
   - Quantidade de testes reprovados (`FAILED`), se houver, detalhando a causa
   - Duração total da execução

---

### Passo 2B: Se o usuário escolher "Selecionar testes específicos da lista"

1. Apresente ao usuário uma pergunta com **checklist interativo** utilizando a ferramenta `ask_question` com `is_multi_select: true`:

```json
{
  "questions": [
    {
      "question": "Quais testes você deseja executar?",
      "options": [
        "test_deputies_api.py - API de Deputados (busca, detalhes, despesas, discursos)",
        "test_proposition_api.py - API de Proposições (busca, autores, tramitações, votações)",
        "test_votacoes_api.py - API de Votações (detalhes, votos, orientações)",
        "test_eventos_api.py - API de Eventos (busca, pauta, participantes)",
        "test_orgaos_api.py - API de Órgãos (detalhes, membros, eventos)",
        "test_legislaturas_partidos_api.py - Partidos, Blocos e Legislaturas",
        "test_referencias_api.py - Tabelas de Referências e Domínios",
        "test_all_tools_registration.py - Registro das 70 ferramentas MCP",
        "test_mcp_server.py - Servidor FastMCP e execução básica de tool",
        "test_comprehensive.py - Suíte abrangente (imports, manifesto, conectividade)",
        "test_client.py - Cliente FastMCP"
      ],
      "is_multi_select": true
    }
  ],
  "toolSummary": "Seleção dos testes a executar",
  "toolAction": "Apresentando checklist de testes disponíveis"
}
```

2. Identifique os arquivos correspondentes às opções marcadas pelo usuário.
   - Exemplo: se o usuário marcar `test_deputies_api.py` e `test_orgaos_api.py`, monte o comando:
     ```bash
     pytest test/test_deputies_api.py test/test_orgaos_api.py -v
     ```

3. Execute os testes selecionados e exiba um relatório estruturado dos resultados.

---

## Boas Práticas e Tratamento de Erros

1. **Dependências e Ambiente**: Certifique-se de executar no diretório raiz do repositório (`c:\Users\thiag\Projetos\MCP_Projects\gov-mcp-server`), onde o Python local e as dependências instaladas estão acessíveis.
2. **Saída Formatada**: Apresente sempre os resultados formatados com tabelas ou listas em Markdown, destacando eventuais erros e traceback de forma legível.
3. **Novos Testes**: Se novos arquivos forem adicionados ao diretório `test/`, liste-os dinamicamente nas opções apresentadas ao usuário.
