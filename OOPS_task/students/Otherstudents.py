import logging
logging.basicConfig(filename="Otherstudents.log", level= logging.INFO, format='%(levelname)s %(asctime)s %(name)s %(message)s')

logging.info("importing class Basiccode_students from Module basic_code_students and package students")

from students.basic_code_students import Basiccode_students

logging.info("Importing objects from module 'java_mentors' and package 'mentors'")

from mentors.java_mentors import jm1
from mentors.java_mentors import jm2

logging.info("Importing objects from module 'dev_mentors' and package 'mentors'")

from mentors.dev_mentors import dm1
from mentors.dev_mentors import dm2

logging.info("Importing objects from module 'cloud_mentors' and package 'mentors'")

from mentors.cloud_mentors import cm1

logging.info("Importing objects from module 'marketing_mentors' and package 'mentors'")

from mentors.marketing_mentors import mm1

logging.info("Inheriting class Basiccode_students in class Other_students")

class Other_students(Basiccode_students) :
    try:
        def Class_timings(self):  # Example of method Overriding
            logging.info("Class timings for all other class is MONDAY and THURSDAY 3 PM to 6 PM")
            return "Class timings for all other class is MONDAY and THURSDAY 3 PM to 6 PM"
    except Exception as e:
        logging.exception("this error occured: ", e)

logging.info("Creating objects for FSJSB students in Other_students class")

fsjb1 = Other_students("sankalp", "Fullstack Javascript Bootcamp",1 ,3000, "B.E.(Electrical)")
fsjb2 = Other_students("shantanu", "Fullstack Javascript Bootcamp, FSDS",2 ,6000, "B.E.(CSE)")

logging.info("Creating objects for Development students in Other_students class")

dev1 = Other_students("shilpa", "Blockchain_community, Cyber_sec_masters",2, 2500, "M.Tech (CSE)")
dev2 = Other_students("Shannon", " Cyber_sec_masters",1, 2500, "B.Tech (Mining)")
dev3 = Other_students("samaira", "Blockchain_community,FSDA, Cyber_sec_masters",3, 4000, "M.Tech (BIOTech)")

logging.info("Creating objects for cloud students in Other_students class")

cloud1 = Other_students("Sheetal", "AWS_Cloud_masters",1, 4000, "M.Tech (Nano_science)")

logging.info("Creating objects for Marketing students in Other_students class")

m1 = Other_students("Samiksha", "YT_master, Digital_marketing_bootcamp",2, 1000, "B.Sc (Maths)")
m2 = Other_students("Sneha", "YT_master, Digital_marketing_bootcamp",2, 1000, "M.A. (English_Literature)")



logging.info("Class Timings for all classes are mentioned Below")

logging.info(m1.Class_timings())

# working with FSJSB students
logging.info("Details and Fees of Fullstack JavaScript Bootcamp students")

fsjb1.course_student()
fsjb1.Total_fee_student()
fsjb2.course_student()
fsjb2.Total_fee_student()

logging.info("Mentor details for FSJSB courses is as below:")

jm1.course_mentor()
jm2.course_mentor()

# working with Development students
logging.info("Details and Fees of Development students")

dev1.course_student()
dev1.Total_fee_student()
dev2.course_student()
dev2.Total_fee_student()
dev3.course_student()
dev3.Total_fee_student()

logging.info("Mentor details for Development courses is as below:")

dm1.course_mentor()
dm2.course_mentor()

# working with cloud students
logging.info("Details and Fees of cloud students")

cloud1.course_student()

cloud1.Total_fee_student()

logging.info("Mentor details for Cloud courses is as below:")

cm1.course_mentor()

# working with Marketing students
logging.info("Details and Fees of Marketing students")

m1.course_student()
m1.Total_fee_student()
m2.course_student()
m2.Total_fee_student()

logging.info("Mentor details for Marketing courses is as below:")

mm1.course_mentor()
