# Regra de Planejamento para Novas Features (Feature Planning Rule)

## Objetivo
Garantir que o usuário tenha controle total sobre a abordagem de desenvolvimento ao solicitar novas funcionalidades (features), ferramentas MCP, integrações de APIs ou modificações estruturais no projeto `gov-mcp-server`.

## Diretriz Obrigatória
Toda vez que o usuário solicitar o desenvolvimento ou adição de uma **nova feature** ou funcionalidade no projeto:

O agente **NÃO DEVE** iniciar a escrita de código ou modificação de arquivos de forma imediata sem antes consultar a preferência do usuário sobre a criação de um plano prévio de implementação.

---

## Fluxo de Confirmação Obrigatório

Ao receber a solicitação de uma nova feature, o agente deve apresentar uma pergunta interativa (utilizando a ferramenta `ask_question`):

### Exemplo de Pergunta com `ask_question`:
```json
{
  "questions": [
    {
      "question": "Como você prefere conduzir a implementação desta nova feature?",
      "options": [
        "(Recomendado) Elaborar um plano de implementação detalhado antes de iniciar",
        "Prosseguir diretamente para a implementação do código"
      ],
      "is_multi_select": false
    }
  ],
  "toolSummary": "Confirmação do fluxo de desenvolvimento",
  "toolAction": "Perguntando preferência de planejamento prévio"
}
```

---

## Comportamento Conforme a Escolha

### 1. Se o usuário escolher "Elaborar um plano de implementação detalhado":
- O agente deve preparar e apresentar uma estratégia completa contendo:
  - **Escopo e Requisitos**: O que será desenvolvido e regras de negócio.
  - **Arquitetura e Componentes**: Módulos em `src/api/`, ferramentas em `src/tools/`, schemas ou configurações impactadas.
  - **Plano de Testes**: Novos testes a serem incluídos em `test/`.
  - **Plano de Verificação**: Como validar o funcionamento da nova feature.
- O agente deve aguardar o feedback ou aprovação do usuário antes de realizar alterações no código-fonte.

### 2. Se o usuário escolher "Prosseguir diretamente para a implementação":
- O agente procede diretamente com a criação/edição dos arquivos necessários, garantindo a implementação da feature, tratamento de exceções, tipagem adequada e testes correspondentes.
