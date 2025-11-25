# Backend - Embarked Telemetry

## Project Structure

```
backend/
├── src/
│   ├── main.py                 # Application entry point
│   ├── _types/                 # Pydantic data models
│   │   ├── address.py
│   │   ├── location.py
│   │   └── telemetry.py
│   ├── configs/                # Configuration and instances
│   │   ├── constants.py
│   │   ├── instances.py        # FastAPI app and database instances
│   │   └── queries.py          # SQL queries
│   ├── databases/              # Database utilities
│   │   ├── PostgreConnection.py
│   │   └── PostgreUtil.py
│   └── routes/                 # API routes
│       └── pages/
│           ├── address.py
│           ├── location.py
│           └── telemetry.py
├── requirements.txt            # Python dependencies
└── README.md
```

## Getting Started

### Prerequisites

- Python 3.8 or higher
- PostgreSQL database

### Configuration

1. **Create `.env` file:**
   Fill in your PostgreSQL credentials:
   ```
   POSTGRE_HOST=localhost
   POSTGRE_PORT=5432
   POSTGRE_DATABASE=your_database_name
   POSTGRE_USER=your_username
   POSTGRE_PASSWORD=your_password
   ```

### Installation

1. **Create virtual environment:**

   ```bash
   py -m venv .venv
   ```

2. **Activate virtual environment:**

   ```bash
   .venv/scripts/activate
   ```

3. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Navigate to source directory:**

   ```bash
   cd ./src
   ```

5. **Run the application:**
   ```bash
   py main.py
   ```

The server will start on `http://127.0.0.1:8000`

## API Endpoints

- `GET /api/v1/location` - Get all locations
- `GET /api/v1/address` - Get all addresses
- `GET /api/v1/telemetry` - Get combined location and address data
