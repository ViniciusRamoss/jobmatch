# jobmath

Ranks job postings by fit with your résumé and explains each score: strengths, gaps, and why.

> 🚧 Work in progress. The full README (usage, example output, architecture) comes with the MVP.

## Development setup

Requires [uv](https://docs.astral.sh/uv/).

```bash
uv sync                  # create .venv and install pinned dependencies
cp .env.example .env     # adjust as needed
uv run jobmath --help
```

Checks (same as CI):

```bash
uv run ruff check && uv run ruff format --check && uv run mypy && uv run pytest
```
