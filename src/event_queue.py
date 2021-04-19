import pygame

class EventQueue:
    def get(self):
        return pygame.event.get()
    def get_pos(self):
        return pygame.mouse.get_pos()