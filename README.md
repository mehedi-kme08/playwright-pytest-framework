# Playwright + pytest Test Automation Framework

End-to-end UI and API test framework built with Playwright and pytest,
using Page Object Model and GitHub Actions CI.

## Features
- UI tests with Page Object Model (playwright.dev)
- Full CRUD API tests (JSONPlaceholder)
- Session-scoped API fixtures
- GitHub Actions workflow — runs on every push/PR
- Containerized — run the full suite with a single `docker run`

## Tech Stack
Python 3.13 · Playwright · pytest · GitHub Actions

## Run locally
```bash
python -m venv venv
venv\Scripts\activate        # Windows
pip install -r requirements.txt
playwright install chromium
pytest -v
```
## Run with Docker
```bash
docker build -t playwright-tests .
docker run --rm playwright-tests
```
## Project structure
- `pages/` — page objects (locators + actions, no assertions)
- `tests/` — UI and API test suites
- `.github/workflows/` — CI pipeline
