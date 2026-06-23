-- INNER JOIN

SELECT employees.name,
       departments.department_name
FROM employees
INNER JOIN departments
ON employees.dept_id = departments.dept_id;

-- LEFT JOIN

SELECT employees.name,
       departments.department_name
FROM employees
LEFT JOIN departments
ON employees.dept_id = departments.dept_id;

-- RIGHT JOIN

SELECT employees.name,
       departments.department_name
FROM employees
RIGHT JOIN departments
ON employees.dept_id = departments.dept_id;
