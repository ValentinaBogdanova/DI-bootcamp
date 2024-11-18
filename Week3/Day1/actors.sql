-- select * from actors  
-- select count (*) as row_count  --Count how many actors are in the table.
-- from actors;

-- insert into actors (first_name,last_name, age, oscars) values ('Alain', 'Delon', NULL, NULL); -- cant add null to age, oscars
--there are a restrictions to add null

-- select avg(oscars) as avg_oscars from actors;

-- select count(first_name) as total_oscars from actors;

-- select sum(oscars) as gm_oscars from actors where last_name = 'Pacino'

-- INSERT INTO actors (first_name, last_name, age, oscars) 
-- VALUES ('Matt', 'Rose', '03/01/1970', 0)

-- select distinct first_name from actors order by first_name desc
-- select first_name, last_name max(oscars) from actors group by first_name, last_name -- так не работает

-- select distinct first_name from actors where first_name in ('George', 'Brad')  -- чтобы найти тех  кто по имени входит или NOT IN

-- select * from actors where age between '1960-01-01' and '1971-01-01'


-- select first_name, last_name, sum(oscars) from actors group by first_name, last_name;

-- select *
-- from actors 
-- where oscars = (select max(oscars) from actors)     -- найти по максимальному признаку


--foreign key: parent and child table
-- the table that has the fk is child


create table movies(
movie_id serial,
movie_title varchar(100) not null,
movie_story text,
actors_playing_id INTEGER,
primary key (movie_id),
foreign key (actors_playing_id) references actors(actor_id));














