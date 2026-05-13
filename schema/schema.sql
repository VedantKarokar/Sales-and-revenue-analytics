-- Active: 1778493718025@@127.0.0.1@5432@superstore_db
CREATE TABLE superstore(
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
);