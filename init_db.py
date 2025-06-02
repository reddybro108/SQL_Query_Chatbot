import sqlite3


def init_db():
    conn = sqlite3.connect("employees.db")
    cursor = conn.cursor()
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS employees (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            department TEXT,
            salary REAL
        )
    """
    )
    cursor.executemany(
        """
        INSERT OR REPLACE INTO employees (id, name, department, salary)
        VALUES (?, ?, ?, ?)
    """,
        [
            (1, "Alice", "HR", 60000),
            (2, "Bob", "IT", 75000),
            (3, "Charlie", "HR", 55000),
            (4, "David", "IT", 80000),
        ],
    )
    conn.commit()
    conn.close()


if __name__ == "__main__":
    init_db()
