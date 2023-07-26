import math

import pygame

from pendulum.period_formulas import Huygens, ExactFormula
from point_on_circle import constants
from point_on_circle.circle import Circle
from point_on_circle.line import Line
from point_on_circle.rect import Rect


g = 9.8


# Это система, которая связывает окружность и двужущийся по ней прямоугольник
# Тут есть сама окружность, прямоугольник и линия из центра окружности до прямоугольника
class Pendulum(object):

    color = constants.WHITE
    screen = None

    # координаты центра окружности относительно окна pygame
    circle = None
    line = None
    rect = None
    speed = 0      # скорость движения по окружности
    angle_alpha = 0       # текущий угол на окружности
    new_fi_max = None     # максимальный угол отклонения в текущем колебании

    acceleration = None  # тангенциальное ускорение в текущий момент времени (отвечает за изменение скорости)
    friction_coefficient = None        # коэф трения
    time_step = None                   # шаг по времени

    huygens_formula = None             # формула Гюйгенса
    exact_formula = None               # точная формула


    def __init__(self, screen: pygame.Surface, radius: int, alpha_start, time_step: int, friction):
        self.screen = screen
        self.time_step = time_step
        self.friction_coefficient = friction
        self.init_system(radius, alpha_start)
        self.circle.radius = radius
        self.huygens_formula = Huygens(screen, radius)
        self.exact_formula = ExactFormula(screen, self.get_fi_angle(alpha_start), radius)
        self.new_fi_max = self.get_fi_angle(alpha_start)


# создаем изначальное положение объектов: окружность, квадрат, линия
    def init_system(self, radius: int, alpha_start):
        circle = Circle(self.screen, self.screen.get_width() / 2, self.screen.get_height() / 2, radius)
        self.circle = circle
        self.angle_alpha = alpha_start
        self.speed = 0
        rect_coordinates = circle.get_pygame_coordinates_from_angle(alpha_start)
        rect = Rect(self.screen, rect_coordinates[0], rect_coordinates[1])
        self.rect = rect
        line = Line(self.screen, circle.center_x, circle.center_y, rect_coordinates[0], rect_coordinates[1])
        self.line = line


    def draw(self):
        self.screen.fill(constants.BLACK)
        self.circle.draw()
        self.rect.draw()
        self.line.draw()
        self.huygens_formula.draw()
        self.calculate_new_period()
        self.exact_formula.draw()



    def get_amplitude(self, fi):
        return self.circle.radius * math.sin(math.radians(fi))



    def get_fi_angle(self, angle_alpha):
        if 270 <= angle_alpha <= 360:
            return angle_alpha - 270
        if 180 <= angle_alpha < 270:
            return 270 - angle_alpha
        if 0 <= angle_alpha < 180:
            print("Ошибка. Начальный угол должен быть до 90 градусов")
            return 0


# 1 сдвиг по окружности против часовой стрелки. Нужно переместить квадрат и линию немного по окружности
    def move_around_and_draw(self):

        self.change_speed()


        delta_alpha = self.speed / self.circle.radius  #сдвиг угла за единицу времени с текущей скоростью
        previous_angle = self.angle_alpha
        new_angle = self.angle_alpha + delta_alpha
        self.get_fi_max(self.get_fi_angle(new_angle))
        self.angle_alpha = new_angle % 360
        new_coordinates = self.circle.get_pygame_coordinates_from_angle(new_angle)

        self.rect.change_center(new_coordinates)
        self.line.change_point(new_coordinates)
        self.draw()


    # получаем максимальный угол отклонения на этом колебании
    def get_fi_max(self, angle):
        # проверяем что маятник достиг максимального угла
        if (angle < 2):
            self.new_fi_max = self.get_fi_angle(self.angle_alpha)



    def calculate_new_period(self):

        fi = self.get_fi_angle(self.angle_alpha)
        if (math.fabs(fi)) < 0.5:
            self.exact_formula.calculate_exact_formula(self.new_fi_max)


    def change_speed(self):
        self.angle_alpha = self.angle_alpha % 360
        fi = 0
        if 270 <= self.angle_alpha <= 360:
            fi = self.angle_alpha - 270
            self.acceleration = -g * math.sin(math.radians(fi))
            self.speed += self.acceleration * self.time_step

        if 180 <= self.angle_alpha < 270:
            fi = 270 - self.angle_alpha
            self.acceleration = g * math.sin(math.radians(fi))
            self.speed += self.acceleration  * self.time_step

        if 0 <= self.angle_alpha <= 90:
            fi = self.angle_alpha + 90
            self.acceleration = g * math.cos(math.radians(fi))
            self.speed += self.acceleration * self.time_step

        if 90 < self.angle_alpha < 180:
            fi = 90 + self.angle_alpha
            self.acceleration = -g * math.cos(math.radians(fi))
            self.speed += self.acceleration * self.time_step

        # это чтобы колебания затухли в конце
        if (-0.05 < self.speed < 0.05) and (math.fabs(self.acceleration)) < 0.05 and (fi < 1) and self.friction_coefficient > 0:
            self.speed = 0
        else:
            self.speed -= self.speed * self.friction_coefficient

    # создает маятник по умолчанию
    @staticmethod
    def create_default_pendulum(screen: pygame.Surface):
        pendulum = Pendulum(screen, 200, 330, 1, 0.001)
        return pendulum