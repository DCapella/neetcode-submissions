-- Write your query below
SELECT DISTINCT
    s.seller_name
FROM seller AS s
LEFT JOIN orders AS o
    ON s.seller_id = o.seller_id
WHERE s.seller_id
    NOT IN (
        SELECT
            seller_id
        FROM orders
        WHERE sale_date
            BETWEEN '2020-01-01' AND '2020-12-31'
    )
ORDER BY s.seller_name ASC