import pygame

class Display():
    def __init__(self, display, width, height, images):
        self.display = display
        self.width = width
        self.images = images
        self.height = height

    def draw_menu(self):
        positions = []
        font = pygame.font.SysFont("Linux Biolinum Keyboard O", 35,bold=False, italic=False)
        font1 = pygame.font.SysFont("latoheavy", 40)
        font2 = pygame.font.SysFont("arial", 17, bold = True)
        #levels
        valitse = font.render("VALITSE", 1, (53, 34, 12))
        vaikeustaso = font.render("VAIKEUSTASO", 1, (53, 34, 12))
        helppo = font1.render("HELPPO", 1, (53, 34, 12))
        keskivaikea = font1.render("KESKIVAIKEA", 1, (53, 34, 12))
        vaikea = font1.render("VAIKEA", 1, (53, 34, 12))
        list = [helppo, keskivaikea, vaikea]
        #end game
        self.display.blit(font2.render("lopeta peli", 1, (0, 0, 0)), (self.width-100,20))
        pygame.draw.line(self.display, (53, 34, 12), (self.width-45,21),(self.width-30,6), 3)
        pygame.draw.line(self.display, (53, 34, 12), (self.width-40,5),(self.width-30,5), 2)
        pygame.draw.line(self.display, (53, 34, 12), (self.width-30,5),(self.width-30,15), 2)
        #draw levels
        self.display.blit(valitse, (self.width/2 - valitse.get_width()/2, 160))
        self.display.blit(vaikeustaso, (self.width/2 - vaikeustaso.get_width()/2, 190))
        self.display.blit(helppo, (self.width/2 - helppo.get_width()/2, 300))
        self.display.blit(keskivaikea, (self.width/2 -
                          keskivaikea.get_width()/2, 400))
        self.display.blit(vaikea, (self.width/2 - vaikea.get_width()/2, 500))
        #draw rectangles
        for i in range(1, 4):
            pygame.draw.rect(self.display, (0, 0, 0), pygame.Rect(
                self.width/2-list[i-1].get_width()/2-10, 185+i*100, list[i-1].get_width()+20, 60), 3)
            positions.append([self.width/2-list[i-1].get_width() /
                             2-10, 185+i*100, list[i-1].get_width()+20, 60])
        pygame.display.update()
        return positions

    def draw_window(self):
        # draw window
        pygame.display.set_caption("Hirsipuu")
        self.display.fill((203, 180, 149))
        font = pygame.font.SysFont("Lordina Solid", 80, bold=True, italic=False)
        text = font.render("HIRSIPUU", True, (0, 0, 0))
        self.display.blit(text, (self.width/2 - text.get_width()/2, 30))
        return font

    def draw_image(self, status, x, y):
        # draw hangman
        self.display.blit(self.images[status], (x, y))

    def draw_display(self, guessed, word, letters):
        self.draw_newword()
        # draw buttons and letters
        for letter in letters:
            if letter[3] is False:
                pygame.draw.circle(self.display, (0, 0, 0),(letter[0], letter[1]), 20, 2)
                letter_font = pygame.font.SysFont("Chilanka", 30)
                letter_text = letter_font.render(letter[2], 1, (0, 0, 0))
                self.display.blit(letter_text, (letter[0]-12, letter[1]-12))
        # draw word
        display_word = ""
        word_font = pygame.font.SysFont("Arial", 25)
        for i in word:
            if i in guessed:
                display_word += i + " "
            else:
                display_word += "_ "
        display_text = word_font.render(display_word, 1, (0, 0, 0))
        self.display.blit(display_text, (270, 240))

        pygame.display.update()

        return display_word

    def render_winscreen(self):
        font = self.draw_window()
        self.draw_newword()
        text = font.render("Voitit!", 1, (224, 3, 65))
        self.display.blit(
            text, (self.width/2 - text.get_width()/2, self.height/2 - text.get_height()/2))
        pygame.display.update()

    def render_loosescreen(self):
        font = self.draw_window()
        self.draw_newword()
        text = font.render("Hävisit!", 1, (224, 3, 65))
        self.display.blit(text, (self.width/2 - text.get_width()/2, 200))
        self.draw_image(6, 200, self.height/2)
        pygame.display.update()

    def draw_newword(self):
        font = pygame.font.SysFont("Comicsans", 25)
        self.display.blit(font.render("Uusi sana", 1, (0, 0, 0)), (self.width-100,20))
        pygame.draw.line(self.display, (0, 0, 0), (self.width-45,21),(self.width-30,6), 3)
        pygame.draw.line(self.display, (0, 0, 0), (self.width-40,5),(self.width-30,5), 2)
        pygame.draw.line(self.display, (0, 0, 0), (self.width-30,5),(self.width-30,15), 2)
