import entry
import sqlite3
from datetime import date

def correcting():
    #Select month
    print('What month do you want to correct in?')
    print('1) This month')
    print('2) Not this month')
    while True:
        try:
            answer = int(input())
        except:
            print('That is not a number')
            continue
        if answer in [1,2]:
            break
    if answer == 1:
        year,month = str(date.today()).split('-')[0:2]
    else:
        year = entry.get_time('year','What year?\n')
        month = entry.get_time('month','What month?\n')
#Display all transactions in month
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()
    query = '''
    SELECT * FROM expenses
    WHERE year = ? AND month = ?
    ORDER BY day ASC
    '''
    expenses = cursor.execute(query,(year,month)).fetchall()
    print('The transactions in this month are:')
    print('id\tDate\t\tamount\t\tcategory\tstore')
    ids = []
    for item in expenses:
        amount = float(item[4])/100
        print(item[0],'\t', item[3] ,'/', item[2], '/', item[1], '\t', amount, 'kr\t', item[5], '\t\t', item[6])
        ids.append(item[0])
#Select transaction
    print('Do you want to do something? [y/n]')
    while True:
        answer = input()
        match answer:
            case 'y':
                break
            case 'n':
                return 0
            case _:
                print('I did not understand that')
    print('What expense are we talking about?')
    while True:
        try:
            expense = int(input('id:'))
        except:
            print('That is not a number')
            continue
        if expense in ids:
            break
        else:
            print('That expence is not in this month')

#Delete or change
    print('What do you want do?')
    print('1) Delete the expense')
    print('2) Change the expense')
    while True:
        try:
            answer = int(input())
        except:
            print('That is not a number')
            continue
        if answer in [1,2]:
            break
        else:
            print('That is not an option')
#Delete
    if answer ==1:
        query = '''
        DELETE FROM expenses
        WHERE id = ?
        '''
        cursor.execute(query,(expense,))
    else: #Change
        print('What do you want to change')
        options = ['year','month','day','amount','category','store']
        counter = 1
        for i in options:
            print(counter,f') {i}')
            counter += 1
        while True:
            try:
                answer = int(input())
            except:
                print('That is not a number')
                continue
            if 0<answer<=len(options):
                break
            else:
                print('That is not an option')
        column = options[answer-1]
        match column:
            case 'year'|'month'| 'day':
                replacement = entry.get_time(column,'What is it?\n')
            case 'amount':
                while True:
                    try:
                        replacement = int(float(input('What is it?\n'))*100)
                    except:
                        print('That is not a number')
                        continue
                    if replacement > 0:
                        break
                    else:
                        print('I do not believe that')
            case 'category':
                print('What is the category then?')
                categories = ['Rent','Insurance','Subscriptions','Internet','Food','Non-food','Transport','Fun','Other']
                replacement = entry.select_category(categories)
            case 'store':
                replacement = input('What is it then?\n')
        query = f'''
            UPDATE expenses
            SET {column} = ?
            WHERE id = ?
            '''
        cursor.execute(query,(replacement,expense))
    connection.commit()
    connection.close()