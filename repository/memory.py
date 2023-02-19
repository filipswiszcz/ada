from entity.entity import Entity

class Memory:

    def __init__(self):
        self.__entities = {}

    def get_entities(self):
        return self.__entities
    
    def get_entity(self, id):
        return self.__entities.keys()[id]
    
    def add_entity(self, entity):
        if not isinstance(entity, Entity): return
        else: self.__entities[entity.get_id()] = entity