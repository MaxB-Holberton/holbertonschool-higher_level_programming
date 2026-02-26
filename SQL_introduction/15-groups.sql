-- get the number of times a score is counted from second_table
SELECT score, COUNT(score) as number
FROM second_table
GROUP BY score
ORDER BY score DESC;
