import logging
from flask import Flask, request
import mysql.connector as conn


logging.basicConfig(filename='api_sql.log', level=logging.INFO, format='%(levelname)s %(asctime)s %(message)s')

logging.info("Establishing connection with MySQL")

try:
    mydb = conn.connect(host="localhost", user="root", passwd="123456")
    cursor = mydb.cursor()
    logging.info("Connection to MySQL established successfully")
except Exception as e:
    logging.exception(e)

logging.info("creating an object 'app' in class Flask")

app = Flask(__name__)

# 1. Write a program to insert a record in sql table via api.

logging.info("Creating api for sql insert")
@app.route('/sql/insert', methods=['POST'])
def sql_insert():
    if (request.method=='POST'):
        a = request.json['query1']
        b = request.json['query2']
        c = request.json['query3']
        d = request.json['query4']
        f = request.json['query5']


        try:
            cursor.execute(a)
            cursor.execute(b)
            cursor.execute(c)
            cursor.execute(d)
            cursor.execute(f)
            mydb.commit()
            logging.info("inserted data successfully")
            return "inserted data successfully"
        except Exception as q:
            logging.exception(q)

"""
In postman
{
    "query1":"create database api_task",
    "query2":"create table api_task.my_details(first_name varchar(30), last_name varchar(30), age int, gender varchar(10),
     email varchar(30) )",
    "query3":"insert into api_task.my_details values('Shubham', 'Verma', 27, 'Male', 'sav@gmail.com')",
    "query4":"insert into api_task.my_details values('Jeetisha', 'Borkar', 26, 'Female', 'jazz@gmail.com')",
    "query5":"insert into api_task.my_details values('Sameer', 'Ingle', 47, 'Male', 'sam@gmail.com')"
    
}
"""

# 2. Write a program to update a record vis api
logging.info("Creating api for sql update")
@app.route('/sql/update', methods=['POST'])
def sql_update():
    if (request.method == 'POST'):
        a = request.json['query6']
        b = request.json['query7']
        try:
            cursor.execute(a)
            cursor.execute(b)
            mydb.commit()
            logging.info("Updated data successfully")
            return "Updated data successfully"
        except Exception as q:
            logging.exception(q)

"""
In postman
{
    "query6":"set SQL_SAFE_UPDATES = 0 ",
    "query7":"update api_task.my_details set age = age + 1, email = 'sav@gmail.com' where first_name = 'Shubham'"
}
"""


# 3. Write a program to delete a record via api

logging.info("Creating api for sql delete")
@app.route('/sql/delete', methods=['POST'])
def sql_delete():
    if (request.method == 'POST'):
        a = request.json['query8']
        try:
            cursor.execute(a)
            mydb.commit()

            logging.info("Deleted data successfully")
            return "Deleted data successfully"
        except Exception as q:
            logging.exception(q)

"""
In postman
{
    "query8":"delete from api_task.my_details where first_name = 'Sameer'"
}
"""

# 4. Write a program to fetch a record via api
logging.info("Creating api for fetching data from MySQL")
@app.route('/sql/fetchdata', methods=['POST'])
def sql_fetch_data():
    if (request.method == 'POST'):
        a = request.json['query9']
        try:
            cursor.execute(a)
            l = []
            for i in cursor.fetchone():
                l.append(i)
            return l
        except Exception as q:
            logging.exception(q)

"""
In postman
Query:
{
    "query9":"select * from api_task.my_details "
}

Output:
[
    [
        "Shubham",
        "Verma",
        28,
        "Male",
        "shub@gmail.com"
    ]
]
"""


if __name__=='__main__':
    app.run()