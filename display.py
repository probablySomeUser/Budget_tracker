import sqlite3
from datetime import date
from utils import get_int
from utils import yes_no
from utils import get_connection
from utils import close_connection

def get_time(unit,message):
    match unit:
        case 'day':
            maximum = 31
            minimum = 1
        case 'month':
            maximum = 12
            minimum  = 1
        case 'year':
            maximum = 3000
            minimum = 0
    answer = get_int(minimum,maximum,message)
    return answer

def display(year,month):
    connection = get_connection()
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
    answer = get_int(1,3,"")
    match answer:
        case 1:
            year,month = str(date.today()).split('-')[0:2]
            display(year,month)
        case 2:
            year,month = str(date.today()).split('-')[0:2]
            month = (int(month)-1)%12
            if month == 0:
                month = 12
                year = int(year) -1
            display(year,month)
        case 3:
            year = get_time('year','What year?\n')
            month = get_time('month','What month?\n')
            display(year,month)