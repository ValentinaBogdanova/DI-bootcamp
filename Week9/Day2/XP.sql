
--🌟 Exercise 1: Movie Rankings and Analysis

-- Task 1: Rank Movies by Popularity within Each Genre

-- Use the RANK() function to rank movies by their popularity within each genre. 
-- Display the genre name, movie title, and their rank based on popularity.

-- SELECT 
--     g.genre_name,
--     m.title AS movie_title,
--     RANK() OVER (PARTITION BY g.genre_name ORDER BY m.popularity DESC) AS rank_by_popularity
-- FROM 
--     movies.movie_genres AS mg
-- JOIN 
--     movies.genre AS g ON mg.genre_id = g.genre_id
-- JOIN 
--     movies.movie AS m ON mg.movie_id = m.movie_id
-- ORDER BY 
--     g.genre_name, rank_by_popularity;


-- SELECT * FROM movies.movie_genres LIMIT 10
-- SELECT * FROM movies.genre LIMIT 10
-- SELECT * FROM movies.movie LIMIT 10

-- Task 2: Identify the Top 3 Movies by Revenue within Each Production Company

-- Use the NTILE() function to divide the movies produced by each production company into quartiles based on revenue. 
-- Display the company name, movie title, revenue, and quartile.

-- SELECT 
-- 	pc.company_name,
-- 	m.title as movie_title,
-- 	m.revenue,
-- 	NTILE(4) over ( PARTITION by pc.company_name order by m.revenue DESC) as revenue_quartile
-- FROM
-- 	movies.movie_company AS mc
-- JOIN
-- 	movies.production_company AS pc ON mc.company_id = pc.company_id
-- JOIN
-- 	movies.movie AS m ON mc.movie_id = m.movie_id
-- ORDER BY
-- 	pc.company_name, revenue_quartile;

-- Task 3: Calculate the Running Total of Movie Budgets for Each Genre

-- Use the SUM() function with the ROWS frame specification to calculate the running total 
-- of movie budgets within each genre. 
-- Display the genre name, movie title, budget, and running total budget.

-- SELECT 
--     g.genre_name,
--     m.title AS movie_title,
--     m.budget,
--     SUM(m.budget) OVER (
--         PARTITION BY g.genre_name 
--         ORDER BY m.budget DESC  
-- 	ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW)
-- 	as running_total_budget
-- FROM
-- 	movies.movie_genres AS mg
-- JOIN
-- 	movies.genre as g on mg.genre_id=g.genre_id
-- JOIN
-- 	movies.movie as m on mg.movie_id=m.movie_id
-- ORDER by
-- 	g.genre_name, running_total_budget DESC

-- SELECT *
-- FROM movies.movie
-- WHERE budget = 59443406599   -- didnt get from where is this number

-- SELECT COUNT(*)
-- FROM movies.movie_genres AS mg
-- JOIN movies.genre AS g ON mg.genre_id = g.genre_id
-- JOIN movies.movie AS m ON mg.movie_id = m.movie_id;


-- Task 4: Identify the Most Recent Movie for Each Genre
-- Use the FIRST_VALUE() function to find the most recent movie 
-- within each genre based on the release date. 
-- Display the genre name, movie title, and release date.

-- SELECT DISTINCT
-- 	g.genre_name,
-- 	FIRST_VALUE(m.title) over(
-- 		partition by g.genre_name
-- 		order by m.release_date desc) as most_recent_movie,
-- 	FIRST_VALUE(m.release_date) over(
-- 		partition by g.genre_name
-- 		order by m.release_date desc) as release_date
-- FROM 
-- 	movies.movie_genres as mg
-- JOIN
-- 	movies.genre as g on mg.genre_id = g.genre_id
-- JOIN
-- 	movies.movie as m on mg.movie_id = m.movie_id
-- ORDER BY 
-- 	g.genre_name;




--🌟 Exercise 2: Cast and Crew Performance Analysis


-- Task 1: Rank Actors by Their Appearance in Movies
-- Use the DENSE_RANK() function to rank actors based on the number of 
-- movies they have appeared in. Display the actor’s name and their rank.

-- SELECT 
--     p.person_name AS actor_name,
--     COUNT(mc.movie_id) AS movie_count,
--     DENSE_RANK() over (order by count(mc.movie_id) DESC) as rank
-- FROM 
--     movies.movie_cast AS mc
-- JOIN 
--     movies.person AS p on mc.person_id = p.person_id
-- GROUP BY 
--     p.person_name
-- ORDER BY 
--     rank;

-- Task 2: Identify the Top Director by Average Movie Rating

-- Use a CTE and the RANK() function to find the director with the highest average movie rating.
-- Display the director’s name and their average rating.

-- WITH best_rating_director AS (
--     SELECT 
--         p.person_name as director_name,
--         AVG(m.vote_average) as average_rating,
--         RANK() OVER (order by avg(m.vote_average) DESC) AS rank
--     FROM 
--         movies.movie_crew AS mc
--     JOIN 
--         movies.person AS p on mc.person_id = p.person_id
--     JOIN 
--         movies.movie AS m on mc.movie_id = m.movie_id
--     WHERE 
--         mc.job = 'Director'
--     GROUP BY 
--         p.person_name
-- )
-- SELECT 
--     director_name,
--     average_rating
-- FROM 
--     best_rating_director
-- WHERE 
--     rank = 1;




-- Task 3: Calculate the Cumulative Revenue of Movies Acted by Each Actor

-- Use the SUM() function to calculate the cumulative revenue of movies acted 
-- by each actor. Display the actor’s name and the cumulative revenue.

-- SELECT 
--     p.person_name as actor_name,
--     SUM(m.revenue) as cumulative_revenue
-- FROM 
--     movies.movie_cast as mc
-- JOIN 
--     movies.person as p on mc.person_id = p.person_id
-- JOIN 
--     movies.movie as m on mc.movie_id = m.movie_id
-- GROUP BY 
--     p.person_name
-- ORDER BY 
--     cumulative_revenue DESC
	
-- Task 4: Identify the Director Whose Movies Have the Highest Total Budget
-- Use a CTE and a window function to find the director whose movies have 
-- the highest total budget. Display the director’s name and the total budget.

-- select job from movies.movie_crew


-- WITH best_budget_director as(
-- 	SELECT
-- 		p.person_name as director_name,
-- 		sum(m.budget) as total_budget,
-- 		rank() over(order by sum(m.budget) desc) as rank
-- 	FROM
-- 		movies.movie_crew as mc
-- 	JOIN
-- 		movies.person as p on mc.person_id=p.person_id
-- 	JOIN
-- 		movies.movie as m on mc.movie_id=m.movie_id
-- 	WHERE
-- 		mc.job= 'Director'
-- 	GROUP BY
-- 		p.person_name)
-- SELECT
-- 	director_name,
-- 	total_budget
-- FROM
-- 	best_budget_director
-- WHERE
-- 	rank = 1
