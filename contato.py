class Contato:

    def __init__(self, id, nome, email):
        self.__id = id
        self.__nome = nome
        self.__email = email

    @property
    def id(self):
        return self.__id
    
    @id.setter
    def id(self, value):
        self.__id = value
        
    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, value):
        self.__nome = value
        
    @property
    def email(self):
        return self.__email
    
    @email.setter
    def email(self, value):
        self.__email = value