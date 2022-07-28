#1. Create a table for attribute dataset and dress dataset

import mysql.connector as conn
import logging
logging.basicConfig(filename='Table_creation.log', level= logging.INFO, format='%(levelname)s %(asctime)s %(message)s' )

logging.info("Creating Mysql connection with pycharm and creating cursor object")

try:
    mydb = conn.connect(host= 'localhost', user= 'root', passwd= 'Shub@1994#')
    cursor = mydb.cursor()
    logging.info("Connection to Mysql established and cursor object created")
except Exception as e:
    logging.exception(e)


logging.info("Creating database 'online_store' and table 'Attribute_dataset_store'")
try:
    cursor.execute("create database online_store")

    s = """create table if not exists online_store.Attribute_dataset_store (
            Dress_ID int ,
            Style varchar(30),
            Price varchar(30),
            Rating decimal(2,1),
            Size varchar(30),
            Season varchar(30),
            NeckLine varchar(30),
            SleeveLength varchar(30),
            waiseline varchar(30),
            Material varchar(30),
            FabricType varchar(30),
            Decoration varchar(30),
            PatternType varchar(30),
            Recommendation int)"""
    cursor.execute(s)
except Exception as e:
    logging.exception(e)


logging.info("Loading data into table 'Attribute_dataset_store' from csv file 'attributedata.csv'")
try:
    s1 = """
    load data  infile 'C:/attributedata.csv' into table online_store.Attribute_dataset_store
    fields terminated by ','
    enclosed by '"'
    lines terminated by '\r\n'
    ignore 1 lines
    """
    cursor.execute(s1)
    mydb.commit()
except Exception as e:
    logging.info(e)


# 7. Write a sql query to find out how many unique dress that we have based on dress id
logging.info("No. of unique dresses is: 475")
try:
    cursor.execute("""
            select count(distinct Dress_ID)
            from online_store.attribute_dataset_store
            """)
    for i in cursor.fetchall():
        print("No. of unique dresses is: ",i[0])

except Exception as e:
    logging.exception(e)

# 8. Try to find out how many dress is having recommendation zero
logging.info("No. of dresses having recommendation Zero is : 290")
try:
    cursor.execute("""
        select count(Recommendation)
        from online_store.attribute_dataset_store
        where Recommendation = 0
    """)
    for i in cursor.fetchall():
        print("No. of dresses having recommendation Zero is :",i[0])

except Exception as e:
    logging.exception(e)


# 6. In sql task try to perform left join operation with attribute dataset and dress dateset on column dress id.
logging.info("attribute_dataset_store table and dress_sales_store table is joined successfully")
try:
    cursor.execute("""
            select * 
            from online_store.attribute_dataset_store ad
            join online_store.dress_sales_store ds 
		        using(Dress_ID) 
            """)
except Exception as e:
    logging.exception(e)




