import streamlit as st
from db.operations import add_employee_to_db, get_all_employees, update_employee_in_db, delete_employee_from_db

# Add Employee Form
def add_employee_form():
    st.header("Add Employee")
    employee_id = st.text_input("Employee ID")
    employee_name = st.text_input("Employee Name")
    employee_salary = st.number_input("Employee Salary", min_value=0, step=1)
    employee_department = st.text_input("Employee Department")

    if st.button("Add Employee"):
        try:
            add_employee_to_db(employee_id, employee_name, employee_salary, employee_department)
            st.success("Employee added successfully!")
        except Exception as e:
            st.error(f"Error: {e}")
       # View Employees
def display_employees():
    st.header("View Employees")
    employees = get_all_employees()

    if employees:
        for emp in employees:
            st.write(f"ID: {emp[0]}, Name: {emp[1]}, Salary: {emp[2]}, Department: {emp[3]}")
    else:
        st.info("No employees found.")

# Update Employee Form
def update_employee_form():
    st.header("Update Employee")
    employee_id = st.text_input("Employee ID to Update")
    new_name = st.text_input("New Name")
    new_salary = st.number_input("New Salary", min_value=0, step=1)
    new_department = st.text_input("New Department")

    if st.button("Update Employee"):
        try:
            update_employee_in_db(employee_id, new_name, new_salary, new_department)
            st.success("Employee updated successfully!")
        except Exception as e:
            st.error(f"Error: {e}") 
             # Delete Employee Form
def delete_employee_form():
    st.header("Delete Employee")
    employee_id = st.text_input("Employee ID to Delete")

    if st.button("Delete Employee"):
        try:
            delete_employee_from_db(employee_id)
            st.success("Employee deleted successfully!")
        except Exception as e:
            st.error(f"Error: {e}")   