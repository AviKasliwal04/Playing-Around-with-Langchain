CREATE TABLE dim.stores AS
WITH store_cte AS (
    SELECT
        store_id,
        store_name,
        store_city,
        store_state
    FROM lake.stores
)
SELECT
    s.store_id AS store_key,
    s.store_name AS name,
    s.store_city AS city,
    s.store_state AS state
FROM store_cte s