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
    def __init__(self, event_type):
        self.type = event_type

class StubEventQueue:
    def __init__(self, events):
        self.events = events
    def get(self):
        return self.events

class StubImages:
    def __init__(self):
        self.images = []

class StubDisplay:
    def __init__(self):
        self.width = 600
        self.height = 700
    def draw_window(self):
        return pygame.font.SysFont("Chilanka", 60)
    def draw_image(self,status,x,y):
        pass
    def draw_display(self, guessed):
        return "_ _"
    def render_winscreen(self):
        pass
    def render_loosescreen(self):
        pass

#(display: Display, word: str, letters: list, status: int, clock: Clock, event_queue: EventQueue)
class TestGameloop(unittest.TestCase):
    def setUp(self):
        self.word = "ab"
        self.letters = letter_positions.letter_positions(600,700)
        self.display = StubDisplay()
    def test_game_lost(self):
        events = [StubEvent(pygame.QUIT)]

        game = Gameloop(self.display, self.word, self.letters, 6, StubClock(), StubEventQueue(events))

        game.start()

        self.assertTrue(game.check_if_lost())

