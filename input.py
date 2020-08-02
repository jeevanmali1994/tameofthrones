import sys


class input:
    def __init__(self):
        """
        __init__ --> Initializes the path variable
        """
        self.__filepath = sys.argv[1]

    def read_input(self):
        """
        read_input --> this function reads the file with all the messages and reciepient and
        creates a list of it

        return: message_list 
        It contains all the messages and the reciepient
        type: list
        """
        file = open(self.__filepath,'r')
        message_list = []
        for line in file:
            array = line.split()
            kingdom = array[0]
            message = "".join(array[1:])
            message_list.append([kingdom, message])
        return message_list    
