from settings import *


class Button:
    def __init__(self, x, y):
        self.on = 0

        self.x = x
        self.y = y

        self.lever = [pygame.image.load("images/lever0.png").convert_alpha(),
                      pygame.image.load("images/lever1.png").convert_alpha()]

        self.image = self.lever[self.on]

        self.rect = self.image.get_rect()

    def is_pressed(self, pos, pressed):
        if self.rect.collidepoint(pos):
            if pressed[0]:
                if self.on == 0:
                    self.on = 1
                    self.image = self.lever[1]
                else:
                    self.on = 0
                    self.image = self.lever[0]
                return True
            return False
        return False