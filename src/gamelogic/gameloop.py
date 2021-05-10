import math
import pygame
from ui.display import Display
from gamelogic.clock import Clock
from highscores import Highscore
from database_connection import get_database_connection

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
    def __init__(self, display: Display, letters: list, status: int, event_queue, word, level):
        """Luokan konstruktori, joka luo uuden pelin

        Args:
            display (Display): Display-olio, joka kuvaa pelialuetta
            letters (list): Kirjainten sijannit peliruudulla [x, y, letter, used (True/False)]
            status (int): Tämänhetkinen pelitilanne, kuinka monta kertaa käyttäjä arvannut väärin
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
        self.level = level
        self.highscore = Highscore(get_database_connection())

    def start(self):
        """Metodi, joka ylläpitää pelinäkymää
        """
        start_time = self.clock.get_ticks()
        while True:
            if self.check_if_won():
                self.win(start_time)
                break
            elif self.check_if_lost():
                self.loose()
            else:
                self.clock.tick(25)
                self.display.draw_window()
                self.display.draw_image(self.status, 60, 150)
                self.guessed = self.display.draw_display(self.guessed, self.word, self.letters)
                self.display.draw_timer(self.clock.get_ticks(), start_time)

            if self.events() is False:
                break

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
                            return True

    def win(self, start_time):
        """Metodi, joka renderöi voittoruudun
        """
        result = self.clock.get_ticks()-start_time
        self.highscore.create(result, self.level)
        db = self.highscore.find_all()
        while True:
            self.display.render_winscreen(self.word, result, db)
            if self.events() is False:
                break

    def loose(self):
        """Metodi, joka renderöi häviöruudun
        """
        self.display.render_loosescreen(self.word)
