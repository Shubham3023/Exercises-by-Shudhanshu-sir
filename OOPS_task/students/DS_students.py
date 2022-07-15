import logging

logging.basicConfig(filename="DS_students.log", level=logging.INFO, format='%(levelname)s %(asctime)s %(name)s %(message)s')

logging.info("importing class 'Basiccode_students' from Module 'basic_code_students' and package 'students'")

from students.basic_code_students import Basiccode_students

logging.info("Importing objects from module 'datasci_mentors' and package 'mentors'")

from mentors.datasci_mentors import dsm1
from mentors.datasci_mentors import dsm2
from mentors.datasci_mentors import dsm3
from mentors.datasci_mentors import dsm4
from mentors.datasci_mentors import dsm5

logging.info("Inheriting class 'Basiccode_students' in class 'FSDS_students' ")

class FSDS_students(Basiccode_students):

    try:

        def Class_timings(self):   #Example of method Overriding
            logging.info("Class timings for FSDS class is SATURDAY and SUNDAY 3 PM to 6 PM")
            return "Class timings for FSDS class is SATURDAY and SUNDAY 3 PM to 6 PM"
    except Exception as e:
        logging.exception("this error occured: ",e)

logging.info("Creating objects for FSDS students in FSDS_students class")

fsds1 = FSDS_students("Shubham", "FSDS, DSA_community", 2, 3000,"B.E (Mechanical)")
fsds2 = FSDS_students("Sameer", "FSDS", 1, 2000,"B.E (CSE)")

# working with methods from Basiccode_students class and FSDS_students class
logging.info("Below is an example of Method Overriding")

logging.info(fsds1.Class_timings())

fsds1.Class_timings()

logging.info("Students details is as below: ")

fsds1.course_student()
fsds2.course_student()

logging.info("Students fee details is as below:")

fsds1.Total_fee_student()
fsds2.Total_fee_student()

logging.info("Mentor details for DS courses is as below:")

dsm1.course_mentor()
dsm2.course_mentor()
dsm3.course_mentor()
dsm4.course_mentor()
dsm5.course_mentor()







