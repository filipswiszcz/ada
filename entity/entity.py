from entity.entity_type import Entity_Type
from network.connection_status import Connection_Status
from security.access_type import Access_Type

class Entity():

    def __init__(self, name, entity_type, access_type):
        self.__id = 0 # take last id and generate next
        self.__name = name
        self.__type = entity_type if isinstance(entity_type, Entity_Type) else Entity_Type.UNKNOWN
        self.__connection_status = Connection_Status.ONLINE
        self.__access_type = access_type if isinstance(access_type, Access_Type) else Access_Type.EXILE

    def get_id(self):
        return self.__id
    
    def __set_id(self):
        print("#######") # parse generator
    
    def get_name(self):
        return self.__name
    
    def get_type(self):
        return self.__type
    
    def set_type(self, entity_type):
        self.__type = entity_type if isinstance(entity_type, Entity_Type) else Entity_Type.UNKNOWN

    def get_connection_status(self):
        return self.__connection_status
    
    def set_connection_status(self, connection_status):
        self.__connection_status = connection_status if isinstance(connection_status, Connection_Status) else Connection_Status.UNKNOWN

    def get_access_type(self):
        return self.__access_type

    def set_access_type(self, access_type):
        self.__access_type = access_type if isinstance(access_type, Access_Type) else Access_Type.EXILE