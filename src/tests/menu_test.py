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

class StubEventQueue4:
    def __init__(self, events):
        self.events = events
    def get(self):
        return self.events
    def get_pos(self):
        return (1,1)

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
    def render_winscreen(self, word):
        pygame.quit()
    def render_loosescreen(self, word):
        pass
    def draw_timer(self,current_time, start_time):
        pass

class TestMenu(unittest.TestCase):
    """Testiluokka Menu-luokalle

    Args:
        unittest
    """
    def setUp(self):
        """SetUp-metodi, joka alustaa valeluokan Display
        """
        self.display = StubDisplay()

    def test_menu_ok(self):
        """Metodi, joka testaa, palauttaako menu_events false, jos mitään tasoa ei klikata
        """
        events = [StubEvent(pygame.QUIT)]
        menu = Menu(self.display, StubEventQueue(events), 600, 700)

        menu.menu()

        self.assertFalse(menu.menu_events([[241.5, 285, 117, 60], [209.0, 385, 182, 60], [244.5, 485, 111, 60]]))

    def test_easy_level_choosing_ok(self):
        """Metodi, joka testaa helpon tason valinnan
        """
        events = [StubEvent(pygame.MOUSEBUTTONDOWN), StubEvent(pygame.QUIT)]
        menu = Menu(self.display, StubEventQueue(events), 600, 700)

        menu.menu()

        self.assertEqual(menu.event_queue.get_pos(), (303, 319))

    def test_medium_level_choosing_ok(self):
        """Metodi, joka testaa keskivaikean tason valinnan
        """
        events = [StubEvent(pygame.MOUSEBUTTONDOWN), StubEvent(pygame.QUIT)]
        menu = Menu(self.display, StubEventQueue2(events), 600, 700)

        menu.menu()

        self.assertEqual(menu.event_queue.get_pos(), (303,414))

    def test_hard_level_choosing_ok(self):
        """Metodi, joka testaa vaikean tason valinnan
        """
        events = [StubEvent(pygame.MOUSEBUTTONDOWN), StubEvent(pygame.QUIT)]
        menu = Menu(self.display, StubEventQueue3(events), 600, 700)

        menu.menu()

        self.assertEqual(menu.event_queue.get_pos(), (303, 523))
