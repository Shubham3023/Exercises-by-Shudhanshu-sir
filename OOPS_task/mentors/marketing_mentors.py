import logging

logging.basicConfig(filename="marketing_mentors.log", level=logging.INFO, format='%(levelname)s %(asctime)s %(name)s %(message)s')

logging.info("importing class Basic_code from Module basic_code and package mentors")
from mentors.basic_code import Basic_code

logging.info("Inheriting class Basic_code in class Marketing_mentor")

class Marketing_mentors(Basic_code):
    pass


logging.info("Creating objects for mentors in Cloud_mentors class")

mm1 = Marketing_mentors("Amresh Bharti", 2000, "Youtube Mastery, Digital_Marketing_Bootcamp", 30)

# working with methods imported from class Basic_code

logging.info("Details and salary of Marketing Mentors is as below: ")

mm1.course_mentor()
mm1._Basic_code__total_salary()

