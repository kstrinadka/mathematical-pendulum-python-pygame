

# Pygame шаблон - скелет для нового проекта Pygame
import pygame
from line import simple_line, rect_on_line, constants
from line.pygame_moving_rect import PygameMovingRect


# Создаем игру и окно
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((constants.WIDTH, constants.HEIGHT))
pygame.display.set_caption("My Game")
clock = pygame.time.Clock()


simpleLine = simple_line.Line(screen, 30, screen.get_height()/2, screen.get_width() - 30, screen.get_height()/2)
rectOnLine = rect_on_line.RectOnLine(simpleLine, screen)
rectOnLine.draw()

# pygameMovingRect = PygameMovingRect.create_default_rect(screen)
# pygameMovingRect.draw_rect()



# Цикл игры
running = True
while running:
    # Держим цикл на правильной скорости
    clock.tick(constants.FPS)
    # pygameMovingRect.move_right_and_draw()
    rectOnLine.move_and_draw()

    # Ввод процесса (события)
    for event in pygame.event.get():
        # check for closing window
        if event.type == pygame.QUIT:
            running = False
    pygame.display.update()

pygame.quit()