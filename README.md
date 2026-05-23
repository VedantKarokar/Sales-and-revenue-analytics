# Sales_dashboard
> An end-to-end data analytics project — from raw retail data in PostgreSQL to an interactive client-facing dashboard in Power BI.

**Status:** In progress

---

## Business Problem

A retail business wants a single, clear view of their sales performance. The goal is to help the owner answer three questions without digging through spreadsheets:

- Where are we making money, and where are we losing it?
- Which products and regions are driving growth?
- Who are our most valuable customers?

This project delivers an interactive Power BI dashboard that answers those questions at a glance.

---

## Project Structure

```
sales-revenue-analytics/
│
├── README.md
├── data/
│   └── .gitignore          # Raw CSV files are excluded from version control
├── queries/
│   ├── 01_data_audit.sql
│   ├── 02_revenue_summary.sql
│   ├── 03_category_performance.sql
│   ├── 04_regional_breakdown.sql
│   ├── 05_customer_ranking.sql
│   └── 06_mom_growth.sql
└── findings/
    └── key_findings.md     # Written narrative — added on project completion
```

---

## Dataset

**Source:** [Superstore Sales Dataset — Kaggle](https://www.kaggle.com/datasets/vivek468/superstore-dataset-final)

**Description:** A retail orders dataset containing 9,994 records across orders, customers, products, and regions. Covers sales, profit, discount, and shipping data from 2015–2018.

> The raw CSV is not committed to this repository. Download it directly from Kaggle using the link above and place it in the `/data` folder.

---

## Tools Used

| Layer | Tool |
|---|---|
| Database | PostgreSQL 16 |
| SQL Interface | pgAdmin 4 |
| Dashboard | Power BI Desktop |
| Version control | GitHub |

---

## Analytical Approach

### Phase 1 — SQL Analysis (PostgreSQL)

All data shaping, aggregation, and business logic is handled in SQL before anything enters Power BI. Each query is saved as a numbered `.sql` file and answers one specific business question.

| Step | Query | Business question answered |
|---|---|---|
| 1 | Data audit | Is the data clean and complete? |
| 2 | Revenue & profit summary | How are we performing overall, by month? |
| 3 | Category & product performance | Which categories and products are most profitable? |
| 4 | Regional breakdown | Which regions and cities drive the most revenue? |
| 5 | Customer value ranking | Who are our top customers by lifetime value? |
| 6 | Month-over-month growth | Are we growing? How does this month compare to last? |

### Phase 2 — Dashboard (Power BI)

The dashboard is structured across three pages, each answering a distinct business question:

- **Page 1 — Executive summary:** KPI cards (revenue, profit, orders, AOV) + monthly trend + category breakdown
- **Page 2 — Product & profitability:** Margin by sub-category, loss-making products, discount impact analysis
- **Page 3 — Customers & geography:** Regional map, top customer table, new vs returning breakdown

---

## Key Findings

*To be added on project completion.*

---

## How to Reproduce

1. Clone this repository
2. Download the Superstore dataset from Kaggle (link above) and place it in `/data`
3. Run the SQL scripts in `/queries` in numbered order against a PostgreSQL database
4. Open the Power BI `.pbix` file and reconnect to your local PostgreSQL instance

<iframe title="S&R dashboard" width="1140" height="541.25" src="https://app.powerbi.com/reportEmbed?reportId=31407923-9d8f-4c28-961e-5b697ac08fd3&autoAuth=true&ctid=17e5a684-4de3-47a4-8d5f-dbc9bd6f5bb9" frameborder="0" allowFullScreen="true"></iframe>
---
