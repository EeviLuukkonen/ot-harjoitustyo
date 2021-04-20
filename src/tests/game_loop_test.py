import unittest
import pygame
from gamelogic.gameloop import Gameloop
from gamelogic.letter_positions import letter_positions

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
    def draw_display(self, guessed, word):
        return "_ _"
    def render_winscreen(self):
        pygame.quit()
    def render_loosescreen(self):
        pass

# (display: Display, word: str, letters: list, status: int, clock: Clock, event_queue: EventQueue)
class TestGameloop(unittest.TestCase):
    def setUp(self):
        self.letters = letter_positions(600, 700)
        self.display = StubDisplay()

    def test_game_lost(self):
        events = [StubEvent(pygame.QUIT)]

        game = Gameloop(self.display, self.letters, 6,
                        StubClock(), StubEventQueue(events))

        game.start("A")

        self.assertTrue(game.check_if_lost())

    def test_game_won(self):
        events = [StubEvent(pygame.MOUSEBUTTONDOWN), StubEvent(pygame.QUIT)]

        game = Gameloop(self.display, self.letters, 0,
                        StubClock(), StubEventQueue(events))

        game.start("A")

        self.assertEqual(game.check_if_won("A"), True)

    def test_wrong_letter(self):
        events = [StubEvent(pygame.MOUSEBUTTONDOWN), StubEvent(pygame.QUIT)]

        game = Gameloop(self.display, self.letters, 0,
                        StubClock(), StubEventQueue(events))

        game.start("B")

        self.assertEqual(game.status, 1)

    def test_menu_ok(self):
        events = [StubEvent(pygame.QUIT)]
        game = Gameloop(self.display, self.letters, 0,
                        StubClock(), StubEventQueue(events))

        game.menu()

        self.assertFalse(game.menu_events([[241.5, 285, 117, 60], [209.0, 385, 182, 60], [244.5, 485, 111, 60]]))

    def test_level_choosing_ok(self):
        events = [StubEvent(pygame.MOUSEBUTTONDOWN), StubEvent(pygame.QUIT)]
        game = Gameloop(self.display, self.letters, 0,
                        StubClock(), StubEventQueue(events))

        game.menu()

        self.assertEqual(game.event_queue.get_pos(), (140,450))
