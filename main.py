import sqlite3

def create_database():
    # Connect to SQLite database (or create it if it doesn't exist)
    conn = sqlite3.connect('exercise_database.db')

    # Create a cursor object to execute SQL queries
    cursor = conn.cursor()

    # Create a table for weightlifting exercises
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS weightlifting_exercises (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            equipment_needed TEXT,
            score INTEGER
        )
    ''')

    # Create a table for gymnastic exercises
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS gymnastic_exercises (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            difficulty TEXT,
            score INTEGER
        )
    ''')

    # Create a table for cardio exercises
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS cardio_exercises (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            intensity TEXT,
            score INTEGER
        )
    ''')

    # Create a table for functional exercises
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS functional_exercises (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            description TEXT,
            score INTEGER
        )
    ''')

    # Commit changes and close the connection
    conn.commit()
    conn.close()

def add_weightlifting_exercise():
    # Prompt the user for weightlifting exercise details
    name = input("Enter the weightlifting exercise name: ")
    equipment_needed = input("Enter the equipment needed: ")
    score = int(input("Enter the exercise score: "))

    # Connect to SQLite database
    conn = sqlite3.connect('exercise_database.db')
    cursor = conn.cursor()

    # Insert the exercise data into the weightlifting table
    cursor.execute('''
        INSERT INTO weightlifting_exercises (name, equipment_needed, score)
        VALUES (?, ?, ?)
    ''', (name, equipment_needed, score))

    # Commit changes and close the connection
    conn.commit()
    conn.close()

# ... Similar functions for other exercise categories (gymnastic, cardio, functional)

if __name__ == "__main__":
    create_database()

    # Allow the user to add weightlifting exercises
    while True:
        add_weightlifting_exercise()
        more_exercises = input("Do you want to add another weightlifting exercise? (yes/no): ")
        if more_exercises.lower() != 'yes':
            break

    # Repeat similar steps for other exercise categories
