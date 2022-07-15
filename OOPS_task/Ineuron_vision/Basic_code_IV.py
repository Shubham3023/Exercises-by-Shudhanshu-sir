import logging

logging.basicConfig(filename="Basic_code_IV.log", level= logging.INFO, format='%(levelname)s %(asctime)s %(message)s ')

logging.info("Creating Class Basic_code_IV")

class Basic_Code_IV:

    try:
        def __init__(self, project, project_description, project_member, project_status):
            self.__project = project
            self.__project_description = project_description
            self.__project_member = project_member
            self.__project_status = project_status
    except Exception as e:
        logging.exception("The error occurred is: ",e)

    try:
        def display_project_details(self):
            logging.info("\nProject Name: %s\nProject_Description: %s\nProject Members: %s\nProject Status: %s Percent Completed\n",self.__project,
                                                                        self.__project_description, self.__project_member, self.__project_status)
            return "\nProject Name: {}\nProject_Description: {}\nProject Members: {}\nProject Status: {} Percent Completed\n".format(self.__project,
                                                                        self.__project_description,self.__project_member, self.__project_status)
    except Exception as e:
        logging.exception("The error occurred is: ",e)
