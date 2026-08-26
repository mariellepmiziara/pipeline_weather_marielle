🌤️ Weather Pipeline - Projeto de ETL Meteorológico


Pipeline completo de ETL (Extract, Transform, Load) para dados meteorológicos, utilizando a API do OpenWeatherMap, com orquestração via Apache Airflow e armazenamento em PostgreSQL.



🎯 Sobre o Projeto
Este projeto implementa um pipeline de dados automatizado que:

Extrai dados climáticos em tempo real da API OpenWeatherMap
Transforma os dados brutos (JSON) em um DataFrame estruturado
Carrega os dados processados em um banco de dados PostgreSQL
Orquestra todo o processo com Apache Airflow, executando a cada 6 horas

O pipeline é ideal para:
Análise de séries temporais climáticas
Monitoramento de condições meteorológicas
Projetos de ciência de dados com dados reais
Estudos de padrões climáticos

🏗️ Arquitetura
┌─────────────────────────────────────────────────────────────────────────┐
│                                                                         │
│                         APACHE AIRFLOW                                  │
│                        (Orquestrador)                                   │
│                                                                         │
└──────────────────────────────┬──────────────────────────────────────────┘
                               │
                               │ Dispara a DAG a cada 6 horas
                               ▼
┌─────────────────────────────────────────────────────────────────────────┐
│                                                                         │
│  ┌─────────────────────────────────────────────────────────────────┐   │
│  │                    ETAPA 1: EXTRACT                             │   │
│  │                                                                 │   │
│  │   extract_weather_data(url)                                     │   │
│  │        │                                                        │   │
│  │        ▼                                                        │   │
│  │   🌐 OpenWeatherMap API (Requisição HTTP GET)                  │   │
│  │        │                                                        │   │
│  │        ▼                                                        │   │
│  │   📄 weather_data.json (Dados brutos salvos localmente)        │   │
│  └─────────────────────────────────────────────────────────────────┘   │
│                               │                                        │
│                               ▼                                        │
│  ┌─────────────────────────────────────────────────────────────────┐   │
│  │                    ETAPA 2: TRANSFORM                           │   │
│  │                                                                 │   │
│  │   data_transformations()                                        │   │
│  │        │                                                        │   │
│  │        ▼                                                        │   │
│  │   📊 JSON → pandas.DataFrame                                    │   │
│  │        │                                                        │   │
│  │        ▼                                                        │   │
│  │   🔄 Normalização da coluna "weather"                           │   │
│  │        │                                                        │   │
│  │        ▼                                                        │   │
│  │   🗑️ Remoção de colunas desnecessárias                          │   │
│  │        │                                                        │   │
│  │        ▼                                                        │   │
│  │   ✏️ Renomeio de colunas (inglês → português)                   │   │
│  │        │                                                        │   │
│  │        ▼                                                        │   │
│  │   ⏰ Conversão de timestamps para datetime                      │   │
│  └─────────────────────────────────────────────────────────────────┘   │
│                               │                                        │
│                               ▼                                        │
│  ┌─────────────────────────────────────────────────────────────────┐   │
│  │                      ETAPA 3: LOAD                              │   │
│  │                                                                 │   │
│  │   load_weather_data(table_name, df)                             │   │
│  │        │                                                        │   │
│  │        ▼                                                        │   │
│  │   🗄️ PostgreSQL Database (sp_weather table)                    │   │
│  │        │                                                        │   │
│  │        ▼                                                        │   │
│  │   ✅ Log de confirmação e total de registros                   │   │
│  └─────────────────────────────────────────────────────────────────┘   │
│                                                                         │
└─────────────────────────────────────────────────────────────────────────┘

🚀 Tecnologias
Tecnologia	Versão	Finalidade
Python	3.14	Linguagem principal
Apache Airflow	3.1.7	Orquestração do pipeline
PostgreSQL	16	Banco de dados final
Redis	7.2	Broker do Celery (Airflow)
Docker & Docker Compose	Latest	Containerização
Pandas	3.0.5	Manipulação de dados
SQLAlchemy	2.0.51	ORM para PostgreSQL
Requests	2.34.2	Cliente HTTP para API
📦 Pré-requisitos
Docker (24.0+)

Docker Compose (2.20+)

Git

Python 3.14 (para desenvolvimento local, opcional)
