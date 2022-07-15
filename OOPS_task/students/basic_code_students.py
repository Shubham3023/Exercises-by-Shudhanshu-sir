import logging
logging.basicConfig(filename="basic_code_students.log", level= logging.INFO, format='%(levelname)s %(asctime)s %(name)s %(message)s')

logging.info("Creating class Basiccode_students")

class Basiccode_students:

    logging.info("Creating constructor in class Basiccode_students")
    try:
        def __init__(self, name, course, no_course, fees, qualif):
            self.name = name
            self.course = course
            self.no_course = no_course
            self.__fees = fees # Private Variable
            self._qualif = qualif # Protected Variable
    except Exception as e:
        logging.exception("the error is this: ",e)

    logging.info("Creating Methods in class Basiccode_students")

    try:
        def course_student(self):
            logging.info("\nStudent: %s,\nCourse opted: %s,\nNo of Course: %s,\nCourse_fee per Course: %s,\nQualification: %s\n",self.name,
                         self.course, self.no_course, self.__fees, self._qualif)
            return "\nStudent: {},\nCourse opted: {},\nNo of Course: {},\nCourse_fee per Course: {},\nQualification: {}\n".format(self.name,
                   self.course, self.no_course, self.__fees, self._qualif)

    except Exception as e:
        logging.exception("the error is this: ", e)

    try:

        def Total_fee_student(self):
            logging.info("\nTotal Fees paid by %s is: Rs. %s",self.name, self.no_course * self.__fees)
            return "\nTotal Fees paid by {} is: Rs. {}".format(self.name,self.no_course * self.__fees)
    except Exception as e:
        logging.exception("the error is this: ", e)


    try:
        def Class_timings(self):
            logging.info("Generalised Class timings is SATURDAY and SUNDAY 3 PM to 6 PM")
            return "Generalised Class timings is SATURDAY and SUNDAY 3 PM to 6 PM"
    except Exception as e:
        logging.exception("the error is this: ",e)


