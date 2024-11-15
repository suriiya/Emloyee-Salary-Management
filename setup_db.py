import sqlite3

def initialize_database():
    conn = sqlite3.connect("db/employee.db")
    cursor = conn.cursor()

    # Create employees table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS employees (
            id TEXT PRIMARY KEY,
            name TEXT NOT NULL,
            salary INTEGER NOT NULL,
            department TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()