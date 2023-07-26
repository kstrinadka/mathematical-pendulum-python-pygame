

# Pygame шаблон - скелет для нового проекта Pygame
import pygame
from point_on_circle import constants
from point_on_circle.circle import Circle
from point_on_circle.line import Line
from point_on_circle.moving_around import CircleSystem
from point_on_circle.rect import Rect

# Создаем игру и окно
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((constants.WIDTH, constants.HEIGHT))
pygame.display.set_caption("My Game")
clock = pygame.time.Clock()



# pygameMovingRect = PygameMovingRect.create_default_rect(screen)
# pygameMovingRect.draw_rect()

radius = 200
circle = Circle(screen, screen.get_width()/2, screen.get_height()/2, radius)
circle.draw()


# рисую квадрат на окружности
circle_system = CircleSystem(screen, 200)
circle_system.draw()



# Цикл игры
running = True
while running:
    # Держим цикл на правильной скорости
    clock.tick(constants.FPS)

    circle_system.move_around_and_draw()

    # Ввод процесса (события)
    for event in pygame.event.get():
        # check for closing window
        if event.type == pygame.QUIT:
            running = False
    pygame.display.update()

pygame.quit()