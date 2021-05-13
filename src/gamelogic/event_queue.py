import pygame

class EventQueue:
    """Luokka, joka huomioi käyttäjän tapahtumat sovelluksen käytön aikana
    """
    def get(self):
        """Metodi, joka palauttaa pygamen tapahtuman

        Returns:
            Käyttäjän viimeisin tapahtuma pelissä
        """
        return pygame.event.get()
    def get_pos(self):
        """Metodi, joka palauttaa käyttäjän klikkauksen sijainnin peliruudulla

        Returns:
            Hiiren klikkauksen sijainti tuplena
        """
        return pygame.mouse.get_pos()
