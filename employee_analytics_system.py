import pandas as pd
import numpy as np

"""
Employee Analytics System

Features:
1.  Add Employee
2.  View Employee Data
3.  Update Employee
4.  Delete Employee
5.  Save to CSV
6.  Load from CSV
7.  Average Salary
8.  Highest Paid Employee
9.  Lowest Paid Employee
10. Department-wise Employee Count
11. Average Experience
12. Employee Grading Report
13. Average Salary by Department
14. Total Company Salary
15. Department Statistics
16. Sort Employees by Salary
17. Sort Employees by Experience
18. Salary Pivot Report
19. Search Employee by Name
20. Above Average Salary
21. Exit

Author: Param Mangukiya
"""

# ==============================
# Load Existing Data
# ==============================

try:
    df = pd.read_csv("employee.csv")
    print("Data Loaded Successfully")
except FileNotFoundError:
    df = pd.DataFrame(
        columns=["Employee_ID", "Name", "Department", "Salary", "Experience"]
    )
    print("New Database Created")


# ==============================
# Grade Helper
# ==============================

def update_grade():
    global df
    if len(df) > 0:
        df["Grade"] = df["Salary"].apply(
            lambda x: "A" if x >= 50000 else
                      "B" if x >= 35000 else
                      "C"
        )

update_grade()


# ==============================
# Functions
# ==============================

def add_employee():
    global df

    print("\n=== Add Employee ===")
    employee_id = int(input("Enter Employee ID: "))

    if employee_id in df["Employee_ID"].values:
        print("Employee ID already exists. Please use a unique ID.")
        return

    name       = input("Enter Name: ")
    department = input("Enter Department: ")
    salary     = int(input("Enter Salary: "))
    experience = int(input("Enter Experience (years): "))

    new_row = {
        "Employee_ID": employee_id,
        "Name":        name,
        "Department":  department,
        "Salary":      salary,
        "Experience":  experience
    }

    df.loc[len(df)] = new_row
    update_grade()
    print("Employee Added Successfully!")


def view_employees():
    print("\n=== Employee Data ===")
    if df.empty:
        print("No employee records found.")
    else:
        print(df.to_string(index=False))


def update_employee():
    global df

    print("\n=== Update Employee ===")
    employee_id = int(input("Enter Employee ID to Update: "))

    if employee_id not in df["Employee_ID"].values:
        print("Employee ID not found.")
        return

    print("What do you want to update?")
    print("1. Name")
    print("2. Department")
    print("3. Salary")
    print("4. Experience")

    field_choice = input("Enter choice: ")

    field_map = {
        "1": "Name",
        "2": "Department",
        "3": "Salary",
        "4": "Experience"
    }

    if field_choice not in field_map:
        print("Invalid choice.")
        return

    field = field_map[field_choice]
    new_value = input(f"Enter new {field}: ")

    if field in ("Salary", "Experience"):
        new_value = int(new_value)

    df.loc[df["Employee_ID"] == employee_id, field] = new_value
    update_grade()
    print(f"{field} updated successfully!")


def delete_employee():
    global df

    print("\n=== Delete Employee ===")
    employee_id = int(input("Enter Employee ID to Delete: "))

    if employee_id not in df["Employee_ID"].values:
        print("Employee ID not found.")
        return

    df = df[df["Employee_ID"] != employee_id].reset_index(drop=True)
    update_grade()
    print("Employee Deleted Successfully!")


def save_to_csv():
    df.to_csv("employee.csv", index=False)
    print("Data Saved to employee.csv Successfully!")


def load_from_csv():
    global df

    filename = input("Enter CSV filename to load (default: employee.csv): ").strip()
    if filename == "":
        filename = "employee.csv"

    try:
        df = pd.read_csv(filename)
        update_grade()
        print(f"Data Loaded from {filename} Successfully!")
    except FileNotFoundError:
        print(f"File '{filename}' not found.")


def average_salary():
    print("\n=== Average Salary ===")
    print(f"Rs. {round(df['Salary'].mean(), 2)}")


def highest_paid_employee():
    print("\n=== Highest Paid Employee ===")
    row = df[df["Salary"] == df["Salary"].max()]
    print(row[["Employee_ID", "Name", "Department", "Salary"]].to_string(index=False))


def lowest_paid_employee():
    print("\n=== Lowest Paid Employee ===")
    row = df[df["Salary"] == df["Salary"].min()]
    print(row[["Employee_ID", "Name", "Department", "Salary"]].to_string(index=False))


def department_wise_count():
    print("\n=== Department-wise Employee Count ===")
    print(df["Department"].value_counts().to_string())


def average_experience():
    print("\n=== Average Experience ===")
    print(f"{round(df['Experience'].mean(), 2)} years")


def employee_grading_report():
    print("\n=== Employee Grading Report ===")
    print(df[["Employee_ID", "Name", "Salary", "Grade"]].to_string(index=False))


def average_salary_by_department():
    print("\n=== Average Salary by Department ===")
    print(df.groupby("Department")["Salary"].mean().round(2).to_string())


def total_company_salary():
    print("\n=== Total Company Salary ===")
    print(f"Rs. {df['Salary'].sum():,}")


def department_statistics():
    print("\n=== Department Statistics ===")
    stats = df.groupby("Department")["Salary"].agg(["mean", "max", "min", "sum", "count"])
    stats.columns = ["Avg Salary", "Max Salary", "Min Salary", "Total Salary", "Count"]
    print(stats.round(2).to_string())


def sort_by_salary():
    print("\n=== Employees Sorted by Salary (High to Low) ===")
    print(df.sort_values("Salary", ascending=False).to_string(index=False))


def sort_by_experience():
    print("\n=== Employees Sorted by Experience (High to Low) ===")
    print(df.sort_values("Experience", ascending=False).to_string(index=False))


def salary_pivot():
    print("\n=== Salary Pivot Report ===")
    pivot = df.pivot_table(values="Salary", index="Department", aggfunc="mean").round(2)
    print(pivot.to_string())


def search_by_name():
    print("\n=== Search Employee by Name ===")
    name = input("Enter name to search: ")
    result = df[df["Name"].str.contains(name, case=False, na=False)]
    if result.empty:
        print("No employee found with that name.")
    else:
        print(result.to_string(index=False))


def above_average_salary():
    print("\n=== Employees Above Average Salary ===")
    avg = df["Salary"].mean()
    print(f"(Average Salary: Rs. {round(avg, 2)})")
    result = df[df["Salary"] > avg]
    print(result.to_string(index=False))


# ==============================
# Main Menu
# ==============================

menu = """
====== EMPLOYEE ANALYTICS SYSTEM ======
1.  Add Employee
2.  View Employee Data
3.  Update Employee
4.  Delete Employee
5.  Save to CSV
6.  Load from CSV
7.  Average Salary
8.  Highest Paid Employee
9.  Lowest Paid Employee
10. Department-wise Employee Count
11. Average Experience
12. Employee Grading Report
13. Average Salary by Department
14. Total Company Salary
15. Department Statistics
16. Sort Employees by Salary
17. Sort Employees by Experience
18. Salary Pivot Report
19. Search Employee by Name
20. Above Average Salary
21. Exit
========================================"""

actions = {
    "1":  add_employee,
    "2":  view_employees,
    "3":  update_employee,
    "4":  delete_employee,
    "5":  save_to_csv,
    "6":  load_from_csv,
    "7":  average_salary,
    "8":  highest_paid_employee,
    "9":  lowest_paid_employee,
    "10": department_wise_count,
    "11": average_experience,
    "12": employee_grading_report,
    "13": average_salary_by_department,
    "14": total_company_salary,
    "15": department_statistics,
    "16": sort_by_salary,
    "17": sort_by_experience,
    "18": salary_pivot,
    "19": search_by_name,
    "20": above_average_salary,
}

while True:
    print(menu)
    choice = input("Enter Your Choice: ").strip()

    if choice == "21":
        save_to_csv()
        print("Thank you for using Employee Analytics System!")
        break
    elif choice in actions:
        actions[choice]()
    else:
        print("Invalid Choice. Please enter a number between 1 and 21.")
