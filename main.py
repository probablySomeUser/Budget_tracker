import sqlite3

def main():
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()
    query = """
    CREATE TABLE IF NOT EXISTS tracking (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    year INTEGER,
    month INTEGER,
    day INTEGER,
    amount INTEGER,
    category TEXT,
    store TEXT
    );    
    """
    cursor.execute(query)
    connection.commit()
    connection.close()

if __name__ == '__main__':
    main()