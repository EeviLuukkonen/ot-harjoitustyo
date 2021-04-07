import pygame
import math

class Gameloop():
    def __init__(self, display, word, letters, status, clock):
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

            game = self.display.draw_display(self.status, self.guessed)

            #check if won
            if "_" not in game:
                self.win()
                self.clock.delay()
            #check if lost
            if self.status == 6:
                self.loose()
                self.clock.delay()
                
            self.clock.tick()

    def events(self):
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        return False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    for letter in self.letters:
                        dis = math.sqrt((letter[0]-pos[0])**2+(letter[1]-pos[1])**2)
                        if dis < 20:
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
        self.display.display.blit(text, (self.display.width/2 - text.get_width()/2, self.display.height/2 - text.get_height()/2))
        pygame.display.update()
