from gamelogic.event_queue import EventQueue
from gamelogic.letter_positions import letter_positions
import pygame
from ui.load_images import load_images
from ui.display import Display
from gamelogic.gameloop import Gameloop
from gamelogic.clock import Clock


def main():
    pygame.init()
    width = 600
    height = 700
    display = pygame.display.set_mode((width, height))
    images = load_images()
    status = 0
    # sql-wordlist will be added later
    clock = Clock()
    event_queue = EventQueue()
    letters = letter_positions(width, height)
    renderer = Display(display, width, height, images, letters)
    gameloop = Gameloop(renderer, letters, status, clock, event_queue)

    gameloop.menu()


if __name__ == "__main__":
    main()
