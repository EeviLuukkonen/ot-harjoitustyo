import pygame
from clock import Clock
from shapes import Shapes
from gameloop import Gameloop
from renderer import Renderer

def main():
    display_height = 700
    display_width = 800
    height = 600
    width = 300
    top_left_x = (display_width - width) // 2
    top_left_y = display_height - height   

    display = pygame.display.set_mode((display_width, display_height))
    pygame.display.set_caption("Tetris")

    clock = Clock()
    renderer = Renderer(display, height, width, top_left_x, top_left_y)
    game_loop = Gameloop(clock, renderer)


    piece_shape = Shapes()
    #piece_shape.get_shape

    pygame.init()
    game_loop.start()



if __name__ == "__main__":
    main()
