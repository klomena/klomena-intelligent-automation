# Klomena Backend (FastAPI)

This folder contains the FastAPI backend that powers the Klomena MVP. It exposes endpoints for intent parsing, vendor plan search, add-on recommendations, and basic vendor administration.

## 1. Prerequisites
- Python 3.11
- [Poetry](https://python-poetry.org/) for dependency management
- Running PostgreSQL database (local Docker or managed instance)

## 2. Setup
1. Install dependencies:
   ```bash
   poetry install
   ```
2. Copy the environment template and adjust credentials:
   ```bash
   cp .env.example .env
   # Update DATABASE_URL with your actual Postgres username/password/host
   ```

## 3. Apply the Initial Migration
The SQL in `infrastructure/migrations/0001_init.sql` creates the `vendors` and `graph_edges` tables.

```bash
cd backend
# Replace the connection string below with your credentials (it should match DATABASE_URL but without the "+psycopg" driver hint).
psql "postgresql://postgres:postgres@localhost:5432/klomena" -f infrastructure/migrations/0001_init.sql
```

## 4. Seed Sample Data
Populate the database with the starter vendors and Celebration Graph edges.

```bash
cd backend
poetry run python -m app.seed.seed
```

This will load the JSON files under `app/seed/data/`.

## 5. Run the API Locally
Start the FastAPI app with auto-reload:

```bash
cd backend
poetry run uvicorn app.main:app --reload
```

The interactive docs will be available at http://127.0.0.1:8000/docs once the server is running.
