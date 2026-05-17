ALTER TABLE superstore 
ADD COLUMN "Shipping Time" INT, 
ADD COLUMN "Margin" INT;

UPDATE superstore
SET "Shipping Time" = "Ship Date" - "Order Date",
"Margin" = ROUND(("Profit"/"Sales" )*100, 2);
SELECT * FROM superstore;
