from clock import Clock
from display import Display
import pygame
import math

class Gameloop():
    def __init__(self, display: Display, word: str, letters: list, status: int, clock: Clock, event_queue):
        self.display = display
        self.letters = letters
        self.status = status
        self.word = word
        self.guessed = []
        self.clock = clock
        self.event_queue = event_queue

    def start(self):
        while True:
            if self.check_if_won():
                self.win()
            elif self.check_if_lost():
                self.loose()
            else: #render game
                self.display.draw_window()
                self.display.draw_image(self.status, 60, 150)

                self.game = self.display.draw_display(self.guessed)
            #chech events
            if self.events() == False:
                pygame.quit()
                break 

            self.clock.tick()

    def check_if_won(self):
        for i in self.word:
            if i not in self.guessed:
                return False
        return True

    def check_if_lost(self):
        if self.status == 6:
            return True
            
    def events(self):
        for event in self.event_queue.get():
                if event.type == pygame.QUIT:
                        return False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    for letter in self.letters:
                        distance = math.sqrt((letter[0]-pos[0])**2+(letter[1]-pos[1])**2)
                        if distance < 20 and letter[2] not in self.guessed:
                            letter[3] = True
                            self.guessed.append(letter[2])
                            if letter[2] not in self.word:
                                self.status += 1

    def win(self):
        self.display.render_winscreen()
                
    def loose(self):
        self.display.render_loosescreen()
