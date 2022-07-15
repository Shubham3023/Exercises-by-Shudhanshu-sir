import logging

logging.basicConfig(filename="affiliates.log", level= logging.INFO, format='%(levelname)s %(asctime)s %(name)s %(message)s ')


logging.info("creating affiliates class")

class affiliates:

    logging.info("Creating constructor in affiliates class")
    def __init__(self, name, reg_details, mobile, salary ):
        self.name = name
        self.reg_details = reg_details
        self.mobile = mobile
        self.salary = salary

    logging.info("Creating methods in affiliates class")
    try:
        def affiliate_details(self):
            logging.info("\nAffiliate Name: %s, Registration_details: %s,\nMobileNo: %s, Salary per registration: %s\n", self.name,
                                                self.reg_details, self.mobile, self.salary)
            return "\nAffiliate Name: {}, Registration_details: {},\nMobileNo: {}, Salary per registration: {}\n".format(self.name,
                                                self.reg_details, self.mobile, self.salary)
    except Exception as e:
        logging.exception("Error occurred is: ",e)

    try:
        def salary_affiliate(self,no_of_reg):
            logging.info("\nsalary of %s is: Rs. %s", self.name, no_of_reg * self.salary)
            return "\nsalary of {} is: Rs. {}".format(self.name, no_of_reg * self.salary)

    except Exception as e:
        logging.exception("Error occurred is: ",e)

# creating objects in class affiliates
logging.info("Creating objects in class affiliates")

af1 = affiliates("rajeev",123124124,9923456784,650)
af2 = affiliates("sameera",12312833123,9934578999,650)
af3 = affiliates("shipra",123324833123,9967578999,650)

# working with methods from class affiliates

logging.info("Details of affiliates in Ineuron is as below: ")


af1.affiliate_details()
af2.affiliate_details()
af3.affiliate_details()


logging.info("Salary of affiliates is as below: ")


af1.salary_affiliate(10)
af2.salary_affiliate(11)
af3.salary_affiliate(19)


logging.info("Below is the details of students working as affiliates")
#Students working as Affiliates
logging.info("importing objects from module 'DS_students' and 'Other_students' from package 'students'")

from students.DS_students import fsds2
from students.Otherstudents import m1
from students.Otherstudents import cloud1

logging.info("Details of students who are affiliates in Ineuron is as below: ")


fsds2.course_student()
m1.course_student()
cloud1.course_student()


logging.info("Creating affiliate class objects for students who are affiliates")

fsds2a = affiliates("Sameer",123414,9967456345,700)
m1a = affiliates("Samiksha",121356,8745672367,700)
cloud1a = affiliates("Sheetal",123478,9867454399,700)

logging.info("affiliate details of students who are affiliate is as below: ")


fsds2a.affiliate_details()
m1a.affiliate_details()
cloud1a.affiliate_details()


logging.info("affiliate salary of students who are affiliates in Ineuron is as below: ")


fsds2a.salary_affiliate(12)
m1a.salary_affiliate(17)
cloud1a.salary_affiliate(15)
