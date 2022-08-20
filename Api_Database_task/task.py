from flask import Flask, request
import mysql.connector as conn
mydb = conn.connect(host= "localhost", user = "root", passwd= "123456")
cursor = mydb.cursor()


app = Flask(__name__)

#1. Write a program to insert a record in sql table via api

@app.route('/sql/insert', methods=['POST'])
def sql_insert():
    if (request.method == 'POST'):
        a = request.json['query1']
        b = request.json['query2']
        c = request.json['query3']

        cursor.execute(a)
        cursor.execute(b)
        cursor.execute(c)
        mydb.commit()

        return "Successful"

"""
In postman
{
    "query1":"create database api_task",
    "query2":"create table api_task.my_details(first_name varchar(30), last_name varchar(30), age int, gender varchar(10),
     email varchar(30) )",
    "query3":"insert into api_task.my_details values('Shubham', 'Verma', 27, 'Male', 'sam@gmail.com')"
}
"""

# 2. Write a program to update a record vis api

@app.route('/sql/update', methods=['POST'])
def sql_update():
    if (request.method == 'POST'):
        a = request.json['query4']
        b = request.json['query5']

        cursor.execute(a)
        cursor.execute(b)

        mydb.commit()

        return "Successful"

"""
In postman
{
    "query4":"set SQL_SAFE_UPDATES = 0 ",
    "query5":"update api_task.my_details set age = age + 1, email = 'sav@gmail.com' where first_name = 'Shubham'"
}
"""

# 3. Write a program to delete a record via api


@app.route('/sql/delete', methods=['POST'])
def sql_delete():
    if (request.method == 'POST'):
        a = request.json['query6']

        cursor.execute(a)

        mydb.commit()

        return "Successful"

"""
In postman
{
    "query6":"delete from api_task.my_details where first_name = 'manoj'"
}
"""

# 4. Write a program to fetch a record via api

@app.route('/sql/fetchdata', methods=['POST'])
def sql_fetch_data():
    if (request.method == 'POST'):
        a = request.json['query7']

        cursor.execute(a)
        l = []
        for i in cursor.fetchall():
            l.append(i)
        return l

"""
In postman
Query:
{
    "query7":"select * from api_task.my_details "
}

Output:
[
    [
        "Shubham",
        "Verma",
        28,
        "Male",
        "sav@gmail.com"
    ]
]
"""

if __name__=='__main__':
    app.run()


