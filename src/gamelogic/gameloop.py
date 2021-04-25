import math
import pygame
from words.config import word_repository
from gamelogic.clock import Clock
from ui.display import Display


class Gameloop():
    def __init__(self, display: Display, letters: list, status: int, clock: Clock, event_queue):
        self.display = display
        self.letters = letters
        self.status = status
        self.guessed = []
        self.clock = clock
        self.event_queue = event_queue

    def menu(self):
        while True:
            self.display.draw_window()
            positions = self.display.draw_menu()
            if self.menu_events(positions) is False:
                pygame.quit()
                break

    def menu_events(self, positions):
        for event in self.event_queue.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = self.event_queue.get_pos()
                words = word_repository()
                if positions[0][0]+positions[0][2] > pos[0] > positions[0][0] and positions[0][1]+positions[0][3] > pos[1] > positions[0][1]:
                    word = words.easy_word()
                elif positions[1][0]+positions[1][2] > pos[0] > positions[1][0] and positions[1][1]+positions[1][3] > pos[1] > positions[1][1]:
                    word = words.medium_word()
                elif positions[0][0]+positions[2][2] > pos[0] > positions[2][0] and positions[2][1]+positions[2][3] > pos[1] > positions[2][1]:
                    word = words.hard_word()
                self.status = 0
                self.guessed = []
                self.start(word.upper())

    def start(self, word):
        while True:
            if self.check_if_won(word):
                self.win()
            elif self.check_if_lost():
                self.loose()
            else:  # render game
                self.display.draw_window()
                self.display.draw_image(self.status, 60, 150)
                self.display.draw_display(self.guessed, word)
            self.clock.tick()
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

    def win(self):
        self.display.render_winscreen()

    def loose(self):
        self.display.render_loosescreen()
