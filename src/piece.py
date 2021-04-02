from shapes import Shapes

class Piece():
    def __init__(self, column, row, shape):
        self.x = column
        self.y = row
        self.shape = shape
        self.color = Shapes.colours[Shapes.shapes.index(shape)]
        self.rotation = 0