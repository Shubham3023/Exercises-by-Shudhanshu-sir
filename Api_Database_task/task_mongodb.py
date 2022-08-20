from flask import Flask, request
from bson.json_util import dumps
import json
import pymongo
client = pymongo.MongoClient("mongodb+srv://sam01091994:Shub1994@clustershub.jujlbeo.mongodb.net/?retryWrites=true&w=majority")
db = client.test


app = Flask(__name__)

#1. Write a program to insert a record in mongoDB via api

@app.route('/mongodb/insert', methods=['POST'])
def mongo_insert():
    if (request.method == 'POST'):
        a = request.json['query1']

        database = client['my_details']
        collection = database['shubham']
        collection.insert_one(a)

        return "Successful"

"""
In postman
{
    "query1": {"name": "shubham" , "age": 27, "gender": "male", "email" : "sam@gmail.com"}
}

{
    "query1": {"name": "Jeetisha" , "age": 26, "gender": "female", "email" : "jazz@gmail.com"}
}

{
    "query1": {"name": "sameer" , "age": 36, "gender": "male", "email" : "sr@gmail.com"}
}
"""

# 2. Write a program to update a record vis api


@app.route('/mongodb/update', methods=['POST'])
def mongo_update():
    if (request.method == 'POST'):
        a = request.json['query2']

        database = client['my_details']
        collection = database['shubham']
        collection.update_one(a)

        return "Successful"

"""
In postman
{
    "query2": {"age": 27} , {"$set": {"age": 28}}
}
Sudhanshu sir this query is working in python but it is giving issue in postman,
i guess postman doesn't support nested dicts.
"""

# 3. Write a program to delete a record via api


@app.route('/mongodb/delete', methods=['POST'])
def mongo_delete():
    if (request.method == 'POST'):
        a = request.json['query3']

        database = client['my_details']
        collection = database['shubham']
        collection.delete_one(a)

        return "Successful"

"""
In postman
{
    "query3": {"name" : "sameer"}
}

"""



# 4. Write a program to fetch a record via api

@app.route('/mongodb/fetchdata', methods=['POST'])
def mongo_fetch_data():
    if (request.method == 'POST'):
        a = request.json['query4']

        database = client['my_details']
        collection = database['shubham']
        x = collection.find_one()

        return json.loads(dumps(x))


"""
In postman
{
    "query4": {"age": 27} 
}

Output:
{
    "_id": {
        "$oid": "6300d818e4c58811f432c09a"
    },
    "age": 27,
    "email": "sam@gmail.com",
    "gender": "male",
    "name": "shubham"
}

"""


if __name__=='__main__':
    app.run()
