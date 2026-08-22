---
name: docker-rebuild
description: Recria e atualiza o container Docker do projeto após alterações.
---

# Docker Rebuild Skill

Esta skill deve ser usada sempre que o usuário solicitar a atualização, recriação ou "rebuild" do container Docker do projeto para aplicar novas alterações no código.

## Quando usar:
- O usuário pede para "atualizar o docker"
- O usuário pede para "recriar o container"
- O usuário quer subir uma imagem atualizada do projeto

## Passos a executar:

1. Acesse a raiz do projeto.
2. Execute o comando para recriar o container forçando o build da imagem em segundo plano (detached mode). O projeto utiliza `docker-compose.yml`.

Comando recomendado:
```bash
docker-compose up -d --build
```

*(O comando `up -d --build` automaticamente recria os containers cujas imagens base ou Dockerfile sofreram alterações e inicia o serviço em background)*

3. Se houver erro, você pode tentar derrubar e subir novamente de forma explícita:
```bash
docker-compose down
docker-compose up -d --build
```

## Confirmação
Após a execução do comando, informe o usuário que o container foi recriado com sucesso e os logs estão disponíveis (se necessário, o usuário pode pedir para vê-los).
