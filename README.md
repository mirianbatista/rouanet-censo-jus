# rouanet-censo-jus

Este projeto é a minha implementação do Desafio de Data Engineering do Jusbrasil.

## Como rodar o projeto

#### Pré- requisitos:

* docker

#### Passo a passo pós clone do repositório:

1º Criar imagem a partir do Dockerfile
```
docker build -t streamlit_jus .
```
2º Executar o contêiner
```
docker run -p 8501:8501 streamlit_jus
```
3º Clicar na url que aparece no terminal
```
http://0.0.0.0:8501
```
