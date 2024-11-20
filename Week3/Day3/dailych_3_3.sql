--DAILY CH

--part 1
-- 1
-- Create 2 tables : Customer and Customer profile. They have a One to One relationship.

-- create table customer(   
-- id serial primary key,
-- first_name varchar(50) not null,
-- last_name varchar(50) not null
-- );

-- create table customer_profile (
-- id serial primary key,
-- isLoggedIn boolean DEFAULT false,
-- customer_id int unique references customer(id)   -- так как отношения один к одному используем unique
-- )

--2

-- insert into customer (first_name, last_name)
-- values
-- ('John', 'Doe'),
-- ('Jerome', 'Lalu'),
-- ('Lea', 'Rive');

--
-- Insert those customer profiles, use subqueries

-- insert into customer_profile (isLoggedIn, customer_id)
-- values 
-- (true, (select id from customer where first_name = 'John')),
-- (false, (select id from customer where first_name = 'Jerome'))


--The first_name of the LoggedIn customers:
-- (inner join)

-- select 
-- c.first_name
-- from customer as c
-- join customer_profile as cp on c.id = cp.customer_id
-- where cp.isLoggedIn = true

--All the customers first_name and isLoggedIn columns - even the customers those who don’t have a profile.

-- select c.first_name, cp.isLoggedIn
-- from customer as c
-- left join customer_profile as cp on c.id = cp.customer_id

--The number of customers that are not LoggedIn
--2

-- select count(*)
-- from customer as c
-- left join customer_profile as cp on c.id = cp.customer_id  --leftjoin чтобы увидеть тех у кого нет данных 
-- where  cp.isLoggedIn = false or cp.isLoggedIn is null



-- part 2

-- create table book(
-- book_id serial primary key,
-- tittle varchar(100) not null,
-- author varchar(50) not null
-- )



-- insert into book(tittle, author)
-- values 
-- ('Alice In Wonderland', 'Lewis Carroll'),
-- ('Harry Potter', 'J.K Rowling'),
-- ('To kill a mockingbird', 'Harper Lee');


-- create table student(
-- student_id serial primary key, 
-- name varchar(50) NOT NULL UNIQUE,
-- age int check (age <= 15)
-- )

-- insert into student (name, age)
-- values
-- ('John', 12),
-- ('Lera', 11),
-- ('Patrick', 10),
-- ('Bob', 14);

-- create table library(
-- book_fk_id INT REFERENCES Book(book_id) ON DELETE CASCADE ON UPDATE CASCADE,
-- student_fk_id INT REFERENCES Student(student_id) ON DELETE CASCADE ON UPDATE CASCADE,
-- borrowed_date DATE,
-- primary key (book_fk_id ,student_fk_id)
-- )


-- insert into library (book_fk_id, student_fk_id, borrowed_date)
-- values
-- ((select book_id from book where tittle = 'Alice In Wonderland'),   -made mistake in word title 
-- (select student_id from student where name = 'John'),
-- '2022-02-15'),
-- ((select book_id from book where tittle = 'To kill a mockingbird'),
-- (select student_id from student where name = 'Bob'),
-- '2021-03-03'),
-- ((select book_id from book where tittle = 'Alice In Wonderland'),
-- (select student_id from student where name = 'Lera'),
-- '2021-05-21'),
-- ((select book_id from book where tittle = 'Harry Potter'),
-- (select student_id from student where name = 'Bob'),
-- '2021-08-12');

--Display the data
--1
-- select*from library


--2
-- select 
-- s.name,
-- b.tittle
-- from library as l
-- join student as s on l.student_fk_id = s.student_id
-- join book b on l.book_fk_id = b.book_id

--3

-- select avg(s.age) as average_age
-- from library as l 
-- join student as s on l.student_fk_id = s.student_id
-- join book as b on l.book_fk_id = b.book_id
-- where b.tittle = 'Alice In Wonderland'


-- select * from book
-- SELECT * 
-- FROM library l
-- JOIN book b ON l.book_fk_id = b.book_id
-- WHERE b.tittle = 'Alice In Wonderland';

--4
-- delete from student where name = 'Lera'
-- select * from library


-- student also deleted from lib
