# Threat Intelligence Aggregator

Backend service for ingesting threat intelligence feeds, processing
logs, and generating alerts when malicious indicators are detected.

This project demonstrates how a simplified **SOC automation pipeline**
can be implemented using Python, FastAPI, and MySQL.

------------------------------------------------------------------------

## Architecture Overview

Threat Feed → Indicators Database\
Logs → IOC Matching → Alerts

Workflow:

1.  Import threat indicators (malicious IPs and domains)
2.  Store indicators in a MySQL database
3.  Ingest log entries
4.  Compare logs against known indicators
5.  Generate alerts when matches are detected

------------------------------------------------------------------------

## Features

-   Threat intelligence ingestion from JSON feeds
-   Log ingestion through REST API
-   Automatic IOC matching
-   Alert generation for malicious indicators
-   Confidence-based severity scoring
-   MySQL database persistence
-   REST API built with FastAPI
-   Swagger API documentation
-   Sample data import for testing
-   Basic automated tests

------------------------------------------------------------------------

## Tech Stack

-   Python
-   FastAPI
-   MySQL
-   SQLAlchemy
-   PyMySQL
-   Pydantic
-   Uvicorn
-   Pytest

------------------------------------------------------------------------

## Project Structure

    threat-intelligence-aggregator
    │
    ├── app
    │   ├── api
    │   │   ├── alerts.py
    │   │   ├── health.py
    │   │   ├── indicators.py
    │   │   └── logs.py
    │   │
    │   ├── core
    │   │   └── config.py
    │   │
    │   ├── db
    │   │   ├── database.py
    │   │   └── init_db.py
    │   │
    │   ├── models
    │   │   ├── alert.py
    │   │   ├── indicator.py
    │   │   └── log_entry.py
    │   │
    │   ├── schemas
    │   │   ├── alert.py
    │   │   ├── indicator.py
    │   │   └── log_entry.py
    │   │
    │   ├── services
    │   │   ├── alert_service.py
    │   │   ├── feed_service.py
    │   │   ├── log_service.py
    │   │   └── matching_service.py
    │   │
    │   └── main.py
    │
    ├── sample_data
    │   ├── threat_feed.json
    │   └── sample_logs.json
    │
    ├── tests
    │   └── test_health.py
    │
    ├── docs
    │   └── api_preview.png
    │
    ├── requirements.txt
    ├── pytest.ini
    ├── .gitignore
    └── README.md

------------------------------------------------------------------------

## Setup

Clone repository:

    git clone https://github.com/YOUR_USERNAME/threat-intelligence-aggregator.git
    cd threat-intelligence-aggregator

Create virtual environment:

    python -m venv venv

Activate environment (Windows):

    venv\Scripts\activate

Install dependencies:

    pip install -r requirements.txt

------------------------------------------------------------------------

## Database Setup

Create database and user:

    CREATE DATABASE threat_intel_db;

    CREATE USER 'threat_user'@'localhost' IDENTIFIED BY 'yourpassword';

    GRANT ALL PRIVILEGES ON threat_intel_db.* TO 'threat_user'@'localhost';

    FLUSH PRIVILEGES;

Create `.env` file:

    DATABASE_URL=mysql+pymysql://threat_user:yourpassword@localhost:3306/threat_intel_db
    APP_NAME=Threat Intelligence Aggregator
    APP_VERSION=1.0.0

Initialize tables:

    python -m app.db.init_db

------------------------------------------------------------------------

## Run the API

    uvicorn app.main:app --reload

Swagger docs:

    http://127.0.0.1:8000/docs

------------------------------------------------------------------------

## Example Workflow

Import threat feed:

    POST /api/indicators/import

Import logs:

    POST /api/logs/import

Check alerts:

    GET /api/alerts/

If a log matches a malicious IP or domain from the threat feed, the
system automatically generates an alert.

------------------------------------------------------------------------

## Example Alert

    {
      "matched_value": "185.220.101.1",
      "indicator_type": "ip",
      "severity": "high",
      "description": "Log entry matched malicious IP indicator"
    }

------------------------------------------------------------------------

## Running Tests

    python -m pytest

------------------------------------------------------------------------

## Future Improvements

-   Integration with real threat intelligence feeds
-   Scheduled feed ingestion
-   SIEM log ingestion pipelines
-   Alert severity scoring improvements
-   Web dashboard
-   Docker deployment

------------------------------------------------------------------------

## License

MIT
