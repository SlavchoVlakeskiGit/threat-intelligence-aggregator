# Threat Intelligence Aggregator

A FastAPI backend for importing threat indicators, ingesting logs, and generating alerts when a log matches a known IOC.

I wanted a project that sits somewhere between backend development and security work, without making it overly complex.

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

I wanted a project that sits somewhere between backend development and security work. It gave me a chance to model a full workflow instead of just building isolated endpoints.

The matching part was the most interesting part for me because it made the app feel less like plain data storage and more like an actual process with a purpose.

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

```bash
git clone https://github.com/SlavchoVlakeskiGit/threat-intelligence-aggregator.git
cd threat-intelligence-aggregator
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Before starting the API, create a local MySQL database and update the connection string in your environment variables.

Open `/docs` in the browser to test the endpoints.

## Typical flow

1. load or import indicators
2. ingest sample logs or events
3. run matching logic
4. review generated alerts

## Notes

This is not meant to replace a SIEM or a full threat platform. I kept the project fairly contained on purpose so the ingestion and matching flow stays easy to understand.

The matching logic started simple, but even that was enough to surface interesting patterns in the sample data.

## Possible next improvements

- scheduled feed refresh
- indicator expiration handling
- severity scoring
- cleaner reporting endpoints
