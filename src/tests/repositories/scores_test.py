from sqlite3.dbapi2 import connect
import unittest
from repositories.highscores import Highscore
from database_connection import get_database_connection
from build import pytest_configure

class TestScores(unittest.TestCase):
    def setUp(self):
        connection = get_database_connection()
        pytest_configure()
        self.scores = Highscore(connection)
    def test_create(self):
        self.scores.create(12,"helppo")
        highscores = self.scores.find_all()

        self.assertEqual(len(highscores), 1)
        self.assertEqual(highscores[0]["time"], 12)
