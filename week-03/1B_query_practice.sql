-- Exercise 1.B Querying a database 
-- Ardita Mrapshtija 


USE northwind;
/*
1.Write a query to list the product id, product name, and unit price of every product that Northwind sells.
(Hint: To help set up your query, look at the schema preview to see what column names belong to each table.
 Or use SELECT * to query all columns first, then refine your query to just the columns you want.)  
 */
SELECT ProductID, ProductName, UnitPrice
FROM products;
-- Returns 77 records

-- 2.Write a query to identify products where the unit price is $7.50 or less.
SELECT ProductID
FROM products
WHERE UnitPrice <= 7.50; 
-- Returns 5 records 

-- 3. What are the products that we carry when we have no units on hand, but 1 or more units are on backorder?
SELECT ProductName, UnitsInStock, UnitsOnOrder
FROM products
WHERE UnitsInStock = 0 AND UnitsOnOrder >= 1;
-- Returns 1 record

-- 4. Products table: How does it identify the category of each item sold? Where can you find a list of all categories?
--    Write a set of queries to answer these questions, ending with a query that creates a list of all the seafood items we carry. 
SELECT ProductName, CategoryID
FROM products; -- to identify the category of each item sold 
-- 77 records returned

SELECT CategoryName, CategoryID
FROM categories; -- list of all categories (from this we see that Seafood CategoryID = 8) 
-- 8 records returned

SELECT ProductName, CategoryID
FROM products 
WHERE CategoryID =8
-- 12 records returned

-- 5. Products: How do you know what supplier each product comes from? Where can you find info on suppliers?
--    Write a set of queries to find the specific identifier for "Tokyo Traders" and then find all products from that supplier.
SELECT SupplierID, CompanyName 
FROM suppliers; -- how to find info on suppliers
-- 29 records returned

SELECT SupplierID, CompanyName
FROM suppliers
WHERE CompanyName = 'Tokyo Traders'; -- to find the supplierID for Tokyo Traders which is 4
-- 1 record returned

SELECT ProductName, SupplierID
FROM products
WHERE SupplierID = 4;
-- 3 records returned

-- 6. How many employees work at northwind? What employees have "manager" somewehere in their job title?
SELECT COUNT(EmployeeID)
FROM employees;
-- 9 records returned

SELECT EmployeeID, FirstName, LastName, Title
FROM employees
WHERE title LIKE '%manager%'; 
-- Steven Buchanan is the Sales Manager

 


 

 
  