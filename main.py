import sqlite3

# Connect to the database
conn = sqlite3.connect('database.db')
cursor = conn.cursor()

# Create a table
cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    email TEXT NOT NULL UNIQUE,
                    age INTEGER
                )''')

# Add a new user to the database
def add_user(name, email, age):
    cursor.execute("INSERT INTO users (name, email, age) VALUES (?, ?, ?)", (name, email, age))
    conn.commit()
    print("User added successfully!")

# Retrieve all users from the database
def get_all_users():
    cursor.execute("SELECT * FROM users")
    rows = cursor.fetchall()
    for row in rows:
        print("ID:", row[0])
        print("Name:", row[1])
        print("Email:", row[2])
        print("Age:", row[3])
        print("------------------------")

# Update a user's age in the database
def update_user_age(user_id, new_age):
    cursor.execute("UPDATE users SET age = ? WHERE id = ?", (new_age, user_id))
    conn.commit()
    print("User age updated successfully!")

# Delete a user from the database
def delete_user(user_id):
    cursor.execute("DELETE FROM users WHERE id = ?", (user_id,))
    conn.commit()
    print("User deleted successfully!")

# Close the database connection
def close_connection():
    cursor.close()
    conn.close()
    print("Database connection closed!")

# Example usage
add_user("John", "john@example.com", 25)
add_user("Alice", "alice@example.com", 30)
get_all_users()
update_user_age(1, 26)
delete_user(2)
get_all_users()
close_connection()
