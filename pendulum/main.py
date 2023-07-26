

# Pygame шаблон - скелет для нового проекта Pygame
import pygame

from pendulum.input_menu import InputBox, OkBox
from pendulum.math_pendulum import Pendulum
from point_on_circle import constants


def show_field_description(text: str, x: int, y: int):
    font = pygame.font.SysFont(None, 24)
    img = font.render(text, True, constants.RED)
    screen.blit(img, (x, y))
    # pygame.display.update()
    return img

def is_digit(string):
    if string.isdigit():
       return True
    else:
        try:
            float(string)
            return True
        except ValueError:
            return False



# Создаем игру и окно
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((constants.WIDTH, constants.HEIGHT))
pygame.display.set_caption("My Game")
clock = pygame.time.Clock()


# это угол на тригонометрической окружности по часовой стрелке от оси x
# типо если хотим чтобы начальная фаза была в 4 четверти, то угол указывам от 270 до 360
start_angle = 330
time_step = 1       # шаг по времени
friction = 0.001    # коэф трения
radius = 200        # длина нити маятника

circle_system = Pendulum(screen, radius, start_angle, time_step, friction)
# circle_system.draw()

clock = pygame.time.Clock()
input_box1 = InputBox(100, 100, 140, 32)
input_box2 = InputBox(100, 300, 140, 32)
input_box3 = InputBox(100, 500, 140, 32)
input_box4 = InputBox(100, 700, 140, 32)
ok_button = OkBox(500, 400, 140, 32)
input_boxes = [input_box1, input_box2, input_box3, input_box4, ok_button]
done = False

text1 = ""
text2 = ""
text3 = ""
text4 = ""


while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or ok_button.button_pressed == True:
            text1 = input_box1.text
            text2 = input_box2.text
            text3 = input_box3.text
            text4 = input_box4.text
            done = True
        for box in input_boxes:
            box.handle_event(event)
    for box in input_boxes:
        box.update()
    screen.fill((30, 30, 30))
    show_field_description("> start phase <", 145, 80)
    show_field_description("> time_step <", 145, 280)
    show_field_description("> friction_coefficient <", 120, 480)
    show_field_description("> radius <", 150, 680)
    show_field_description("> OK <", 570, 410)
    for box in input_boxes:
        box.draw(screen)
    pygame.display.flip()
    clock.tick(30)


circle_system = None

if is_digit(text1) and is_digit(text2) and is_digit(text3) and is_digit(text4):
    start_angle_text_field = float(text1) + 270 # поле для ввода начальной фазы
    time_step_text_field = float(text2)  # поле для ввода шага по времени
    friction_text_field = float(text3)  # поле для ввода коэффициента трения
    radius_text_field = float(text4)    # длина нити
    circle_system = Pendulum(screen, radius_text_field, start_angle_text_field, time_step_text_field, friction_text_field)
    print("new pendulum")
    circle_system.draw()
else:
    circle_system = Pendulum.create_default_pendulum(screen)

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