import pygame
from gamelogic.letter_positions import letter_positions
from gamelogic.gameloop import Gameloop
from words.config import word_repository
from ui.display import Display

class Menu:
    def __init__(self, display: Display, event_queue, width, height):
        self.display = display
        self.event_queue = event_queue
        self.width = width
        self.height = height

    def menu(self):
        while True:
            self.display.draw_window()
            positions = self.display.draw_menu()
            if self.menu_events(positions) is False:
                pygame.quit()
                break

    def menu_events(self, pos):
        letters = []
        word = ""
        for event in self.event_queue.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.MOUSEBUTTONDOWN:
                mou = self.event_queue.get_pos()
                words = word_repository()
                if pos[0][0]+pos[0][2]>mou[0]>pos[0][0] and pos[0][1]+pos[0][3]>mou[1]>pos[0][1]:
                    word = words.easy_word()
                    letters = letter_positions(self.width,self.height)
                elif pos[1][0]+pos[1][2]>mou[0]>pos[1][0] and pos[1][1]+pos[1][3]>mou[1]>pos[1][1]:
                    word = words.medium_word()
                    letters = letter_positions(self.width,self.height)
                elif pos[0][0]+pos[2][2]>mou[0]>pos[2][0] and pos[2][1]+pos[2][3]>mou[1]>pos[2][1]:
                    word = words.hard_word()
                    letters = letter_positions(self.width,self.height)
                game = Gameloop(self.display,letters,0,self.event_queue)
                game.start(word.upper())
        return True
