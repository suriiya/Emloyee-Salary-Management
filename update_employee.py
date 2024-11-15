from db.operations import update_employee_in_db

def update_employee(employee_id, updated_data):
    update_employee_in_db(employee_id, updated_data)