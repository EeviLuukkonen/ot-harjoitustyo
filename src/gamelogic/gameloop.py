import math
import pygame
from ui.display import Display
from gamelogic.clock import Clock
import time

class Gameloop():
    """Luokka, joka huolehtii pelinäkymän toiminnallisuudesta

    Attributes:
        display: Display-olio, joka kuvaa pelialuetta
        letters: Lista kirjainten sijanneista peliruudulla, mallia [x, y, letter, used (True/False)]
        status: Tämänhetkinen pelitilanne, eli kuinka monta kertaa käyttäjä on arvannut väärin
        event_queue: EventQueue-olio, joka kuvaa pelin tapahtumia
        guessed: Käyttäjän jo arvatut kirjaimet
        word =  Arvattava sana
    """
    def __init__(self, display: Display, letters: list, status: int, event_queue, word):
        """Luokan konstruktori, joka luo uuden pelin

        Args:
            display (Display): Display-olio, joka kuvaa pelialuetta
            letters (list): Lista kirjainten sijanneista peliruudulla, mallia [x, y, letter, used (True/False)]
            status (int): Tämänhetkinen pelitilanne, eli kuinka monta kertaa käyttäjä on arvannut väärin
            event_queue (EventQueue): EventQueue-olio, joka kuvaa pelin tapahtumia
            word (str): Arvattava sana
        """
        self.display = display
        self.letters = letters
        self.status = status
        self.guessed = []
        self.event_queue = event_queue
        self.word = word
        self.clock = Clock()

    def start(self):
        """Metodi, joka ylläpitää pelinäkymää 
        """
        while True:
            if self.check_if_won():
                self.win()
            elif self.check_if_lost():
                self.loose()
            else:  # render game
                self.display.draw_window()
                self.display.draw_image(self.status, 60, 150)
                self.guessed = self.display.draw_display(self.guessed, self.word, self.letters)
            # check events
            if self.events() is False:
                break
            self.clock.tick(60)
            
    def check_if_won(self):
        """Metodi, joka tarkistaa, onko peli voitettu

        Returns:
            True, jos peli on voitettu, muuten False
        """
        for i in self.word:
            if i not in self.guessed:
                return False
        return True

    def check_if_lost(self):
        """Metodi, joka tarkistaa, onko peli hävitty

        Returns:
            True, jos peli on hävitty, muuten False
        """
        if self.status == 6:
            return True
        return False

    def events(self):
        """Metodi, joka tarkistaa pelinaikaiset tapahtumat
        """
        for event in self.event_queue.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = self.event_queue.get_pos()
                for letter in self.letters:
                    distance = math.sqrt((letter[0]-pos[0])**2+(letter[1]-pos[1])**2)
                    if distance < 20 and letter[2] not in self.guessed and self.status < 6:
                        letter[3] = True
                        self.guessed.append(letter[2])
                        if letter[2] not in self.word:
                            self.status += 1

    def win(self):
        """Metodi, joka renderöi voittoruudun
        """
        self.display.render_winscreen(self.word)

    def loose(self):
        """Metodi, joka renderöi häviöruudun
        """
        self.display.render_loosescreen(self.word)
