import pygame

class Renderer:
    def __init__(self, display, height, width, top_left_x, top_left_y):
        self._display = display
        self._height = height
        self._width = width
        self._top_left_x = top_left_x
        self._top_left_y = top_left_y

    def render_window(self):
        self._display.fill((0,0,0))
        font = pygame.font.SysFont("Arial", 60)
        text = font.render("Tetris", 1, (255,255,255))

        self._display.blit(text, (self._top_left_x+self._width/2-text.get_width()/2, 30))

        for i in range(21):
            pygame.draw.line(self._display, (128,128,128), (self._top_left_x, self._top_left_y+i*30), (self._top_left_x+self._width, self._top_left_y+i*30))
            for j in range(11):
                pygame.draw.line(self._display, (128,128,128), (self._top_left_x+j*30, self._top_left_y), (self._top_left_x+j*30, self._top_left_y+self._height))

        pygame.display.update()

 