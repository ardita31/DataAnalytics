-- Exercise 1.C More Pracrice with queries 
-- Ardita Mrapshtija

USE northwind;

-- 1. Write a query to list the product id, product name, and unit price of every product. Display them in ascending order by price.
SELECT ProductID, ProductName, UnitPrice
FROM products
ORDER BY UnitPrice ASC;
-- 77 records returned

-- 2. What are the products that we carry where we have at least 100 units on hand? Order them in descending order by price.
SELECT ProductName, UnitPrice, UnitsInStock
FROM products
WHERE UnitsInStock >= 100
ORDER BY UnitPrice DESC;
-- 10 rows returned 

-- 3. What are the products that we carry where we have at least 100 units on hand? Order them in descending order by price.
--    If two or more have the same price, list those in ascending order by product name. 
SELECT ProductName, UnitPrice, UnitsInStock
FROM products
WHERE UnitsInStock >= 100
ORDER BY UnitPrice DESC, ProductName ASC;
-- 10 records returned

-- 4. Write a query against the orders table that displays the total number of distinct customers who have placed orders, based on customer id. 
--    Use an alias to label the count calculation as CustomerCount. 
SELECT COUNT(DISTINCT CustomerID) AS CustomerCount
FROM orders;
-- CustomerCount is 89.

-- 5. Write a query against the orders table that displays the total number of distinct customers who have placed orders, by customer ID, for each 
--    country where orders have been shipped. Use an alias to label the count as CustomerCount, Order the list by the CustomerCount, largest to smallest.
SELECT ShipCountry,
	count(DISTINCT CustomerID) AS CustomerCount
FROM orders
GROUP BY ShipCountry 
ORDER BY CustomerCount DESC;
-- 21 records returned

-- 6. What are the products that we carry where we have less than 25 units on hand but 1 or more units of them are in oder? Write a query that orders them 
--    by quantity on order (high to low), then by product name.
SELECT ProductName, UnitsInStock, UnitsOnOrder
FROM products 
WHERE UnitsInStock < 25 AND UnitsOnOrder >= 1
ORDER BY UnitsOnOrder DESC, ProductName ASC;
-- 17 recrods returned

-- 7. Write a query to list each of the job titles in employees, along with a count of how many employees hold each job title.
SELECT Title,
	COUNT(*) AS EmployeeCount
FROM employees
GROUP BY Title;
-- 4 records returned

-- 8. What employees have a monthly salary that is between $2000 and $2500? Write a query that orders them by job title. 
SELECT EmployeeID, concat(LastName,' ', FirstName) AS EmployeeName, Title, Salary
FROM employees
WHERE Salary BETWEEN 2000 AND 2500
ORDER BY TITLE;
-- 4 employees have a salary between $2000 and $2500.
-- Concat was used to combine the FirstName and LastName columns as EmployeeName. 