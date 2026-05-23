CREATE VIEW Measures AS
    SELECT SUM("Sales") AS total_sales,
           SUM("Profit") AS total_profit,
           SUM("Quantity") AS total_quantity,
           COUNT(DISTINCT "Customer ID") AS total_customers,
           (SUM("Profit")/SUM("Sales")) * 100 AS margin,
            SUM("Sales")/COUNT(DISTINCT "Order ID") AS aov,
            (SUM("Discount" * "Sales")) AS discount_impact
        FROM superstore;
SELECT * FROM Measures;

