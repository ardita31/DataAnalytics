-- Exercise 3A Aggregate functions and grouping
-- Ardita Mrapshtija

USE northwind;
-- 1.Write a query to find the price of the cheapest item that Northwind sells. 
-- Then write a second query to find the name of the product that has that price. 
SELECT MIN(UnitPrice) AS CheapestItem
FROM products;
-- Minimum Price = Cheapest item is $2.50
SELECT ProductName, UnitPrice
FROM products
WHERE UnitPrice = 2.50;
-- OR 
SELECT ProductName, UnitPrice
FROM products
WHERE UnitPrice = (SELECT MIN(UnitPrice) FROM products);
-- Cheapest Item is Geitost

-- 2.Write a query to find the average price of all items that Northwind sells.
-- Use the ROUND function to average the price to the nearest cent. 
SELECT AVG(UnitPrice) AS AveragePrice
FROM products;
-- Average Price = 28.866364
SELECT ROUND(AVG(UnitPrice),2) AS AvgPriceRounded
FROM products;
-- Average price rounded to the nearest cent is $28.87.

-- 3.Write a query to find the price of the most expensive item that Northwind sells. 
-- Then write a second query to find the name of the product with that price, plus the name of the supplier for that product. 
SELECT MAX(UnitPrice) AS MostExpensiveItem
FROM products;
-- Most expensive item is $263.50
SELECT p.ProductName, s.CompanyName, p.UnitPrice
FROM products p
JOIN suppliers s 
	ON p.SupplierID = s.SupplierID
WHERE UnitPrice = (SELECT MAX(UnitPrice) FROM products);
-- Most expensive item is Cte de Blaye from Aux joeyeux ecclsiastiques

-- 4.Write a query to find total monthly payroll (the sum of all the employees' monthly salaries).
SELECT SUM(Salary) AS MonthlyPayroll
FROM employees;
-- Monthly payroll is $20,362.93

-- 5.Write a query to identify the highest salary and the lowest salary amounts which any employee makes
SELECT  MIN(Salary) AS LowestSalary,
		MAX(Salary) AS HighestSalary
FROM employees;
-- Highest Salary = $3,119.15   Lowest Salary= $1,744.21

-- 6. Write a query to find the name and the supplier ID of each supplier and the number of items they supply. 
SELECT s.SupplierID, s.CompanyName, COUNT(p.ProductID) AS ItemCount
FROM suppliers s
INNER JOIN products p 
	ON p.SupplierID = s.SupplierID
GROUP BY s.SupplierID, s.CompanyName
ORDER BY ItemCount DESC;
-- 29 records returned

-- 7.Write a query to find the list of all category names and the average price for items in each category.
SELECT c.CategoryName, ROUND(AVG(p.UnitPrice),2) AS AveragePrice
FROM categories c
INNER JOIN products p
		ON c.CategoryID = p.CategoryID
GROUP BY c.CategoryName
ORDER BY AveragePrice;
-- 8 records returned

-- 8.Write a query to find, for all suppliers that provide at least 5 items to Northwind, what is the name of 
--   each supplier and the number of items they supply.
SELECT s.CompanyName AS Supplier, COUNT(p.ProductID) AS ItemsSupplied
FROM suppliers s
INNER JOIN products p 
		ON p.SupplierID = s.SupplierID
GROUP BY s.CompanyName
HAVING ItemsSupplied >=5
ORDER BY ItemsSupplied;
-- 2 records returned: Pavlova,Ltd and Plutzer Lebensmittelgromrkte AG

-- 9.Write a query to list products currently in inventory by the product id, product name,and inventory value 
-- (calculated by multiplying unit price by the number of units on hand). Sort the results in descending order by value. 
-- If two or more have the same value, order by product name. If a product is not in stock, leave it off the list.
SELECT ProductID, ProductName, (UnitPrice * UnitsInStock) AS InventoryValue
FROM products
WHERE UnitsInStock > 0
ORDER BY InventoryValue DESC, ProductName;
-- 72 records returned


