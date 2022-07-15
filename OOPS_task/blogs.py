import logging
logging.basicConfig(filename="blogs.log", level= logging.INFO, format='%(levelname)s %(asctime)s %(name)s %(message)s ')

logging.info("Creating Blogs Class")

class Blogs:

    logging.info("Creating Constructor in class Blogs")
    try:
        def __init__(self, name, contact_details, previous_association):
            self.name = name
            self.contact_details = contact_details
            self.previous_association = previous_association
    except Exception as e:
        logging.exception("error is: ",e)

    logging.info("Creating Methods in Class Blogs")
    try:
        def blogger_details(self):
            logging.info("\nBlogger Name: %s, Contact_details: %s,\nPrevious_Association: %s\n", self.name,
                                                self.contact_details, self.previous_association)
            return "\nBlogger Name: {}, Contact_details: {},\nPrevious_Association: {}\n".format(self.name,
                                                self.contact_details, self.previous_association)
    except Exception as e:
        logging.exception("Error occurred is: ",e)

logging.info("Creating objects in class Blogs")

b1 = Blogs("Jeevan",998877665544, "No")
b2 = Blogs("Sanjeevan", 8877665523, "No")
b3 = Blogs("Samarkumar", 8976564323, "No")

#working with class Blogs Methods

logging.info("Details of Blogger is as below: ")

b1.blogger_details()
b2.blogger_details()
b3.blogger_details()


# Students who are writing blogs
logging.info("importing objects from module 'DS_students' and 'Other_students' from package 'students'")

from students.DS_students import fsds2
from students.Otherstudents import m1
from students.Otherstudents import cloud1

logging.info("Details of students who are writing blogs in Ineuron is as below: ")

fsds2.course_student()
m1.course_student()
cloud1.course_student()

logging.info("Creating Blogs class objects for students who are writing blogs in Ineuron")

fsds2b = Blogs("Sameer",123414,"Student in iNeuron")
m1b = Blogs("Samiksha",121356,"Student in iNeuron")
cloud1b = Blogs("Sheetal",123478,"Student in iNeuron")

logging.info("Blogger details of students who are writing blogs in iNeuron is as below: ")


fsds2b.blogger_details()
m1b.blogger_details()
cloud1b.blogger_details()