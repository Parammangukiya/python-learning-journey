SELECT * FROM employees;

SELECT name FROM employees;

SELECT name, salary FROM employees;

SELECT name
FROM employees
WHERE departent = 'IT';

SELECT *
FROM employees
WHERE salary > 47000;

SELECT *
FROM employees
ORDER BY salary DESC;

SELECT name, salary
FROM employees
WHERE salary > 45000
ORDER BY salary DESC;
