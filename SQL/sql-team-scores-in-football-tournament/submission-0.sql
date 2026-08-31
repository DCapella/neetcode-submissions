-- Write your query below
SELECT
    t.team_id
    ,t.team_name
    ,SUM(CASE
        WHEN m.host_team = t.team_id AND m.host_goals > m.guest_goals THEN 3
        WHEN m.guest_team = t.team_id AND m.host_goals < m.guest_goals THEN 3
        WHEN m.host_goals = m.guest_goals THEN 1
        ELSE 0
    END) AS num_points
FROM teams t
    LEFT JOIN matches m ON t.team_id = m.host_team OR t.team_id = m.guest_team
GROUP BY (t.team_id)
ORDER BY num_points DESC, team_id ASC