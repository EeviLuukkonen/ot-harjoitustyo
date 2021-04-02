import pygame

class Gameloop:
    def __init__(self, clock, renderer):
        self.clock = clock
        self.renderer = renderer

    def start(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        pygame.quit()
            #if self.events() == False:
                #break

            #current_time = self._clock.get_ticks()

            #self._level.update(current_time)
            #self._render()

            #if self._level.is_completed():
                #break
            self._render()

            self.clock.tick(60)

    def _render(self):
        self.renderer.render_window()

    #def events(self):
        #pass