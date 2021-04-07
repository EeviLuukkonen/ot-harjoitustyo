import pygame

class Display():
    def __init__(self, display, width, height, images, letters):
        self.display = display
        self.width = width
        self.images = images
        self.letters = letters
        self.height = height

    def draw(self):
        #draw window
        self.display.fill((255,255,255))
        font = pygame.font.SysFont("Chilanka", 60)
        text = font.render("Hirsipuu", 1, (0,0,0))
        self.display.blit(text, (self.width/2 - text.get_width()/2, 30))

        #draw status
        self.display.blit(self.images[0], (60, 150))

        #draw buttons and letters
        for letter in self.letters:
            if letter[3] == False:
                pygame.draw.circle(self.display, (0,0,0), (letter[0],letter[1]), 20, 2)
                letter_font = pygame.font.SysFont("Chilanka", 30)
                letter_text = letter_font.render(letter[2], 1, (0,0,0))
                self.display.blit(letter_text, (letter[0]-12,letter[1]-12))

        pygame.display.update()