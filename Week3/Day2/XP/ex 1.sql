-- Instructions
-- We will work on the public database that we created yesterday.

-- Use SQL to get the following from the database:
-- All items, ordered by price (lowest to highest).
-- Items with a price above 80 (80 included), ordered by price (highest to lowest).
-- The first 3 customers in alphabetical order of the first name (A-Z) – exclude the primary key column from the results.
-- All last names (no other columns!), in reverse alphabetical order (Z-A)

-- select * from items order by price ASC 
-- select * from items where price >= 80 order by price DESC

-- select first_name, last_name
-- from customers
-- order by first_name ASC
-- limit 3;

-- select last_name
-- from customers
-- order by last_name Desc
