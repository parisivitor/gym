# Imagem base
FROM python:3.9-alpine

# Define variáveis de ambiente
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

ENV TZ=America/Sao_Paulo

ENV LANG C.UTF-8
ENV LANGUAGE=pt_BR:pt
ENV LC_ALL C.UTF-8

# Instalação de dependências
RUN apk update \
    && apk add --no-cache build-base postgresql-dev \
    && pip install --upgrade pip

# Criação do diretório de trabalho
RUN mkdir /app
WORKDIR /app

# Instalação de dependências Python
COPY requirements.txt /app/
RUN pip install -r requirements.txt

# Copia a aplicação para dentro da imagem
COPY . /app/

# Executa a migração com o alembic
# RUN alembic upgrade head

# Expor a porta que o gunicorn estará rodando
EXPOSE 80

# Inicia a aplicação com gunicorn
#CMD ["uvicorn", "--host=0.0.0.0", "--port=8000", "main:api"]
