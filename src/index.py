from pygame import Pygame
from display import Display

def main():
    width = 800
    height = 500
    pygame.display.set_mode(width, height)
    pygame.display.set_caption("Hangman")
    pygame.init()