class kingdom:
    def __init__(self, name, emblem):
        """
        __init__ --> Initilizes two variables with name of kindom and its emblem
        """
        self.__name = name
        self.__emblem = emblem
    
    def get_name(self):
        """
        get_name --> this function return the name of the kingdom

        return: __name  name of the kingdom
        type: String
        """
        return self.__name
    
    def get_emblem(self):
        """
        get_emblem --> this function return the emblem of the kingdom

        return: __emblem  emblem of the kingdom
        type: String
        """
        return self.__emblem