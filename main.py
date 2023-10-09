import sqlite3

if __name__ == "__main__":
    conn = sqlite3.connect("mydatabase.db")
    cursor = conn.cursor()
    # Create a table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            username TEXT NOT NULL
        )
    """)


    # Update
    cursor.execute("INSERT INTO users (username) VALUES ('rc381')")
    cursor.execute("INSERT INTO users (username) VALUES ('sc123')")
    
    conn.commit()

    # Delete
    cursor.execute("DELETE from users where username = 'rc381'")
    cursor.execute("DELETE FROM users")

    # Read
    cursor.execute("SELECT username FROM users WHERE id = 2")
    users = cursor.fetchall()
    
    for user in users:
        print(user)
    
    # Close the connection
    conn.close()
