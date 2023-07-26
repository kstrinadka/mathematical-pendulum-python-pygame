import math

import pygame

from pendulum import constants


g = 9.8
pygame.init()
FONT = pygame.font.Font(pygame.font.get_default_font(), 20)


# класс для вывода формулы Гюйгенса на экран
class Huygens(object):

    #значение формулы Гюйгенса
    huygens_value = None

    # текст, который будет выводиться на экран
    result_string = None
    pygame_text = None

    # длина нити
    l = None

    color = constants.WHITE
    screen = None

    #координаты текста на экране
    x = 10
    y = 650


    def __init__(self, screen: pygame.Surface, l):
        self.l = l / 100
        self.screen = screen
        self.result_string = self.get_result_string()
        self.pygame_text = FONT.render(self.result_string, True, self.color)


    def calculate_huygens_formula(self):
        self.huygens_value = 2 * math.pi * math.sqrt(self.l / g)
        return self.huygens_value


    def get_result_string(self):
        self.result_string = f'Huygens formula: T = {self.huygens_value}'
        return self.result_string


    def draw(self):
        self.calculate_huygens_formula()
        self.result_string = self.get_result_string()
        self.pygame_text = FONT.render(self.result_string, True, self.color)
        self.screen.blit(self.pygame_text, (self.x, self.y))


# класс для вывода точной формулы на экран
class ExactFormula(object):

    # значение точной формулы
    exact_value = None

    # текст, который будет выводиться на экран
    result_string = None
    pygame_text = None

    # длина нити
    l = None

    # начальный угол
    fi_0 = None

    color = constants.WHITE
    screen = None

    # координаты текста на экране
    x = 10
    y = 700

    def __init__(self, screen: pygame.Surface, fi_0, l):
        self.fi_0 = fi_0
        self.l = l /100
        self.screen = screen
        self.result_string = self.get_result_string()
        self.pygame_text = FONT.render(self.result_string, True, self.color)

    # считает полный эллиптический интеграл первого рода
    def ceil(self, k):
        t = 1 - (k * k)
        a = (((0.01451196212 * t + 0.03742563713) * t + 0.03590092383) * t + 0.09666344259) * t + 1.38629436112
        b = (((0.00441787012 * t + 0.03328355346) * t + 0.06880248576) * t + 0.12498593597) * t + 0.5
        return (a - b * math.log(t))


    def calculate_exact_formula(self, fi_0):
        self.fi_0 = fi_0
        self.exact_value = 4 * math.sqrt(self.l / g) * self.ceil(math.sin(math.radians(self.fi_0) / 2))
        return self.exact_value


    def get_result_string(self):
        self.result_string = f'Exact formula: T = {self.exact_value}'
        return self.result_string

    def draw(self):
        self.result_string = self.get_result_string()
        self.pygame_text = FONT.render(self.result_string, True, self.color)
        self.screen.blit(self.pygame_text, (self.x, self.y))