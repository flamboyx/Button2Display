from settings import *


class InputBox:
    def __init__(self, x, y, width, height, text=''):
        self.rect = pygame.Rect(x, y, width, height)
        
        self.color_inactive = pygame.Color("Gray")
        self.color_active = pygame.Color("White")
        self.color = self.color_inactive
        
        self.text = text
        
        self.text_surface = FONT.render(text, False, self.color)
        
        self.active = False
        
        self.done = False

    def check_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.active = not self.active
            else:
                self.active = False
            self.color = self.color_active if self.active else self.color_inactive
        if event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_RETURN:
                    self.done = True
                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode
                    
                self.text_surface = FONT.render(self.text, True, self.color)

    def update(self):
        width = max(200, self.text_surface.get_width() + 10)
        self.rect.w = width
        
    def draw(self, screen):
        screen.blit(self.text_surface, (self.rect.x, self.rect.y))
        pygame.draw.rect(screen, self.color, self.rect, 2)