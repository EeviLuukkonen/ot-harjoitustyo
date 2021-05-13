class Highscore():
    """Luokka, joka toteuttaa sovelluksen tietokannan toiminnallisuuden
    """
    def __init__(self, connection):
        """Konstruktori

        Args:
            connection: Polku tietokantaan
        """
        self._connection = connection

    def create(self, time, level):
        """Metodi, joka luo tietokantaan taulun highscores.

        Args:
            time: pelissä kulunut aika
            level: taso
        """
        cursor = self._connection.cursor()

        cursor.execute(
            'insert into highscores (time, level) values (?, ?)',
            (time,level)
        )

        self._connection.commit()

    def find_all(self):
        """Medodi, joka löytää tietokannasta viisi parasta tulosta paremmuusjärjestyksessä.

        Returns:
            Enintään viisi nopeinta riviä tietokannasta highscores
        """
        cursor = self._connection.cursor()

        cursor.execute('select * from highscores order by time limit 5')

        rows = cursor.fetchall()

        return rows
