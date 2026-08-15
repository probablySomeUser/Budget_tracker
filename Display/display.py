import sqlite3
from pathlib import Path
from datetime import date

def display(year,month):
    database_path = Path(__file__).resolve().parent.parent / "database.db"
    connection = sqlite3.connect(database_path)
    cursor = connection.cursor()
    query = """
    SELECT category, SUM(amount)/100 FROM expenses
    WHERE year = ? AND month = ?
    GROUP BY category
    """
    result = cursor.execute(query,(year,month)).fetchall()
    connection.close()
    #print(result)
    # Create table
    for entry in result:
        print(f'{entry[0]}: {entry[1]}')

if __name__ == '__main__':
    year, month = str(date.today()).split('-')[0:2]
    display(year,month)