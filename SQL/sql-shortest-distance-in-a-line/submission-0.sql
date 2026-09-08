-- Write your query below
SELECT
    MIN(pp.x - p.x) as shortest
FROM point p
    JOIN point pp ON p.x < pp.x