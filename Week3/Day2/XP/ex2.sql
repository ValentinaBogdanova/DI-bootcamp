-- select * from customer       --1

-- select first_name ||' '|| last_name as full_name from customer   --2

-- select distinct create_date from customer       --3 

-- select * from customer order by first_name desc     --4

-- select film_id, title, description, release_year, rental_rate from film order by rental_rate asc    --5

-- select * from address

-- select address, phone from address where district = 'Texas'  --6

-- select * from film where film_id = 15 or film_id = 150  --7

-- select film_id, title, description, length, rental_rate from film where title = 'Ghost'  --8

-- select film_id, title, description, length, rental_rate from film where title = 'City of Angels' --8 

-- select film_id, title, description, length, rental_rate from film where title ILIKE 'Ci%' --9

-- select min(rental_rate) as min_rate
-- from film;

-- select * from film where rental_rate = 0.99 limit 10    --10

-- select * from film where rental_rate = 0.99 limit 10 offset 10    --11


-- select * from film WHERE rental_rate = 0.99, row_num > 10 AND row_num <= 20 --11

-- select                   --12
-- customer.first_name,
-- customer.last_name,
-- payment.amount,
-- payment.payment_date
-- from customer
-- join payment
-- on customer.customer_id = payment.customer_id
-- order by customer.customer_id



-- select * from film                  --13
-- where film_id not in (select film_id from inventory)

-- select          --14
-- city.city,
-- country.country
-- from city
-- join country
-- on city.country_id = country.country_id
-- order by country.country_id

-- SELECT                 --15
--     customer.customer_id, 
--     customer.first_name, 
--     customer.last_name, 
--     payment.amount, 
--     payment.payment_date,
--     payment.staff_id
-- FROM customer
-- JOIN payment ON customer.customer_id = payment.customer_id
-- ORDER BY payment.staff_id;



