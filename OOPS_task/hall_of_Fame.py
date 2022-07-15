import logging
logging.basicConfig(filename="hall_of_Fame.log", level= logging.INFO, format='%(levelname)s %(asctime)s %(message)s')

logging.info("Creating Class Hall_of_Fame")

class Hall_of_Fame :

    logging.info("creating constructor in Class Hall_of_Fame")
    try:
        def __init__(self, name, company,designation, message):
            self.name = name
            self.company = company
            self.designation = designation
            self.message = message
    except Exception as e:
        logging.exception("error is: ", e)

    logging.info("Creating Methods in Class Hall_of_Fame")
    try:
        def student_hof_deatils(self):
            logging.info("\nStudent Name: %s,\nCompany Name: %s and\nMessage for Juniors: %s\n",
                         self.name, self.company, self.message )
            return "\nStudent Name: {}, \nCompany Name: {} and \nMessage to Juniors: {}\n".format(
                         self.name, self.company, self.message )
    except Exception as e:
        logging.exception("error is: ", e)

    try:
        def Hof_mesage(self):
            logging.info("\nMessage for Juniors: %s\n",self.message)
            return "\nMessage for Juniors: {}\n".format(self.message)
    except Exception as e:
        logging.exception("error is: ", e)

# Creating objects in Class Hall_of_Fame

hf1 = Hall_of_Fame("Santosh Kumar", "MU-Sigma","Decision Scientist","One of the best things I ever did in my career path is to choose INEURON as my career buddy.\n"
                                        "I am so thankful to Sudhanshu Sir , Krish naik sir for introducing iNeuron platform which changed \n"
                                        "my learning patterns, practicing real life projects etc. Hi, I am Santhosh from FSDS batch from iNeuron,\n"
                                        "which made me to get into Data Science domain from platform support with in a small while. Still so \n"
                                        "many are there to learn from iNeuron and hope this platform would change lives of many more aspiring \n"
                                        "people in all domains.")

hf2 = Hall_of_Fame("Sachin Mishra", "Data Society", "Data Scientist", "Hello All, I can't believe that I am going to join Data Society as a Data Scientist.\n"
                                        "But It all happened due to the whole Ineuron team and the super-power available for all of us, yes you guessed it right (Internet).\n"
                                        "I still remember when I started my journey into the data field I was so afraid of coding and logic building, but as time passed away \n"
                                        "I was like just keep practicing and follow the best practices, and the best advice that my mentor is giving. I would like to thank\n"
                                        "Mr. Sudhanshu Kumar, Krish Naik and Dhaval Patel (Codebasics). These guys are simply awesome. So much legitimate contents are available\n"
                                        "on youtube regarding data science due to Krish Naik and Dhaval Patel. I learned from them very much but when I joined Inueron I came to\n"
                                        "know how we can build industry(Production) grade Projects. Overall I want to say that if I can become a data scientist,\n"
                                        "I think anybody who loves the field of data and process and not the outcome only, he/she definitely become more successful in the field\n"
                                        "of Data Science.")
hf3 = Hall_of_Fame("Saurabh Kumar","Wiseanalytics.io","Data Engineer","Hi, I am a Saurabh, completed my bachelor's in Petroleum Engineering in 2021. After completing my graduation,\n"
                                        "I joined an IT Consulting firm and worked there for 1 year but my inclination from the beginning was towards ML/Data analytics or in simple words\n"
                                        "playing around with the data and programming. One day I saw Sudhanshu and Krish Sir's videos on youtube. After seeing that I purchased the ML\n"
                                        "masters course from iNeuron.ai (on the canvas platform). After completing that course I started giving interviews, I was able to clear ML-related\n"
                                        "questions but I was stuck when questions were asked on a big data-related topic. Then I purchased a Big Data course by Saurav Agarwal sir.\n"
                                        "After completing that I started giving interviews and I gave around 7-8 interviews 2 months back, out of which I was able to get the offer from\n"
                                        "5 (Business analyst, Data Analyst, Business operation analyst, Python developer, and last but not least Data Engineer). I was just in flow and\n"
                                        "continuously giving the interviews and in the end, I was able to clear all the profiles. The way Sudhanshu sir teaches is just amazing, it gives\n"
                                        "me the confidence that in an interview I told to an interviewer to ask anything about any ML algorithm. I recommend everyone if they really want to\n"
                                        "excel in the field of AI/ML/Data engineering and don't have an idea where to start, just start with iNeuron.ai, because here you not only get\n"
                                        "the theoretical concept clear but also do the practical implementation of the concepts. Thanks")


# Working with methods in Class Hall_of_Fame

logging.info("Working with Method student_hof_deatils")

hf1.student_hof_deatils()
hf2.student_hof_deatils()
hf3.student_hof_deatils()
