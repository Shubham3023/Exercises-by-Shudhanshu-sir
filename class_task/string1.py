#initiating logging

import logging

logging.basicConfig(filename="string1.log", level= logging.DEBUG, format= '%(levelname)s %(asctime)s %(name)s  %(message)s ')

logging.info("i have started logging my codes")



    #defining class

class String1 :

    logging.info("we are inside class String1")
    logging.info("""we are creating methods inside class strings and 
    implementing exception handling along with logging. """)

    #creating class methods

    #1 . Try to extract data from index one to index 300 with a jump of 3
    def ind_jump_3(self, string1):
        """
        This function returns string with jump of 3.
        :param string:
        :return: string with jump 3
        """
        # initiating exception handling
        try:
            logging.info("String with jump 3 is %s: ", string1[1:300:3])
            return string1[::3]
        except Exception as e:
            logging.exception(e)

    #2. Try to reverse a string without using reverse function
    def rev_str(self, string1):
        """
        This func reverses the string.
        :param string:
        :return: reversed string
        """
        try:
            logging.info("Reversed String  is %s: ", string1[::-1])
            return string1[::-1]
        except Exception as e:
            logging.exception(e)

    #3. Try to split a string after conversion of entire string in uppercase

    def S_upper(self,string1):
        """
        This func converts string to uppercase.
        :param string1:
        :return: upper-cased string
        """
        try:
            p = string1.upper()
            logging.info("Splitted uppercased string is  %s: ", p.split())
            return p.split()
        except Exception as e:
            logging.exception(e)

    #4. try to convert the whole string into lower case
    def S_lower(self,string1):
        """
        This func converts string to lowercase.
        :param string1:
        :return: lowercased string
        """
        try:
            logging.info("Lowercased string is  %s: ", string1.lower())
            return string1.lower()
        except Exception as e:
            logging.exception(e)


    #5 Try to give an example of expand tab
    def exp_tabs(self,string1):
        """
        This func returns expandtabs of string.
        :param string1:
        :return: string with expandtabs
        """
        try:
            logging.info("Expandtabs string is  %s: ", string1.expandtabs())
            return string1.expandtabs()
        except Exception as e:
            logging.exception(e)

    #6 : Try to filter out all the vowels form below text in string s by using while loop :
    def return_vowels(self,string1):
        """
        This func returns vowels from string.
        :param string1:
        :return: returns vowels from string.
        """
        try:
            string1.lower()
            l = string1.split(" ")
            l1 = []
            k = 0

            while k < len(l):
                if type(l[k]) == str:
                    p = 0
                    while p < len(l[k]):
                        if l[k][p] in ["a", "e","i","o", "u"]:
                            l1.append(l[k][p])
                        p += 1
                k += 1

            logging.info("Expandtabs string is  %s: ", l1)
            return l1
        except Exception as e:
            logging.exception(e)

    #7 . Give an example of strip , lstrip and rstrip
    def lr_strip(self,string1):
        """
        This func returns strip, left and right strip of string.
        :param string1:
        :return: strip, left and right strip of string
        """
        try:
            logging.info("strip, left and right strip of string is  %s, %s and %s: ", string1.strip(),string1.lstrip(), string1.rstrip() )
            return string1.strip(),string1.lstrip(), string1.rstrip()
        except Exception as e:
            logging.exception(e)

    #8 Replace a string charecter by another charector by taking your own example "shubham "
    def rep_char(self,string1):
        """
        This func replaces a character in a string.
        :param string1:
        :return: replace character
        """
        try:
            logging.info("New string is is  %s: ", string1.replace(" ", "Verma") )
            return string1.replace(" ", " Verma")
        except Exception as e:
            logging.exception(e)



#creating object in class string1
str_s = String1()


#working with class methods

try:
    print(str_s.ind_jump_3("this is My First Python programming class and i am learNING python string and its function"))
    print(str_s.rev_str("this is My First Python programming class and i am learNING python string and its function"))
    print(str_s.S_upper("this is My First Python programming class and i am learNING python string and its function"))
    print(str_s.S_lower("THIS IS MY FIRST PYTHON PROGRAMMING CLASS AND I AM LEARNING PYTHON STRING AND ITS FUNCTION"))
    print(str_s.exp_tabs("My\tname\tis\tShubham\tVerma\tand\tI\twant\tto\tbecome\ta\tdata\tscientist"))

    print(str_s.return_vowels("Python is a high-level, interpreted, general-purpose programming language."))

    print(str_s.lr_strip("    ShubhaM     "))
    print(str_s.rep_char("ShubhaM "))


except Exception as e:
    logging.exception(e)
