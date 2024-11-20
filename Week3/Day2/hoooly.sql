-- SQL JOINS, left, right, full
-- INNER JOIN SYNTAX

-- select actors.first_name, actors.last_name, movies.movie_title
-- from actors
-- inner join movies
-- on actors.actor_id = movies.actors_playing_id


-- create table producers(
-- producer_id serial,
-- producer_fn varchar(100) not null,
-- producer_ln varchar(100) not null,
-- movie_title varchar(100) not null,
-- movie_id INTEGER,
-- primary key (producer_id),
-- foreign key (movie_id) references movies(movie_id));


-- INSERT INTO producers (producer_fn, producer_ln, movie_title, movie_id)
-- VALUES ('Lawrence', 'Bender', 'Good Will Hunting',
-- (SELECT movie_id from movies WHERE movie_title = 'Good Will Hunting'));

-- select *from producers.producer_fn,producers.producer_ln, movie_title, movie_id
-- select actors.first_name, actors.last_name, movies.movie_title
-- from actors
-- inner join movies
-- on actors.actor_id = movies.actors_playing_id


-- CREATE TABLE countries (
--     country_id SERIAL PRIMARY KEY,
--     country_name VARCHAR(255) NOT NULL
-- );


-- INSERT INTO countries (country_name)
-- VALUES 
-- ('USA'),
-- ('Israel'),
-- ('Canada'),
-- ('Russia');

--INNER JOIN:

-- SELECT actors.actor_id, actors.first_name, actors.last_name, countries.country_name
-- FROM actors
-- INNER JOIN countries
-- ON actors.actor_id = countries.country_id;


-- SELECT actors.first_name, countries.country_name
-- FROM actors
-- INNER JOIN countries
-- ON actors.actor_id = countries.country_id;




