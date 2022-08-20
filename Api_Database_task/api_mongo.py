import logging
from flask import Flask, request
from bson.json_util import dumps
import json
import pymongo
logging.basicConfig(filename='api_mongo.log', level=logging.INFO, format='%(levelname)s %(asctime)s %(message)s')

logging.info("Establishing connection with MongoDB")
try:
    client = pymongo.MongoClient("mongodb+srv://sam01091994:Shub1994@clustershub.jujlbeo.mongodb.net/?retryWrites=true&w=majority")
    db = client.test
    logging.info("Connection to MongoDB successful")
except Exception as e:
    logging.exception(e)


logging.info("creating an object 'app' in class Flask")
app = Flask(__name__)


#1. Write a program to insert a record in mongoDB via api
logging.info("Creating api for MongoDB insert")
@app.route('/mongodb/insert', methods=['POST'])
def mongo_insert():
    if (request.method == 'POST'):
        a = request.json['query1']
        b = request.json['query2']
        c = request.json['query3']
        try:
            database = client['my_details']
            collection = database['shubham']
            collection.insert_one(a)
            collection.insert_one(b)
            collection.insert_one(c)
            logging.info("Data insertion successful")
            return "Data insertion successful"
        except Exception as q:
            logging.exception(q)

"""
In postman
{
    "query1": {"name": "shubham" , "age": 27, "gender": "male", "email" : "sam@gmail.com"},
    "query2": {"name": "Jeetisha" , "age": 26, "gender": "female", "email" : "jazz@gmail.com"},
    "query3": {"name": "sameer" , "age": 36, "gender": "male", "email" : "sr@gmail.com"}
}
"""

# 2. Write a program to update a record vis api

logging.info("Creating api for MongoDB update")
@app.route('/mongodb/update', methods=['POST'])
def mongo_update():
    if (request.method == 'POST'):
        a = request.json['query4']
        b = request.json['query5']
        try:
            database = client['my_details']
            collection = database['shubham']
            collection.update_one(a, b)
            logging.info("Data updation successful")
            return "Data updation successful"
        except Exception as q:
            logging.exception(q)

"""
In postman
{
    "query4": {"age": 27} ,
    "query5": {"$set": {"age": 28}}
}
"""

# 3. Write a program to delete a record via api

logging.info("Creating api for MongoDB delete")
@app.route('/mongodb/delete', methods=['POST'])
def mongo_delete():
    if (request.method == 'POST'):
        a = request.json['query6']
        try:
            database = client['my_details']
            collection = database['shubham']
            collection.delete_one(a)
            logging.info("Data deletion successful")
            return "Data deletion successful"
        except Exception as q:
            logging.exception(q)

"""
In postman
{
    "query6": {"name" : "sameer"}
}

"""

# 4. Write a program to fetch a record via api

logging.info("Creating api for MongoDB fetch record")
@app.route('/mongodb/fetchdata', methods=['POST'])
def mongo_fetch_data():
    if (request.method == 'POST'):
        a = request.json['query7']
        try:
            database = client['my_details']
            collection = database['shubham']
            x = collection.find_one(a)
            logging.info("data fetched successfully from MongoDB")
            return json.loads(dumps(x))
        except Exception as q:
            logging.exception(q)

"""
In postman
{
    "query7": {"age": 28} 
}
Output
{
    "_id": {
        "$oid": "63013254649dfded6165632c"
    },
    "age": 28,
    "email": "sam@gmail.com",
    "gender": "male",
    "name": "shubham"
}

"""



if __name__=='__main__':
    app.run()