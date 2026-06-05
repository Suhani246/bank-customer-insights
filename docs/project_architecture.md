# Project Architecture

The project follows an end-to-end analytics pipeline architecture.

## Workflow

1. Synthetic data generation using Python
2. Raw CSV data storage
3. Data cleaning and ETL processing
4. PostgreSQL relational database loading
5. SQL analytical querying
6. Power BI dashboard visualization

---

## Architecture Flow

Python Scripts
↓
Raw CSV Files
↓
ETL Cleaning
↓
PostgreSQL Database
↓
SQL Analytics
↓
Power BI Dashboards

---

## Components

### Python
Used for:
- Data generation
- ETL pipeline
- Data transformation

### PostgreSQL
Used for:
- Relational database storage
- Table relationships
- SQL analytics

### Power BI
Used for:
- KPI dashboards
- Business intelligence reporting
- Data visualization