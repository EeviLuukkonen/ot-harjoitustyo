import random

class WordRepository:
    """Luokka, joka arpoo sanan tiedostosta peliin
    """
    def __init__(self, file_path):
        """Konstruktori

        Args:
            file_path: polku sanatiedostoon
        """
        self.file_path = file_path
    def easy_word(self):
        """Metodi, joka arpoo helppotasoisen sanan

        Returns:
            satunnainen 4-5 kirjaiminen sana
        """
        easy_words = []
        words = self.find_all()
        for i in words:
            if  3 < len(i) < 6:
                easy_words.append(i)
        return random.choice(easy_words)
    def medium_word(self):
        """Metodi, joka arpoo keskitasoisen sanan

        Returns:
            satunnainen 6-9 kirjaiminen sana
        """
        medium_words = []
        words = self.find_all()
        for i in words:
            if 5 < len(i) < 10:
                medium_words.append(i)
        return random.choice(medium_words)
    def hard_word(self):
        """Metodi, joka arpoo vaikeatasoisen sanan

        Returns:
            satunnainen 10-14 kirjaiminen sana
        """
        hard_words = []
        words = self.find_all()
        for i in words:
            if 9 < len(i) < 15:
                hard_words.append(i)
        return random.choice(hard_words)
    def find_all(self):
        return self.read()
    def read(self):
        """Metodi, joka lukee sanatiedoston rivit listaan

        Returns:
            lista kaikista sanoista
        """
        words = []
        with open(self.file_path) as file:
            for row in file:
                row = row.replace("\n", "")
                words.append(row)
        return words
