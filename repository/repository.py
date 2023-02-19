import csv
import security.protocol as protocol
from entity.entity import Entity

# TODO
# - map that stores common used words or sentences in memory, to quick access
# - scrapper for word searching, handler for cataloging it
# - save it with the value of pronunciation
# 
# ada is asking me to pronunce new or stored words, to strip it and group it into known or new keys
# I (read: "aj") has value e.g. 01 ???
# builder is connecting them into whole number e.g. 015454223
# ada is using this number to perform action (function)
class Dictionary:

    def __init__(self, status):
        self.__status = status
        self.__map = {}
        self.__common_words = []
        self.__load_words()

    def __load_words(self):
        if self.__status == protocol.Flag.LOCKED: return "The system is locked."
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        for char in alphabet: 
            words = self.__get_file(char)
            self.__map[char] = len(words) if words != None else 0

    def __get_file(self, char):
        holder = []
        try:
            with open("resource/" + str(char) + ".csv", "r", newline = "") as output:
                for line in csv.reader(output, delimiter = ";"):
                    for word in line: holder.append(word)
            return holder
        except FileNotFoundError: self.__set_file(char)
        except Exception: return "Error occured while a file loading."

    def __set_file(self, char, words):
        try:
            with open("resource/" + str(char) + ".csv", "x", newline = "") as input:
                 writer = csv.writer(input, delimiter = ";")
                 for word in words: writer.writerow
                 # here get some scrapper for words
        except Exception: return "Error occured while a file creating."

    def get_map(self):
        return self.__map
    
    def get_common_words(self):
        return self.__common_words