1° Passo - criar uma imagem de python
docker pull python

1.1° passo - versão 3.8
docker pull python:3.8

2° passo - docker run -it --rm python:3.8

3° passo - criar um DockerFile

4° passo - docker build -t my-python-app .

5° passo - docker run -it --rm --name my-running-app my-python-app

6° passo - docker run -it --rm --name nome-do-seu-script -v "$PWD":/usr/src/myapp -w /usr/src/myapp python:3 python seu-arquivo.py

# -v "$PWD":/usr/src/myapp - monta o diretório atual para dentro do contêiner
# -w /usr/src/myapp - muda o WORKDIR para executar o comando no diretório recém montado.