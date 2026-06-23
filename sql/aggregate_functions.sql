SELECT COUNT(*)
FROM employees;

SELECT SUM(salary)
FROM employees;

SELECT AVG(salary)
FROM employees;

SELECT MAX(salary)
FROM employees;

SELECT MIN(salary)
FROM employees;

SELECT dept_id, COUNT(*)
FROM employees
GROUP BY dept_id;

SELECT dept_id, SUM(salary)
FROM employees
GROUP BY dept_id;

SELECT dept_id, AVG(salary)
FROM employees
GROUP BY dept_id;

SELECT dept_id, AVG(salary)
FROM employees
GROUP BY dept_id
HAVING AVG(salary) > 50000;
