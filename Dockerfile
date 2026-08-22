FROM python:3.11-slim

# Variáveis de ambiente para Python e MCP
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONPATH=/app \
    MCP_TRANSPORT=http \
    HOST=0.0.0.0 \
    PORT=8000

WORKDIR /app

# Instalação das dependências
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia o código-fonte
COPY . .

# Expõe a porta do MCP Server
EXPOSE 8000

# Inicia o servidor em modo SSE
CMD ["python", "main.py"]
