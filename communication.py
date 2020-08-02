from kingdom import kingdom
from crypttask import crypttask
class communication:
    def __init__(self, message,kingdom ):
        """
        __init__ --> Initilizes the message to be sent and the recipient kingdom object

        param message: message to be sent
        type: String

        param kingdom: kingdom object of the recipient
        type: kingdom
        """
        self.__message = message
        self.__kingdom = kingdom
    
    def is_valid_message(self):
        """
        is_valid_message --> this methods checks the message and returns whether its valid or not

        return: True or False as per the message validation
        type: boolean
        """
        key = len(self.__kingdom.get_emblem())
        cryptobject = crypttask(key)
        encryptedemblem = cryptobject.encrypt(self.__kingdom.get_emblem())

        frequency = {}
        for char in encryptedemblem:
            if char in frequency:
                frequency[char] += 1
            else:
                frequency[char] = 1
        
        count = len(encryptedemblem)
        index = 0

        while count != 0 and index < len(self.__message):
            if self.__message[index] in frequency and frequency[self.__message[index]] > 0:
                count -= 1
                frequency[self.__message[index]] -= 1
            index += 1
        
        if count == 0:
            return True
        else:
            return False

    def getname(self):
        """
        get_name --> this functions return the name of the kingdom. It calls the get_name function of kingdom class

        return: __name
        type: String
        """
        return self.__kingdom.get_name()

