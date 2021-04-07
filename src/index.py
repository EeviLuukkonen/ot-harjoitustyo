from letter_positions import letter_positions
from load_images import load_images
import pygame
from display import Display
from gameloop import Gameloop

def main():
    pygame.init()
    width = 600
    height = 700
    display = pygame.display.set_mode((width,height))
    images = load_images()
    letters = letter_positions(width, height)
    renderer = Display(display, width, height, images, letters)
    gameloop = Gameloop(renderer, letters)

    gameloop.start()


if __name__ == "__main__":
    main()
