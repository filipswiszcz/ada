import enum

class Authorization():

    def __init__(self, ada):
        self.__parent = ada
        self.__connected_entities = {}
        self.__encryption_level = 0

    def get_connected_entities(self):
        return self.connected_entities