import logging
logging.basicConfig(filename="internship.log", level= logging.INFO, format='%(levelname)s %(asctime)s %(message)s')

logging.info("Creating Class Internship")

class Internship:

    logging.info("Creating constructor in Class Internship")
    try:
        def __init__(self, name, course, project_topic, project_status):
            self.name = name
            self.course = course
            self.project_topic = project_topic
            self.project_status = project_status
    except Exception as e:
        logging.exception("error is: ", e)


    logging.info("Creating Method in Class Internship")
    try:
        def project_status_details(self):

            logging.info("\nName: %s,Course_name: %s,\nProject_topic: %s,Project status: %s percent completed\n", self.name,
                         self.course, self.project_topic, self.project_status)
            return "\nName: {},Course_name: {},\nProject_topic: {}, Project status: {} percent completed\n".format(self.name,
                         self.course, self.project_topic, self.project_status)
    except Exception as e:
        logging.exception("error is: ", e)

# Creating objects in Class Internship

in1 = Internship("Shubham","FSDS", "YouTube Project", 30)
in2 = Internship("Sameer","FSDS", "Automobile", 35)
in3 = Internship("Shantanu","Fullstack Javascript Bootcamp", "Java Project",67)


# Importing Objects from module 'DS_students' and 'Otherstudents' Package 'students'
from students.DS_students import fsds1
from students.DS_students import fsds2
from students.Otherstudents import fsjb2



# Importing Objects from module 'Datasci_mentors' and 'Java_mentors' from Package 'mentors'
from mentors.datasci_mentors import dsm1
from mentors.datasci_mentors import dsm2
from mentors.java_mentors import jm1

# working with methods in Class Internship
logging.info("Student Internship Project Details and student details")
in1.project_status_details()
fsds1.course_student()

logging.info("Mentor for above student is: ")
dsm1.course_mentor()

logging.info("Student Internship Project Details and student details")
in2.project_status_details()
fsds2.course_student()

logging.info("Mentor for above student is: ")
dsm2.course_mentor()

logging.info("Student Internship Project Details and student details")
in3.project_status_details()
fsjb2.course_student()

logging.info("Mentor for above student is: ")
jm1.course_mentor()
