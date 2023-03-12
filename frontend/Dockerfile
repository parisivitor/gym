# Imagem base
FROM node:14-alpine

# Define variáveis de ambiente
ENV TZ=America/Sao_Paulo

# Criação do diretório de trabalho
WORKDIR /app

# Copia apenas o package.json para dentro da imagem
COPY package.json .

# Instalação de dependências
RUN npm install

# Copia o restante da aplicação para dentro da imagem
COPY . .

# Build da aplicação
RUN npm run build

# Define o comando que será executado quando o contêiner for iniciado
CMD ["npm", "start"]
