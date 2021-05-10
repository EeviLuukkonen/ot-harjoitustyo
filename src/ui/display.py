import pygame

class Display():
    """Käyttöjärjestelmäluokka, jolla eri näkymät piirretään ruudulle

        Attributes:
            display: pygame-display -ikkuna
            width: pelialueen leveys
            images: lista kuvista, joita ruudulle tulee
            height: pelialueen korkeus
    """
    def __init__(self, display, width, height, images):
        """Konstruktori, joka luo uuden pygame-pelinäkymän

        Args:
            display: pygame-display -ikkuna
            width: pelialueen leveys
            images: lista kuvista, joita ruudulle tulee
            height: pelialueen korkeus
        """
        self.display = display
        self.width = width
        self.images = images
        self.height = height

    def draw_window(self):
        """Piirtää alustan, joka on kaikisssa pelin näkymissä

        Returns:
            pygame-fontti muiden luokan metodien käyttöön
        """
        # draw window
        pygame.display.set_caption("Hirsipuu")
        self.display.fill((203, 180, 149))
        font = pygame.font.SysFont("Lordina Solid", 80, bold=True, italic=False)
        text = font.render("HIRSIPUU", True, (0, 0, 0))
        self.display.blit(text, (self.width/2 - text.get_width()/2, 30))
        return font

    def draw_menu(self):
        """Menu-näkymän piirtävä metodi, piirtää tasovalinnat, lopeta peli -ruudun sekä otsikon

        Returns:
            Lista sijanneista, joissa vaikeustasot ruudulla ovat
        """
        positions = []
        font = pygame.font.SysFont("Linux Biolinum Keyboard O", 35,bold=False, italic=False)
        font1 = pygame.font.SysFont("latoheavy", 40)
        font2 = pygame.font.SysFont("arial", 17, bold = True)
        
        valitse = font.render("VALITSE", 1, (53, 34, 12))
        vaikeustaso = font.render("VAIKEUSTASO", 1, (53, 34, 12))
        helppo = font1.render("HELPPO", 1, (53, 34, 12))
        keskivaikea = font1.render("KESKIVAIKEA", 1, (53, 34, 12))
        vaikea = font1.render("VAIKEA", 1, (53, 34, 12))
        list = [helppo, keskivaikea, vaikea]

        self.display.blit(font2.render("lopeta peli", 1, (0, 0, 0)), (self.width-100,20))
        pygame.draw.line(self.display, (53, 34, 12), (self.width-45,21),(self.width-30,6), 3)
        pygame.draw.line(self.display, (53, 34, 12), (self.width-40,5),(self.width-30,5), 2)
        pygame.draw.line(self.display, (53, 34, 12), (self.width-30,5),(self.width-30,15), 2)

        self.display.blit(valitse, (self.width/2 - valitse.get_width()/2, 160))
        self.display.blit(vaikeustaso, (self.width/2 - vaikeustaso.get_width()/2, 190))
        self.display.blit(helppo, (self.width/2 - helppo.get_width()/2, 300))
        self.display.blit(keskivaikea, (self.width/2 -
                          keskivaikea.get_width()/2, 400))
        self.display.blit(vaikea, (self.width/2 - vaikea.get_width()/2, 500))

        for i in range(1, 4):
            pygame.draw.rect(self.display, (0, 0, 0), pygame.Rect(
                self.width/2-list[i-1].get_width()/2-10, 185+i*100, list[i-1].get_width()+20, 60), 3)
            positions.append([self.width/2-list[i-1].get_width() /
                             2-10, 185+i*100, list[i-1].get_width()+20, 60])
        pygame.display.update()
        return positions

    def draw_image(self, status, x, y):
        """Metodi, joka renderöi hirsipuu-ukon peliruudulle

        Args:
            status (int): Tämänhetkinen pelitilanne eli väärien arvausten määrä
            x: X-koordinaatti kuvan paikalle
            x: Y-koordinaatti kuvan paikalle
        """
        # draw hangman
        self.display.blit(self.images[status], (x,y))

    def draw_display(self, guessed, word, letters):
        """Pelinäkymän piirtävä metodi, joka luo ruudulle arvattavan sanan ja kirjainnäppäimet

        Args:
            guessed: Tämänhetkiset jo arvatut kirjaimet
            word: Pelattava sana
            letters: Lista kirjaimista ja niiden sijanneista 

        Returns:
            Tämänhetkiset arvatut kirjaimet (ja sanan ensimmäinen kirjain)
        """
        display_word = ""
        word_font = pygame.font.SysFont("Arial", 25)
        for i in range(len(word)):
            if i == 0:
                display_word += word[i] + " "
                guessed.append(word[i])
            elif word[i] in guessed:
                display_word += word[i] + " "
            else:
                display_word += "_ "
        display_text = word_font.render(display_word, 1, (0, 0, 0))
        self.display.blit(display_text, (270, 240))

        for letter in letters:
            if letter[3] is False and letter[2] not in guessed:
                pygame.draw.circle(self.display, (0, 0, 0),(letter[0], letter[1]), 20, 2)
                letter_font = pygame.font.SysFont("Chilanka", 30)
                letter_text = letter_font.render(letter[2], 1, (0, 0, 0))
                self.display.blit(letter_text, (letter[0]-12, letter[1]-12))

        self.draw_newword()
        pygame.display.update()
        return guessed

    def render_correct_answer(self, word):
        """Metodi, joka piirtää voitto- ja häviöruutuun arvatun sanan

        Args:
            word: Pelattu sana
        """
        font = pygame.font.SysFont("latoheavy", 40)
        text = font.render(f"Sana oli: {word}", 1, (0,0,0))
        self.display.blit(text, (self.width/2 - text.get_width()/2, 295))

    def render_time_spent(self, time):
        font = pygame.font.SysFont("latoheavy", 40)
        text = font.render(f"Aikaa kului: {str((time)/1000).zfill(2)} sekuntia", 1, (0,0,0))
        self.display.blit(text, (self.width/2 - text.get_width()/2, 335))

    def render_winscreen(self, word, result, db):
        """Metodi, joka piirtäää voittoruudun

        Args:
            word: Pelattu sana
        """
        font = self.draw_window()
        self.draw_newword()
        text = font.render("Voitit!", 1, (224, 3, 65))
        self.display.blit(
            text, (self.width/2 - text.get_width()/2, 230))
        self.render_correct_answer(word)
        self.render_time_spent(result)
        self.scoreboard(db)
        pygame.display.update()

    def scoreboard(self,db):
        font = pygame.font.SysFont("latoheavy", 30)
        start_y = 500
        start_score = 1
        tulostaulu = font.render("TULOSTAULU:", 1, (0,0,0))
        info = font.render("{:<20}{:<25}{:<20}".format("sija","aika (sek)", "taso"), 1, (0,0,0))
        self.display.blit(tulostaulu, (self.width/2 - tulostaulu.get_width()/2, 405))
        self.display.blit(info, (100, 460))
        for row in db:
            time = str((row["time"])/1000).zfill(2)
            level = str(row["level"])
            text = font.render("{:<20} {:<25} {:<20}".format(start_score,time,level), 1, (0,0,0))
            self.display.blit(text, (100, start_y))
            start_y += 30
            start_score += 1

    def render_loosescreen(self, word):
        """Metodi, joka piirtää häviöruudun

        Args:
            word: Pelattu sana
        """
        font = self.draw_window()
        self.draw_newword()
        text = font.render("Hävisit!", 1, (224, 3, 65))
        self.display.blit(text, (self.width/2 - text.get_width()/2, 200))
        self.draw_image(6, 200, self.height/2+10)
        self.render_correct_answer(word)
        pygame.display.update()

    def draw_newword(self):
        """Metodi, joka pirtää "Uusi sana" -tekstin ruudun yläreunaan
        """
        font = pygame.font.SysFont("Comicsans", 25)
        self.display.blit(font.render("Uusi sana", 1, (0, 0, 0)), (self.width-100,20))
        pygame.draw.line(self.display, (0, 0, 0), (self.width-45,21),(self.width-30,6), 3)
        pygame.draw.line(self.display, (0, 0, 0), (self.width-40,5),(self.width-30,5), 2)
        pygame.draw.line(self.display, (0, 0, 0), (self.width-30,5),(self.width-30,15), 2)

    def draw_timer(self, current_time, start_time):
        font = pygame.font.SysFont("Comicsans", 32)
        counting_time = current_time - start_time
        counting_seconds = str((counting_time)/1000).zfill(2)
        timer = font.render(f"Aika: {counting_seconds}",1,(0,0,0))
        self.display.blit(timer, (450,130))
        pygame.display.update()
