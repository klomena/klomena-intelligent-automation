-- Schema setup for the Klomena MVP backend.

CREATE TABLE IF NOT EXISTS vendors (
    id TEXT PRIMARY KEY,
    name TEXT NOT NULL,
    areas_served TEXT[] NOT NULL,
    categories TEXT[] NOT NULL,
    themes TEXT[] NOT NULL,
    price_band INTEGER NOT NULL CHECK (price_band BETWEEN 1 AND 3),
    age_min INTEGER NOT NULL,
    age_max INTEGER NOT NULL CHECK (age_min <= age_max),
    is_verified BOOLEAN NOT NULL DEFAULT FALSE,
    response_time_score DOUBLE PRECISION,
    freshness_score DOUBLE PRECISION,
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    updated_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

CREATE TABLE IF NOT EXISTS graph_edges (
    id SERIAL PRIMARY KEY,
    relation_type TEXT NOT NULL,
    source_node_type TEXT NOT NULL,
    source_value TEXT NOT NULL,
    target_node_type TEXT NOT NULL,
    target_value TEXT NOT NULL,
    weight DOUBLE PRECISION NOT NULL DEFAULT 1.0,
    CONSTRAINT uq_graph_edge UNIQUE (
        relation_type,
        source_node_type,
        source_value,
        target_node_type,
        target_value
    )
);
