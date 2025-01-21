CREATE TABLE lake.sales (
    transaction_id BIGINT,
    product_id BIGINT,
    customer_id BIGINT,
    store_id BIGINT,
    sale_date DATE,
    quantity INT,
    total_amount DECIMAL(10, 2)
)