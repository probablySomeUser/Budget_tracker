import sqlite3
from datetime import date
from sys import exit
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

def get_price_of_category(amount,total):
    sub_amount = 0
    while True: 
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
        answer = yes_no("Is this the final item of the category? [y/n]\n")
        if answer == 'y':
            return sub_amount,total

def add_to_database(year,month,day,amount,category,store):
    connection = get_connection()
    cursor = connection.cursor()
    query = """
        INSERT INTO expenses (year, month, day, amount, category, store)
        VALUES (?,?,?,?,?,?)
    """
    cursor.execute(query,(year,month,day,amount,category,store))
    close_connection(connection)

def select_category(categories):
    counter = 1
    for i in categories:
        print(counter, ') ',i)
        counter += 1
    answer = get_int(1,len(categories),"")
    category = categories[answer-1]
    return category

def multiple_categories(amount,categories,year,month,day,store):
    connection = get_connection()
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
        answer = yes_no("Is this the final category? [y/n]\n")
        match answer:
            case 'y':
                query = """
        INSERT INTO expenses (year, month, day, amount, category, store)
        VALUES (?,?,?,?,?,?)
    """
                cursor.execute(query,(year,month,day,amount-total,category,store))
            case 'n':
                query = """
        INSERT INTO expenses (year, month, day, amount, category, store)
        VALUES (?,?,?,?,?,?)
    """
                cursor.execute(query,(year,month,day,amount-total,category,store))
        if answer == 'y':
                    break
    close_connection(connection)



def enter():
    print('You have chosen to enter a purchase. When was the purchase?')
    print('1) Today')
    print('2) This month, but not today')
    print('3) Not this month')
    answer = get_int(1,3,"")
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
    answer = get_int(0,len(categories),"")

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
        answer = yes_no("is that all? [y/n]\n")
        match answer:
            case 'y':
                break
            case 'n':
                enter()
                continue