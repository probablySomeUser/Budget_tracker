import sqlite3
from pathlib import Path
from datetime import date

def display(year,month):
    database_path = Path(__file__).resolve().parent.parent / "database.db"
    connection = sqlite3.connect(database_path)
    cursor = connection.cursor()
    query = """
    SELECT category, SUM(amount) FROM expenses
    WHERE year = ? AND month = ?
    GROUP BY category
    """
    result = cursor.execute(query,(year,month)).fetchall()
    connection.close()
    for entry in result:
        amount = int(entry[1])/100
        print(f'{entry[0]}: {amount}')

def process():
    print('What month do you wish to display?')
    print('1) This month')
    print('2) Last month')
    print('3) Another month')
    while True:
        try:
            answer = int(input())
        except:
            print('That is not a number. Try again')
        match answer:
            case 1:
                year,month = str(date.today()).split('-')[0:2]
                display(year,month)
                break
            case 2:
                year,month = str(date.today()).split('-')[0:2]
                month = (int(month)-1)%12
                if month == 0:
                    month = 12
                    year = int(year) -1
                display(year,month)
                break
            case 3:
                year = input('What year?\n')
                month = input('What month?\n')
                display(year,month)
                break
            case _:
                print('That is not an option')