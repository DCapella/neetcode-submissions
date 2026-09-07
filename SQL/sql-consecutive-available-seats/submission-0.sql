-- Write your query below
SELECT DISTINCT
    s1.seat_id
FROM cinema s1
    JOIN cinema s2
        ON s2.free = 1
            AND (
                s1.seat_id + 1 = s2.seat_id
                OR s1.seat_id - 1 = s2.seat_id
            )
WHERE s1.free = 1
ORDER BY s1.seat_id