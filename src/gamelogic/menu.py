from gamelogic.letter_positions import letter_positions
from gamelogic.event_queue import EventQueue
import pygame
from words.config import word_repository
from gamelogic.gameloop import Gameloop
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

    def menu_events(self, positions):
        for event in self.event_queue.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = self.event_queue.get_pos()
                words = word_repository()
                if positions[0][0]+positions[0][2] > pos[0] > positions[0][0] and positions[0][1]+positions[0][3] > pos[1] > positions[0][1]:
                    word = words.easy_word()
                    letters = letter_positions(self.width,self.height)
                elif positions[1][0]+positions[1][2] > pos[0] > positions[1][0] and positions[1][1]+positions[1][3] > pos[1] > positions[1][1]:
                    word = words.medium_word()
                    letters = letter_positions(self.width,self.height)
                elif positions[0][0]+positions[2][2] > pos[0] > positions[2][0] and positions[2][1]+positions[2][3] > pos[1] > positions[2][1]:
                    word = words.hard_word()
                    letters = letter_positions(self.width,self.height)
                game = Gameloop(self.display,letters,0,self.event_queue)
                game.start(word.upper())
