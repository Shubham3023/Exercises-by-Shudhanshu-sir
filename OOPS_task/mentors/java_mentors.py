import logging

logging.basicConfig(filename="Java_mentors.log", level=logging.INFO, format='%(levelname)s %(asctime)s %(name)s %(message)s')

logging.info("importing class DS_mentor from Module datasci_mentors and package mentors")
from mentors.basic_code import Basic_code

logging.info("Inheriting class Basic_code in class Java_mentor")

class Java_mentor(Basic_code):
    pass

logging.info("creating objects in class java_mentors")

jm1 = Java_mentor("Hitesh Choudhary", 2000, "FSJSB, JSMARATHON", 30)
jm2 = Java_mentor("Shubham Waje", 1000, "FSJSB", 30)

# working with methods imported from class Basic_code

logging.info("Details and salary of Java Mentors is as below: ")

jm1.course_mentor()
jm1._Basic_code__total_salary()
jm2.course_mentor()
jm2._Basic_code__total_salary()
