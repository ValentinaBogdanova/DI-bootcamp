--EXERCISE 1

-- select * from language
-- select name from language  --1

-- select                     --2
-- film.title, 
-- film.description,
-- language.name as language_name
-- from film
-- join language
-- on film.language_id = language.language_id


-- select                    --3
-- language.name as language_name,
-- film.title,
-- film.description
-- from language
-- left join film
-- on film.language_id = language.language_id

-- create table new_film (        --4
-- new_film_id serial primary key,
-- new_film_title varchar(100)
-- );


-- insert into new_film (new_film_title) --4
-- values ('Harry Potter and the Deathly hallows')

-- create table customer_review (        --5
-- review_id serial primary key,
-- title varchar(100) NOT NULL,
-- score int NOT NULL check (score between 1 and 10),
-- review_text TEXT,
-- last_update timestamp not null DEFAULT CURRENT_TIMESTAMP, -- чтобы момент записи отследить
-- film_id INT NOT NUll references new_film (new_film_id) on delete cascade on update cascade,
-- language_id INT not null references language (language_id) on delete cascade on update cascade
-- );

-- select * from language

-- insert into customer_review (title, score, review_text, film_id, language_id)    -- 6
-- values ('My favourite part of the story', 10, 'The amazing plot, adore Sirius and i was worried about Buckbeat till the very end.', 3, 1
-- );

-- insert into customer_review (title, score, review_text, film_id, language_id)
-- values ('So sad that it`s THE END', 9, 'I was crying all film long. All good heroes died in the end...', 7, 1
-- );

-- select * from customer_review

-- delete from new_film  --7 
-- where new_film_id = 7

-- it will also delete from customer_review cause i put a condition ON DELETE CASCADE  --7
-- select * from customer_review

