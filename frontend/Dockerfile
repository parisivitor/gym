# Imagem base
FROM node:14-alpine

# Define variáveis de ambiente
ENV TZ=America/Sao_Paulo

# Criação do diretório de trabalho
WORKDIR /app

# Copia a aplicação para dentro da imagem
COPY . .

# Instalação de dependências
RUN npm install

# Build da aplicação
RUN npm run build

# Define o comando que será executado quando o contêiner for iniciado
CMD ["npm", "start"]