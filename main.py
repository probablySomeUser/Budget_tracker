import sqlite3
import entry
import display
import correcting

from utils import get_int
from utils import yes_no
from utils import get_connection
from utils import close_connection

def create_table():
    connection = get_connection()
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
    close_connection(connection)

def main():
    create_table()
    print('What do you want to do?')
    print('1) Enter expense(s)')
    print('2) See monthly display')
    print('3) Correct entry',end='')
    match get_int(1,3,"\n"):
        case 1:
            entry.process()
        case 2:
            display.process()
        case 3:
            correcting.correcting()

if __name__ == '__main__':
    main()