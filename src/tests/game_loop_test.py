import unittest
import pygame
from gamelogic.gameloop import Gameloop
from gamelogic.letter_positions import letter_positions

class StubEvent:
    def __init__(self, event_type):
        self.type = event_type

class StubEventQueue:
    def __init__(self, events):
        self.events = events
    def get(self):
        return self.events
    def get_pos(self):
        return (140,450)

class StubImages:
    def __init__(self):
        self.images = []

class StubDisplay:
    def __init__(self):
        self.width = 600
        self.height = 700
    def draw_menu(self):
        return [[241.5, 285, 117, 60], [209.0, 385, 182, 60], [244.5, 485, 111, 60]]
    def draw_window(self):
        pygame.init()
        return pygame.font.SysFont("Chilanka", 60)
    def draw_image(self, status, x, y):
        pass
    def draw_display(self, guessed, word, letters):
        return []
    def render_winscreen(self, word, result, db):
        pygame.quit()
    def render_loosescreen(self, word):
        pass
    def draw_timer(self, current_time, start_time):
        pass

class TestGameloop(unittest.TestCase):
    """Testiluokka Gameloop-luokalle

    Args:
        unittest
    """
    def setUp(self):
        """SetUp-metodi, jossa alustetaan kirjainten sijainnit ja valeluokka Display
        """
        self.letters = letter_positions(600, 700)
        self.display = StubDisplay()

    def test_game_lost(self):
        """Metodi, joka testaa pelin häviämistä
        """
        events = [StubEvent(pygame.QUIT)]

        game = Gameloop(self.display, self.letters, 6, StubEventQueue(events), "A", "helppo")

        game.start()

        self.assertTrue(game.check_if_lost())

    def test_wrong_letter(self):
        """Metodi, joka testaa väärän kirjaimen painamista
        """
        events = [StubEvent(pygame.MOUSEBUTTONDOWN), StubEvent(pygame.QUIT)]

        game = Gameloop(self.display, self.letters, 5, StubEventQueue(events), "BC", "helppo")

        game.start()

        self.assertEqual(game.status, 6)

    def test_right_letter(self):
        """Metodi, joka testaa oikean kirjaimen painamista
        """
        events = [StubEvent(pygame.MOUSEBUTTONDOWN), StubEvent(pygame.QUIT)]

        game = Gameloop(self.display, self.letters, 5, StubEventQueue(events), "BCA", "helppo")

        game.start()

        self.assertEqual(game.status, 5)
