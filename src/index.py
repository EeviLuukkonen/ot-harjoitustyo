from event_queue import EventQueue
from letter_positions import letter_positions
from load_images import load_images
import pygame
from display import Display
from gameloop import Gameloop
from clock import Clock
import random

def main():
    pygame.init()
    width = 600
    height = 700
    display = pygame.display.set_mode((width,height))
    images = load_images()
    status = 0
    # sql-wordlist will be added later
    clock = Clock()
    event_queue = EventQueue()
    letters = letter_positions(width, height)
    renderer = Display(display, width, height, images, letters)
    gameloop = Gameloop(renderer, letters, status, clock, event_queue)

    gameloop.menu()
    gameloop.start()


if __name__ == "__main__":
    main()
