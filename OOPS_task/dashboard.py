import logging
logging.basicConfig(filename="dashboard.log", level= logging.INFO, format='%(levelname)s %(asctime)s %(message)s')

logging.info("Creating a dashboard for displaying all Class info on single page")

logging.info("Displaying Students and Mentors details by importing required packages, modules and classes")

# Displaying FSDS students and mentors details
print("FSDS Students and Mentors\n")
from students.DS_students import fsds1
from students.DS_students import fsds2
from mentors.datasci_mentors import dsm1
from mentors.datasci_mentors import dsm2
from mentors.datasci_mentors import dsm3
from mentors.datasci_mentors import dsm4
from mentors.datasci_mentors import dsm5

print(fsds1.course_student())
print(fsds1.Total_fee_student())
print(fsds2.course_student())
print(fsds2.Total_fee_student())

print(dsm1.course_mentor())
print(dsm1._Basic_code__total_salary())
print(dsm2.course_mentor())
print(dsm2._Basic_code__total_salary())
print(dsm3.course_mentor())
print(dsm3._Basic_code__total_salary())
print(dsm4.course_mentor())
print(dsm4._Basic_code__total_salary())
print(dsm5.course_mentor())
print(dsm5._Basic_code__total_salary())


# Displaying FSJSB students and mentors details
print("\nFSJSB Students and Mentors\n")

from students.Otherstudents import fsjb1
from students.Otherstudents import fsjb2
from mentors.java_mentors import jm1
from mentors.java_mentors import jm2

print(fsjb1.course_student())
print(fsjb1.Total_fee_student())
print(fsjb2.course_student())
print(fsjb2.Total_fee_student())

print(jm1.course_mentor())
print(jm1._Basic_code__total_salary())
print(jm2.course_mentor())
print(jm2._Basic_code__total_salary())

# Displaying Development students and mentors details
print("\nDevelopment Students and Mentors\n")

from students.Otherstudents import dev1
from students.Otherstudents import dev2
from students.Otherstudents import dev3
from mentors.dev_mentors import dm1
from mentors.dev_mentors import dm2


print(dev1.course_student())
print(dev1.Total_fee_student())
print(dev2.course_student())
print(dev2.Total_fee_student())
print(dev3.course_student())
print(dev3.Total_fee_student())

print(dm1.course_mentor())
print(dm1._Basic_code__total_salary())
print(dm2.course_mentor())
print(dm2._Basic_code__total_salary())


# Displaying Cloud students and mentors details
print("\nCloud Students and Mentors\n")

from students.Otherstudents import cloud1
from mentors.cloud_mentors import cm1


print(cloud1.course_student())
print(cloud1.Total_fee_student())

print(cm1.course_mentor())
print(cm1._Basic_code__total_salary())

# Displaying Marketing students and mentors details
print("\nMarketing Students and Mentors\n")

from students.Otherstudents import m1
from students.Otherstudents import m2
from mentors.marketing_mentors import mm1

print(m1.course_student())
print(m1.Total_fee_student())
print(m2.course_student())
print(m2.Total_fee_student())

print(mm1.course_mentor())
print(mm1._Basic_code__total_salary())


# Displaying Ineuron Vision Product Details
print("\nIneuron Vision Product Details\n")

from Ineuron_vision.products import ad1
from Ineuron_vision.products import ad2
from Ineuron_vision.products import ad3
from Ineuron_vision.products import ad4
from Ineuron_vision.products import ad5
from Ineuron_vision.products import ad6
from Ineuron_vision.products import ad7
from Ineuron_vision.products import ad8
from Ineuron_vision.products import ad9
from Ineuron_vision.products import ad10

print(ad1.display_project_details())
print(ad2.display_project_details())
print(ad3.display_project_details())
print(ad4.display_project_details())
print(ad5.display_project_details())
print(ad6.display_project_details())
print(ad7.display_project_details())
print(ad8.display_project_details())
print(ad9.display_project_details())
print(ad10.display_project_details())

# Displaying Hall of Fame Students Details
print("\nHall of Fame Students Details\n")

from hall_of_Fame import hf1
from hall_of_Fame import hf2
from hall_of_Fame import hf3

print(hf1.student_hof_deatils())
print(hf2.student_hof_deatils())
print(hf3.student_hof_deatils())

# Displaying Internship Students Details
print("\nInternship Students Details\n")

from internship import in1
from internship import in2
from internship import in3

# Importing Objects from module 'DS_students' and 'Otherstudents' Package 'students'
from students.DS_students import fsds1
from students.DS_students import fsds2
from students.Otherstudents import fsjb2

# Importing Objects from module 'Datasci_mentors' and 'Java_mentors' from Package 'mentors'
from mentors.datasci_mentors import dsm1
from mentors.datasci_mentors import dsm2
from mentors.java_mentors import jm1

logging.info("Student Internship Project Details and student details")
print("Student Internship Project Details and student details\n")
print(in1.project_status_details())
print(fsds1.course_student())
logging.info("Mentor for above student is: ")
print("Mentor for above student is: ")
print(dsm1.course_mentor(),"\n")

logging.info("Student Internship Project Details and student details")
print("Student Internship Project Details and student details\n")
print(in2.project_status_details())
print(fsds2.course_student())
logging.info("Mentor for above student is: ")
print("mentor for above student is: ")
print(dsm2.course_mentor(),"\n")

logging.info("Student Internship Project Details and student details")
print("Student Internship Project Details and student details\n")
print(in3.project_status_details())
print(fsjb2.course_student())
logging.info("Mentor for above student is: ")
print("Mentor for above student is: ")
print(jm1.course_mentor())


# Displaying Blog Page Details
print("\nBlog Page Details\n")

from blogs import b1
from blogs import b2
from blogs import b3

from students.DS_students import fsds2
from students.Otherstudents import m1
from students.Otherstudents import cloud1

logging.info("Pure Bloggers are as below: ")
print("Pure Bloggers are as below: \n")
print(b1.blogger_details())
print(b2.blogger_details())
print(b3.blogger_details())


logging.info("Blogger and student details of students who are writing blogs in iNeuron is as below: ")
from blogs import fsds2b
from blogs import m1b
from blogs import cloud1b
print("\nBlogger and student details of students who are writing blogs in iNeuron is as below: \n")
print(fsds2b.blogger_details())
print(fsds2.course_student())
print(m1b.blogger_details())
print(m1.course_student())
print(cloud1b.blogger_details())
print(cloud1.course_student())


# Displaying Affiliates Details
print("\nAffiliates Details\n")

from affiliates import af1
from affiliates import af2
from affiliates import af3

logging.info("Details and salary of affiliates in Ineuron is as below: ")

print("Details and salary of affiliates in Ineuron is as below: \n")
print(af1.affiliate_details())
print(af1.salary_affiliate(10))
print(af2.affiliate_details())
print(af2.salary_affiliate(11))
print(af3.affiliate_details())
print(af3.salary_affiliate(19))

#Students working as Affiliates
logging.info("importing objects from module 'DS_students' and 'Other_students' from package 'students'")

from students.DS_students import fsds2
from students.Otherstudents import m1
from students.Otherstudents import cloud1


from affiliates import fsds2a
from affiliates import m1a
from affiliates import cloud1a

logging.info("affiliate and salary details of students who are affiliate is as below: ")

print("\naffiliate, student and salary details of students who are affiliate is as below: \n")
print(fsds2a.affiliate_details())
print(fsds2.course_student())
print(fsds2a.salary_affiliate(12))
print(m1a.affiliate_details())
print(m1.course_student())
print(m1a.salary_affiliate(17))
print(cloud1a.affiliate_details())
print(cloud1.course_student())
print(cloud1a.salary_affiliate(15))








