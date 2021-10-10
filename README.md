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

```
# Imagem com Jupyter Notebook e algumas bibliotecas.

FROM python:3.8-slim-buster

RUN mkdir -p /home/notebooks

WORKDIR /home/notebooks

RUN pip install numpy \ pandas \ scikit-learn \ tensorflow \ seaborn \ jupyter \ notebook

EXPOSE 8888

ENTRYPOINT [ "jupyter", "notebook", "--ip=0.0.0.0", "--allow-root", "--no-browser" ]

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
