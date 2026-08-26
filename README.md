# 🌤️ Weather Pipeline — Projeto de ETL Meteorológico

Pipeline completo de **ETL (Extract, Transform, Load)** para dados meteorológicos, utilizando a **API OpenWeatherMap**, com orquestração via **Apache Airflow** e armazenamento em **PostgreSQL**.

---

## 🎯 Sobre o Projeto

Este projeto implementa um pipeline de dados automatizado que:

* 🌐 **Extrai** dados climáticos em tempo real da API OpenWeatherMap
* 🔄 **Transforma** os dados brutos em um DataFrame estruturado
* 🗄️ **Carrega** os dados processados em um banco PostgreSQL
* ⚙️ **Orquestra** todo o processo utilizando Apache Airflow
* ⏰ Executa automaticamente a cada **6 horas**

### 💡 Aplicações

O pipeline pode ser utilizado para:

* 📈 Análise de séries temporais climáticas
* 🌡️ Monitoramento de condições meteorológicas
* 🧪 Projetos de ciência de dados com dados reais
* 🌎 Estudos de padrões climáticos
* 📊 Construção de dashboards e análises exploratórias

---

## 🏗️ Arquitetura

```text
                         ┌───────────────────────────┐
                         │       APACHE AIRFLOW      │
                         │       Orquestrador        │
                         └─────────────┬─────────────┘
                                       │
                              Executa a DAG
                              a cada 6 horas
                                       │
                                       ▼
        ┌─────────────────────────────────────────────────────┐
        │                       EXTRACT                       │
        │                                                     │
        │  extract_weather_data(url)                          │
        │                       │                             │
        │                       ▼                             │
        │  🌐 OpenWeatherMap API                              │
        │       Requisição HTTP GET                           │
        │                       │                             │
        │                       ▼                             │
        │  📄 weather_data.json                               │
        │       Dados brutos salvos localmente                │
        └─────────────────────────┬───────────────────────────┘
                                  │
                                  ▼
        ┌─────────────────────────────────────────────────────┐
        │                      TRANSFORM                      │
        │                                                     │
        │  data_transformations()                             │
        │                       │                             │
        │                       ▼                             │
        │  📊 JSON → pandas.DataFrame                         │
        │                       │                             │
        │                       ▼                             │
        │  🔄 Normalização da coluna "weather"                │
        │                       │                             │
        │                       ▼                             │
        │  🗑️ Remoção de colunas desnecessárias              │
        │                       │                             │
        │                       ▼                             │
        │  ✏️ Renomeação de colunas                           │
        │                       │                             │
        │                       ▼                             │
        │  ⏰ Conversão de timestamps para datetime           │
        └─────────────────────────┬───────────────────────────┘
                                  │
                                  ▼
        ┌─────────────────────────────────────────────────────┐
        │                        LOAD                         │
        │                                                     │
        │  load_weather_data(table_name, df)                  │
        │                       │                             │
        │                       ▼                             │
        │  🗄️ PostgreSQL                                      │
        │       Tabela: sp_weather                            │
        │                       │                             │
        │                       ▼                             │
        │  ✅ Log de confirmação                              │
        │       + total de registros carregados               │
        └─────────────────────────────────────────────────────┘
```

### 🔄 Fluxo do Pipeline

```text
OpenWeatherMap API
        │
        ▼
    EXTRACT
        │
        ▼
weather_data.json
        │
        ▼
   TRANSFORM
        │
        ▼
pandas.DataFrame
        │
        ▼
      LOAD
        │
        ▼
    PostgreSQL
        │
        ▼
   sp_weather
```

---

## 🚀 Tecnologias

| Tecnologia        | Versão | Finalidade                           |
| ----------------- | -----: | ------------------------------------ |
| 🐍 Python         |   3.14 | Linguagem principal                  |
| 🛫 Apache Airflow |  3.1.7 | Orquestração do pipeline             |
| 🐘 PostgreSQL     |     16 | Banco de dados final                 |
| 🔴 Redis          |    7.2 | Broker do Celery/Airflow             |
| 🐳 Docker         | Latest | Containerização                      |
| 🐳 Docker Compose | Latest | Gerenciamento dos containers         |
| 🐼 Pandas         |  3.0.5 | Manipulação e transformação de dados |
| 🔗 SQLAlchemy     | 2.0.51 | Conexão/ORM para PostgreSQL          |
| 🌐 Requests       | 2.34.2 | Requisições HTTP para a API          |

---

## 📦 Pré-requisitos

Antes de executar o projeto, certifique-se de ter instalado:

* [Docker](https://www.docker.com/) **24.0+**
* Docker Compose **2.20+**
* Git
* Python **3.14** — opcional, para desenvolvimento local

---

## 🔑 API OpenWeatherMap

O projeto utiliza a **OpenWeatherMap API** para obtenção dos dados meteorológicos.

Para executar o pipeline, é necessário criar uma conta na plataforma e obter uma **API Key**.

A chave deve ser armazenada em uma variável de ambiente e **não deve ser incluída diretamente no código ou versionada no Git**.

Exemplo:

```env
OPENWEATHER_API_KEY=sua_api_key
```

> ⚠️ Nunca publique sua API Key no GitHub.

---

## 📂 Estrutura do Projeto

```text
weather-pipeline/
│
├── dags/
│   └── weather_pipeline.py
│
├── src/
│   ├── extract.py
│   ├── transform.py
│   └── load.py
│
├── data/
│   └── weather_data.json
│
├── docker/
│   └── ...
│
├── .env
├── .gitignore
├── docker-compose.yml
├── requirements.txt
└── README.md
```

---

## ⚙️ Etapas do ETL

### 1️⃣ Extract

A etapa de **Extract** realiza uma requisição HTTP para a API OpenWeatherMap e coleta os dados meteorológicos em formato JSON.

```python
extract_weather_data(url)
```

Os dados brutos são armazenados localmente para posterior processamento.

---

### 2️⃣ Transform

Na etapa de **Transform**, os dados JSON são convertidos em um `pandas.DataFrame` e passam por processos de tratamento.

Principais transformações:

* Conversão de JSON para DataFrame
* Normalização da coluna `weather`
* Remoção de colunas desnecessárias
* Renomeação de colunas
* Conversão de timestamps para `datetime`
* Estruturação dos dados para armazenamento

---

### 3️⃣ Load

A etapa de **Load** utiliza SQLAlchemy para carregar os dados tratados no PostgreSQL.

```python
load_weather_data(table_name, df)
```

Os dados são armazenados na tabela:

```text
sp_weather
```

Após o carregamento, o pipeline registra informações como:

* Status da operação
* Quantidade de registros carregados
* Possíveis erros durante o processo

---

## 🛫 Orquestração com Apache Airflow

O Apache Airflow é responsável por controlar e executar o pipeline.

A DAG executa automaticamente a cada **6 horas**, seguindo o fluxo:

```text
EXTRACT
   │
   ▼
TRANSFORM
   │
   ▼
LOAD
```

Isso permite automatizar todo o processo sem necessidade de execução manual.

---

## 🐳 Execução com Docker

Clone o repositório:

```bash
git clone https://github.com/seu-usuario/weather-pipeline.git
```

Entre no diretório:

```bash
cd weather-pipeline
```

Configure as variáveis de ambiente no arquivo `.env`.

Depois, inicialize os containers:

```bash
docker compose up -d
```

Verifique os containers em execução:

```bash
docker compose ps
```

Para acompanhar os logs:

```bash
docker compose logs -f
```

Para encerrar os serviços:

```bash
docker compose down
```

---

## 🗄️ Banco de Dados

O PostgreSQL é utilizado como camada final de armazenamento.

### Tabela principal

```text
sp_weather
```

Os dados carregados podem posteriormente ser utilizados para:

* Consultas SQL
* Análises exploratórias
* Dashboards
* Estudos de séries temporais
* Projetos de Data Analytics
* Projetos de Machine Learning

---

## 📊 Possíveis Evoluções

Algumas melhorias que podem ser implementadas futuramente:

* [ ] Adicionar testes automatizados
* [ ] Implementar validações de qualidade dos dados
* [ ] Criar logs estruturados
* [ ] Adicionar monitoramento do pipeline
* [ ] Implementar retry automático para chamadas à API
* [ ] Adicionar alertas de falha
* [ ] Criar dashboard em Power BI
* [ ] Implementar armazenamento em Data Lake
* [ ] Adicionar CI/CD
* [ ] Implementar particionamento dos dados
* [ ] Adicionar novas fontes meteorológicas

---

## 🧠 Conceitos de Engenharia de Dados Aplicados

Este projeto demonstra conceitos importantes de Engenharia de Dados:

* **ETL**
* **Data Pipeline**
* **API Integration**
* **Data Transformation**
* **Data Loading**
* **Data Orchestration**
* **Apache Airflow**
* **Docker**
* **PostgreSQL**
* **Python**
* **Pandas**
* **SQLAlchemy**
* **Environment Variables**
* **Data Automation**

---

## 👩‍💻 Autora

**Marielle Miziara**

Projeto desenvolvido como parte do portfólio de **Engenharia de Dados**, com foco em construção e orquestração de pipelines ETL utilizando Python, APIs, Apache Airflow, Docker e PostgreSQL.

---

