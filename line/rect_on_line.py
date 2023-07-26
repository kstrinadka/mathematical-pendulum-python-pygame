import pygame

from line import simple_line, constants, moving_rect
from line.pygame_moving_rect import PygameMovingRect


# прямоугольник, который движется по линии
class RectOnLine(object):
    movingRect = None
    color = constants.WHITE
    pygameRect = None
    line = None
    screen = None
    rectDirection = 1    # -1 => движется влево;  1 => движется вправо


    def __init__(self, line: simple_line.Line, screen: pygame.Surface):
        self.line = line
        self.screen = screen
        self.pygameRect = self.create_rect_on_line()


# создает квадрат исходя из линии
    def create_rect_on_line(self) -> PygameMovingRect:
        movingRect = moving_rect.MovingRect(self.line.firstPoint[0], self.line.firstPoint[1], 30, 30)
        pygameMovingRect = PygameMovingRect(movingRect, self.screen)
        #pygameMovingRect.pygameRect = pygameMovingRect.create_pygameRect(movingRect)
        return pygameMovingRect


#двигает квадрат по линии
    def move_and_draw(self):
        if self.rectDirection == 1:
            self.pygameRect.move_right_and_draw()

        if self.rectDirection == -1:
            self.pygameRect.move_left_and_draw()

        self.check_and_change_direction()
        self.draw()


# отрисовывает заново  квадрат и линию (типо оно сдвинулось и надо отрисовать)
    def draw(self):
        self.screen.fill(constants.BLACK)
        self.line.draw_line()
        self.pygameRect.draw_rect()


# проверяет нужно ли менять направление и меняет если нужно
    def check_and_change_direction(self):
        if self.pygameRect.movingRect.x_coordinate <= self.line.firstPoint[0] and self.rectDirection == -1:
            self.change_direction()

        if self.pygameRect.movingRect.x_coordinate >= self.line.secondPoint[0] and self.rectDirection == 1:
            self.change_direction()

# меняет направление квадратика
    def change_direction(self):

        if self.rectDirection == 1:
            self.rectDirection = -1
            print("Меняю направление")
            return
        if self.rectDirection == -1:
            self.rectDirection = 1
            print("Меняю направление")