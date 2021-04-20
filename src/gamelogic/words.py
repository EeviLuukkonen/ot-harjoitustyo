import random


def words(level: int):
    if level == 0:
        return random.choice(["KESÄ", "MAJA", "VILTTI", "TAULU"])
    elif level == 1:
        return random.choice(["KESÄLOMA", "MAJAKKA", "VILLATAKKI", "MITTARI"])
    elif level == 2:
        return random.choice(["XYLOFONI", "FILOSOFINEN", "TIETOJENKÄSITTELY", ])
