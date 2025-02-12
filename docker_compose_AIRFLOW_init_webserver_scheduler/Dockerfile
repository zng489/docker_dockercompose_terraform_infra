##### FROM apache/airflow:2.10.1

#USER root

# FROM apache/airflow:1.10.9
#ADD requirements.txt .
##### COPY requirements.txt /requirements.txt
##### RUN pip install --user --upgrade pip
##### RUN pip install --no-cache-dir --user -r /requirements.txt 
#RUN pip install apache-airflow==${AIRFLOW_VERSION} -r requirements.txt
#https://stackoverflow.com/questions/67887138/how-to-install-packages-in-airflow-docker-compose

# Customize the airflow.cfg file


FROM apache/airflow:2.10.1
# Optionally, specify the shell without complex options
##### SHELL ["/bin/sh", "-c"]

# You don't need to switch to root as Airflow images typically run as root by default.
# Uncomment the following line if needed for specific operations
# USER root

# Copy the requirements file into the container
COPY requirements.txt /requirements.txt

# Upgrade pip globally without the --user flag
RUN pip install --upgrade pip

# Install the required packages without the --user flag
RUN pip install --no-cache-dir -r /requirements.txt

# Optionally switch back to the airflow user (if you uncommented the USER root line)
# USER airflow




#FROM apache/airflow:2.6.0
#COPY requirements.txt /requirements.txt
#RUN pip install --upgrade pip
#RUN pip install --no-cache-dir -r /requirements.txt