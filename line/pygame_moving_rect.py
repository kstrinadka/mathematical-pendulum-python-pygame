import pygame

from line import moving_rect, constants


class PygameMovingRect(object):
    movingRect = None
    color = constants.WHITE
    pygameRect = None
    screen = None

    def __init__(self, movingRect: moving_rect.MovingRect, screen: pygame.Surface):
        self.movingRect = movingRect
        self.screen = screen
        self.pygameRect = self.create_pygameRect(movingRect)

    def draw_rect(self):
        pygame.draw.rect(self.screen, self.color, self.pygameRect, 0)

    def move_right_and_draw(self):
        self.movingRect.move_right()
        self.pygameRect = self.create_pygameRect(self.movingRect)
        self.screen.fill(constants.BLACK)
        self.draw_rect()

    def move_left_and_draw(self):
        self.movingRect.move_left()
        self.pygameRect = self.create_pygameRect(self.movingRect)
        self.screen.fill(constants.BLACK)
        self.draw_rect()

    @staticmethod
    def create_pygameRect(movingRect: moving_rect.MovingRect):
        left = movingRect.x_coordinate - movingRect.width / 2
        top = movingRect.y_coordinate - movingRect.height / 2
        return pygame.Rect(left, top, movingRect.width, movingRect.height)

    @staticmethod
    def create_default_rect(screen: pygame.Surface):
        movingRect = moving_rect.MovingRect(screen.get_width() / 2, screen.get_height() / 2, 30, 30)
        pygameMovingRect = PygameMovingRect(movingRect, screen)
        pygameMovingRect.pygameRect = pygameMovingRect.create_pygameRect(movingRect)
        return pygameMovingRect
