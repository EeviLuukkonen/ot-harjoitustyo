from clock import Clock
from display import Display
import pygame
import math

class Gameloop():
    def __init__(self, display: Display, word: str, letters: list, status: int, clock: Clock):
        self.display = display
        self.letters = letters
        self.status = status
        self.word = word
        self.guessed = []
        self.clock = clock

    def start(self):
        while True:
            #chech events
            if self.events() == False:
                pygame.quit()
                break  
            #render game
            self.display.draw_window()
            self.display.draw_image(self.status, 60, 150)

            self.game = self.display.draw_display(self.guessed)

            if self.check_if_won():
                self.win()
                self.clock.delay()

            if self.check_if_lost():
                self.loose()
                self.clock.delay()
                
            self.clock.tick()

    def check_if_won(self):
        if "_" not in self.game:
            return True


    def check_if_lost(self):
        if self.status == 6:
            return True
            

    def events(self):
        for event in pygame.event.get():
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
        font = self.display.draw_window()
        text = font.render("Voitit!", 1, (224,3,65))
        self.display.display.blit(text, (self.display.width/2 - text.get_width()/2, self.display.height/2 - text.get_height()/2))
        pygame.display.update()
                
    def loose(self):
        font = self.display.draw_window()
        text = font.render("Hävisit!", 1, (224,3,65))
        self.display.display.blit(text, (self.display.width/2 - text.get_width()/2, 200))
        self.display.draw_image(self.status, 200, self.display.height/2)
        pygame.display.update()
