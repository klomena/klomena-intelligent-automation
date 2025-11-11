"""Entry point for the FastAPI application."""

from fastapi import FastAPI

from .routers import api_router

app = FastAPI(
    title="Klomena API",
    version="0.1.0",
    description="Klomena MVP backend for celebration planning.",
)

app.include_router(api_router)


@app.get("/health", tags=["meta"])
def healthcheck() -> dict[str, str]:
    """Provide a simple health endpoint for uptime checks."""

    return {"status": "ok"}
