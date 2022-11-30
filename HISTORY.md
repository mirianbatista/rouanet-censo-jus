## Registros do desenvolvimento do desafio

Escolhi realizar o desenvolvimento com python por ter experiência prévia com pandas. Assim que li a descrição do desafio, pensei em ter como entrega final um app streamlit pra fazer o download do csv com os dados tratados, por ser simples de implementar e de fazer deploy, além de proporcionar uma experiência de uso satisfatória. Sempre gosto de fazer transformações em jupyter notebook por ser um ambiente que eu já estou acostumada e onde eu consigo fazer testes de maneira descomplicada. O notebook que usei [está aqui](https://github.com/mirianbatista/rouanet-censo-jus/blob/main/rouanet_censo_jus.ipynb). Abaixo descrevo pontos que considerei válidos de compartilhar acerca do momento em que eu estava implementando as transformações e testando o contêiner.

#### Jupyter Notebook

* Precisei revisar o conceito de Natural Key para entender o que precisava fazer.
    
* Fiquei um pouco em dúvida por ter no email "remover as linhas duplicadas de acordo com a **surrogate key**", mas no gist ter "remover as linhas duplicadas de acordo com a **natural key**". Considerei que a natural key faria mais sentido e usei ela na transformação.
  
#### Docker

* Tive dificuldade de montar minha pasta local no contêiner pra alterar o arquivo rouanet_censo_jus_app.py para conseguir ir vendo as alterações (sem precisar fazer rebuild). Então, fiz a implementação e testes do rouanet_censo_jus_app.py em um venv e executei o contêiner só quando ele estava pronto, uma vez que a prioridade era finalizar o desafio.
    
Por último, gostaria de documentar algumas possibilidades que possivelmente eu tentaria se tivesse mais tempo:

* Colocaria o projeto na aws ou gcp.
    
* Talvez faria uma dag que realizasse o processo do projeto.
