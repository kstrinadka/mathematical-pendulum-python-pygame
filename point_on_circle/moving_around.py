import pygame

from point_on_circle import constants
from point_on_circle.circle import Circle
from point_on_circle.line import Line
from point_on_circle.rect import Rect


# Это система, которая связывает окружность и двужущийся по ней прямоугольник
# Тут есть сама окружность, прямоугольник и линия из центра окружности до прямоугольника
class CircleSystem(object):

    color = constants.WHITE
    screen = None

    # координаты центра окружности относительно окна pygame
    circle = None
    line = None
    rect = None

    speed = 200      # скорость движения по окружности
    angle = 0       # текущий угол на окружности


    def __init__(self, screen: pygame.Surface, radius: int):
        self.screen = screen
        self.init_system(radius)


# создаем изначальное положение объектов: окружность, квадрат, линия
    def init_system(self, radius: int):
        circle = Circle(self.screen, self.screen.get_width() / 2, self.screen.get_height() / 2, radius)
        self.circle = circle

        rect_coordinates = circle.get_pygame_coordinates_from_angle(0)
        rect = Rect(self.screen, rect_coordinates[0], rect_coordinates[1])
        self.rect = rect

        line = Line(self.screen, circle.center_x, circle.center_y, rect_coordinates[0], rect_coordinates[1])
        self.line = line


    def draw(self):
        self.screen.fill(constants.BLACK)
        self.circle.draw()
        self.rect.draw()
        self.line.draw()


# 1 сдвиг по окружности против часовой стрелки. Нужно переместить квадрат и линию немного по окружности
    def move_around_and_draw(self):
        delta_alpha = self.speed / self.circle.radius  #сдвиг угла за единицу времени с текущей скоростью
        new_angle = self.angle + delta_alpha
        self.angle = new_angle % 360
        new_coordinates = self.circle.get_pygame_coordinates_from_angle(new_angle)

        self.rect.change_center(new_coordinates)
        self.line.change_point(new_coordinates)
        self.draw()

