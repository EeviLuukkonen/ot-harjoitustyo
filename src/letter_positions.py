
def letter_positions(width, height):
    letters = [] # [x, y, letter, used (True/False)]
    rad = 20
    gap = 15
    startx = width - (14*rad+12*gap)
    starty = height - 250
    for i in range(28):
        x =startx+ (rad*2 + gap) * (i%7)
        y =starty+ i//7 * (gap+rad*2)
        if i <=25:
            letters.append([x,y,chr(65+i), False])
        elif i == 26:
            letters.append([x,y,chr(196), False])
        elif i == 27:
            letters.append([x,y,chr(214), False])
         
    return letters