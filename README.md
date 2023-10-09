[![CI](https://github.com/Jason-Guo1999/IDS706-Python-Template/actions/workflows/main.yml/badge.svg)](https://github.com/Jason-Guo1999/IDS706-Python-Template/actions/workflows/main.yml)

# IDS706-MiniProj5

## Overview

This project utilizes the `sqlite3` library to interact with a SQL database and perform CRUD (Create, Read, Update, Delete) operations. It is designed to showcase basic database functionality within a Python application.

## Components

1. **`workflows`**: This directory contains GitHub Actions workflows that enable automated Continuous Integration and Continuous Deployment (CI/CD) for the project.

2. **`Makefile`**: The `Makefile` provides a list of make commands and instructions for building and managing the project.

3. **`requirements.txt`**: This file lists the project's dependencies, including the necessary package for working with SQLite databases (`sqlite3`).

4. **`main.py`**: The `main.py` script connects to an SQLite3 database, creates a new table named "users," adds two new user records, and performs basic inquiry operations on the database.

5. **`test_main.py`**: The `test_main.py` script is used to test whether the insertion of two user records into the database was successful.

## CRUD 

The project demonstrates basic CRUD operations on an SQLite database:

- **Create**: The following code creates a new table named "users" if it does not already exist:

```python
cursor.execute('''CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username TEXT NOT NULL)''')
```

- **Read**: The following code retrieves usernames from the "users" table:

```python
cursor.execute('SELECT username FROM users WHERE id = 2')
```

- **Update**: The following code inserts a new user with the username "rc381" into the "users" table:

```python
cursor.execute('INSERT INTO users (username) VALUES ('rc381')')
```

- **Delete**: The following code deletes a user with the username "rc381" from the "users" table:

```python
cursor.execute('DELETE FROM users WHERE username = 'rc381'')
cursor.execute("DELETE FROM users")
```

Feel free to explore and modify this project to learn more about SQLite database operations in Python.