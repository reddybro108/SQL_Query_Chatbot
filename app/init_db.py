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

    # Generate 50,000 employee records in batches
    batch_size = 1000
    total_records = 50000
    for start in range(1, total_records + 1, batch_size):
        employees = []
        end = min(start + batch_size - 1, total_records)
        for i in range(start, end + 1):
            name = fake.name()
            department = random.choice(departments)
            salary = round(random.uniform(30000, 150000), 2)
            employees.append((i, name, department, salary))

        # Insert batch
        cursor.executemany('''
            INSERT OR REPLACE INTO employees (id, name, department, salary)
            VALUES (?, ?, ?, ?)
        ''', employees)
        conn.commit()
        print(f"Inserted {total_records} records into employees.db")


    conn.close()
    print(f"Inserted {total_records} records into employees.db")


if __name__ == "__main__":
    init_db()
