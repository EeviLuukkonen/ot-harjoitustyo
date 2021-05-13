from database_connection import get_database_connection

def drop_tables(connection):
    """Funktio, joka tyhjentää tietokannasta Highscores-taulun

    Args:
        connection: polku tietokantaan
    """
    cursor = connection.cursor()

    cursor.execute('''
        drop table if exists highscores;
    ''')

    connection.commit()

def create_tables(connection):
    """Funktio, joka luo taulun Highscores ja sille sarakkeet time ja level

    Args:
        connection: polku tietokantaan
    """
    cursor = connection.cursor()

    cursor.execute('''
        create table highscores (
            time int primary key,
            level int
        );
    ''')

    connection.commit()

def initialize_database():
    """Funktio, joka suorittaa tietokannan alustuksen
    """
    connection = get_database_connection()

    drop_tables(connection)
    create_tables(connection)

if __name__=="__main__":
    initialize_database()
