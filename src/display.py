import pygame

class Display():
    def __init__(self, display, width, height, images, letters):
        self.display = display
        self.width = width
        self.images = images
        self.letters = letters
        self.height = height

    def draw_menu(self):
        positions = []
        font = pygame.font.SysFont("Arial", 30)
        valitse = font.render("Valitse vaikeustaso:", 1, (0,0,0))
        helppo = font.render("Helppo", 1, (0,0,0))
        keskivaikea = font.render("Keskivaikea", 1, (0,0,0))
        vaikea = font.render("Vaikea", 1, (0,0,0))
        list = [helppo, keskivaikea, vaikea]
        self.display.blit(valitse, (self.width/2 - valitse.get_width()/2, 180))
        self.display.blit(helppo, (self.width/2 - helppo.get_width()/2, 300))
        self.display.blit(keskivaikea, (self.width/2 - keskivaikea.get_width()/2, 400))
        self.display.blit(vaikea, (self.width/2 - vaikea.get_width()/2, 500))
        for i in range(1,4):
            pygame.draw.rect(self.display, (0,0,0), pygame.Rect(self.width/2-list[i-1].get_width()/2-10, 185+i*100, list[i-1].get_width()+20, 60),2)
            positions.append([self.width/2-list[i-1].get_width()/2-10, 185+i*100, list[i-1].get_width()+20, 60])
        pygame.display.update()
        return positions

    def draw_window(self):
        #draw window
        self.display.fill((255,255,255))
        font = pygame.font.SysFont("Chilanka", 60)
        text = font.render("Hirsipuu", 1, (0,0,0))
        self.display.blit(text, (self.width/2 - text.get_width()/2, 30))
        return font

    def draw_image(self,status,x,y):
        #draw hangman
        self.display.blit(self.images[status], (x,y))

    def draw_display(self, guessed, word):
        #draw buttons and letters
        for letter in self.letters:
            if letter[3] == False:
                pygame.draw.circle(self.display, (0,0,0), (letter[0],letter[1]), 20, 2)
                letter_font = pygame.font.SysFont("Chilanka", 30)
                letter_text = letter_font.render(letter[2], 1, (0,0,0))
                self.display.blit(letter_text, (letter[0]-12,letter[1]-12))
        #draw word
        display_word = ""
        word_font = pygame.font.SysFont("Arial", 30)
        for i in word:
            if i in guessed:
                display_word += i + " "
            else:
                display_word += "_ "
        display_text = word_font.render(display_word, 1, (0,0,0))
        self.display.blit(display_text, (300,300))

        pygame.display.update()

        return display_word

    def render_winscreen(self):
        font = self.draw_window()
        text = font.render("Voitit!", 1, (224,3,65))
        self.display.blit(text, (self.width/2 - text.get_width()/2, self.height/2 - text.get_height()/2))
        pygame.display.update()

    def render_loosescreen(self):
        font = self.draw_window()
        text = font.render("Hävisit!", 1, (224,3,65))
        self.display.blit(text, (self.width/2 - text.get_width()/2, 200))
        self.draw_image(6, 200, self.height/2)
        pygame.display.update()