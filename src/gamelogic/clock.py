import pygame

class Clock:
    """Luokka, joka vastaa ajan kulusta pelissä
    """
    def __init__(self):
        self._clock = pygame.time.Clock()

    def tick(self, fps):
        """Metodi, jolla aika kuluu eteenpäin"

        Args:
            fps: frames per second
        """
        self._clock.tick(fps)

    def get_ticks(self):
        """Metodi, joka palauttaa tähän mennessä pelin alusta kuluneen ajan

        Returns:
            Aika millisekunteina pelin alusta
        """
        return pygame.time.get_ticks()
