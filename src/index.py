import pygame
from images.load_images import load_images
from ui.display import Display
from gamelogic.menu import Menu
from gamelogic.event_queue import EventQueue
from initialize_database import initialize_database

def main():
    pygame.init()
    width = 600
    height = 700
    win = pygame.display.set_mode((width, height))
    images = load_images()
    initialize_database()
    event_queue = EventQueue()
    display = Display(win, width, height, images)
    menu = Menu(display, event_queue, width, height)
    menu.menu()


if __name__ == "__main__":
    main()
