import logging

logging.basicConfig(filename="basic_code.log", level=logging.INFO, format='%(levelname)s %(asctime)s %(name)s %(message)s')

class Basic_code :

    logging.info("Creating constructor in Basic_code class")
    try:
        def __init__(self,name, salary, course, attendance):
            self.name = name
            self.__salary = salary # Private Variable
            self.course = course
            self._attendance = attendance # Protected Variable
    except Exception as e:
        logging.exception("The Error is: ",e)

    logging.info("Creating methods in Basic_code class")

    try:

        def course_mentor(self):
            logging.info("\nMentor: %s,\nSalary per day: %s,\nCurrent_Course: %s\n",self.name, self.__salary, self.course)
            return "\nMentor: {},\nSalary per day: {},\nCurrent_Course: {}\n".format(self.name, self.__salary, self.course)

    except Exception as e:
        logging.exception("The error is: ",e)

    try:
        def __total_salary(self): # Private Function
            logging.info("\nTotal salary of %s is: Rs. %s", self.name ,self._attendance * self.__salary)
            return "\nTotal salary of {} is: Rs. {}".format(self.name, self._attendance * self.__salary)

    except Exception as e:
        logging.exception("The Error is: ",e)
