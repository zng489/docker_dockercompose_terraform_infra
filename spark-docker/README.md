# 🐳 Spark + Hadoop + Jupyter — Ambiente Docker

> Documentação do cluster local com Apache Spark, HDFS e JupyterLab rodando via Docker Compose.

---

## 📁 Estrutura Geral

```
spark-docker/
├── spark/
│   └── Dockerfile          # Imagem do Spark Master e Workers
├── hadoop/
│   └── Dockerfile          # Imagem do HDFS NameNode e DataNode
├── jupyter/
│   └── Dockerfile          # Imagem do JupyterLab com PySpark
└── docker-compose.yml      # Orquestração de todos os serviços
```

---

## 🏗️ Arquitetura do Cluster

```
┌──────────────────────────────────────────────────────┐
│                    spark-net                          │
│                                                      │
│  Jupyter ──────────────────▶ Spark Master (:7077)    │
│  (:8888)                        │                    │
│                           ┌─────┴─────┐              │
│                           ▼           ▼              │
│                     Worker 1     Worker 2            │
│                     (:8081)      (:8081)             │
│                                                      │
│  HDFS DataNode ◀──────────▶ HDFS NameNode (:8020)   │
│  (:9864)                      (:9870)                │
│                                                      │
└──────────────────────────────────────────────────────┘
```

---

## 🌐 Portas e Mapeamentos

### Portas internas dos containers

| Container        | Porta | Protocolo  | Função                                          |
|------------------|-------|------------|-------------------------------------------------|
| spark-master     | 7077  | Spark RPC  | Workers e clientes enviam/recebem jobs          |
| spark-master     | 8080  | HTTP       | UI web do Master                                |
| spark-worker-1   | 8081  | HTTP       | UI web do Worker 1                              |
| spark-worker-2   | 8081  | HTTP       | UI web do Worker 2                              |
| jupyter          | 8888  | HTTP       | Interface JupyterLab                            |
| hdfs-namenode    | 8020  | Hadoop RPC | DataNodes e clientes HDFS se conectam           |
| hdfs-namenode    | 9870  | HTTP       | UI web do NameNode                              |
| hdfs-datanode    | 9864  | HTTP       | UI web do DataNode                              |

### Mapeamento Container → Host (formato `"HOST:CONTAINER"` no compose)

| Container        | Porta no Container | Porta no Host | No docker-compose.yml |
|------------------|--------------------|---------------|-----------------------|
| spark-master     | 8080               | 8080          | `"8080:8080"`         |
| spark-master     | 7077               | 7077          | `"7077:7077"`         |
| spark-worker-1   | 8081               | 8081          | `"8081:8081"`         |
| spark-worker-2   | 8081               | **8082**      | `"8082:8081"`         |
| jupyter          | 8888               | 8888          | `"8888:8888"`         |
| hdfs-namenode    | 9870               | 9870          | `"9870:9870"`         |
| hdfs-namenode    | 8020               | 8020          | `"8020:8020"`         |
| hdfs-datanode    | 9864               | 9864          | `"9864:9864"`         |

> **Por que o Worker 2 usa porta 8082 no host?**
> O processo do Worker sempre roda na porta 8081 dentro do container.
> Como o Worker 1 já ocupa a porta 8081 no host, o Worker 2 é mapeado para 8082.
> `Browser → localhost:8082 → Docker → container → porta 8081`

---

## 🔗 Conexões Internas (rede `spark-net`)

```
Jupyter          →  spark-master:7077     (envia jobs PySpark)
spark-worker-1   →  spark-master:7077     (se registra, recebe tarefas)
spark-worker-2   →  spark-master:7077     (se registra, recebe tarefas)
hdfs-datanode    →  hdfs-namenode:8020    (se registra, reporta blocos)
```

---

## 🌍 URLs para acesso no Browser

| Serviço           | URL                                        |
|-------------------|--------------------------------------------|
| Spark Master UI   | http://localhost:8080                      |
| Spark Worker 1 UI | http://localhost:8081                      |
| Spark Worker 2 UI | http://localhost:8082                      |
| JupyterLab        | http://localhost:8888?token=spark123       |
| HDFS NameNode UI  | http://localhost:9870                      |
| HDFS DataNode UI  | http://localhost:9864                      |

---

## ⚙️ Dockerfiles — Problemas e Soluções

### 🔶 Spark (`spark/Dockerfile`)

**Problema:** O download do binário do Spark com `-q` (quiet) silencia erros, dificultando diagnóstico.

```dockerfile
# ❌ Com -q: erros ficam ocultos — difícil de depurar
RUN wget -q https://...

# ✅ Alternativa mais segura para depuração:
RUN wget https://...
```

**Versões a verificar:**
- Conferir a versão do Spark (`SPARK_VERSION`) está correta e disponível no mirror
- Testar o link de download antes de rodar o build
- Às vezes é necessário fazer login no Docker Hub para acessar algumas imagens base

**Abordagens testadas para download:**

```dockerfile
# Opção 1: curl com pipe direto
RUN curl -fsSL https://archive.apache.org/dist/spark/spark-${SPARK_VERSION}/spark-${SPARK_VERSION}-bin-hadoop3.tgz \
    | tar -xz -C /opt && mv /opt/spark-${SPARK_VERSION}-bin-hadoop3 ${SPARK_HOME}

# Opção 2: wget com extração manual (mais explícita)
RUN wget https://dlcdn.apache.org/spark/spark-${SPARK_VERSION}/spark-${SPARK_VERSION}-bin-hadoop3.tgz \
    && tar xf spark-${SPARK_VERSION}-bin-hadoop3.tgz \
    && mv spark-${SPARK_VERSION}-bin-hadoop3 ${SPARK_HOME} \
    && rm spark-${SPARK_VERSION}-bin-hadoop3.tgz
```

> **Nota sobre Alpine (musl) vs glibc:**
> O Spark usa libs nativas (ex: Snappy para compressão Parquet) compiladas para glibc.
> Se a imagem base for Alpine (musl), adicione `gcompat` no `apk add`.

---

### 🔷 Hadoop (`hadoop/Dockerfile`)

**Dockerfile final recomendado:**

```dockerfile
FROM eclipse-temurin:17-jre-alpine

# gcompat: necessário porque libhadoop.so foi compilada para glibc (não musl/Alpine)
RUN apk add --no-cache bash wget procps tini gcompat

ENV HADOOP_VERSION=3.3.6
ENV HADOOP_HOME=/opt/hadoop
ENV PATH="${HADOOP_HOME}/bin:${HADOOP_HOME}/sbin:${PATH}"
ENV HDFS_NAMENODE_USER=root
ENV HDFS_DATANODE_USER=root

RUN wget -q https://archive.apache.org/dist/hadoop/common/hadoop-${HADOOP_VERSION}/hadoop-${HADOOP_VERSION}.tar.gz \
    && tar xf hadoop-${HADOOP_VERSION}.tar.gz \
    && mv hadoop-${HADOOP_VERSION} ${HADOOP_HOME} \
    && rm hadoop-${HADOOP_VERSION}.tar.gz

# Desabilita libs nativas para evitar SIGSEGV (segfault) no DataNode em Alpine
# Também adiciona flags de módulos Java 17 para compatibilidade com JAXB/WebHDFS
RUN printf 'export JAVA_HOME=${JAVA_HOME}\n\
export HADOOP_OPTS="${HADOOP_OPTS} -Djava.library.path="\n\
export HADOOP_NAMENODE_OPTS="${HADOOP_NAMENODE_OPTS} --add-opens java.base/java.lang=ALL-UNNAMED"\n\
export HADOOP_DATANODE_OPTS="${HADOOP_DATANODE_OPTS} --add-opens java.base/java.lang=ALL-UNNAMED"\n\
export HADOOP_OPTIONAL_TOOLS=""\n' >> ${HADOOP_HOME}/etc/hadoop/hadoop-env.sh

# Remove as libs nativas para garantir que não sejam carregadas
RUN rm -f ${HADOOP_HOME}/lib/native/*

# core-site.xml: define o endereço do NameNode
RUN printf '<?xml version="1.0"?>\n\
<configuration>\n\
  <property>\n\
    <name>fs.defaultFS</name>\n\
    <value>hdfs://hdfs-namenode:8020</value>\n\
  </property>\n\
</configuration>\n' > ${HADOOP_HOME}/etc/hadoop/core-site.xml

# hdfs-site.xml: desabilita verificação de permissões (ok para desenvolvimento local)
RUN printf '<?xml version="1.0"?>\n\
<configuration>\n\
  <property>\n\
    <name>dfs.permissions.enabled</name>\n\
    <value>false</value>\n\
  </property>\n\
</configuration>\n' > ${HADOOP_HOME}/etc/hadoop/hdfs-site.xml

WORKDIR ${HADOOP_HOME}
ENTRYPOINT ["tini", "--"]
```

**Problemas resolvidos:**

| Problema                          | Causa                                         | Solução                                                |
|-----------------------------------|-----------------------------------------------|--------------------------------------------------------|
| DataNode crasha com SIGSEGV       | `libhadoop.so` usa glibc, imagem usa musl     | Adicionar `gcompat`; remover libs nativas              |
| `NoClassDefFoundError` no JAXB    | Java 17 não carrega JAXB sem flags extras      | `--add-opens java.base/java.lang=ALL-UNNAMED`          |
| Permissão negada no HDFS          | DataNode pertence ao root, Jupyter roda como jovyan | `dfs.permissions.enabled=false` no hdfs-site.xml |
| `HADOOP_OPTS` ignorado pelo DataNode | Variável de ambiente não propagada corretamente | Definir diretamente no `hadoop-env.sh`              |

---

### 🟢 Jupyter (`jupyter/Dockerfile`)

**Problema: Java ausente**

A abordagem de copiar o Java de outra imagem com `COPY --from` não funciona se a imagem de origem não tiver Java no caminho esperado:

```dockerfile
# ❌ Não funciona — eclipse-temurin:17-jre-alpine não expõe /opt/java
COPY --from=eclipse-temurin:17-jre-alpine /opt/java /opt/java
```

**Solução: instalar Java diretamente via apt:**

```dockerfile
# ✅ Instala Java via apt — necessário para SparkSession funcionar
RUN apt-get update && apt-get install -y --no-install-recommends \
    wget curl tini procps default-jre-headless \
    && rm -rf /var/lib/apt/lists/*

ENV JAVA_HOME=/usr/lib/jvm/java-17-openjdk-amd64
ENV PATH="${JAVA_HOME}/bin:${PATH}"
```

> ⚠️ **Importante:** O caminho do `JAVA_HOME` deve estar correto.
> Sem isso, a `SparkSession` falha ao iniciar — o PySpark não consegue localizar a JVM.

> **Por que Jupyter não precisa de `gcompat`?**
> A imagem base do Jupyter é Debian, que já usa glibc nativamente.
> `gcompat` só é necessário em Alpine (que usa musl).

---

## 📊 Resumo: `gcompat` por imagem

| Imagem                        | Precisa de `gcompat`? | Motivo                                      |
|-------------------------------|----------------------|---------------------------------------------|
| spark (Workers/Master)        | ✅ Sim               | Snappy (compressão Parquet) usa glibc       |
| hadoop (NameNode + DataNode)  | ✅ Sim               | `libhadoop.so` usa glibc                    |
| jupyter                       | ❌ Não               | Base Debian já tem glibc                    |

---

## ⚠️ Limitação Conhecida: HDFS WebUI no Docker

### O "Browse Directory" não consegue abrir arquivos

Isso é uma **limitação arquitetural**, não um bug de configuração.

**Por quê acontece:**
1. O NameNode faz um **HTTP redirect** para o DataNode
2. Esse redirect usa **hostnames internos do container** (ex: `hdfs-datanode`)
3. O navegador no host **não consegue resolver esses hostnames internos**

**Solução:** Não existe via configuração simples. Exigiria que o Hadoop implementasse proxy em vez de redirect, ou modificação no código-fonte do HDFS.

### O que funciona e o que não funciona:

| Operação                                  | Status                    |
|-------------------------------------------|---------------------------|
| Gravar arquivos via Spark                 | ✅ Funciona               |
| Ler arquivos via Spark                    | ✅ Funciona               |
| Listar via terminal (`hdfs dfs -ls`)      | ✅ Funciona               |
| WebHDFS REST API (`?op=LISTSTATUS`)       | ✅ Funciona               |
| Navegar diretórios na UI web              | ✅ Funciona               |
| Ver **conteúdo** de arquivos na UI web    | ❌ Limitação no Docker    |

### Testando via WebHDFS REST API:

```bash
# Listar arquivos em um diretório
curl http://localhost:9870/webhdfs/v1/teste/ui/?op=LISTSTATUS
```

> Para **estudo e desenvolvimento**, o ambiente está completo.
> A limitação do WebUI é apenas cosmética — não afeta o uso real do HDFS.

---

## 🛠️ Comandos Úteis

```bash
# Subir o cluster
docker compose up -d

# Ver status de todos os containers
docker compose ps

# Ver logs de um container específico
docker compose logs spark-master
docker compose logs -f jupyter          # -f = acompanha em tempo real
docker compose logs hdfs-namenode
docker compose logs hdfs-datanode

# Parar todos os containers
docker compose down

# Parar e remover volumes (⚠️ dados serão perdidos)
docker compose down -v

# Entrar num container interativamente
docker exec -it jupyter bash
docker exec -it spark-master bash

# Reiniciar um container específico
docker compose restart spark-worker-1

# Build de uma imagem específica (ex: durante desenvolvimento)
docker build -t testing .
docker build -t jupyter .
```

---

## 📝 Notas Adicionais

- O flag `-q` no `wget` silencia a saída — útil em produção, mas **evite durante depuração** pois esconde erros
- Sempre verifique a versão do Spark/Hadoop disponível no mirror antes de definir `SPARK_VERSION` / `HADOOP_VERSION`
- O token padrão do JupyterLab no ambiente é `spark123` (configurável no docker-compose.yml)