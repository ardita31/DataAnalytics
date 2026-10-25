/* 
The name of the table that holds the items Northwind sells is "products".
The name of the table that holds the types/categories of the items Northwind sells is "categories".
*/
SELECT * FROM employees; -- Peacock Margaret. 
SELECT * FROM products; 
# Query returns 50 rows. I can change the Limit to 10 rows.
/* Bonus: SELECT * FROM TABLE LIMIT number of rows you want returned */ 
SELECT * FROM categories; -- Seafood category id is 8
SELECT OrderID, OrderDate, ShipName, ShipCountry
 FROM orders
LIMIT 50; 
