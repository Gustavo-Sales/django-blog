# Usar uma imagem base oficial do Python 3.12.4
FROM python:3.12.4-slim

# Definir o diretório de trabalho no contêiner
WORKDIR /app

# Instalar dependências do sistema
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        build-essential \
        libpq-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Copiar os arquivos de requisitos para o diretório de trabalho
COPY requirements.txt .

# Instalar as dependências do projeto
RUN pip install --no-cache-dir -r requirements.txt

# Copiar o código do projeto para o diretório de trabalho no contêiner
COPY . .

# Expor a porta que a aplicação Django usará
EXPOSE 8000

# Rodar comandos para coletar arquivos estáticos, aplicar migrações e iniciar o servidor
CMD ["sh", "-c", "python manage.py migrate && gunicorn DjangoBlog.wsgi:application --bind 0.0.0.0:8000"]
