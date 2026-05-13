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

engine = create_engine(url, echo = True)

conn = engine.connect()

conn.execute(
    text(
        """CREATE TABLE IF NOT EXISTS superstore (
            "Row ID"  INT,
            "Order ID"    CHAR(255),
            "Order Date"  DATE,
            "Ship Date"   DATE,
            "Ship Mode"   CHAR(255),
            "Customer ID" CHAR(255),
            "Customer Name"   CHAR(255),
            Segment CHAR(255),
            Country CHAR(255),
            City    CHAR(255),
            State   CHAR(255),
            "Postal Code" INT,
            Region  CHAR(255),
            "Product ID"  CHAR(255),
            Category    CHAR(255),
            "Sub-Category"    CHAR(255),
            "Product Name"    VARCHAR(255),
            Sales   DECIMAL(10,5),
            Quantity    INT,
            Discount    DECIMAL(10,2),
            Profit  DECIMAL(10,6)
        );"""
    ))

# load CSV into the table
try:
    base_dir = os.path.dirname(os.path.abspath(__file__))
    csv_path = os.path.join(base_dir, 'data', 'Superstore.csv')
    df = pd.read_csv(csv_path)
    df.to_sql('Superstore', engine, if_exists='fail', index=False)
except ValueError:
    print("Table and Data already exist")


