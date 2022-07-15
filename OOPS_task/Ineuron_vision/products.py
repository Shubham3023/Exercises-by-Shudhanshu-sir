import logging

logging.basicConfig(filename="Products.log", level= logging.INFO, format='%(levelname)s %(asctime)s %(message)s')

logging.info("importing Class 'Basic_Code_IV' from module 'Basic_code_IV' and package 'Ineuron_vision'")
from Ineuron_vision.Basic_code_IV import Basic_Code_IV

logging.info("Creating Class Products and inheriting class Basic_code_IV in it.")

class Products(Basic_Code_IV):
    pass


logging.info("Creating objects in Class Products")

ad1 = Products("Appareal Detection","Detection of proper clothing and wearables by the employees in a working environment.",
                        ["Sudhanshu","Sunny Chandra", "Saksham Choudhary","Sachin Agarwal"],100)

ad2 = Products("Appliance Energy Consumption Prediction", "Track spending on different appliances by single power consumption forecating application.",
               ["Krish Naik","Shashank Mishra","Sunny Chandra", "Saksham Choudhary","Sachin Agarwal"],100)

ad3 = Products("Diabetes Prediction", "Keep your anatomy measurement with you for quick and easy prognosis of diabetes.",
               ["Sudhanshu Kumar","Krish Naik","Shashank Mishra","Saksham Choudhary","Sachin Agarwal"],100)

ad4 = Products("Credit Card Approval Prediction", "Evaulate immcalcuted credit card approval propability.",
               ["Shashank Mishra","Saksham Choudhary","Sachin Agarwal"],100)

ad5 = Products("Spam Message Prediction", "An application to ensure whether the message is spam or not.",
               ["Sunny Savita","Shashank Mishra","Saksham Choudhary","Sachin Agarwal"],100)

ad6 = Products("Metro Interstate Traffic Prediction", "Calibration of traffic prediction on the bases of weather conditions.",
               ["Shivan Roy","Sunny Savita","Shashank Mishra","Saksham Choudhary","Sachin Agarwal"],100)

ad7 = Products("Oil Spill Detection", "Prevention of oil leaks from carriers & segmenting oil spill patches in waterways.",
               ["Sudhanshu Kumar","Shashank Mishra","Saksham Choudhary","Sachin Agarwal"],100)

ad8 = Products("Spam Message Prediction", "An application to ensure whether the message is spam or not.",
               ["Sudhanshu Kumar","Sunny Savita","Shashank Mishra","Saksham Choudhary","Sachin Agarwal"],100)

ad9 = Products("Pipeline Leakage Detection", "Mainting fault tolearance systems & detecting leaks in oil & gas pipelines.",
               ["Shivan Roy","Sunny Savita","Shashank Mishra","Saksham Choudhary","Sachin Agarwal"],100)

ad10 = Products("Forest Cover Type Prediction", "To predict 7 different types of forest cover on the basis of land surrounding of predominant terrestrial ecosystem.",
               ["Sudhanshu Kumar","Sunny Savita","Shashank Mishra","Saksham Choudhary","Sachin Agarwal"],100)

ad1.display_project_details()
ad2.display_project_details()
ad3.display_project_details()
ad4.display_project_details()
ad5.display_project_details()
ad6.display_project_details()
ad7.display_project_details()
ad8.display_project_details()
ad9.display_project_details()
ad10.display_project_details()

