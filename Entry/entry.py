import sqlite3
from pathlib import Path


def enter():
    database_path = Path(__file__).resolve().parent.parent / "database.db"
    year = int(input('year: '))
    month = int(input('month: '))
    day = int(input('day: '))
    amount = int(float(input('amount: '))*100) #Stores the amount in øre
    category = input('category: ')
    store = input('store: ')
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