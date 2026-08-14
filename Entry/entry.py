import math
import sqlite3
from pathlib import Path
from datetime import date
from unicodedata import category


def enter():
    database_path = Path(__file__).resolve().parent.parent / "database.db"
    global date
    print('You have chosen to enter a purchase. When was the purchase?')
    print('1) Today')
    print('2) This month, but not today')
    print('3) Not this month')
    while True:
        answer=int(input())
        if answer in (1,2,3):
            break
        else:
            print('That was not an option')
    match answer:
        case 1:
            year,month,day = str(date.today()).split('-')
        case 2: 
            year, month = str(date.today()).split('-')[0:2]
            day = int(input('What day was it?\n'))
        case 3:
            year = input('What year was the purchase?\n')
            month = input('What month was the purchase?\n')
            day = input('What day was the purchase?\n')
    amount = int(float(input('What did you pay?:\n'))*100) #Stores the amount in øre
    print('What is the cateory? Your options are')
    categories = ['Rent','Insurance','Subscriptions','Internet','Food','Non-food','Transport','Fun','Other']
    counter = 1
    for i in categories:
        print(counter, ') ',i)
        counter += 1
    while True:
        try:
           answer = int(input())
        except:
            print('That is not a number')
            continue
        if 0<answer <= counter:
            break
        else:
            print('That is not an option')
    category = categories[answer-1]
    store = input('Where did you buy it?\n')
    connection = sqlite3.connect(database_path)
    cursor = connection.cursor()
    query = """
        INSERT INTO expenses (year, month, day, amount, category, store)
        VALUES (?,?,?,?,?,?)
    """
    cursor.execute(query,(year,month,day,amount,category,store))
    connection.commit()
    connection.close()
enter()
while True:
    answer = input('Is that all? [y/n]\n')
    match answer:
        case 'y':
            break
        case 'n':
            enter()
            continue
        case _:
            print('I did not understand that, try again')
    