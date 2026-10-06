# Visual Blueprint Search

Visual Blueprint Search is a document search service for architectural and
engineering PDFs. It is organized as a FastAPI backend with planned ingestion,
retrieval, and Next.js frontend layers.

## Project layout

- `src/visual_blueprint_search/api`: HTTP application and routers
- `src/visual_blueprint_search/core`: application configuration
- `src/visual_blueprint_search/schemas`: request and response contracts
- `src/visual_blueprint_search/ingestion`: PDF parsing, OCR/VLM, and indexing
- `src/visual_blueprint_search/retrieval`: search and answer generation
- `src/visual_blueprint_search/storage`: PostgreSQL, Qdrant, and page-image adapters
- `apps/web`: reserved for the Next.js frontend
- `data`: local PDFs and rendered page images (ignored by Git)

## Quick start

1. Install [uv](https://docs.astral.sh/uv/) and create the environment:

   ```powershell
   uv sync
   ```

2. Copy the environment template and adjust credentials:

   ```powershell
   Copy-Item .env.example .env
   ```

3. Start local infrastructure:

   ```powershell
   docker compose up -d
   ```

4. Run the API:

   ```powershell
   uv run uvicorn visual_blueprint_search.api.main:app --reload
   ```

The health endpoint is available at <http://127.0.0.1:8000/health>.

## Development

Run the checks with:

```powershell
uv run ruff check .
uv run pytest
```

The API contracts should be established before implementing the frontend in
`apps/web`.