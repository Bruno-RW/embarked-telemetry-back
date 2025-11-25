# Backend - Embarked Telemetry

## Estrutura do Projeto

```
backend/
├── src/
│   ├── main.py                 # Ponto de entrada da aplicação
│   ├── _types/                 # Modelos de dados Pydantic
│   │   ├── address.py
│   │   ├── location.py
│   │   └── telemetry.py
│   ├── configs/                # Configuração e instâncias
│   │   ├── constants.py
│   │   ├── instances.py        # Instâncias do FastAPI e banco de dados
│   │   └── queries.py          # Consultas SQL
│   ├── databases/              # Utilitários de banco de dados
│   │   ├── PostgreConnection.py
│   │   └── PostgreUtil.py
│   └── routes/                 # Rotas da API
│       └── pages/
│           ├── address.py
│           ├── location.py
│           └── telemetry.py
├── requirements.txt            # Dependências Python
└── README.md
```

## Começando

### Pré-requisitos

- Python 3.8 ou superior
- Banco de dados PostgreSQL

### Configuração

1. **Criar arquivo `.env`:**
   Preencha suas credenciais do PostgreSQL:
   ```
   POSTGRE_HOST=localhost
   POSTGRE_PORT=5432
   POSTGRE_DATABASE=nome_do_seu_banco
   POSTGRE_USER=seu_usuario
   POSTGRE_PASSWORD=sua_senha
   ```

### Instalação

1. **Criar ambiente virtual:**

   ```bash
   py -m venv .venv
   ```

2. **Ativar ambiente virtual:**

   ```bash
   .venv/scripts/activate
   ```

3. **Instalar dependências:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Navegar para diretório de origem:**

   ```bash
   cd ./src
   ```

5. **Executar a aplicação:**
   ```bash
   py main.py
   ```

O servidor será iniciado em `http://127.0.0.1:8000`

## Endpoints da API

- `GET /api/v1/location` - Obter todas as localizações
- `GET /api/v1/address` - Obter todos os endereços
- `GET /api/v1/telemetry` - Obter dados combinados de localização e endereço
