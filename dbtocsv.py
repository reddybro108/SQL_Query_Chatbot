import sqlite3
import mysql.connector
import csv

# Step 1: Read from SQLite
sqlite_conn = sqlite3.connect('employees.db')
sqlite_cursor = sqlite_conn.cursor()

sqlite_cursor.execute("SELECT * FROM employees")
rows = sqlite_cursor.fetchall()
columns = [description[0] for description in sqlite_cursor.description]

# Step 2: Insert into MySQL
mysql_conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='Amolreddy@108',
    database='amoldb'
)
mysql_cursor = mysql_conn.cursor()

# Optional: clear MySQL table first (only if needed)
mysql_cursor.execute("DELETE FROM employees")

# Insert rows into MySQL
placeholders = ', '.join(['%s'] * len(columns))
insert_query = f"INSERT INTO employees ({', '.join(columns)}) VALUES ({placeholders})"

mysql_cursor.executemany(insert_query, rows)
mysql_conn.commit()

# Step 3: Export from MySQL to CSV
mysql_cursor.execute("SELECT * FROM employees")
with open('employees.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow([i[0] for i in mysql_cursor.description])  # write headers
    writer.writerows(mysql_cursor.fetchall())

# Cleanup
sqlite_cursor.close()
sqlite_conn.close()
mysql_cursor.close()
mysql_conn.close()

print("Data successfully migrated from SQLite to MySQL and exported to employees.csv")
