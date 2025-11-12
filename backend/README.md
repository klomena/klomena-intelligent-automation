# Klomena Backend

FastAPI backend for Klomena Intelligent Automation.

## Setup

1. Install dependencies:
```bash
pip install -e .
```

2. Copy `.env.example` to `.env` and configure:
```bash
cp .env.example .env
```

3. Seed the database:
```bash
python -m app.seed.seed
```

4. Run the development server:
```bash
uvicorn app.main:app --reload
```

The API will be available at `http://localhost:8000`

## API Endpoints

- `GET /health` - Health check
- `POST /parse-intent` - Parse user intent from text
- `POST /plans/search` - Search for celebration plans
- `POST /addons/recommend` - Get addon recommendations
- `GET /vendors` - List vendors (with optional `city` and `category` filters)
- `GET /vendors/{vendor_id}` - Get a specific vendor

## API Documentation

Once the server is running, visit:
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`
