import random

class WordFinder:
    """Class for selecting random words from text file"""
    def __init__(self, path):
        """Iterates through dictionary and reports the number of words read"""
        dictionary_file = open(path)
        self.words = self.parse(dictionary_file)
        print(f"{len(self.words)} number of words read")
    
    def parse (self, dictionary_file):
        """Parses file for list of words"""
        return [word.strip() for word in dictionary_file]

    def random(self):
        """Chooses random word from parsed list"""
        return random.choice(self.words)

class SpecialWordFinder(WordFinder):
    """Class that excludes any comments or blank lines"""

    def parse (self, dictionary_file):
        """Parses file skipping comments and blank lines"""
        return [word.strip() for word in dictionary_file if word.strip() and not word.startswith('#')]
        



