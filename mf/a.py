Sure, here is an example of a Python function that connects to a SQLite database, creates a table, inserts data into the table, and retrieves the data:

```python
import sqlite3

def manage_database():
    # Connect to the SQLite database
    conn = sqlite3.connect('example.db')
    c = conn.cursor()

    # Create a table
    c.execute('''CREATE TABLE IF NOT EXISTS users
                 (id INTEGER PRIMARY KEY, name TEXT, age INTEGER)''')

    # Insert data into the table
    c.execute("INSERT INTO users (name, age) VALUES ('Alice', 25)")
    c.execute("INSERT INTO users (name, age) VALUES ('Bob', 30)")
    
    # Commit changes and close the connection
    conn.commit()
    conn.close()
    
    # Connect to the database again
    conn = sqlite3.connect('example.db')
    c = conn.cursor()

    # Retrieve data from the table
    c.execute("SELECT * FROM users")
    rows = c.fetchall()
    
    # Print the retrieved data
    for row in rows:
        print(row)
    
    # Close the connection
    conn.close()

# Call the function
manage_database()
```
