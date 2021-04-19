import pygame


class Clock:
    def __init__(self):
        self._clock = pygame.time.Clock()

    def tick(self):
        self._clock.tick()

    def get_ticks(self):
        return pygame.time.get_ticks()

    def delay(self):
        pygame.time.delay(3000)
