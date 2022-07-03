#initiating logging

import logging

logging.basicConfig(filename="list1.log", level= logging.DEBUG, format= '%(levelname)s %(asctime)s %(name)s  %(message)s ')

#initiating exception handeling


logging.info("This is my list class")

#defining class

class List1 :

    #creating class methods

    #1 . Try to reverse a list
    def rev_list(self,list1):
        """
        This func reverses the list.
        :param list1:
        :return: reversed list
         """
        try:

            logging.info("Reversed list  is %s: ", list1[::-1])
            return list1[::-1]
        except Exception as e:
            logging.exception(e)


    #2. try to access 234 out of this list
    def ret_list_234(self,list1):
        """
        This func returns 234 from list.
        :param list1:
        :return: returns 234
        """
        try:
            logging.info("required output  is %s and %s: ", list1[7][0] , list(list1[8].keys())[1] )
            return list1[7][0], list(list1[8].keys())[1]
        except Exception as e:
            logging.exception(e)



    #3 . try to access 456
    def ret_list_456(self,list1):
        """
        This func returns 456 from list.
        :param list1:
        :return: returns 456
        """
        try:

            logging.info("required output  is %s : ", list1[5][1]  )
            return list1[5][1]
        except:
            logging.exception(e)


    # 4 . Try to extract only a list collection form list l
    def ret_list_ele(self,list1):
        """
        This func returns list elements from list.
        :param list1:
        :return: returns list elements
        """
        try:

            logging.info("required output  is %s and %s : ", list1[5] ,list1[6]  )
            return list1[5] ,list1[6]
        except Exception as e:
            logging.exception(e)

    #5. Try to extract "sudh"
    def ret_list_sudh(self,list1):
        """
        This func returns sudh from list.
        :param list1:
        :return: returns sudh
        """
        try:

            logging.info("required output  is %s  : ", list1[8]["key1"] )
            return list1[8]["key1"]
        except Exception as e:
            logging.exception(e)

    #6. Try to list all the key in dict element avaible in list
    def ret_keys_values(self,list1):
        """
        This func returns keys from dict in list.
        :param list1:
        :return: returns keys from dict
        """
        try:

            logging.info("required output  is %s and %s : ", list(list1[8].keys()),list(list1[8].values())  )
            return list(list1[8].keys()) , list(list1[8].values())
        except Exception as e:
            logging.exception(e)

    #l = [[1,2,3,4] , (2,3,4,5,6) , (3,4,5,6,7) , set([23,4,5,45,4,4,5,45,45,4,5]) ,
    # {'k1' :"sudh" , "k2" : "ineuron","k3":"kumar" , 3:6 , 7:8} , ["ineuron" , "data science "]]


    # 7. Try to extract all the list entity
    def ext_list(self,l):
        """
        This func extracts list entity from list.
        :param l:
        :return: list entity
        """
        try:
            l1 = []
            for i in l:
                if type(i) == list:
                    l1.append(i)
            logging.info("List entities are: %s", l1)
            return l1
        except Exception as e:
            logging.exception(e)

    #8 Try to extract all the dict entities
    def ext_dict(self,l):
        """
        This func extracts dict entity from list.
        :param l:
        :return: dict entity
        """
        try:
            l1 = []
            for i in l:
                if type(i) == dict:
                    l1.append(i)
            logging.info("dict entities are: %s", l1)
            return l1
        except Exception as e:
            logging.exception(e)

    #9. Try to extract all the tuples entities
    def ext_tuples(self,l):
        """
        This func extracts tuple entity from list.
        :param l:
        :return: tuple entity
        """
        try:

            l1 = []
            for i in l:
                if type(i) == tuple:
                    l1.append(i)
            logging.info("tuple entities are: %s", l1)
            return l1
        except Exception as e:
            logging.exception(e)

    #10. Try to extract all the numerical data it may b a part of dict key and values
    def numeric_list(self,l):
        """
        Thsi func returns all numeric data
        :param l:
        :return:Numeric data
        """
        try:
            l1 = []
            for i in l:
                if type(i) == list or type(i) == tuple or type(i) == set:
                    for j in i:
                        if type(j) == int:
                            logging.info("numeric data from list, tuple and set is %s",j)
                            l1.append(j)

                if type(i) == dict:
                    for j in i:
                        if type(j) == int or type(i[j]) == int:
                            logging.info("numeric data from dict is %s and %s", j, i[j])
                            l1.append(j)
                            l1.append(i[j])
            logging.info("total numeric data is %s", l1)
            return l1

        except Exception as e:
            logging.exception(e)

    #11. Get summation, multiplication and filter even number from numeric data
    def sum_prod_even_list(self):
        """
        This func returns summation, multiplication and even numbers in list
        :return: summation, multiplication and even numbers in list
        """
        try:
            l1 = [1, 2, 3, 4, 2, 3, 4, 5, 6, 3, 4, 5, 6, 7, 45, 4, 5, 23, 3, 6, 7, 8]
            leven = []
            sum = 0
            prod = 1
            for i in l1:
                sum += i
                prod *= i
                if i % 2 == 0:
                    leven.append(i)

            logging.info("Summation, multiplication and even number list is %s, %s and %s", sum, prod, leven)
            return sum, prod, leven

        except Exception as e:
            logging.exception(e)

    #12. Try to find out a number of occurances of all the data
    def Occurance_list(self,l):
        """
        This func returns occurance of each element in list
        :param l:
        :return: occurance of each element
        """
        try:
            l3 = []
            for i in l:
                if type(i) == list or type(i) == tuple or type(i) == set:
                    for j in i:
                        l3.append(j)
            for i in l:
                if type(i) == dict:
                    for j in i:
                        l3.append(j)
                        l3.append(i[j])

            for i in set(l3):
                logging.info("count of %s in list is %s",i , l3.count(i))
                print("count of {} in list  is {} ".format(i,l3.count(i)))

        except Exception as e:
            logging.exception(e)

    #13. Try to find out number of keys in dict element
    def Key_list(self,l):
        """
        This func returns key of dict in list
        :param l:
        :return: key of dict in list
        """
        try:
            l4 = []
            for i in l:
                if type(i) == dict:
                    for j in i:
                        l4.append(j)
            logging.info("Keys in dict of list is: %s and no of keys is:  %s", l4, len(l4))
            return "Keys in list is: {} and no of keys are {} ".format( l4, len(l4))
        except Exception as e:
            logging.exception(e)

    #14 Try to filter out all the string data using flat list in previous question

    def String_list(self):
        """
        This func returns string data from list
        :return: string data
        """

        try:
            l = [1, 2, 3, 4, 2, 3, 4, 5, 6, 3, 4, 5, 6, 7, 45, 4, 5, 23, 'ineuron', 'data science ', 'k1', 'sudh',
                 'k2', 'ineuron', 'k3', 'kumar', 3, 6, 7, 8]
            l1 = []
            for i in l:
                if type(i) == str:
                    l1.append(i)

            logging.info("String element in list is %s",l1)
            return "String element in list is: {}".format(l1)

        except Exception as e:
            logging.exception(e)





# creating object in class List1

list_l = List1()

# working with class methods

try:

    print(list_l.rev_list([3,4,5,6,7 , [23,456,67,8,78,78] , [345,56,87,8,98,9] , (234,6657,6) , {"key1" :"sudh" , 234:[23,45,656]}]))

    print(list_l.ret_list_234([3, 4, 5, 6, 7, [23, 456, 67, 8, 78, 78], [345, 56, 87, 8, 98, 9], (234, 6657, 6),{"key1": "sudh", 234: [23, 45, 656]}]))

    print(list_l.ret_list_456([3, 4, 5, 6, 7, [23, 456, 67, 8, 78, 78], [345, 56, 87, 8, 98, 9], (234, 6657, 6),{"key1": "sudh", 234: [23, 45, 656]}]))

    print(list_l.ret_list_ele([3, 4, 5, 6, 7, [23, 456, 67, 8, 78, 78], [345, 56, 87, 8, 98, 9], (234, 6657, 6),{"key1": "sudh", 234: [23, 45, 656]}]))

    print(list_l.ret_list_sudh([3, 4, 5, 6, 7, [23, 456, 67, 8, 78, 78], [345, 56, 87, 8, 98, 9], (234, 6657, 6),{"key1": "sudh", 234: [23, 45, 656]}]))

    print(list_l.ret_keys_values([3, 4, 5, 6, 7, [23, 456, 67, 8, 78, 78], [345, 56, 87, 8, 98, 9], (234, 6657, 6),{"key1": "sudh", 234: [23, 45, 656]}]))

    print(list_l.ext_list([[1,2,3,4] , (2,3,4,5,6) , (3,4,5,6,7) , set([23,4,5,45,4,4,5,45,45,4,5]) ,
                            {'k1' :"sudh" , "k2" : "ineuron","k3":"kumar" , 3:6 , 7:8} , ["ineuron" , "data science "]]))

    print(list_l.ext_dict([[1, 2, 3, 4], (2, 3, 4, 5, 6), (3, 4, 5, 6, 7), set([23, 4, 5, 45, 4, 4, 5, 45, 45, 4, 5]),
                           {'k1': "sudh", "k2": "ineuron", "k3": "kumar", 3: 6, 7: 8}, ["ineuron", "data science "]]))

    print(list_l.ext_tuples([[1, 2, 3, 4], (2, 3, 4, 5, 6), (3, 4, 5, 6, 7), set([23, 4, 5, 45, 4, 4, 5, 45, 45, 4, 5]),
                           {'k1': "sudh", "k2": "ineuron", "k3": "kumar", 3: 6, 7: 8}, ["ineuron", "data science "]]))

    print(list_l.numeric_list([[1, 2, 3, 4], (2, 3, 4, 5, 6), (3, 4, 5, 6, 7), set([23, 4, 5, 45, 4, 4, 5, 45, 45, 4, 5]),
                             {'k1': "sudh", "k2": "ineuron", "k3": "kumar", 3: 6, 7: 8}, ["ineuron", "data science "]]))

    print(list_l.sum_prod_even_list())

    list_l.Occurance_list([[1, 2, 3, 4], (2, 3, 4, 5, 6), (3, 4, 5, 6, 7), set([23, 4, 5, 45, 4, 4, 5, 45, 45, 4, 5]),
                             {'k1': "sudh", "k2": "ineuron", "k3": "kumar", 3: 6, 7: 8}, ["ineuron", "data science "]])

    print(list_l.Key_list([[1, 2, 3, 4], (2, 3, 4, 5, 6), (3, 4, 5, 6, 7), set([23, 4, 5, 45, 4, 4, 5, 45, 45, 4, 5]),
                             {'k1': "sudh", "k2": "ineuron", "k3": "kumar", 3: 6, 7: 8}, ["ineuron", "data science "]]))

    print(list_l.String_list())




except Exception as e:
    logging.exception(e)

