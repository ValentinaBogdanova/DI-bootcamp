-- 🌟 Exercise 1: Complex Subquery Analysis
-- Task 1: Find the average age of competitors who have won at least one medal,
-- grouped by the type of medal they won. Use a correlated subquery to achieve this.

/*
SELECT 
    m.medal_name,
    AVG(gc.age) AS average_age
FROM games_competitor gc
JOIN competitor_event ce ON gc.id = ce.competitor_id
JOIN medal m ON ce.medal_id = m.id
WHERE ce.medal_id IS NOT NULL
GROUP BY m.medal_name;
*/

--Task 2: Identify the top 5 regions with the highest number of unique competitors 
--who have participated in more than 3 different events. Use nested subqueries to filter and aggregate the data.
/*
SELECT 
    nr.region_name,
    COUNT(DISTINCT pr.person_id) AS unique_competitors
FROM person_region pr
JOIN noc_region nr ON pr.region_id = nr.id
WHERE pr.person_id IN
    (SELECT gc.person_id
    FROM games_competitor gc
    JOIN competitor_event ce ON gc.id = ce.competitor_id
    GROUP BY gc.person_id
    HAVING COUNT(DISTINCT ce.event_id) > 3)
GROUP BY nr.region_name
ORDER BY unique_competitors DESC
LIMIT 5
   */ 
   
-- Task 3: Create a temporary table to store the total number of medals won by each competitor 
-- and filter to show only those who have won more than 2 medals. Use subqueries to aggregate the data.
 /*
CREATE TEMPORARY TABLE total_medal AS
SELECT
	ce.competitor_id,
    COUNT(ce.medal_id) as medal_count
FROM competitor_event ce
WHERE ce.medal_id is NOT NULL
GROUP BY ce.competitor_id

SELECT *
FROM total_medal
WHERE medal_count > 2
*/

--Task 4: Use a subquery within a DELETE statement to remove records of competitors
--who have not won any medals from a temporary table created for analysis.
 /*
CREATE TEMPORARY TABLE zero_medal AS
SELECT * FROM games_competitor as gc

DELETE FROM zero_medal
WHERE id not in (
  SELECT DISTINCT ce.competitor_id
  FROM competitor_event as ce
  WHERE ce.medal_id is not null )
*/
--SELECT*FROM zero_medal

--🌟 Exercise 2: Advanced Data Manipulation and Optimization

--Task 1: Update the heights of competitors based on 
--the average height of competitors from the same region. Use a correlated subquery within the UPDATE statement.

/*
UPDATE person
SET height = (
  SELECT AVG(p.height)
  FROM person as p
  join person_region as prg on p.id=prg.person_id
  WHERE prg.region_id = (
    SELECT pr.region_id
    FROM person_region as pr
    WHERE pr.person_id = person_id))
WHERE height is null  -- forgot to write this row and updated all height ....
    
SELECT * FROM  person
*/

--Task 2: Insert new records into a temporary table for competitors who participated in more than one event in the same games 
--and list their total number of events participated. Use nested subqueries for filtering.
/*
CREATE TEMPORARY TABLE multi_event_competitors AS
SELECT 
    gc.id AS competitor_id,
    gc.games_id,
    COUNT(DISTINCT ce.event_id) AS total_events
FROM games_competitor gc
JOIN competitor_event ce ON gc.id = ce.competitor_id
GROUP BY gc.id, gc.games_id
HAVING COUNT(DISTINCT ce.event_id) > 1
*/

--SELECT*FROM multi_event_competitors

/*
SELECT 
    nr.region_name,
    AVG(medals.total_medals) AS avg_medals_per_competitor
FROM (
    SELECT 
        pr.region_id,
        COUNT(ce.medal_id) AS total_medals
    FROM person_region pr
    LEFT JOIN competitor_event ce ON pr.person_id = ce.competitor_id
    GROUP BY pr.region_id, pr.person_id) AS medals
JOIN noc_region nr ON medals.region_id = nr.id
GROUP BY nr.region_name
HAVING AVG(medals.total_medals) > (
    SELECT AVG(total_medals)
    FROM (
        SELECT 
            COUNT(ce.medal_id) AS total_medals
        FROM person_region pr
        LEFT JOIN competitor_event ce ON pr.person_id = ce.competitor_id
        GROUP BY pr.person_id
    ) AS overall)
*/

--Task 4: Create a temporary table to track competitors’ participation across different
--seasons and identify those who have participated in both Summer and Winter games.
/*
CREATE TEMPORARY TABLE competitor_seasons AS
SELECT 
    gc.person_id,
    g.season
FROM games_competitor gc
JOIN games g ON gc.games_id = g.id
GROUP BY gc.person_id, g.season

SELECT 
    cs.person_id
FROM competitor_seasons cs
WHERE cs.season = 'Summer'
INTERSECT
SELECT 
    cs.person_id
FROM competitor_seasons cs
WHERE cs.season = 'Winter'
*/