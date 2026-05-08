# ETL de Notas Fiscais com Python e PostgreSQL

## Sobre o projeto

Este projeto simula um pipeline ETL utilizado em integrações de sistemas ERP com prefeituras e serviços de emissão fiscal.

O pipeline realiza:

- Extração de dados em JSON
- Transformação e validação dos dados
- Carga de dados no PostgreSQL
- Tratamento de duplicidade
- Logging de execução
- Utilização de variáveis de ambiente (.env)

---

## Tecnologias utilizadas

- Python
- PostgreSQL
- DBeaver
- psycopg2
- python-dotenv

---

## Estrutura do projeto

```bash
etl-notas-fiscais/
│
├── data/
├── logs/
├── sql/
├── src/
├── venv/
├── .env
├── .gitignore
├── README.md
└── requirements.txt
```

---

## Funcionalidades

- Inserção automatizada de notas fiscais
- Verificação de notas duplicadas
- Logs de execução
- Integração Python + PostgreSQL
- Pipeline ETL modularizado

---

## Como executar

### 1. Clone o repositório

```bash
git clone URL_DO_REPOSITORIO
```

---

### 2. Crie o ambiente virtual

```bash
python -m venv venv
```

---

### 3. Ative o ambiente virtual

#### Windows

```bash
venv\Scripts\activate
```

#### Linux/macOS

```bash
source venv/bin/activate
```

---

### 4. Instale as dependências

```bash
pip install -r requirements.txt
```

---

### 5. Configure o arquivo .env

```env
DB_HOST=localhost
DB_PORT=5434
DB_NAME=etl_notas
DB_USER=postgres
DB_PASSWORD=sua_senha
```

---

### 6. Execute o script SQL

Arquivo:

```bash
sql/create_tables.sql
```

---

### 7. Execute o projeto

Entre na pasta src:

```bash
cd src
```

Depois execute:

```bash
python main.py
```

---

## Melhorias futuras

- Docker
- Integração com XML
- API REST
- Dashboard
- Orquestração de pipeline
- Pandas para transformação de dados

---

## Autor

Victor Rothmann