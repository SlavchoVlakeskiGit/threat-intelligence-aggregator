# Threat Intelligence Aggregator

A backend service that imports threat intelligence indicators, stores them in a MySQL database, analyzes logs for IOC matches, and generates alerts.

## Overview

Security teams often need to compare internal log activity against known malicious IP addresses and domains. This project provides a simple backend service for collecting threat indicators and matching them against log entries.

## Features

- Import threat indicators from a JSON feed
- Store indicators in MySQL
- Ingest log data through REST endpoints
- Match logs against known malicious indicators
- Generate alerts for suspicious matches
- Query indicators, logs, and alerts
- Run scheduled threat feed refresh jobs

## Tech Stack

- Python
- FastAPI
- MySQL
- SQLAlchemy
- APScheduler
- pytest

## Project Status

In development.