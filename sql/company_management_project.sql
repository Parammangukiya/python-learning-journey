-- COMPANY MANAGEMENT SQL PROJECT

CREATE DATABASE company_project;

USE company_project;

CREATE TABLE departments (
    dept_id INT,
    department_name VARCHAR(50)
);

INSERT INTO departments VALUES
(101,'IT'),
(102,'HR'),
(103,'Sales'),
(104,'Marketing');

CREATE TABLE employees (
    emp_id INT,
    name VARCHAR(50),
    dept_id INT,
    salary INT
);

INSERT INTO employees VALUES
(1,'Param',101,50000),
(2,'Rahul',102,45000),
(3,'Raj',101,47000),
(4,'Neha',103,55000),
(5,'Riya',101,65000),
(6,'Amit',104,40000);

-- Show all employees

SELECT *
FROM employees;

-- Employees earning more than 50000

SELECT *
FROM employees
WHERE salary > 50000;

-- Employees sorted by salary

SELECT *
FROM employees
ORDER BY salary DESC;

-- Total company salary

SELECT SUM(salary)
FROM employees;

-- Average salary

SELECT AVG(salary)
FROM employees;

-- Employee count by department

SELECT dept_id, COUNT(*)
FROM employees
GROUP BY dept_id;

-- Total salary by department

SELECT dept_id, SUM(salary)
FROM employees
GROUP BY dept_id;

-- Average salary by department

SELECT dept_id, AVG(salary)
FROM employees
GROUP BY dept_id;

-- Departments with average salary greater than 50000

SELECT dept_id, AVG(salary)
FROM employees
GROUP BY dept_id
HAVING AVG(salary) > 50000;

-- Employee names with department names

SELECT employees.name,
       departments.department_name
FROM employees
INNER JOIN departments
ON employees.dept_id = departments.dept_id;

-- Highest paid employee

SELECT *
FROM employees
ORDER BY salary DESC
LIMIT 1;
