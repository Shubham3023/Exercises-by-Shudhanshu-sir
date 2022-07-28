#2. Do a bulk load for these two table for respective dataset

import mysql.connector as conn
import logging
logging.basicConfig(filename='Table_creation_dresssales.log', level= logging.INFO, format='%(levelname)s %(asctime)s %(message)s' )

logging.info("Creating Mysql connection with pycharm and creating cursor object")
try:
    mydb = conn.connect(host= 'localhost', user= 'root', passwd= 'Shub@1994#',allow_local_infile=True)
    cursor = mydb.cursor()
except Exception as e:
    logging.exception(e)

logging.info("Creating table 'Dress_sales_store'")
try:
    s = cursor.execute("""create table if not exists online_store.Dress_sales_store ( 
            Dress_ID int,
            `29/8/2013` int,
            `31/8/2013` int,
            `09-02-2013` int,
            `09-04-2013` int,
            `09-06-2013` int,
            `09-08-2013` int,
            `09-10-2013` int,
            `09-12-2013` int,
            `14/9/2013` int,
            `16/9/2013` int,
            `18/9/2013` int,
            `20-09-2013` int,
            `22/9/2013` int,
            `24/9/2013` int,
            `26/9/2013` int,
            `28/9/2013` int,
            `30/9/2013` int,
            `10-02-2013` int,
            `10-04-2013` int,
            `10-06-2013` int,
            `10-08-2010` int,
            `10-10-2013` int,
            `10-12-2013` int)"""
                       )
    cursor.execute(s)
except Exception as e:
    logging.exception(e)

logging.info("Loading data into table 'Dress_sales_store' from csv file 'dresssales.csv'")
try:
    s1 = """
    load data local infile 'C:/dresssales.csv' into table online_store.Dress_sales_store
    fields terminated by ','
    enclosed by '"'
    lines terminated by '\n'
    ignore 1 lines
    """
    cursor.execute(s1)
    mydb.commit()
except Exception as e:
    logging.exception(e)


#  9. Try to find out total dress sell for individual dress id

logging.info("Selecting all from Dress_sales_store table")
try:
    cursor.execute("select * from online_store.Dress_sales_store")
    sum_dress_id = []
    for i in cursor.fetchall() :
        sum = 0
        for j in i[1:]:
            sum += j
        sum_dress_id.append((i[0], sum))

    print("List of Dress_Id and total sales pair for Dress sales table is : \n",sum_dress_id )

except Exception as e:
    logging.exception(e)


#  10. Try to find out third highest most selling dress

logging.info("Finding third highest most selling dress")
try:
    logging.info("sorting sum_dress_id list in descending order")
    sum_dress_id.sort(key= lambda x : x[1], reverse= True)
    print("Sorted dress sales based in descending order is: \n",sum_dress_id)

    print("Third highest selling Dress_ID and Total sales is: ", sum_dress_id[2])
    cursor.execute("""  select *
                        from online_store.attribute_dataset_store
                        where Dress_ID = 1006032852 """)
    for i in cursor.fetchall():
        "Details of third highest most selling dress is: {}".format(i)
        print("Details of third highest most selling dress is: {}".format(i))

except Exception as e:
    logging.exception(e)


