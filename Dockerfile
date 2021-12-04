##############################################################
# Building a image from a pre-build
FROM jupyter/pyspark-notebook:latest

##############################################################
# Creating a directory for your file in the container

#RUN mkdir -p /home/notebooks
#WORKDIR /home/notebooks

# Or just simple like that, it depende on what do you want it 
RUN mkdir -p /home/jovyan/workspace
WORKDIR /home/jovyan/workspace

##############################################################
# Installling

# Updating
RUN pip install --upgrade pip

# Copy files and installing
#COPY requirements.txt ./  
# Or Copy files in the /home/jovyan/work and installing
COPY requirements.txt /home/jovyan/workspace
# Or copying all the files
#COPY ..
# Executing the installation
RUN pip install -r requirements.txt

# Installling
RUN pip install numpy \ pandas \ scikit-learn \ tensorflow \ seaborn
##############################################################

EXPOSE 8888

#Short answer:
#EXPOSE is a way of documenting
#--publish (or -p) is a way of mapping a host port to a running container port
#Notice below that:
#
#EXPOSE is related to Dockerfiles ( documenting )
#--publish is related to docker run ... ( execution / run-time )

#############################################################################################

ENTRYPOINT [ "jupyter", "notebook", "--ip=0.0.0.0", "--allow-root", "--no-browser" ]


# acessar meu servidor local por ip usando o comando mostrado abaixo:
#jupyter notebook --ip xx.xx.xx.xx --port 8888
# substitua o xx.xx.xx.xxpelo seu ip local do servidor jupyter.
# usei jupyter notebook --ip 0.0.0.0 --port 8888 0.0.0.0permitirá o acesso ao notebook em todas as interfaces de rede, não apenas localhost. Se você estiver executando e acessando na mesma máquina, ou estiver executando um servidor como o nginx na frente dele, você deve limitá-lo a 127.0.0.1apenas 

##########################################################################################

# docker build -t jupyter_yuan .


# docker run -p 8988:8888 -v "c:/Users/Yuan/Desktop/Jupyter_Docker:/home/jovyan/workspace" jupyter_yuan

# -p = --publish


# Commando to push: C:\Users\Yuan>docker tag c402ee9c2d7f yuan28/pyspark:tagname <tagname> can be anything, it`s just ID created..
# docker tag f35f5304b517 jupyter_yuan:notebook


