# rouanet-censo-jus

Este projeto é a minha implementação do Desafio de Data Engineering do Jusbrasil. Ele consiste na realização de transformações em dados do Censo e da Lei Rouanet, e a posterior disponibilização desses dados tratados em um site onde é possível realizar download deles.

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
