# Threat Intelligence Aggregator

A FastAPI backend project that imports threat indicators, stores them in MySQL, ingests log entries, and raises alerts when a log matches a known indicator.

I built this to practice a backend workflow that is a bit more specific than a generic CRUD app: data ingestion, persistence, matching logic, and alert generation.

## What it does

- imports threat indicators from JSON sample feeds
- stores indicators in MySQL
- accepts log entries through API endpoints
- checks logs against stored indicators
- creates alerts when a match is found
- exposes endpoints for indicators, logs, alerts, and health checks

## Tech stack

- Python
- FastAPI
- MySQL
- SQLAlchemy
- Pytest

## Why I built it

I wanted a project that sits between backend development and security.

The goal was not to build a full SOC product. The goal was to show that I can model a workflow, break it into API endpoints and services, and implement the matching logic cleanly.

## Architecture

```text
Threat feed JSON -> Indicators table -> Log ingestion -> IOC matching -> Alerts
```

## Project structure

```text
threat-intelligence-aggregator/
├── app/
│   ├── api/
│   ├── core/
│   ├── db/
│   ├── models/
│   ├── schemas/
│   └── services/
├── docs/
├── sample_data/
├── tests/
├── .env.example
├── pytest.ini
├── requirements.txt
└── README.md
```

## Run locally

### 1. Clone the repo

```bash
git clone https://github.com/SlavchoVlakeskiGit/threat-intelligence-aggregator.git
cd threat-intelligence-aggregator
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure the database

Create a local MySQL database and update the connection string in your environment variables.

### 4. Start the API

```bash
uvicorn app.main:app --reload
```

### 5. Open the docs

Open `/docs` in the browser to test the endpoints.

## Sample workflow

A typical flow in this project is:

1. load indicator data
2. store indicators in the database
3. submit log entries
4. compare logs against indicators
5. review generated alerts

## What this repo is meant to show

This repo is strongest when it is framed as a backend practice project with a security-themed use case.

It shows:

- API design
- database-backed application structure
- service-layer logic
- simple matching rules
- tests and sample data

## Useful next improvements

- deduplication of repeated indicators
- more explicit severity rules
- better request/response examples in the README
- clearer sample payloads for indicator and log ingestion

## Notes

Keep the wording grounded. This is a portfolio backend project with a security use case, not a commercial threat intel platform.
