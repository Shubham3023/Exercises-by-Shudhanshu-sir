import logging

logging.basicConfig(filename="dev_mentors.log", level=logging.INFO, format='%(levelname)s %(asctime)s %(name)s %(message)s')

logging.info("importing class Basic_code from Module basic_code and package mentors")
from mentors.basic_code import Basic_code

logging.info("Inheriting class Basic_code in class Dev_mentor")
class Dev_mentors(Basic_code):
    pass


logging.info("Creating objects for mentors in Dev_mentors class")

dm1 = Dev_mentors("Sanjeevan Thorat", 1000, "Blockchain_community", 30)
dm2 = Dev_mentors("Saksham Choudhary", 2000, "CyberSec_community, Cybersec_Masters", 30)

# working with methods imported from class Basic_code

logging.info("details and salary of Development Mentors is as below: ")

dm1.course_mentor()
dm1._Basic_code__total_salary()
dm2.course_mentor()
dm2._Basic_code__total_salary()







