import pygame

from line import constants


# прямоугольник, который будет двигаться по окружности
class Rect(object):

    color = constants.WHITE
    screen = None

    # координаты центра окружности относительно окна pygam
    center_x = None
    center_y = None

    height = None
    width = None


    def __init__(self, screen: pygame.Surface, center_x, center_y):
        self.screen = screen
        self.center_x = center_x
        self.center_y = center_y
        self.height = 30
        self.width = 30


    def draw(self):
        r = self.create_pygame_rect()
        pygame.draw.rect(self.screen, constants.RED, r)


    def create_pygame_rect(self):
        left = self.center_x - self.width/2
        top = self.center_y - self.height/2
        return pygame.Rect(left, top, self.width, self.height)


    def change_center_and_draw(self, point):
        self.center_x = point[0]
        self.center_y = point[1]
        self.draw()


    def change_center(self, point):
        self.center_x = point[0]
        self.center_y = point[1]