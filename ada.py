from entity.entity import Entity
from entity.entity_type import Entity_Type
from repository.memory import Memory
from security.access_type import Access_Type
from util.util import Util

# TODO
# - security flags
# - some kind of verification
# - channeling
# - encrypting
class Ada(object):

    def __init__(self):
        self.version = "0.0.1"
        #self.status = Flag.OPEN
        #self.dictionary = Dictionary(self.status)
        self.memory = Memory()
        self.properties = Util().get_global_properties()

    def get_version(self):
        return self.version
    
    def get_status(self):
        return self.status
    
    def set_status(self, flag):
        self.status = flag

    def get_dictionary(self):
        return self.dictionary
    
    def test(self):
        a = [141, 21, 123, 11, 2]
        for i in range(5):
            for j in range(5):
                if a[i] < a[j]: a[i], a[j] = a[j], a[i]
        print(a)


ada, atom = Ada(), Entity("Atom", Entity_Type.ROBOT, Access_Type.ROOT)
#ada.memory.add_entity(atom)
#print(ada.memory.get_entities()[0].get_name())
print(ada.properties["host"])
#print(ada.get_dictionary().get_map())