import sqlite3
from pathlib import Path
from datetime import date
from sys import exit

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
    while True:
        try:
            answer = int(input(message))
        except:
            print('Not at number')
            continue
        if minimum <= answer <= maximum:
            break
        else:
            print('That number is not accepted')
    return answer

def get_price_of_category(amount,total):
    sub_amount = 0
    while True: #Gets price
        while True:
           try:
               price = int(float(input('Price of item:\n'))*100)
           except:
               print('That is not a number')
               continue
           if 0<price:
               break
           else:
               print('Not possible')
        sub_amount += price
        total += price
        if total > amount:
            print('You have spent more than you originally said??')
            exit()
        #Ask if category is done
        while True:
            answer = input('Is this the final item of the category?[y/n]')
            match answer:
                case 'y'|'n':
                    break
                case _:
                    print('I did not understand that')
                    continue
        if answer == 'y':
            return sub_amount,total

def add_to_database(year,month,day,amount,category,store):
    database_path = Path(__file__).resolve().parent.parent / "database.db"
    connection = sqlite3.connect(database_path)
    cursor = connection.cursor()
    query = """
        INSERT INTO expenses (year, month, day, amount, category, store)
        VALUES (?,?,?,?,?,?)
    """
    cursor.execute(query,(year,month,day,amount,category,store))
    connection.commit()
    connection.close()

def select_category(categories):
    counter = 1
    for i in categories:
        print(counter, ') ',i)
        counter += 1
    while True: #Selects category
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
    return category

def multiple_categories(amount,categories,year,month,day,store):
    database_path = Path(__file__).resolve().parent.parent / "database.db"
    connection = sqlite3.connect(database_path)
    cursor = connection.cursor()
    print('What is the first category? Your options are')
    category = select_category(categories)
    total = 0
    sub_amount,total = get_price_of_category(amount,total)
    query = """
        INSERT INTO expenses (year, month, day, amount, category, store)
        VALUES (?,?,?,?,?,?)
        """
    cursor.execute(query,(year,month,day,sub_amount,category,store))
    while True: #Deals with the remaining categories
        print('What is the next category?\n')
        category = select_category(categories)
        #Ask if is final category
        while True:
                answer = input('Is this the final category?[y/n]\n')
                match answer:
                    case 'y':
                        query = """
        INSERT INTO expenses (year, month, day, amount, category, store)
        VALUES (?,?,?,?,?,?)
    """
                        cursor.execute(query,(year,month,day,amount-total,category,store))
                        break
                    case 'n':
                        sub_amount,total = get_price_of_category(amount,total)
                        query = """
        INSERT INTO expenses (year, month, day, amount, category, store)
        VALUES (?,?,?,?,?,?)
        """
                        cursor.execute(query,(year,month,day,sub_amount,category,store))
                        break
                    case _:
                        print('I do not understand')
        if answer == 'y':
                    break
    connection.commit()
    connection.close()



def enter():
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
            day = get_time('day','What day was the purchase?\n')
        case 3:
            year = get_time('year','What year was the purchase?\n')
            month = get_time('month','What month was the purchase?\n')
            day = get_time('day','What day was the purchase?\n')
    while True:
        try:
            amount = int(float(input('How much did you pay(kr)?:\n'))*100) #Stores the amount in øre
            if amount > 0:
                break
            else:
                print("I don't believe that")
        except:
            print('That is not a number')
    while True:
        store = input('Where did you buy it?\n')
        if store != '':
            break
        else:
            print('Please enter something')
    print('What is the category? Your options are')
    categories = ['Rent','Insurance','Subscriptions','Internet','Food','Non-food','Transport','Fun','Other']
    print('0) Multiple categories')
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
        if 0<=answer <= counter:
            break
        else:
            print('That is not an option')
    if answer == 0:
        multiple_categories(amount,categories,year,month,day,store)
        return 0
    else:
        category = categories[answer-1]
        add_to_database(year,month,day,amount,category,store)
        return 0

def process():
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