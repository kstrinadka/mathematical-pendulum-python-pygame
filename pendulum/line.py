import pygame

from point_on_circle import constants


class Line(object):

#координаты центра окружности
    center_x = None
    center_y = None
    center = None

#координаты точки на окружности
    point_x = None
    point_y = None
    point = None

    color = constants.BLUE
    screen = None

    def __init__(self, screen: pygame.Surface, center_x, center_y, point_x, point_y):
        self.center_x = center_x
        self.center_y = center_y
        self.center = (center_x, center_y)
        self.point_x = point_x
        self.point_y = point_y
        self.point = (point_x, point_y)
        self.screen = screen


#рисует линию
    def draw(self):
        pygame.draw.aaline(self.screen, self.color,
                           self.center, self.point)


#рисует линию к точке, после смены положения
    def change_point_and_draw(self, point):
        self.point = point
        self.draw()


    def change_point(self, point):
        self.point = point