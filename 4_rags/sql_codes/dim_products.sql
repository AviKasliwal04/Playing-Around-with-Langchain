CREATE TABLE dim.products AS
WITH product_cte AS (
    SELECT
        product_id,
        product_name,
        category,
        price
    FROM lake.products
)
SELECT
    p.product_id AS product_key,
    p.product_name AS name,
    p.category AS category,
    p.price AS unit_price
FROM product_cte p