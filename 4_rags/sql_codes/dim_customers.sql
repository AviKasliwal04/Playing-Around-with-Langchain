CREATE TABLE dim.customers AS
WITH customer_cte AS (
    SELECT
        customer_id,
        customer_name,
        customer_email,
        region
    FROM lake.customers
)
SELECT
    c.customer_id AS customer_key,
    c.customer_name AS name,
    c.customer_email AS email,
    c.region AS region
FROM customer_cte c