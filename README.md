🏗 Bank Marketing ETL Pipeline
📌 Project Overview

This project simulates a real-world data engineering task where marketing campaign data must be cleaned, standardized, and structured for PostgreSQL ingestion.

The bank requires a clean and scalable dataset so future marketing campaign data can be seamlessly imported into their relational database.


🎯 Business Objective

The bank wants:

Clean and validated campaign data

A consistent schema

PostgreSQL-compatible data types

Structured tables to support future campaign imports

This project implements a modular ETL pipeline to meet those requirements.


🏛 Architecture

Extract → Transform → Load → Visualize

1️⃣ Extract

Reads bank_marketing.csv

Validates file

Logs extraction details

2️⃣ Transform

Standardizes column names

Removes duplicates

Converts categorical values

Enforces strict numeric and boolean types

Applies business rules

Splits dataset into normalized relational tables

3️⃣ Load

Outputs three PostgreSQL-ready CSV files:

client_data.csv

campaign_data.csv

loan_outcomes.csv

4️⃣ Visualize

Generates analytical figures

Saves visual outputs to /reports/figures

🗄 Database Design
client_data

Primary key: client_id

Contains static demographic information.

campaign_data

Foreign key: client_id

Contains campaign interaction details.

loan_outcomes

Foreign key: client_id

Contains final subscription outcome.

Referential integrity is maintained across tables.

📦 Final Deliverables

After running:

python src/main.py

The pipeline generates:

data/processed/
    client_data.csv
    campaign_data.csv
    loan_outcomes.csv

These files:

Conform to a predefined schema

Use consistent data types

Are directly importable into PostgreSQL

Support future campaign ingestion

🔍 Data Quality Controls

✔ Duplicate removal
✔ Strict data type enforcement
✔ Boolean normalization
✔ Categorical standardization
✔ Business rule handling
✔ Stable primary keys
✔ Referential integrity

🚀 How this Meets the Bank's Requirements
Requirement	Implemented

Clean raw CSV	                        ✅
Enforce schema structure	            ✅
PostgreSQL-ready	                    ✅
Split into 3 structured files	        ✅
Maintain relational integrity	        ✅
Future campaign scalability	            ✅

🛠 Tools

Python

Pandas

PostgreSQL

Matplotlib

Logging

Modular ETL architecture


🏆 Project Outcome

This project transforms raw marketing campaign data into a structured, database-ready format using production-style ETL practices. It ensures data integrity, schema stability, and future scalability for additional campaign imports.
