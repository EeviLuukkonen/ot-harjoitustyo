
def letter_positions(width, height):
    """Funktio, joka tallettaa kirjainnappien sijainnit

    Args:
        width (int): peliruudun leveys
        height (int): peliruudun korkeus

    Returns:
        Lista, jossa on kirjaimet, niiden sijainnit ja False-arvo (onko kirjain jo arvattu)
    """
    letters = []
    rad = 20
    gap = 15
    start_x = width - (14*rad+12*gap)
    start_y = height - 250
    for i in range(28):
        changing_x = start_x + (rad*2 + gap) * (i % 7)
        changing_y = start_y + i//7 * (gap+rad*2)
        if i <= 25:
            letters.append([changing_x, changing_y, chr(65+i), False])
        # letter ä
        elif i == 26:
            letters.append([changing_x, changing_y, chr(196), False])
        # letter ö
        elif i == 27:
            letters.append([changing_x, changing_y, chr(214), False])
    return letters
