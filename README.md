# Docker

```
# Docker Command

- docker version
- docker info
- docker container run == docker run
- docker <command> (options)
- docker <command> <sub-command> (options)
- C:\Users\Yuan>docker container run --publish 80:80 nginx
- docker container ls
- docker container stop 690
- docker container ls -a
- docker container rm 690
- docker run --name mongo -d mongo
- docker ps
- docker top mongo
- docker start mongo
- docker logs f8c91284636e
- docker exec <id do container> -ti /bin/bash
```

============================================================================================
============================================================================================

# Dockerfile

```
# Imagem com Jupyter Notebook e algumas bibliotecas.

-------------------------------------------
-------------------------------------------

FROM python:3.8-slim-buster

RUN mkdir -p /home/notebooks

WORKDIR /home/notebooks

RUN pip install numpy \ pandas \ scikit-learn \ tensorflow \ seaborn \ jupyter \ notebook

EXPOSE 8888

ENTRYPOINT [ "jupyter", "notebook", "--ip=0.0.0.0", "--allow-root", "--no-browser" ]

-------------------------------------------
-------------------------------------------

docker run -d --rm --name jupyterserver -p 8888:8888 -v "c:/Users/Yuan/Desktop/folder/new:/home/notebooks" image-ds

C:\Users\Yuan\Desktop\folder>docker images
REPOSITORY               TAG       IMAGE ID       CREATED         SIZE
image-ds                 latest    8348a24c62a1   2 minutes ago   2.41GB
jupyter/scipy-notebook   latest    19b33596f37c   2 days ago      2.57GB
mongo                    latest    c1a14d3979c5   9 days ago      691MB
nginx                    latest    f8f4ffc8092c   12 days ago     133MB
continuumio/anaconda3    latest    f78cb37fb1bd   4 weeks ago     2.81GB
docker/getting-started   latest    083d7564d904   4 months ago    28MB

```
============================================================================================
============================================================================================

# Docker Run

```
>> docker run -it -p 8888:8888 -v "c:/Users/Yuan/docker_test:/home" continuumio/anaconda3 /bin/bash
                                   => Folder of your computer:Folder of your container
>> (base) root@b385e6ba35f5:/# ls
>> bin  boot  dev  etc  home  lib  lib64  media  mnt  opt  proc  root  run  sbin  srv  sys  tmp  usr  var
>> (base) root@b385e6ba35f5:/# home
>> bash: home: command not found
>> (base) root@b385e6ba35f5:/# cd /home/
                            ==> Folder of container
>> (base) root@b385e6ba35f5:/home# jupyter notebook --ip='*' --port=8888 --no-browser --allow-root &
>> http://b385e6ba35f5:8888/?token=14a31f116e1aac471fcd9b03390fc3dcf5e937e426cd33af
```

======================================================================================
======================================================================================
```
docker build -t python-imdb
"docker build" requires exactly 1 argument.
See 'docker build --help'

docker build -t python-imdb .


docker run python-imdb


Para cada modificacao, o docker precisa ser re-build it novamente!!!!

======================================================================================================

https://hub.docker.com/r/jupyter/pyspark-notebook

Conteiner Name:
PySpark

Ports
Local Host:
8050
http://localhost:8050/

========================================================================================================

Microsoft Windows [Version 10.0.18363.418]
(c) 2019 Microsoft Corporation. All rights reserved.

C:\Users\Yuan>docker run hello-world
Unable to find image 'hello-world:latest' locally
latest: Pulling from library/hello-world
2db29710123e: Pull complete                                                                                             Digest: sha256:9ade9cc2e26189a19c2e8854b9c8f1e14829b51c55a630ee675a5a9540ef6ccf
Status: Downloaded newer image for hello-world:latest

C:\Users\Yuan>

========================================================================================================

docker images

docker run -it -d ubuntu


C:\Users\Yuan>docker run -it -d ubuntu
c8c4ef5a14f4aa0851811be74ffbef6b904bf77527b8143dd1d198d846c63e8a

========================================================================================================

# Showing Continer ID
# docker ps -a

C:\Users\Yuan>docker ps -a

CONTAINER ID   IMAGE                             COMMAND                  CREATED          STATUS                      PORTS     NAMES
c8c4ef5a14f4   ubuntu                            "bash"                   44 seconds ago   Up 43 seconds                         lucid_jemison
85fa03fc84e3   hello-world                       "/hello"                 13 minutes ago   Exited (0) 13 minutes ago             dreamy_franklin
c3ab5367ed4c   jupyter/pyspark-notebook:latest   "tini -g -- start-no…"   9 hours ago      Exited (0) 8 hours ago                PySpark

========================================================================================================

Logando em um container
Você gerou um container a partir de uma imagem e agora, por alguma razão, precisa logar neste container. Sim, isso é possível e o comando exec existe para atender este propósito.

Primeiro você precisa do id do container que você deseja logar.

Para isso, utilize o comando docker ps.
Copie o valor da coluna container id do container que você quer logar
Utilize o comando:
Shell
docker exec <id do container> -ti /bin/bash
1
docker exec <id do container> -ti /bin/bash
No comando acima, a flag -ti indica que você vai inciar um terminal interativo e o /bin/bash indica qual tipo de shell você vai utilizar. Você pode substituir este valor por sh.

Após utilizar utilizar este comando, seu terminal vai mudar e indicar que você está dentro do container. Agora você consegue acessar e modificar todos os arquivos que estão naquele container. Para sair, utilize o comando exit.


>> docker exec <id do container> -ti /bin/bash
>> docker exec c8c4ef5a14f4 -it /bin/bash
>> docker exec -it c8c4ef5a14f4 bash
>> root@c8c4ef5a14f4:/#
     
>> root@c8c4ef5a14f4:/# echo hello
hello 

>> root@c8c4ef5a14f4:/# exit
exit

C:\Users\Yuan>docker stop c8c4ef5a14f4
c8c4ef5a14f4

====================================================================================================================================

C:\Users\Yuan>docker commit c8c4ef5a14f4 yuan/ubuntu
sha256:bf32953a561f94c33b6eaa14507771d638f52e35d3ee9195f694a3df3947062a

C:\Users\Yuan>docker images
REPOSITORY                 TAG       IMAGE ID       CREATED          SIZE
yuan/ubuntu                latest    bf32953a561f   47 seconds ago   72.8MB
jupyter/pyspark-notebook   latest    484925ed0451   21 hours ago     3.21GB
ubuntu                     latest    597ce1600cf4   7 days ago       72.8MB
hello-world                latest    feb5d9fea6a5   2 weeks ago      13.3kB

C:\Users\Yuan>












C:\Users\Yuan>docker login
Authenticating with existing credentials...
Login Succeeded

C:\Users\Yuan>docker push yuan/ubuntu
Using default tag: latest
The push refers to repository [docker.io/yuan/ubuntu]
74f3e21680f2: Preparing                                        da55b45d310b: Preparing                                        denied: requested access to the resource is denied


denied: requested access to the resource is denied

C:\Users\Yuan>

docker rm [OPTIONS] CONTAINER [CONTAINER...]


C:\Users\Yuan>docker rm bf32953a561f
Error: No such container: bf32953a561f




C:/Users/Yuan/Desktop/Docker_Test_Tutorial/cd_for_docker
```
