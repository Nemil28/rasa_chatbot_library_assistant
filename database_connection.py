import psycopg2
from psycopg2 import Error

def DataUpdate(bookresponse): 
    mydb = psycopg2.connect(
        host="localhost", 
        user="postgres",  
        passwd="root", 
        port="5432",
        database="rasa_chatbot"
    ) 
    
    mycursor = mydb.cursor() 

#    sql = 'CREATE TABLE rasa_project (BookResponse VARCHAR(255))'
#    mycursor.execute(sql)
    
    sql = """ INSERT INTO FeedBack_rasa_date (bookresponse) VALUES (%s) """
    record_to_insert = (bookresponse)
    mycursor.execute(sql) 
    
    mydb.commit()

    mycursor.close()
    mydb.close()