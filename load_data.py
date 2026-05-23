from sqlalchemy import create_engine, text
from dotenv import load_dotenv
from sqlalchemy.exc import SQLAlchemyError
import pandas as pd
import os

load_dotenv()       #loads .env variables

POSTGRES_PORT = os.getenv('POSTGRES_PORT')
POSTGRES_USER = os.getenv('POSTGRES_USER')
POSTGRES_PASSWORD = os.getenv('POSTGRES_PASSWORD')
POSTGRES_HOST = os.getenv('POSTGRES_HOST')
POSTGRES_DATABASE = os.getenv('POSTGRES_DATABASE')

url = f'postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DATABASE}'

# This is the database schema for superstore table
schema = """
CREATE TABLE IF NOT EXISTS superstore (
    "Row ID"  INT,
    "Order ID"    CHAR(255),
    "Order Date"  DATE,
    "Ship Date"   DATE,
    "Ship Mode"   CHAR(255),
    "Customer ID" CHAR(255),
    "Customer Name"   CHAR(255),
    "Segment" CHAR(255),
    "Country" CHAR(255),
    "City"    CHAR(255),
    "State"   CHAR(255),
    "Postal Code" INT,
    "Region"  CHAR(255),
    "Product ID"  CHAR(255),
    "Category"    CHAR(255),
    "Sub-Category"    CHAR(255),
    "Product Name"    VARCHAR(255),
    "Sales"   DECIMAL(10,5),
    "Quantity"    INT,
    "Discount"    DECIMAL(10,2),
    "Profit"  DECIMAL(10,6)
);
"""
engine = create_engine(url, echo = True)
with engine.connect() as conn:
    # Table creation
    conn.execute(text(schema))
    conn.commit()

    # Checks number of rows (ideally 0)
    check = conn.execute(text("SELECT COUNT(*) FROM superstore;"))
    
    # Checks if there are no rows in the table and loads data
    if check.scalar() == 0:
        # Loads data
        df = pd.read_csv(r"data/Superstore.csv")
        df.to_sql('superstore', conn, if_exists='append', index=False)
        conn.commit()
        print("Successfully data loaded.")
    else:
        print("Skipped operation, table and data already exist.")

