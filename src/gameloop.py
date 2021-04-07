import pygame
import math

class Gameloop():
    def __init__(self, display, letters):
        self.display = display
        self.letters = letters

    def start(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        pygame.quit()
                        break

                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    for letter in self.letters:
                        dis = math.sqrt((letter[0]-pos[0])**2+(letter[1]-pos[1])**2)
                        if dis < 20:
                            letter[3] = True


            self.display.draw()