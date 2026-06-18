#Employee Analytics System

"""
Employee Analytics System

Features:
1. Average Salary
2. Highest Paid Employee
3. Lowest Paid Employee
4. Salary Filtering
5. Department-wise Employee Count
6. Average Experience
7. Employee Grading
8. Average Salary by Department

Author: Param Mangukiya
"""
import pandas as pd
import numpy as np

data = {
    "Employee_ID": [1,2,3,4,5],
    "Name": ["Rahul","Amit","Riya","Priya","Karan"],
    "Department": ["IT","HR","IT","Finance","HR"],
    "Salary": [40000,35000,45000,60000,38000],
    "Experience": [1,3,4,6,2]
}

df = pd.DataFrame(data)

conditions = [
    df['Salary'] >= 50000,
    df['Salary'] >= 40000,
    df['Salary'] < 40000
]

choices = ['A', 'B', 'C']

df['Grade'] = np.select(
    conditions,
    choices,
    default='C'
)

def average_salary():
 print("\n=== 1. Average Salary ===")
 print(df["Salary"].mean())

def highest_paid_employee():
 print("\n=== 2. Highest Paid Employee ===")
 print(df[df["Salary"] == df["Salary"].max()]["Name"])

def lowest_paid_employee():
 print("\n=== 3. Lowest Paid Employee ===")
 print(df[df["Salary"] == df["Salary"].min()]["Name"])

def salary_filtering():
 print("\n=== 4. Employees with Salary > 40000 ===")
 print(df[df["Salary"]>40000])

def department_wise_employee_count():
 print("\n=== 5. Department-wise Employee Count ===")
 print(df["Department"].value_counts())

def average_experience():
 print("\n=== 6. Average Experience ===")
 print(df["Experience"].mean())

def employee_grading():
    print(df)

def average_salary_by_department():
 print("\n=== 8. Average Salary By Department ===")
 print(df.groupby("Department")["Salary"].mean())

def highest_experience_employee():
 print("\n=== 9. Highest Experience Employee ===")
 print(df[df["Experience"] == df["Experience"].max()]["Name"])

def lowest_experience_employee():
 print("\n=== 10. Lowest Experience Employee ===")
 print(df[df["Experience"] == df["Experience"].min()]["Name"])

def total_company_salary():
 print("\n=== 11. Total Company Salary ===")
 print(df["Salary"].sum())

def employees_with_grade_a():
 print("\n=== 12. Employees with Grade A ===")
 print(df[df["Grade"] == "A"])

def employees_with_grade_b():
 print("\n=== 13. Employees with Grade B ===")
 print(df[df["Grade"] == "B"])

def employees_with_grade_c():
 print("\n=== 14. Employees with Grade C ===")
 print(df[df["Grade"] == "C"])


while True:

   print("1. Average Salary")
   print("2. Highest Paid Employee")
   print("3. Lowest Paid Employee")
   print("4. Employees with Salary > 40000")
   print("5. Department-wise Employee Count")
   print("6. Average Experience") # Fixed typo here
   print("7. Employee Grading")
   print("8. Average Salary by Department")
   print("9. Highest Experience Employee")
   print("10. Lowest Experience Employee")
   print("11. Total Company Salary")
   print("12. Employees with Grade A")
   print("13. Employees with Grade B")
   print("14. Employees with Grade C")
   print("15. Exit")

   choice = input("Choose: ")

   if choice == "1":
       average_salary()
   elif choice == "2":
      highest_paid_employee()
   elif choice == "3":
      lowest_paid_employee() # Added parentheses
   elif choice == "4":
      salary_filtering()
   elif choice == "5":
     department_wise_employee_count() # Added parentheses and corrected name
   elif choice == "6":
     average_experience()
   elif choice == "7":
     employee_grading()
   elif choice == "8":
     average_salary_by_department() # Added parentheses
   elif choice == "9":
     highest_experience_employee() # Added parentheses
   elif choice == "10":
     lowest_experience_employee() # Added parentheses
   elif choice == "11":
      total_company_salary() # Added parentheses
   elif choice == "12":
      employees_with_grade_a() # Added parentheses
   elif choice == "13":
      employees_with_grade_b() # Added parentheses
   elif choice == "14":
      employees_with_grade_c() # Added parentheses
   elif choice == "15":
    print("Thank you for using Employee Analytics System!")
    break
   else:
    print("Invalid Choice")
