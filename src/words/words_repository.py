import random

class WordRepository:
    def __init__(self, file_path):
        self.file_path = file_path
    def easy_word(self):
        medium_words = []
        words = self.find_all()
        for i in words:
            if 5 < len(i) < 10:
                medium_words.append(i)
        return random.choice(medium_words)
    def medium_word(self):
        hard_words = []
        words = self.find_all()
        for i in words:
            if 9 < len(i) < 15:
                hard_words.append(i)
        return random.choice(hard_words)
    def hard_word(self):
        easy_words = []
        words = self.find_all()
        for i in words:
            if  3 < len(i) < 6:
                easy_words.append(i)
        return random.choice(easy_words)
    def find_all(self):
        return self.read()
    def read(self):
        words = []
        with open(self.file_path) as file:
            for row in file:
                row = row.replace("\n", "")
                words.append(row)
        return words
