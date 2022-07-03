#initiating logging

import logging

logging.basicConfig(filename="dict1.log", level= logging.DEBUG, format= '%(levelname)s %(asctime)s %(name)s  %(message)s ')




#defining class

class Dict1 :

    #creating class methods

    # Write a fun which will take input as a dict and give me out as a list of all the values even in case of 2
    # level nesting it should work.
    def dict_list(self,d):
        """
        This func returns list of values.
        :param dict1:
        :return: returns list of values.
        """
        try:
            l = []
            for i in d:
                if type(d[i]) == str or type(d[i]) == list or type(d[i]) == tuple or type(d[i]) == int or type(
                        d[i]) == set:
                    l.append(d[i])
            for i in d:
                p = d[i]
                if type(d[i]) == dict:
                    for j in p:
                        if type(p[j]) == dict:
                            q = p[j]
                            pass
                        else:
                            l.append(p[j])
                        if type(p[j]) == dict:
                            for k in q:
                                l.append(q[k])
            logging.info("List of values from dict is: %s", l)
            return "List of values from dict is: {}".format(l)
        except Exception as e:
            logging.exception(e)


# creating object in class List1

dict_l = Dict1()

# working with class methods
try:

    print(dict_l.dict_list({"k1": 2121 ,1:(1,2,3), 2:[4,5,6], 3: {1,2,3,4}, 45: {"k2": 723183, "k3": {34:"sherkhan",35: "manoj singh"},
                                                                             12312:"padma"}, "k5":"sanjay leela bhansali"}))

except Exception as e:
    logging.exception(e)





















