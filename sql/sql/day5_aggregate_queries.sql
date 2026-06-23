-- DAY 5 SQL AGGREGATE FUNCTIONS

-- Total employees
SELECT COUNT(*)
FROM employees;

-- Total salary
SELECT SUM(salary)
FROM employees;

-- Average salary
SELECT AVG(salary)
FROM employees;

-- Highest salary
SELECT MAX(salary)
FROM employees;

-- Lowest salary
SELECT MIN(salary)
FROM employees;

-- Employee count by department
SELECT departent, COUNT(*)
FROM employees
GROUP BY departent;

-- Total salary by department
SELECT departent, SUM(salary)
FROM employees
GROUP BY departent;

-- Average salary by department
SELECT departent, AVG(salary)
FROM employees
GROUP BY departent;

-- Highest salary by department
SELECT departent, MAX(salary)
FROM employees
GROUP BY departent;

-- Lowest salary by department
SELECT departent, MIN(salary)
FROM employees
GROUP BY departent;

-- Departments with more than 1 employee
SELECT departent, COUNT(*)
FROM employees
GROUP BY departent
HAVING COUNT(*) > 1;

-- Departments with average salary greater than 46000
SELECT departent, AVG(salary)
FROM employees
GROUP BY departent
HAVING AVG(salary) > 46000;

-- Departments with total salary greater than 50000
SELECT departent, SUM(salary)
FROM employees
GROUP BY departent
HAVING SUM(salary) > 50000;
