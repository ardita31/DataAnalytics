/*
a) In the columns of the "actor" table there is information about the actors first and last name, their ID in the DVD store and when it was last updated. 
b) In the columns of "film" we have information such as the title, the release year, decription, the rental rate, the rental duration, the ratinf etc.
c) The table "film_actor" contains columns for both "actor_id" and "film_id"
d) On the "rental" table we can find information such as when the movie was rented and/or returned, which employee id performed the transaction, the customer id
 and the rental id. This information is all in numerical values so we can't see movie names, or the name of the customer or employee, so it's not easy to read or
 understand.
e) On the "inventory" table we can find information related to different stores physical inventory of each film and when it was last updated.
f)In order to understand the names of all films that were rented on a specific date, I need tables "film", "rental", and "inventory". They are related to each other because 
they share attributes such as film_id, inventory_id or last_updated. The inventory_id can be used to tell which physical copy of a film was rented, and its relationship 
to the film table through film_id tells us the actual title of the film.
*/

SELECT rental_id, rental_date, inventory_id FROM rental;
select inventory_id, film_id FROM inventory;
SELECT film_id, title FROM film;

