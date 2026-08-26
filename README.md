🌤️ Weather Pipeline - Projeto de ETL Meteorológico
https://img.shields.io/badge/Python-3.14-blue.svg
https://img.shields.io/badge/Airflow-3.1.7-orange.svg
https://img.shields.io/badge/PostgreSQL-16-blue.svg
https://img.shields.io/badge/Docker-24.0-blue.svg

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
┌─────────────────────────────────────────────────────────┐
│                    Apache Airflow                       │
│                     (Orquestrador)                      │
└─────────────────────┬───────────────────────────────────┘
                      │
                      ▼
┌─────────────────────────────────────────────────────────┐
│                    EXTRACT (extract_data.py)            │
│  ┌─────────────────────────────────────────────────┐   │
│  │   OpenWeatherMap API → JSON → weather_data.json │   │
│  └─────────────────────────────────────────────────┘   │
└─────────────────────┬───────────────────────────────────┘
                      │
                      ▼
┌─────────────────────────────────────────────────────────┐
│                   TRANSFORM (transform_data.py)         │
│  ┌─────────────────────────────────────────────────┐   │
│  │  JSON → DataFrame → Normalização → Limpeza      │   │
│  │  → Renomeio de colunas → Conversão de Datetime  │   │
│  └─────────────────────────────────────────────────┘   │
└─────────────────────┬───────────────────────────────────┘
                      │
                      ▼
┌─────────────────────────────────────────────────────────┐
│                      LOAD (load_data.py)                │
│  ┌─────────────────────────────────────────────────┐   │
│  │       DataFrame → PostgreSQL (sp_weather)      │   │
│  └─────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────┘

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
