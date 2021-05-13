import os
import sqlite3
from config import SCORES_FILEPATH

connection = sqlite3.connect(SCORES_FILEPATH)
connection.row_factory = sqlite3.Row

def get_database_connection():
    return connection
