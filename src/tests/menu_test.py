import unittest
import pygame
from gamelogic.gameloop import Gameloop
from gamelogic.menu import Menu

class StubEvent:
    def __init__(self, event_type):
        self.type = event_type

class StubEventQueue:
    def __init__(self, events):
        self.events = events
    def get(self):
        return self.events
    def get_pos(self):
        return (303, 319)

class StubEventQueue2:
    def __init__(self, events):
        self.events = events
    def get(self):
        return self.events
    def get_pos(self):
        return (303,414)

class StubEventQueue3:
    def __init__(self, events):
        self.events = events
    def get(self):
        return self.events
    def get_pos(self):
        return (303, 523)

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
        return "_ _"
    def render_winscreen(self):
        pygame.quit()
    def render_loosescreen(self):
        pass

class TestMenu(unittest.TestCase):
    def setUp(self):
        self.display = StubDisplay()

    def test_menu_ok(self):
        events = [StubEvent(pygame.QUIT)]
        menu = Menu(self.display, StubEventQueue(events), 600, 700)

        menu.menu()

        self.assertFalse(menu.menu_events([[241.5, 285, 117, 60], [209.0, 385, 182, 60], [244.5, 485, 111, 60]]))

    def test_easy_level_choosing_ok(self):
        events = [StubEvent(pygame.MOUSEBUTTONDOWN), StubEvent(pygame.QUIT)]
        menu = Menu(self.display, StubEventQueue(events), 600, 700)

        menu.menu()

        self.assertEqual(menu.event_queue.get_pos(), (303, 319))

    def test_medium_level_choosing_ok(self):
        events = [StubEvent(pygame.MOUSEBUTTONDOWN), StubEvent(pygame.QUIT)]
        menu = Menu(self.display, StubEventQueue2(events), 600, 700)

        menu.menu()

        self.assertEqual(menu.event_queue.get_pos(), (303,414))

    def test_hard_level_choosing_ok(self):
        events = [StubEvent(pygame.MOUSEBUTTONDOWN), StubEvent(pygame.QUIT)]
        menu = Menu(self.display, StubEventQueue3(events), 600, 700)

        menu.menu()

        self.assertEqual(menu.event_queue.get_pos(), (303, 523))