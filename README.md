# Threat Intelligence Aggregator

Backend service for ingesting threat intelligence feeds, processing logs, and generating alerts when malicious indicators are detected.

This project demonstrates a simplified SOC automation pipeline built with Python, FastAPI, and MySQL.

---

## Architecture Overview

Threat Feed JSON -> Indicators Database -> Log Ingestion -> IOC Matching -> Alerts API

Workflow:

1. Import threat indicators (malicious IPs and domains)
2. Store indicators in a MySQL database
3. Ingest log entries
4. Compare logs against known indicators
5. Generate alerts when matches are detected

---

## Features

- Threat intelligence ingestion from JSON feeds
- Log ingestion through REST API
- Automatic IOC matching
- Alert generation for malicious indicators
- Confidence-based severity scoring
- MySQL database persistence
- REST API built with FastAPI
- Swagger API documentation
- Sample data import for testing
- Basic automated tests

---

## Tech Stack

- Python
- FastAPI
- MySQL
- SQLAlchemy
- PyMySQL
- Pydantic
- Uvicorn
- Pytest

---

## Project Structure

```text
threat-intelligence-aggregator
│
├── app
│   ├── api
│   │   ├── alerts.py
│   │   ├── health.py
│   │   ├── indicators.py
│   │   └── logs.py
│   ├── core
│   │   └── config.py
│   ├── db
│   │   ├── database.py
│   │   └── init_db.py
│   ├── models
│   │   ├── alert.py
│   │   ├── indicator.py
│   │   └── log_entry.py
│   ├── schemas
│   │   ├── alert.py
│   │   ├── indicator.py
│   │   └── log_entry.py
│   ├── services
│   │   ├── alert_service.py
│   │   ├── feed_service.py
│   │   ├── log_service.py
│   │   └── matching_service.py
│   └── main.py
│
├── sample_data
│   ├── threat_feed.json
│   └── sample_logs.json
├── tests
│   ├── test_alerts.py
│   ├── test_health.py
│   ├── test_indicators.py
│   └── test_logs.py
├── docs
│   └── architecture.md
├── requirements.txt
├── pytest.ini
├── .gitignore
├── LICENSE
└── README.md
```

---

## Setup

```bash
git clone https://github.com/YOUR_USERNAME/threat-intelligence-aggregator.git
cd threat-intelligence-aggregator
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

---

## Database Setup

Create database and user:

```sql
CREATE DATABASE threat_intel_db;

CREATE USER 'threat_user'@'localhost' IDENTIFIED BY 'yourpassword';

GRANT ALL PRIVILEGES ON threat_intel_db.* TO 'threat_user'@'localhost';

FLUSH PRIVILEGES;
```

Create `.env` file in the project root:

```env
DATABASE_URL=mysql+pymysql://threat_user:yourpassword@127.0.0.1:3306/threat_intel_db
APP_NAME=Threat Intelligence Aggregator
APP_VERSION=1.0.0
```

Initialize tables:

```bash
python -m app.db.init_db
```

---

## Run the API

```bash
uvicorn app.main:app --reload
```

Open Swagger docs:

```text
http://127.0.0.1:8000/docs
```

---

## Example Workflow

Import threat indicators:

```text
POST /api/indicators/import
```

Import sample logs:

```text
POST /api/logs/import
```

Check alerts:

```text
GET /api/alerts/
```

If a log matches a malicious IP or domain from the threat feed, the system automatically generates an alert.

---

## Example Alert

```json
{
  "matched_value": "185.220.101.1",
  "indicator_type": "ip",
  "severity": "high",
  "description": "Log entry matched malicious IP indicator: 185.220.101.1 (confidence: 90)"
}
```

---

## Limitations

- Uses local sample JSON feeds instead of live threat intelligence sources
- Matching is currently exact-match only
- Alert scoring is rule-based and simplified
- API does not yet include authentication or rate limiting

---

## Running Tests

```bash
python -m pytest
```

---

## Future Improvements

- Integration with real threat intelligence feeds
- Scheduled feed ingestion
- SIEM log ingestion pipelines
- Authentication for protected endpoints
- Indicator expiration and source weighting
- Docker deployment
- Web dashboard for alerts and indicators

---

## License

MIT
