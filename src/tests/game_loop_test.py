import unittest
import pygame
from gameloop import Gameloop
from display import Display
import letter_positions

class StubClock:
    def tick(self):
        pass

    def delay(self):
        pass

class StubEvent:
    def __init__(self, event_type, key):
        self.type = event_type
        self.key = key

class StubImages:
    def __init__(self):
        self.images = []

class StubDisplay:
    def __init__(self):
        self.display = pygame.display.set_mode((600,700))
        self.width = 600
        self.height = 700
    def draw_window(self):
        pygame.init()
        return pygame.font.SysFont("Chilanka", 60)
    def draw_image(self,status,x,y):
        pass
    def draw_display(self, guessed):
        return "_ _"


#(display: Display, word: str, letters: list, status: int, clock: Clock)
class TestGameloop(unittest.TestCase):
    def setUp(self):
        self.word = "ab"
        self.letters = letter_positions.letter_positions(600,700)
        self.display = StubDisplay()
    def test_game_lost(self):

        game = Gameloop(self.display, self.word, self.letters, 6, StubClock())

        game.start()

        self.assertTrue(game.check_if_lost())

