CREATE TABLE fact.sales AS
WITH sales_aggregated_cte AS (
    SELECT
        transaction_id,
        product_id,
        customer_id,
        store_id,
        sale_date,
        SUM(quantity) OVER (PARTITION BY product_id) AS total_quantity_sold,
        SUM(total_amount) OVER (PARTITION BY product_id) AS total_revenue
    FROM lake.sales
)
SELECT
    s.transaction_id AS sale_key,
    s.product_id AS product_key,
    s.customer_id AS customer_key,
    s.store_id AS store_key,
    s.sale_date AS date_of_sale,
    s.total_quantity_sold AS quantity_sold,
    s.total_revenue AS revenue_generated
FROM sales_aggregated_cte s