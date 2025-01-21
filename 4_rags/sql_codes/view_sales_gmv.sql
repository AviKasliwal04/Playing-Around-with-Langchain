SELECT
    f.sale_key,
    p.name AS product_name,
    c.name AS customer_name,
    s.name AS store_name,
    f.date_of_sale,
    f.quantity_sold,
    f.revenue_generated
FROM fact.sales f
INNER JOIN dim.products p ON f.product_key = p.product_key
INNER JOIN dim.customers c ON f.customer_key = c.customer_key
INNER JOIN dim.stores s ON f.store_key = s.store_key
WHERE f.date_of_sale >= '2025-01-01'
ORDER BY f.date_of_sale DESC