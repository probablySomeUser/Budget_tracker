#import sqlite3

def get_int(minimum:int,maximum:int,message:str,error_message_not_integer="That is not an integer",error_message_integer="That is not an option") -> int:
    while True:
        try:
            answer = int(input(message))
        except:
            print(error_message_not_integer)
        if minimun <= answer <= maximum:
            break
        else:
            print(error_message_integer)