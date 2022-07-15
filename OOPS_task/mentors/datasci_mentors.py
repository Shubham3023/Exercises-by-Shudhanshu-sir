import logging

logging.basicConfig(filename="datasci_mentors.log", level=logging.INFO, format='%(levelname)s %(asctime)s %(name)s %(message)s')

logging.info("importing class Basic_code from Module basic_code and package mentors")
from mentors.basic_code import Basic_code

logging.info("Inheriting class Basic_code in class DS_mentor")
class DS_mentor(Basic_code) :
    pass


logging.info("Creating objects for mentors in DS_mentors class")

dsm1 = DS_mentor("Sudhanshu Kumar", 4000, "FSDS, MLDL, DLCVNLP, BIGDBOOT", 30)
dsm2 = DS_mentor("Krish Naik", 3000, "FSDS, MLDL, DLCVNLP", 30)
dsm3 = DS_mentor("Sunny Chandra", 2000, "FSDS, AIOPS", 30)
dsm4 = DS_mentor("Shashank Mishra", 1000, "BIGDBOOT", 30)
dsm5 = DS_mentor("Saurav Agarwal", 1000, "BIGDATA_MASTER", 30)

# working with methods from class Basic_code

logging.info("details and salary of Data science Mentors is as below: ")

dsm1.course_mentor()
dsm1._Basic_code__total_salary()
dsm2.course_mentor()
dsm2._Basic_code__total_salary()
dsm3.course_mentor()
dsm3._Basic_code__total_salary()
dsm4.course_mentor()
dsm4._Basic_code__total_salary()
dsm5.course_mentor()
dsm5._Basic_code__total_salary()












