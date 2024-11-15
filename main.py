import streamlit as st
from src.ui import add_employee_form, display_employees, update_employee_form, delete_employee_form
from db.setup_db import initialize_database

def app():
    st.title("Employee Salary Management System")

    # Navigation menu
    menu = ["Add Employee", "View Employees", "Update Employee", "Delete Employee"]
    choice = st.sidebar.selectbox("Menu", menu)

    # Menu options
    if choice == "Add Employee":
        add_employee_form()
    elif choice == "View Employees":
        display_employees()
    elif choice == "Update Employee":
        update_employee_form()
    elif choice == "Delete Employee":
        delete_employee_form()

if __name__ == "__main__":
    initialize_database()  # Ensure the database is set up
    app()    


