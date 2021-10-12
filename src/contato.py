import json

class Contato:

    def __init__(self, id, nome, email):
        self.__id = id
        self.__nome = nome
        self.__email = email

    def __repr__(self):
        return f"Contato(id={self.id}, nome='{self.nome}', email='{self.email}')"

    def __str__(self):
        return f"{self.id} - {self.nome} - {self.email}"

    def __eq__(self, other):
        return self.id == other.id and self.nome == other.nome and self.email == other.email

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
    
    @property
    def sobrenome(self):
        return self.__sobrenome
    
    @sobrenome.setter
    def sobrenome(self, value):
        self.__sobrenome = value
    
    @sobrenome.deleter
    def sobrenome(self):
        del self.__sobrenome
