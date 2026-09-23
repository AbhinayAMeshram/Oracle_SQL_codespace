import sqlite3


# Connect to SQLite. The database file is created if it does not exist.
connection = sqlite3.connect("company.db")

# Create a cursor for executing SQL statements.
cursor = connection.cursor()

# Start with fresh tables so the script always contains exactly five records.
cursor.execute("DROP TABLE IF EXISTS employee")
cursor.execute("DROP TABLE IF EXISTS department")

# Execute SQL to create the department and employee tables.
cursor.execute("""
	CREATE TABLE department (
		id INTEGER PRIMARY KEY,
		name TEXT,
		location TEXT
	)
""")

cursor.execute("""
	CREATE TABLE employee (
		id INTEGER PRIMARY KEY,
		name TEXT,
		deptid INTEGER
	)
""")

# Execute SQL to insert five departments. Departments 4 and 5 will have no employees.
cursor.execute("INSERT INTO department VALUES (1, 'Human Resources', 'Bengaluru')")
cursor.execute("INSERT INTO department VALUES (2, 'Sales', 'Mumbai')")
cursor.execute("INSERT INTO department VALUES (3, 'Information Technology', 'Hyderabad')")
cursor.execute("INSERT INTO department VALUES (4, 'Finance', 'Chennai')")
cursor.execute("INSERT INTO department VALUES (5, 'Operations', 'Pune')")

# Insert five employees. Employee 5 has no matching department.
cursor.execute("INSERT INTO employee VALUES (1, 'Anita Sharma', 1)")
cursor.execute("INSERT INTO employee VALUES (2, 'Rahul Verma', 2)")
cursor.execute("INSERT INTO employee VALUES (3, 'Priya Nair', 3)")
cursor.execute("INSERT INTO employee VALUES (4, 'Vikram Singh', 3)")
cursor.execute("INSERT INTO employee VALUES (5, 'Neha Patel', 99)")

# Save the table definitions and inserted records.
connection.commit()

# Fetch and display all employee records.
print("Employees:")
print("ID | Name | DeptID")
cursor.execute("SELECT id, name, deptid FROM employee")
employee_records = cursor.fetchall()
for employee in employee_records:
	print(f"{employee[0]} | {employee[1]} | {employee[2]}")

print()

# Fetch and display all department records.
print("Departments:")
print("ID | Name | Location")
cursor.execute("SELECT id, name, location FROM department")
department_records = cursor.fetchall()
for department in department_records:
	print(f"{department[0]} | {department[1]} | {department[2]}")

# Find and display the names of employees who work in Human Resources.
print("\nEmployees in Human Resources:")
cursor.execute("""
	SELECT employee.name
	FROM employee
	INNER JOIN department ON employee.deptid = department.id
	WHERE department.name = 'Human Resources'
""")
hr_employees = cursor.fetchall()
for employee in hr_employees:
	print(employee[0])

# Close the cursor and database connection.
cursor.close()
connection.close()
