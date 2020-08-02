class crypttask:
    def __init__(self, key):
        """
        __init__ --> Initilizes the key for the encryption and decryption
        """
        self.__key = key


    def getkey(self):
        return self.__key
    
    def encrypt(self,data):
        """
        encrypt --> this method encrypts the incoming data

        param: data -- the data to be encrypted

        return: encryptedmessage
        type: String
        """
        encryptedmessage = ""
        for char in data:
            encryptedchar = (ord(char) - ord("A")) + self.__key
            encryptedchar %= 26
            encryptedchar = chr(encryptedchar + ord("A"))
            encryptedmessage += encryptedchar
        return encryptedmessage