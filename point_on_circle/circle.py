import math

import pygame

from line import constants


# Окружность
class Circle(object):

    color = constants.WHITE
    screen = None

    # координаты центра окружности относительно окна pygame
    center_x = None
    center_y = None

    radius = None


    def __init__(self, screen: pygame.Surface, center_x, center_y, radius):
        self.screen = screen
        self.radius = radius
        self.center_x = center_x
        self.center_y = center_y


    def draw(self):
        pygame.draw.circle(self.screen, constants.WHITE, (self.center_x, self.center_y), self.radius)
        pygame.draw.circle(self.screen, constants.BLACK, (self.center_x, self.center_y), self.radius-10)


# получаем координаты относительно центра окружности (оси направлены как в pygame)
    def get_circle_coordinates(self, coord: list):
        circle_coordinates = []
        circle_coordinates.append(coord[0] - self.center_x)
        circle_coordinates.append(coord[1] - self.center_y)
        return circle_coordinates


# получаем pygame координаты из координат относительно окружности
    def get_pygame_coordinates_from_circle(self, circle_coordinates: list):
        pygame_coordinates = []
        pygame_coordinates.append(circle_coordinates[0] + self.center_x)
        pygame_coordinates.append(circle_coordinates[1] + self.center_y)
        return  pygame_coordinates


# получить координаты на окружности в зависимости от угла
# тут в зависимости от четверти на окружности нужно будет прибавлять или отнимать координаты от центра
    def get_pygame_coordinates_from_angle(self, angle):
        x_coord = y_coord = 0

        if 0 <= angle <= 90:
            radians = math.radians(angle)
            x_coord = self.center_x + (self.radius * math.cos(radians))
            y_coord = self.center_y - (self.radius * math.sin(radians))

        if 90 < angle <= 180:
            angle = angle - 90
            radians = math.radians(angle)
            x_coord = self.center_x - (self.radius * math.sin(radians))
            y_coord = self.center_y - (self.radius * math.cos(radians))

        if 180 < angle <= 270:
            angle = angle - 180
            radians = math.radians(angle)
            x_coord = self.center_x - (self.radius * math.cos(radians))
            y_coord = self.center_y + (self.radius * math.sin(radians))

        if 270 < angle <= 360:
            angle = angle - 270
            radians = math.radians(angle)
            x_coord = self.center_x + (self.radius * math.sin(radians))
            y_coord = self.center_y + (self.radius * math.cos(radians))

        pygame_coordinates = []
        pygame_coordinates.append(x_coord)
        pygame_coordinates.append(y_coord)
        return pygame_coordinates