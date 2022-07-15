import logging

logging.basicConfig(filename="cloud_mentors.log", level=logging.INFO, format='%(levelname)s %(asctime)s %(name)s %(message)s')

logging.info("importing class Basic_code from Module basic_code and package mentors")
from mentors.basic_code import Basic_code

logging.info("Inheriting class Basic_code in class cloud_mentor")

class Cloud_mentors(Basic_code):
    pass


logging.info("Creating objects for mentors in Cloud_mentors class")

cm1 = Cloud_mentors("Sachin Agarwal", 1000, "AWS Cloud Masters",30)

cm1.course_mentor()

cm1._Basic_code__total_salary()

