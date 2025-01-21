CREATE TABLE fact.customer_behavior AS
WITH behavior_cte AS (
    SELECT
        customer_id,
        COUNT(DISTINCT transaction_id) AS total_transactions,
        SUM(quantity) AS total_items_purchased,
        SUM(total_amount) AS total_spent,
        ROW_NUMBER() OVER (PARTITION BY customer_id ORDER BY SUM(total_amount) DESC) AS top_purchase_rank
    FROM lake.sales
    GROUP BY customer_id
)
SELECT
    c.customer_id AS customer_key,
    b.total_transactions AS total_purchases,
    b.total_items_purchased AS total_quantity,
    b.total_spent AS total_spent_amount,
    b.top_purchase_rank AS ranking_in_spending
FROM behavior_cte b
INNER JOIN dim.customers c ON b.customer_id = c.customer_key