--EXERSICES 2

-- select * from film 
-- select * from language

-- update film     -- 1
-- set language_id = 5
-- where film_id between 100 and 200

-- select * from film 


--2
--Which foreign keys (references) are defined for the customer table? How does this affect the way in which we INSERT into the customer table?
-- store_id
-- adress_id
-- we need to use exist values id from parent tables store and adress


--3
-- We created a new table called customer_review. Drop this table. Is this an easy step, or does it need extra checking?
-- it is easy step cause this table isnt a parent one for any tab

-- drop table customer_review


--4
--Find out how many rentals are still outstanding (ie. have not been returned to the store yet).

-- select * from customer
-- select count(*) from rental where return_date is null   -183

--5
-- Find the 30 most expensive movies which are outstanding (ie. have not been returned to the store yet)

-- select
-- f.title,
-- f.rental_rate,
-- i.film_id,
-- i.inventory_id,
-- r.return_date
-- from film as f
-- join inventory as i on i.film_id = f.film_id
-- join rental as r on r.inventory_id = i.inventory_id
-- where r.return_date is null
-- order by f.rental_rate DESC limit 30



--6
-- Your friend is at the store, and decides to rent a movie. He knows he wants to see 4 movies, but he can’t remember their names. Can you help him find which movies he wants to rent?
--1. The 1st film : The film is about a sumo wrestler, and one of the actors is Penelope Monroe.
--Park Citizen

-- select 
-- f.title,
-- fa.actor_id,
-- fa.film_id,
-- a.first_name,
-- a.last_name
-- from film as f
-- join film_actor as fa on f.film_id = fa.film_id
-- join actor as a on fa.actor_id = a.actor_id
-- where f.description ilike '%sumo wrestler%'
-- and a.first_name = 'Penelope' 
-- and a.last_name = 'Monroe';

--2
--
--The 2nd film : A short documentary (less than 1 hour long), rated “R”.
-- Cupboard Sinners


-- select
-- c.name,
-- fc.film_id,
-- fc.category_id,
-- f.title,
-- f.length,
-- f.rating
-- from category as c
-- join film_category as fc on c.category_id = fc.category_id
-- join film as f on f.film_id = fc.film_id
-- where c.name ilike 'documentary' 
-- and f.length <= 60
-- and f.rating = 'R';


-- The 3rd film : A film that his friend Matthew Mahan rented. 
-- He paid over $4.00 for the rental, and he returned it between the 28th of July and the 1st of August, 2005.

-- -Sugar Wonka

-- select 
-- c.customer_id,
-- p.payment_id,
-- r.rental_id,
-- i.inventory_id,
-- i.film_id,
-- f.title
-- from customer as c
-- join payment as p on c.customer_id = p.customer_id
-- join rental as r on r.rental_id = p.rental_id
-- join inventory as i on i.inventory_id = r.inventory_id
-- join film as f on i.film_id = f.film_id
-- where c.first_name = 'Matthew' 
-- and c.last_name = 'Mahan'
-- and p.amount > 4
-- and r.return_date between '2005-07-28' and '2005-08-01'



--The 4th film : His friend Matthew Mahan watched this film, as well. 
-- It had the word “boat” in the title or description, and it looked like it was a very expensive DVD to replace.

- "Stone Fire"

-- select 
-- c.customer_id,
-- p.payment_id,
-- r.rental_id,
-- i.inventory_id,
-- i.film_id,
-- f.title,
-- f.replacement_cost
-- from customer as c
-- join payment as p on c.customer_id = p.customer_id
-- join rental as r on r.rental_id = p.rental_id
-- join inventory as i on i.inventory_id = r.inventory_id
-- join film as f on i.film_id = f.film_id
-- where c.first_name = 'Matthew' 
-- and c.last_name = 'Mahan'
-- and (f.description ilike '%boat%' or f.title ilike '%boat%')
-- order by f.replacement_cost desc





