import sqlite3

# Add an employee
def add_employee_to_db(employee_id, employee_name, employee_salary, employee_department):
    conn = sqlite3.connect("db/employee.db")
    cursor = conn.cursor()

    try:
        cursor.execute(
            "INSERT INTO employees (id, name, salary, department) VALUES (?, ?, ?, ?)",
            (str(employee_id), str(employee_name), int(employee_salary), str(employee_department)),
        )
        conn.commit()
    except sqlite3.IntegrityError as e:
        raise Exception(f"Database Error: {e}")
    finally:
        conn.close()

# View all employees
def get_all_employees():
    conn = sqlite3.connect("db/employee.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM employees")
    rows = cursor.fetchall()
    conn.close()
    return rows
# Update an employee
def update_employee_in_db(employee_id, new_name, new_salary, new_department):
    conn = sqlite3.connect("db/employee.db")
    cursor = conn.cursor()

    cursor.execute(
        "UPDATE employees SET name = ?, salary = ?, department = ? WHERE id = ?",
        (new_name, new_salary, new_department, employee_id),
    )
    conn.commit()
    conn.close()

# Delete an employee
def delete_employee_from_db(employee_id):
    conn = sqlite3.connect("db/employee.db")
    cursor = conn.cursor()

    cursor.execute("DELETE FROM employees WHERE id = ?", (employee_id,))
    conn.commit()
    conn.close()