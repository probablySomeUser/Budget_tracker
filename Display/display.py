import sqlite3
from pathlib import Path

def display():
    database_path = Path(__file__).resolve().parent.parent / "database.db"
    connection = sqlite3.connect(database_path)
    cursor = connection.cursor()
    query = """
    SELECT category, amount FROM expenses
    """
    outprint = cursor.execute(query)
    a= outprint.fetchmany(2)
    connection.close()
    print(a)

display()