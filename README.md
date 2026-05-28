# Superstore Sales & Revenue Analytics
> End-to-end retail analytics from raw Superstore data to PostgreSQL, through SQL transformation, into a Power BI dashboard.
---
## Objective
This analysis answers three business questions:
 
- Where is money being made and where is it being lost?
- Which products, categories, and regions drive the most revenue?
- Who are the most valuable customers?


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
- `load_data.py` - loads `data/Superstore.csv` into PostgreSQL using SQLAlchemy.
- `requirements.txt` - Python dependencies required for data loading.
- `schema/schema.sql` - PostgreSQL table schema definition for the Superstore data.
- `queries/features.sql` - SQL logic for feature creation and analytics.
- `queries/views.sql` - SQL views built for reporting and dashboard consumption.
- `dashboard/dashboard.pbix` - dashboard for cleaning and analysis using visuals.

---

## Tools Used
- PostgreSQL
- Docker
- Python 3
    - SQLAlchemy
    - pandas
- Power BI Desktop

---

## Setup and Run
1. Install Python dependencies from `requirements.txt`:

   ```powershell
   pip install -r requirements.txt
   ```
2. Configure PostgreSQL credentials in a `.env` file, use '.env.example' as a reference.
3. Create `/data` and place `Superstore.csv` inside it and download the dataset from this [link](https://www.kaggle.com/datasets/vivek468/superstore-dataset-final).
5. Run the command
    ```powershell
    docker compose up
    ```
    and connect to PostgreSQL using any thirdparty extension.
4. Run the command in powershell `python load_data.py` to create the `superstore` table and load the data.
5. Use the SQL files in `/queries` to build analytics views.
6. This SQL database can be further connected with the Power BI to create a report.
7. You can access my Power BI dashboard in the `dashboard/dashboard.pbix`.

---

## Key Findings
Superstore Analytics — Key Findings
Based on 2014–2017 transactional data across all regions and segments

`Total Sales: $2.30M` `Total Profit: $286.4K` `Profit Margin: 12.47%`

- Sales grew from $484K in 2014 to $733K in 2017 a 51% increase over four years. Q4 consistently outperforms all other quarters each year, suggesting strong seasonal demand that could be leveraged for targeted campaigns.

- West leads all regions in total sales, followed closely by East. Central and South trail significantly. South represents an underperforming market with potential for growth through region-specific strategies.

- Consumer (50.56%) dominates segment contribution, with Corporate at 30.74% and Home Office at 18.7%. Despite this, Corporate orders likely carry higher AOV a segment worth prioritising for deeper penetration given its profit efficiency.

- The waterfall chart reveals Copiers and Phones contribute the most to cumulative profit. These are high margin products that anchor overall profitability and should be protected from heavy discounting.

- Tables register a loss of $18K the only sub-category in negative territory. This is a critical flag. The business is selling Tables at a net loss, likely due to heavy discounting or poor pricing strategy. Immediate review of pricing and discount policy for this sub-category is recommended.

- Standard Class dominates profit contribution across all ship modes at ~$164K, with Second Class and First Class significantly behind. Same Day delivery contributes the least worth evaluating whether the cost of offering it justifies its current usage and margin.

**Bottom line:** The business is growing steadily but margin pressure exists at the sub-category level. Prioritise Copiers and Phones, fix the Tables pricing problem, and double down on Q4 and the West/East regions for maximum impact.

---
## Dashboard Visuals

**Page 1:**
![alt text](<visuals/Screenshot 2026-05-23 132951-1.png>)

**Page 2:**
![alt text](<visuals/Screenshot 2026-05-24 110140.png>)

**Page 3:**
![alt text](<visuals/Screenshot 2026-05-24 110157.png>)

**Page 4:**
![alt text](<visuals/Screenshot 2026-05-24 110218.png>)

---
## Notes
- `load_data.py` checks whether the `superstore` table already contains rows and skips loading if data exists, run it.
- `schema/schema.sql` documents the expected table structure for this project and it is for display purpose only, don't run it.
- `dashboard/dashboard.pbix` consists of the powerbi dashboard, you can locally import it in your own powerbi and interact with it or check out `visuals` folder.
