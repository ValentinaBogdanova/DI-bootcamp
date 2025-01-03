
--🌟 Exercise 1: Detailed Medal Analysis
--Task 1: Identify competitors who have won at least one medal in events spanning both Summer 
--and Winter Olympics. Create a temporary table to store these competitors 
--and their medal counts for each season, and then display the contents of this table.


/*
CREATE TEMPORARY TABLE competitors_medals AS
SELECT 
    gc.person_id,
    g.season,
    COUNT(ce.medal_id) AS medal_count
FROM games_competitor gc
JOIN competitor_event ce ON gc.id = ce.competitor_id
JOIN games g ON gc.games_id = g.id
WHERE ce.medal_id IS NOT NULL
GROUP BY gc.person_id, g.season
*/
/*
SELECT 
cm.person_id,
SUM(CASE WHEN cm.season = 'Summer' THEN cm.medal_count ELSE 0 END) AS summer_medals,
SUM(CASE WHEN cm.season = 'Winter' THEN cm.medal_count ELSE 0 END) AS winter_medals
FROM competitors_medals cm
GROUP BY cm.person_id
HAVING 
SUM(CASE WHEN cm.season = 'Summer' THEN cm.medal_count ELSE 0 END) > 0 AND
SUM(CASE WHEN cm.season = 'Winter' THEN cm.medal_count ELSE 0 END) > 0

*/

--Task 2: Create a temporary table to store competitors who have won medals in exactly two different sports, and then use a subquery to identify the top 3 competitors
--with the highest total number of medals across all sports. Display the contents of this table.

/*
CREATE TEMPORARY TABLE two_sport_medalists AS
SELECT 
    ce.competitor_id,
    COUNT(DISTINCT e.sport_id) AS sport_count,
    COUNT(ce.medal_id) AS total_medals
FROM competitor_event ce
JOIN event e ON ce.event_id = e.id
WHERE ce.medal_id IS NOT NULL 
GROUP BY ce.competitor_id
HAVING COUNT(DISTINCT e.sport_id) = 2
*/
/*
SELECT 
    tsm.competitor_id,
    tsm.sport_count,
    tsm.total_medals
FROM two_sport_medalists tsm
ORDER BY tsm.total_medals DESC
LIMIT 3
*/

--🌟 Exercise 2: Region and Competitor Performance

--Task 1: Retrieve the regions that have competitors who have won the highest number of medals in a single Olympic event. 
--Use a subquery to determine the event with the highest number of medals
--for each competitor, and then display the top 5 regions with the highest total medals.
/*
SELECT 
    ce.competitor_id,
    ce.event_id,
    COUNT(ce.medal_id) AS total_medals
FROM competitor_event ce 
WHERE ce.medal_id IS NOT NULL
GROUP BY ce.competitor_id, ce.event_id

SELECT 
    competitor_id,
    COUNT(medal_id) AS total_medals
FROM competitor_event
WHERE medal_id IS NOT NULL
GROUP BY competitor_id, event_id

SELECT 
    competitor_id,
    event_id,
    COUNT(medal_id) AS total_medals
FROM competitor_event
WHERE medal_id IS NOT NULL
GROUP BY competitor_id, event_id

CREATE TEMPORARY TABLE max_medals AS
SELECT 
    ce.competitor_id,
    MAX(total_medals) AS max_medals
FROM (
    SELECT 
        competitor_id,
        event_id,
        COUNT(medal_id) AS total_medals
    FROM competitor_event
    WHERE medal_id IS NOT NULL
    GROUP BY competitor_id, event_id
) AS medal_counts
GROUP BY competitor_id
 
 PRAGMA table_info(competitor_event)
 
 CREATE TEMPORARY TABLE max_medals_per_event AS
SELECT 
    competitor_id,
    event_id,
    total_medals
FROM (
    SELECT 
        competitor_id,
        event_id,
        COUNT(medal_id) AS total_medals,
        RANK() OVER (PARTITION BY competitor_id ORDER BY COUNT(medal_id) DESC) AS rank
    FROM competitor_event
    WHERE medal_id IS NOT NULL
    GROUP BY competitor_id, event_id
) ranked_events
WHERE rank = 1


SELECT 
    nr.region_name,
    SUM(mmpe.total_medals) AS total_medals
FROM max_medals_per_event mmpe
JOIN person_region pr ON mmpe.competitor_id = pr.person_id
JOIN noc_region nr ON pr.region_id = nr.id
GROUP BY nr.region_name
ORDER BY total_medals DESC
LIMIT 5
*/

--Task 2: Create a temporary table to store competitors who have participated in more than three Olympic Games but have not won any medals.
--Retrieve and display the contents of this table,
--including their full names and the number of games they participated in.
/*
CREATE TEMPORARY TABLE competitors_no_medals AS
SELECT 
    p.id AS competitor_id,
    p.full_name,
    COUNT(DISTINCT gc.games_id) AS games_participated
FROM person p
JOIN games_competitor gc ON p.id = gc.person_id
LEFT JOIN competitor_event ce ON gc.id = ce.competitor_id
WHERE ce.medal_id IS NULL 
GROUP BY p.id, p.full_name
HAVING COUNT(DISTINCT gc.games_id) > 3

SELECT * FROM competitors_no_medals
*/

--Seems there is no atheletes who participated in 3 and more and dont have medals