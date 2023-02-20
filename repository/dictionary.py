import csv
from entity.human import Human

# key => value, e.g. 02 => "hi", 256123 = "rocket"
# using heuristics to get pattern of sentence arranging
# store rare words and sentences from every human, because it can be used by someone else, as a way of repeating
# Default sentence parts: subject + verb + object + prepositional phrase e.g. I + like + spaghetti + for dinner
class Dictionary:

    def __init__(self, entities):
        self.__entities = entities
        self.__rare_words = []
        self.__rare_sentence_patterns = {}

    def __load_common_words(self, entity_id):
        if not self.__entities.has_entity(entity_id): return
        if not isinstance(self.__entities.get_entity(entity_id), Human): return
        try:
            with open("resource/" + self.__entities.get_entity(entity_id).get_name() + ".csv", "r", newline = "") as output:
                for line in csv.reader(output, delimiter = ";"):
                    for word in line: self.__entities.get_entity(entity_id).add_common_word(word)
        except FileNotFoundError: return "File of that entity does not exist."
        except Exception: return "Error occured while a file loading."

