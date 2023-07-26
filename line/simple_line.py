import pygame

from line import constants


class Line(object):


    firstPoint = None
    secondPoint = None
    movingRect = None
    color = constants.RED
    screen = None

    def __init__(self, screen: pygame.Surface, x1, y1, x2, y2):
        self.firstPoint = (x1, y1)
        self.secondPoint = (x2, y2)
        self.screen = screen


    def draw_line(self):
        pygame.draw.aaline(self.screen, self.color,
                           self.firstPoint, self.secondPoint)
