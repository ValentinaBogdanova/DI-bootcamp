-- create table movies(
-- movie_id serial,
-- movie_title varchar(100) not null,
-- movie_story text,
-- actors_playing_id INTEGER,
-- primary key (movie_id),
-- foreign key (actors_playing_id) references actors(actor_id));
-- DROP TABLE IF EXISTS movies;

-- INSERT INTO movies (movie_title, movie_story, actors_playing_id)
-- VALUES
--     ( 'Good Will Hunting', 
--     'Written by Affleck and Damon, the film follows 20-year-old South Boston janitor Will Hunting',
-- (SELECT actor_id from actors WHERE first_name='Matt' AND last_name='Damon'));

-- INSERT INTO movies (movie_title, movie_story, actors_playing_id) 
-- VALUES ( 'Oceans Eleven', 
--     'American heist film directed by Steven Soderbergh and written by Ted Griffin.', 
--     (SELECT actor_id from actors WHERE first_name='Matt' AND last_name='Damon'));
select * from movies

