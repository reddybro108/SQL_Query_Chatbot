import sqlite3
from faker import Faker
import random

def init_db():
    # Initialize Faker for name generation
    fake = Faker()
    
    # Define possible departments
    departments = ['HR', 'IT', 'Finance', 'Sales', 'Marketing', 'Operations', 'Research', 'Support']
    
    # Connect to SQLite database
    conn = sqlite3.connect('employees.db')
    cursor = conn.cursor()
    
    # Create employees table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS employees (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            department TEXT,
            salary REAL
        )
    ''')
    
    # Generate 5,000 employee records
    employees = []
    for i in range(1, 50001):
        name = fake.name()
        department = random.choice(departments)
        salary = round(random.uniform(30000, 150000), 2)
        employees.append((i, name, department, salary))
    
    # Insert records
    cursor.executemany('''
        INSERT OR REPLACE INTO employees (id, name, department, salary)
        VALUES (?, ?, ?, ?)
    ''', employees)
    
    conn.commit()
    conn.close()
    print(f"Inserted {len(employees)} records into employees.db")

if __name__ == "__main__":
    init_db()