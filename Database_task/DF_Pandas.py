#3. Read these dataset in pandas as a dataframe

import mysql.connector as conn
import pandas as pd
import logging
import pymongo
import json
logging.basicConfig(filename='DF_Pandas.log', level= logging.INFO, format='%(levelname)s %(asctime)s %(message)s' )

logging.info("Creating Mysql connection with pycharm and creating cursor object")
try:
    mydb = conn.connect(host= 'localhost', user= 'root', passwd= 'Shub@1994#', use_pure = True)
    cursor = mydb.cursor()
    logging.info("Connection to Mysql established and cursor object created")
except Exception as e:
    logging.exception(e)

logging.info("Reading data from both the table into pandas")
try:
    read_attribute = pd.read_sql('select * from online_store.Attribute_dataset_store', mydb)
    read_dresssales = pd.read_sql('select * from online_store.Dress_sales_store', mydb)
except Exception as e:
    logging.exception(e)

logging.info("converting Mysql data into pandas dataframe")
try:
    attribute_data_df = pd.DataFrame(read_attribute,columns= ['Dress_ID','Style','Price' ,'Rating','Size' ,
        'Season' ,'NeckLine' ,'SleeveLength','waiseline' ,'Material' ,'FabricType' ,'Decoration' ,'PatternType',
        'Recommendation'] )

    dress_sales_df = pd.DataFrame(read_dresssales, columns=['Dress_ID','29/8/2013','31/8/2013','09-02-2013','09-04-2013',
        '09-06-2013','09-08-2013','09-10-2013','09-12-2013','14/9/2013','16/9/2013','18/9/2013','20-09-2013','22/9/2013',
        '24/9/2013','26/9/2013','28/9/2013','30/9/2013','10-02-2013','10-04-2013','10-06-2013','10-08-2010','10-10-2013',
        '10-12-2013'])
except Exception as e:
    logging.exception(e)

logging.info(attribute_data_df)
logging.info(dress_sales_df)

#4. Convert tables in json format

logging.info("converting pandas dataframe for attribute_data and dress_sales to json file")

try:
    attribute_data_json = attribute_data_df.to_json("C:\\Users\\Shubham\\PycharmProjects\\Data_task_24.07.2022\\attribute_data_json.json")
    dress_sales_json = dress_sales_df.to_json("C:\\Users\\Shubham\\PycharmProjects\\Data_task_24.07.2022\\dress_sales_json.json")
except Exception as e:
    logging.info(e)

#5. Store this data set into mongo db



try:
    logging.info("Connecting to mongodb atlas")

    client = pymongo.MongoClient(
        "mongodb+srv://sam01091994:Shub1994@clustershub.jujlbeo.mongodb.net/?retryWrites=true&w=majority")
    dbmongo = client.test

    logging.info("Connection to mongodb atlas is successful")

    logging.info("Creating database for online_store and collection for attribute_data and dress_sales")

    database = client['online_store_mongo']
    collection_att = database['Attribute_data_mongo']
    collection_dress = database['dress_sales_mongo']

    logging.info("Collection and database creation successful")

    logging.info("loading data into collection Attribute_data_mongo")
    with open('C:\\Users\\Shubham\\PycharmProjects\\Data_task_24.07.2022\\attribute_data_json.json') as file:
        file_data = json.load(file)

    if isinstance(file_data, list):
        collection_att.insert_many(file_data)
    else:
        collection_att.insert_one(file_data)
    logging.info("loading data into collection Attribute_data_mongo successful")

    logging.info("loading data into collection dress_sales_mongo")
    with open('C:\\Users\\Shubham\\PycharmProjects\\Data_task_24.07.2022\\dress_sales_json.json') as file1:
        file_data1 = json.load(file1)

    if isinstance(file_data, list):
        collection_dress.insert_many(file_data)
    else:
        collection_dress.insert_one(file_data)
    logging.info("loading data into collection dress_sales_mongo successful")

except Exception as e:
    logging.exception(e)

