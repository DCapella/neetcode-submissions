-- Write your query below
SELECT DISTINCT
    sp.name
FROM sales_person sp
    LEFT JOIN orders o
        ON o.sales_id = sp.sales_id
    LEFT JOIN company c
        ON o.com_id = c.com_id
WHERE sp.sales_id
    NOT IN (
        SELECT o.sales_id
        FROM orders o
        JOIN company c
            ON o.com_id = c.com_id
        WHERE c.name = 'CRIMSON'
    )