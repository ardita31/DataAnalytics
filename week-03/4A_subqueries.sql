-- Exercise 4.A Working with subqueries

USE northwind;
-- 1. What is the product name(s) of the most expensive products?
SELECT ProductName, UnitPrice
FROM products
WHERE UnitPrice = (SELECT MAX(UnitPrice) FROM products);
-- Most expensive product is Cte de Blaye

-- 2. What is the product name(s) and categories of the least expensive products?
SELECT p.ProductName, c.CategoryName, p.UnitPrice
FROM products p
INNER JOIN categories c 
		ON p.CategoryID = c.CategoryID
WHERE UnitPrice = (SELECT MIN(UnitPrice) FROM products p);
-- Least expensive product is in the dairy category: Geitost

-- 3. What is the order id, shipping name and shipping address of all orders shipped via
--   "Federal Shipping"?
SELECT OrderID, ShipName, ShipAddress
FROM orders
WHERE ShipVia = (SELECT ShipperID FROM shippers
WHERE CompanyName = 'Federal Shipping');
-- 255 records returned 

-- 4. What are the order ids of the orders that included "Sasquatch Ale"?
SELECT OrderID
FROM `order details`
WHERE ProductID = (SELECT ProductID FROM products 
WHERE ProductName LIKE '%Sasquatch Ale%');

-- 5. What is the name of the employee that sold order 10266?
SELECT LastName, FirstName
FROM employees 
WHERE EmployeeID = (SELECT EmployeeID FROM orders
WHERE OrderID = 10266);
-- Janet Leverling

-- 6. What is the name of the customer that bought order 10266?
SELECT ContactName 
FROM customers 
WHERE CustomerID = (SELECT CustomerID FROM orders 
WHERE OrderID = 10266);
-- Pirkko Koskitalo