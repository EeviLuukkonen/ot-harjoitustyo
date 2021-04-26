import math
import pygame
from ui.display import Display

class Gameloop():
    def __init__(self, display: Display, letters: list, status: int, event_queue):
        self.display = display
        self.letters = letters
        self.status = status
        self.guessed = []
        self.event_queue = event_queue

    def start(self, word):
        while True:
            if self.check_if_won(word):
                self.win()
            elif self.check_if_lost():
                self.loose()
            else:  # render game
                self.display.draw_window()
                self.display.draw_image(self.status, 60, 150)
                self.display.draw_display(self.guessed, word, self.letters)
            # check events
            if self.events(word) is False:
                break

    def check_if_won(self, word):
        for i in word:
            if i not in self.guessed:
                return False
        return True

    def check_if_lost(self):
        if self.status == 6:
            return True
        return False

    def events(self, word):
        for event in self.event_queue.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = self.event_queue.get_pos()
                for letter in self.letters:
                    distance = math.sqrt((letter[0]-pos[0])**2+(letter[1]-pos[1])**2)
                    if distance < 20 and letter[2] not in self.guessed:
                        letter[3] = True
                        self.guessed.append(letter[2])
                        if letter[2] not in word:
                            self.status += 1
        return True

    def win(self):
        self.display.render_winscreen()

    def loose(self):
        self.display.render_loosescreen()
