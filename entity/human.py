from entity.entity import Entity

class Human(Entity):

    def __init__(self, name, entity_type, access_type):
        super().__init__(name, entity_type, access_type)
        self.__common_words = []
        self.__common_sentence_patterns = []

    def get_common_words(self):
        return self.__common_words
    
    def add_common_word(self, word):
        self.__common_words.append(word)

    def remove_common_word(self, word):
        if word not in self.__common_words: return
        self.__common_words.remove(word)