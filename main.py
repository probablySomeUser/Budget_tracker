import sqlite3
from pathlib import Path
from Entry import entry
from Display import display

def create_table():
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()
    query = """
    CREATE TABLE IF NOT EXISTS expenses (
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

def main():
    create_table()
    print('What do you want to do?')
    print('1) Enter expense(s)')
    print('2) See monthly display')
    while True:
        try:
            answer = int(input())
        except:
            print('That is not a number')
            continue
        match answer:
            case 1:
                entry.process()
                break
            case 2:
                display.process()
                break
            case _:
                continue

if __name__ == '__main__':
    main()