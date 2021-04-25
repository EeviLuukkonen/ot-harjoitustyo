from gamelogic.event_queue import EventQueue
from gamelogic.letter_positions import letter_positions
import pygame
from images.load_images import load_images
from ui.display import Display
from gamelogic.gameloop import Gameloop
from gamelogic.menu import Menu

def main():
    pygame.init()
    width = 600
    height = 700
    win = pygame.display.set_mode((width, height))
    images = load_images()
    event_queue = EventQueue()
    letters = letter_positions(width, height)
    display = Display(win, width, height, images)
    menu = Menu(display, event_queue, width, height)
    menu.menu()


if __name__ == "__main__":
    main()
