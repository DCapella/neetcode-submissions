-- Write your query below
SELECT
    e.left_operand
    ,e.operator
    ,e.right_operand
    ,CASE
        WHEN e.operator = '>' AND vl.value > vr.value THEN 'true'
        WHEN e.operator = '<' AND vl.value < vr.value THEN 'true'
        WHEN e.operator = '=' AND vl.value = vr.value THEN 'true'
        ELSE 'false'
    END AS value
FROM expressions e
    JOIN variables vl ON e.left_operand = vl.name
    JOIN variables vr ON e.right_operand = vr.name