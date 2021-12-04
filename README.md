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

==========================================================================================
==========================================================================================

# Dockerfile

```
# Imagem com Jupyter Notebook e algumas bibliotecas.
# Folder + Dockerfile

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

docker build -t image-ds .

docker run -d --rm --name jupyterserver -p 8888:8888 -v "c:/Users/Yuan/Desktop/folder/new:/home/notebooks" image-ds

docker container logs jupyterserver

C:\Users\Yuan\Desktop\folder>docker images
REPOSITORY               TAG       IMAGE ID       CREATED         SIZE
image-ds                 latest    8348a24c62a1   2 minutes ago   2.41GB
jupyter/scipy-notebook   latest    19b33596f37c   2 days ago      2.57GB
mongo                    latest    c1a14d3979c5   9 days ago      691MB
nginx                    latest    f8f4ffc8092c   12 days ago     133MB
continuumio/anaconda3    latest    f78cb37fb1bd   4 weeks ago     2.81GB
docker/getting-started   latest    083d7564d904   4 months ago    28MB

```
==========================================================================================
==========================================================================================

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

```
>> docker run -it -p 8888:8888 -v "c:/Users/Yuan/Desktop/pyspark_notebook:/home" jupyter/pyspark-notebook /bin/bash
                                   => Folder of your computer:Folder of your container
>> (base) root@b385e6ba35f5:/# ls
>> bin  boot  dev  etc  home  lib  lib64  media  mnt  opt  proc  root  run  sbin  srv  sys  tmp  usr  var
>> (base) root@b385e6ba35f5:/# home
>> bash: home: command not found
>> (base) root@b385e6ba35f5:/# cd /home/
                            ==> Folder of container
>> (base) root@b385e6ba35f5:/home# jupyter notebook --ip='*' --port=8888 --no-browser --allow-root &
>> http://b385e6ba35f5:8888/?token=14a31f116e1aac471fcd9b03390fc3dcf5e937e426cd33a


docker run -d --rm --name jupyterserver -p 8888:8888 -v "c:/Users/Yuan/Desktop/pyspark_notebook:/home" pyspark 



jupyter/pyspark-notebook

docker run -d -p 8888:8888 -e JUPYTER_ENABLE_LAB=yes --name zhang_pyspark -v "c:/Users/Yuan/Desktop/pyspark_notebook:/home/jovyan/work" jupyter/pyspark-notebook

docker run -d -p 8888:8888 --name zhang_pyspark -v "c:/Users/Yuan/Desktop/pyspark_notebook:/home/jovyan/work" jupyter/pyspark-notebook
```




# DOCKERFILE
```
=========================================================================================================================
FROM python:3.8-slim-buster

RUN mkdir -p /folder
WORKDIR /folder

RUN pip install --upgrade pip

COPY requirements.txt ./
RUN pip install -r requirements.txt

RUN pip install numpy \ pandas \ scikit-learn \ tensorflow \ seaborn \ plotly \ jupyter \ notebook

EXPOSE 8888

ENTRYPOINT [ "jupyter", "notebook", "--ip=0.0.0.0", "--allow-root", "--no-browser" ]
=========================================================================================================================
-r requirements.txt

absl-py==0.14.1
argon2-cffi==21.1.0
astunparse==1.6.3
attrs==21.2.0
backcall==0.2.0
beautifulsoup4==4.10.0
bleach==4.1.0
bs4==0.0.1
cachetools==4.2.4
cassandra-driver==3.25.0
certifi==2021.10.8
cffi==1.15.0
chardet==4.0.0
charset-normalizer==2.0.7
clang==5.0
click==8.0.3
colorama==0.4.4
cycler==0.10.0
debugpy==1.5.0
decorator==5.1.0
defusedxml==0.7.1
entrypoints==0.3
et-xmlfile==1.1.0
flatbuffers==1.12
gast==0.4.0
geomet==0.2.1.post1
google-auth==2.3.0
google-auth-oauthlib==0.4.6
google-pasta==0.2.0
greenlet==1.1.2
grpcio==1.41.0
h5py==3.1.0
idna==3.3
ipykernel==6.4.1
ipython==7.28.0
ipython-genutils==0.2.0
ipywidgets==7.6.5
jedi==0.18.0
Jinja2==3.0.2
joblib==1.1.0
jsonschema==4.1.0
jupyter==1.0.0
jupyter-client==7.0.6
jupyter-console==6.4.0
jupyter-core==4.8.1
jupyterlab-pygments==0.1.2
jupyterlab-widgets==1.0.2
keras==2.6.0
Keras-Preprocessing==1.1.2
kiwisolver==1.3.2
Markdown==3.3.4
MarkupSafe==2.0.1
matplotlib==3.4.3
matplotlib-inline==0.1.3
mistune==0.8.4
nbclient==0.5.4
nbconvert==6.2.0
nbformat==5.1.3
nest-asyncio==1.5.1
notebook==6.4.4
numpy==1.19.5
oauthlib==3.1.1
openpyxl==3.0.9
opt-einsum==3.3.0
packaging==21.0
pandas==1.3.3
pandocfilters==1.5.0
parso==0.8.2
pexpect==4.8.0
pickleshare==0.7.5
Pillow==8.3.2
plotly==5.3.1
prometheus-client==0.11.0
prompt-toolkit==3.0.20
protobuf==3.18.1
ptyprocess==0.7.0
pyasn1==0.4.8
pyasn1-modules==0.2.8
pycparser==2.20
Pygments==2.10.0
pyparsing==2.4.7
pyrsistent==0.18.0
python-dateutil==2.8.2
pytz==2021.3
pywinpty==0.5.7
pyzmq==22.3.0
qtconsole==5.1.1
QtPy==1.11.2
requests==2.26.0
requests-oauthlib==1.3.0
retrying==1.3.3
rsa==4.7.2
scikit-learn==1.0
scipy==1.7.1
seaborn==0.11.2
Send2Trash==1.8.0
simplegeneric==0.8.1
six==1.15.0
sklearn==0.0
soupsieve==2.2.1
SQLAlchemy==1.4.25
tenacity==8.0.1
tensorboard==2.7.0
tensorboard-data-server==0.6.1
tensorboard-plugin-wit==1.8.0
tensorflow==2.6.0
tensorflow-estimator==2.6.0
termcolor==1.1.0
terminado==0.12.1
testpath==0.5.0
threadpoolctl==3.0.0
tornado==6.1
traitlets==5.1.0
typing-extensions==3.7.4.3
Unidecode==1.3.2
urllib3==1.26.7
wcwidth==0.2.5
webencodings==0.5.1
Werkzeug==2.0.2
widgetsnbextension==3.5.1
win-unicode-console==0.5
wincertstore==0.2
wrapt==1.12.1
xlrd==2.0.1
=========================================================================================================================
-r requirements.txt

absl-py
argon2-cffi
astunparse
attrs
backcall
beautifulsoup4
bleach
bs4
cachetools
cassandra-driver
certifi
cffi
chardet
charset-normalizer
clang
click
colorama
cycler
debugpy
decorator
defusedxml
entrypoints
et-xmlfile
flatbuffers
gast
geomet
google-auth
google-auth-oauthlib
google-pasta
greenlet
grpcio
h5py
idna
ipykernel
ipython
ipython-genutils
ipywidgets
jedi
Jinja2
joblib
jsonschema
jupyter
jupyter-client
jupyter-console=
jupyter-core==4.8.1
jupyterlab-pygments==0.1.2
jupyterlab-widgets==1.0.2
keras==2.6.0
Keras-Preprocessing==1.1.2
kiwisolver==1.3.2
Markdown==3.3.4
MarkupSafe==2.0.1
matplotlib==3.4.3
matplotlib-inline==0.1.3
mistune==0.8.4
nbclient==0.5.4
nbconvert==6.2.0
nbformat==5.1.3
nest-asyncio==1.5.1
notebook==6.4.4
numpy==1.19.5
oauthlib==3.1.1
openpyxl==3.0.9
opt-einsum==3.3.0
packaging==21.0
pandas==1.3.3
pandocfilters==1.5.0
parso==0.8.2
pexpect==4.8.0
pickleshare==0.7.5
Pillow==8.3.2
plotly==5.3.1
prometheus-client==0.11.0
prompt-toolkit==3.0.20
protobuf==3.18.1
ptyprocess==0.7.0
pyasn1==0.4.8
pyasn1-modules==0.2.8
pycparser==2.20
Pygments==2.10.0
pyparsing==2.4.7
pyrsistent==0.18.0
python-dateutil==2.8.2
pytz==2021.3
pywinpty==0.5.7
pyzmq==22.3.0
qtconsole==5.1.1
QtPy==1.11.2
requests==2.26.0
requests-oauthlib==1.3.0
retrying==1.3.3
rsa==4.7.2
scikit-learn==1.0
scipy
seaborn
Send2Trash
simplegeneric
six
sklearn
soupsieve
SQLAlchemy
tenacity
tensorboard
tensorboard-data-server
tensorboard-plugin-wit
tensorflow
tensorflow-estimator
termcolor
terminado
testpath
threadpoolctl
tornado
traitlets
typing-extensions
Unidecode
urllib3
wcwidth
webencodings
Werkzeug
widgetsnbextension
win-unicode-console
wincertstore
wrapt
xlrd
=========================================================================================================================
docker build -t zhang .
=========================================================================================================================
docker run -d --rm --name jupyterserver -p 8888:8888 -v "c:/Users/Yuan/Desktop/Building:/folder" zhang
=========================================================================================================================
```

# Docker Normal
```
=========================================================================================================================
docker run -d -p 8888:8888 -e JUPYTER_ENABLE_LAB=yes --name zhang_pyspark -v "c:/Users/Yuan/Desktop/pyspark_notebook:/home/jovyan/work" jupyter/pyspark-notebook
=========================================================================================================================
docker run -d -p 8888:8888 --name zhang_pyspark -v "c:/Users/Yuan/Desktop/pyspark_notebook:/home/jovyan/work" jupyter/pyspark-notebook
=========================================================================================================================
```


```html

Go to the

<a href="dasdasda" style="font-style: italic">
    
    Markdown Monster Web Site
    
</a>

```

# Docker Repository

```
Repository create: yuan28/pyspark

Commando to push: C:\Users\Yuan>docker tag c402ee9c2d7f yuan28/pyspark:tagname <tagname> can be anything, it`s just ID created..

C:\Users\Yuan>docker images
REPOSITORY                 TAG       IMAGE ID       CREATED        SIZE
dbc2csv                    latest    66ae2082b35c   42 hours ago   617MB
jupyter/pyspark-notebook   latest    c402ee9c2d7f   2 days ago     3.32GB
zhang                      latest    15f58dab56b9   3 weeks ago    2.67GB

C:\Users\Yuan>docker push yuan28/pyspark:tagname <tagname> can be anything, it`s just ID created..
```

# Docker Full Code

```
docker container run --publish 80:80 nginx
- docker container run
- docker run(old way)
- 8888(any port whatever you want it):80
```


# Differences between "CMD" and "ENTRYPOINT
```
CMD

The CMD instruction has three forms:

    CMD ["executable","param1","param2"] (exec form, this is the preferred form)
    CMD ["param1","param2"] (as default parameters to ENTRYPOINT)
    CMD command param1 param2 (shell form)
------------------------------------------
	### CMD ###

FROM ubuntu:latest

CMD ["echo","Hello"]

TERMINAL:
>>docker run --rm wesleywillians/hello
Hello

>>docker run --rm wesleywillians/hello echo "ola"
ola

>>docker run --rm wesleywillians/hello bash
>>

CMD:
- It`s a flexible command, which means basically you can replace for any command you want it.

- É um command flexível, ou seja, você pode substituir por qualquer comando.


	### ENTRYPOINT ###

FROM ubuntu:latest

ENTRYPOINT ["echo","Hello"]

TERMINAL:
>>docker run --rm wesleywillians/hello bash
Hello bash

ENTRYPOINT:
- It`s a not flexible command.

```

```
COPY .. 
- copiando todos arquivos da minha maquina no container

RUN go build main.go

EXPOSE 8080

ENTRYPOINT ["./main"]
```
