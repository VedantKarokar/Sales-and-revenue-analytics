# Sales & Revenue Analytics
> End-to-end retail analytics from raw Superstore data to PostgreSQL, through SQL transformation, into a Power BI dashboard.

---

## Project Overview
This repository supports a sales analytics workflow for Superstore retail data. It includes:
- a data load script for PostgreSQL,
- database schema definition,
- SQL feature/query files,
- and a dashboard access section for the final Power BI report.

---

## Repository Contents
```
Sales-and-revenue-analytics/
├── README.md
├── docker-compose.yml
├── load_data.py
├── requirements.txt
├── data/
│   └── Superstore.csv
├── schema/
│   └── schema.sql
└── queries/
    ├── features.sql
    └── views.sql
```

### Key files
- `load_data.py` — loads `data/Superstore.csv` into PostgreSQL using SQLAlchemy.
- `requirements.txt` — Python dependencies required for data loading.
- `schema/schema.sql` — PostgreSQL table schema definition for the Superstore data.
- `queries/features.sql` — SQL logic for feature creation and analytics.
- `queries/views.sql` — SQL views built for reporting and dashboard consumption.

---

## Dashboard Access
View the interactive [**Dashboard**](https://app.powerbi.com/reportEmbed?reportId=31407923-9d8f-4c28-961e-5b697ac08fd3&autoAuth=true&ctid=17e5a684-4de3-47a4-8d5f-dbc9bd6f5bb9) to explore sales, profitability, and customer insights.

> Click the Dashboard link above to open the live Power BI report in your browser.

---

## Dataset
**Source:** [Superstore Sales Dataset — Kaggle](https://www.kaggle.com/datasets/vivek468/superstore-dataset-final)

**Description:** A retail dataset containing order, customer, product, shipping, sales, discount, and profit information. The dataset is used for sales performance analysis, product profitability, regional performance, and customer value.

---

## Tools Used
- PostgreSQL
- Python 3
- SQLAlchemy
- pandas
- Power BI Desktop
- Docker

---

## Setup and Run
1. Install Python dependencies from `requirements.txt`:

   ```powershell
   pip install -r requirements.txt
   ```
2. Configure PostgreSQL credentials in a `.env` file, use '.env.example' as a reference.
3. Create `/data` and place `Superstore.csv` inside it.
4. Run the command
    ```powershell
    docker compose up
    ```
    and connect to PostgreSQL using any thirdparty extension.
4. Run the command in powershell `python load_data.py` to create the `superstore` table and load the data.
5. Use the SQL files in `/queries` to build analytics views.
6. Open the Power BI dashboard using link or connect it to the PostgreSQL database if needed.

---

## Notes
- `load_data.py` checks whether the `superstore` table already contains rows and skips loading if data exists.
- `schema/schema.sql` documents the expected table structure for this project.

