[>]Activate conda env
>> conda activate ambiente



[>] Docker
>> sudo systemctl start docker
>> docker infos
>> docker ps # Ver o que esta rodando
>> docker stop <nome-ou-id-do-container> 
>> docker stop c3a2012dd98f 
>> docker rm <nome-ou-id-do-container>
>> docker rmi e81e0a41fed7 # IMAGE ID
>> docker images
>> docker run -d -p 5000:5000 --name python-on-kube-container python-on-kube
>> http://localhost:5000
>> docker exec -it python-on-kube-container /bin/bash
>> exit
>> docker stop $(docker ps -q)



[>] Docker Login
>> docker login
>> yuan489@hotmail.com
>> 28dockerhub
>> docker tag NOME_LOCAL USUARIO_DOCKER/NOME_REPO:TAG
| Campo                       | O que é                                     | Exemplo          |
| --------------------------- | ------------------------------------------- | ---------------- |
| `NOME_LOCAL`                | Nome da sua imagem Docker local             | `python-on-kube` |
| `USUARIO_DOCKER`            | Seu nome de usuário no Docker Hub           | `fulano123`      |
| `NOME_REPO`                 | Nome que o repositório terá no Docker Hub   | `python-on-kube` |
| `TAG` (opcional, mas comum) | Versão da imagem (ex: `latest`, `v1`, etc.) | `latest`         |
>> docker tag python-on-kube yuan28/exemplo_push:teste
>> docker push yuan28/exemplo_push:teste



[>] Setar como docker padrao - Quando você usa docker context use default, está dizendo que quer que todos os comandos Docker sejam executados no contexto padrão, geralmente o Docker que está rodando localmente na sua máquina.
>> docker context use default
>> default
>> Current context is now "default"



[>] permission denied while trying to connect to the Docker daemon socket at unix:///var/run/docker.sock: Get "http://%2Fvar%2Frun%2Fdocker.sock/v1.51/info": dial unix /var/run/docker.sock: connect: permission denied
>> groups
asus adm cdrom sudo dip plugdev users lpadmin
>> sudo usermod -aG docker $USER
>> newgrp docker
>> groups
>> docker adm cdrom sudo dip plugdev users lpadmin asus



[>] docker-credential-desktop issues
>> nano ~/.docker/config.json
>> comentar
>> {
>>   // "credsStore": "desktop"
>> }
>> No nano: pressione Ctrl + O para salvar, depois Ctrl + X para sair.
>> WARNING: Error parsing config file (/home/asus/.docker/config.json): invalid character '/' looking for beginning of object >> key string
>> Para tirar esse warning message apenas deletar // "credsStore": "desktop"



[>] Minikube, verifica se esta ativado ou nao
>> minikube start
>> minikube status
>> minikube profile list



[>] Minikube, verifica se esta ativado ou nao
>> kubectl get services
>> kubectl get pods
>> minikube stop
>> minikube start
>> eval $(minikube docker-env)
>> docker build -t python-on-kube .
>> kubectl delete deployment python-on-kube
>> kubectl delete service python-on-kube-service
>> kubectl apply -f deployment.yaml
>> kubectl apply -f service.yaml
>> kubectl get pods
>> minikube service python-on-kube-service --url
>> kubectl get svc python-on-kube-service



sudo apt install flatpak



Explicando passo a passo:

Você acessa a aplicação no seu PC, no navegador ou curl, usando:

IP da Minikube + porta NodePort, ex: 192.168.58.2:30000

Ou com o comando minikube service <nome> --url que retorna essa URL.

Minikube encaminha a requisição da porta NodePort (ex: 30000) para a porta do Service dentro do cluster (ex: 6000).

O Service encaminha para a porta correta do Pod (container), que está rodando sua aplicação na porta 5000.

A aplicação Python Flask dentro do container escuta na porta 5000 e responde.



# Usar uma imagem base do Python # FROM python:3.9-slim # Copiar o script Python para o contêiner # COPY main.py /kubernetes/main.py # Definir o diretório de trabalho como /app # WORKDIR /kubernetes # Executar o script Python quando o contêiner for iniciado # CMD ["python", "main.py"] #FROM python:3.12 # RUN mkdir /app # WORKDIR /app # ADD . /app/ # RUN pip install -r requirements.txt # EXPOSE 5000 # CMD ["python", "/app/main.py"] # Imagem base com Python FROM python:3.9-slim # Definir o diretório de trabalho no contêiner WORKDIR /app # Copiar os arquivos da aplicação para dentro do contêiner COPY . . # Instalar as dependências RUN pip install -r requirements.txt # Expor a porta 5000 EXPOSE 5000 # Comando para rodar a aplicação CMD ["python", "app.py"] apiVersion: apps/v1 kind: Deployment metadata: name: python-on-kube # docker build -t python-on-kube . labels: app: python-on-kube # docker build -t python-on-kube . spec: replicas: 4 selector: matchLabels: app: python-on-kube # docker build -t python-on-kube . template: metadata: labels: app: python-on-kube # docker build -t python-on-kube . spec: containers: - name: python-on-kube image: python-on-kube imagePullPolicy: IfNotPresent #imagePullPolicy: Never ports: - containerPort: 5000 # resources: # limits: # memory: 512Mi # cpu: "1" # requests: # memory: 256Mi # cpu: "0.1" apiVersion: v1 kind: Service metadata: name: python-on-kube-service spec: selector: app: python-on-kube ports: - protocol: "TCP" port: 6000 targetPort: 5000 type: NodePort rodar ni minikube kubernetes



(ambiente) asus@asus-VivoBook-S14-X430UN:~/Desktop/docker_minikube_kuberbetes$ kubectl get pods
kubectl get services
NAME                              READY   STATUS    RESTARTS   AGE
python-on-kube-7877bc4d67-2b8bp   1/1     Running   0          14s
python-on-kube-7877bc4d67-2mdc8   1/1     Running   0          14s
python-on-kube-7877bc4d67-ghdfk   1/1     Running   0          14s
python-on-kube-7877bc4d67-rvhfs   1/1     Running   0          14s
NAME                     TYPE        CLUSTER-IP       EXTERNAL-IP   PORT(S)          AGE
kubernetes               ClusterIP   10.96.0.1        <none>        443/TCP          26m
python-on-kube-service   NodePort    10.105.184.136   <none>        6000:31410/TCP   



Report this ad
0

    Update your system

    sudo apt update && sudo apt upgrade -y

    Download the latest .deb package

    wget https://github.com/shiftkey/desktop/releases/download/release-3.4.1-linux1/GitHubDesktop-linux-amd64-3.4.1-linux1.deb

    Install the package

    sudo apt install ./GitHubDesktop-linux-amd64-3.4.1-linux1.deb -y

