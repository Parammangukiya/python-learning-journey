import pandas as pd
import numpy as np

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
9. Highest Experience Employee
10. Lowest Experience Employee
11. Total Company Salary
12. Employees with Grade A
13. Employees with Grade B
14. Employees with Grade C
15. Department Statistics
16. Sort Employees by Salary
17. Sort Employees by Experience
18. Salary Pivot Report
19. Above Average Salary Employees
20. Search Employee by Name

Author: Param Mangukiya
"""

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
 print(round(df["Salary"].mean(),2))

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

def department_statistics():
 print("\n=== 15. Department Statistics ===")
 stats = df.groupby("Department")["Salary"].agg(
     ["mean","max","min","sum","count"]
 )

 print(stats)


def sort_salary():
  print("\n=== 16. Sort Employees by Salary ===")
  print(df.sort_values("Salary",ascending=False))
def sort_experience():
  print("\n=== 17. Sort Employees by Experience ===")
  print(df.sort_values("Experience",ascending=False))

def salary_pivot():
  print("\n=== 18. Salary Pivot Report ===")
  print(df.pivot_table(
      values = "Salary",
      index = "Department",
      aggfunc = "mean"
  ))


def above_average_salary():
    avg_salary = df["Salary"].mean()
    print(
        df[df["Salary"] > avg_salary]
    )  

def search_by_name():
    name = input("Enter name to search: ")
    print(df[df["Name"].str.contains(name,case=False)]
          )



while True:

   print("1. Average Salary")
   print("2. Highest Paid Employee")
   print("3. Lowest Paid Employee")
   print("4. Employees with Salary > 40000")
   print("5. Department-wise Employee Count")
   print("6. Average Experience") 
   print("7. Employee Grading")
   print("8. Average Salary by Department")
   print("9. Highest Experience Employee")
   print("10. Lowest Experience Employee")
   print("11. Total Company Salary")
   print("12. Employees with Grade A")
   print("13. Employees with Grade B")
   print("14. Employees with Grade C")
   print("15. Department Statistics")
   print("16. Sort Employees by Salary")
   print("17. Sort Employees by Experience")
   print("18. Salary Pivot Report")
   print("19. Above Average Salary Employees")
   print("20. Search Employee by Name")
   print("21. Exit")

   choice = input("Choose: ")

   if choice == "1":
       average_salary()
   elif choice == "2":
      highest_paid_employee()
   elif choice == "3":
      lowest_paid_employee() 
   elif choice == "4":
      salary_filtering()
   elif choice == "5":
     department_wise_employee_count() 
   elif choice == "6":
     average_experience()
   elif choice == "7":
     employee_grading()
   elif choice == "8":
     average_salary_by_department() 
   elif choice == "9":
     highest_experience_employee() 
   elif choice == "10":
     lowest_experience_employee()
   elif choice == "11":
      total_company_salary() 
   elif choice == "12":
      employees_with_grade_a() 
   elif choice == "13":
      employees_with_grade_b() 
   elif choice == "14":
      employees_with_grade_c() 
   elif choice == "15":
      department_statistics()
   elif choice == "16":
      sort_salary()
   elif choice == "17":
      sort_experience()
   elif choice == "18":
      salary_pivot()
   elif choice == "19":
      above_average_salary()
   elif choice == "20":
      search_by_name()
   elif choice == "21":
    print("Thank you for using Employee Analytics System!")
    break
   else:
    print("Invalid Choice")
