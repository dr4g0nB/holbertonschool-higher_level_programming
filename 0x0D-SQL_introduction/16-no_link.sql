-- Lists all records of the second_table of db.
SELECT score, name 
FROM second_table
WHERE name IS NOT NULL ORDER BY score DESC;
