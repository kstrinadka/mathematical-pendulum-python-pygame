

class MovingRect(object):
    x_coordinate = 0
    y_coordinate = 0
    height = 0
    width = 0
    direction = -1 #  -1 => движется влево;  1 => движется вправо

    def __init__(self, x, y, height, width):
        self.x_coordinate = x
        self.y_coordinate = y
        self.height = height
        self.width = width


    def move_right(self):
        self.x_coordinate += 5


    def move_left(self):
        self.x_coordinate -= 5


    def method1(self, x):
        return 2*x