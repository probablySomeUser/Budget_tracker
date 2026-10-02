import psycopg
import os

def get_int(minimum:int,maximum:int,message:str,error_message_not_integer="That is not an integer",error_message_integer="That is not an option") -> int:
    while True:
        try:
            answer = int(input(message))
        except:
            print(error_message_not_integer)
        if minimum <= answer <= maximum:
            break
        else:
            print(error_message_integer)
    return answer

def yes_no(question:str,not_answer="I did not understand that, try again")->str:
    while True:
        answer = input(question)
        match answer:
            case 'y' | 'n':
                return answer
            case _:
                print(not_answer)

def get_connection():
    #while True:
    conn = psycopg.connect(
        host=os.environ["DB_HOST"],
        dbname=os.environ["POSTGRES_DB"],
        user=os.environ["POSTGRES_USER"],
        password=os.environ["POSTGRES_PASSWORD"],
    )
    return conn

def close_connection(connection):
    connection.commit()
    connection.close()