import pygame

class EventQueue:
    """Luokka, joka huomioi käyttäjän tapahtumat sovelluksen käytön aikana
    """
    def get(self):
        return pygame.event.get()
    def get_pos(self):
        return pygame.mouse.get_pos()
