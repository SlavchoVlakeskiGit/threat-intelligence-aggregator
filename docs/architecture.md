# Architecture

```text
Threat Feed JSON
      |
      v
Indicator Import Service
      |
      v
 Indicators Table (MySQL)
      |
      +-------------------+
                          |
                          v
                Log Ingestion API
                          |
                          v
                   IOC Matching Service
                          |
                          v
                     Alerts Table
                          |
                          v
                     Alerts API
```

## Components

### 1. Threat Feed Import
Reads a local JSON feed and stores indicators in MySQL.

### 2. Log Ingestion
Accepts log entries through REST endpoints or sample file import.

### 3. IOC Matching
Checks ingested logs against stored indicators for exact IP and domain matches.

### 4. Alert Generation
Creates alerts with severity based on indicator confidence score.

## Current Severity Rules

- 85 and above -> high
- 60 to 84 -> medium
- below 60 -> low
