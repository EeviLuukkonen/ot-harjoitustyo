import os
from words.words_repository import WordRepository

dirname = os.path.dirname(__file__)

def word_repository():
    return WordRepository(os.path.join(dirname, "words.txt"))
