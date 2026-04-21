-- Day 4: SQL Queries Against a Star Schema

-- Query 1: Total revenue per product category
SELECT
    dp.category,
    SUM(fo.total_amount) AS total_revenue
FROM fact_orders fo
JOIN dim_product dp ON fo.product_id = dp.product_id
GROUP BY dp.category;

-- Query 2: Top customer by total spending
SELECT
    dc.customer_name,
    SUM(fo.total_amount) AS total_amount
FROM fact_orders fo
JOIN dim_customer dc ON fo.customer_id = dc.customer_id
GROUP BY dc.customer_name
ORDER BY total_amount DESC
LIMIT 1;

-- Query 3: Monthly revenue trend for 2024
SELECT
    dda.month,
    SUM(fo.total_amount) AS revenue
FROM fact_orders fo
JOIN dim_date dda ON dda.date_id = fo.date_id
WHERE dda.year = 2024
GROUP BY dda.month
ORDER BY dda.month ASC;
