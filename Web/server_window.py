from settings import *


class Window:
    def __init__(self, text):
        pygame.init()

        self.running = True
        self.light = 0
        self.changed = False

        self.window = pygame.display.set_mode((WIDTH // 3, HEIGHT // 2))
        self.width = self.window.get_width()
        self.height = self.window.get_height()
        
        self.font = FONT
        self.text = self.font.render(text, False, "White")
        
        self.clock = pygame.time.Clock()
        
        self.lamp = [pygame.image.load("images/lamp0.png").convert_alpha(),
                     pygame.image.load("images/lamp1.png").convert_alpha()]
        
        self.lamp_sounds = [pygame.mixer.Sound("sounds/lamp0.ogg"),
                            pygame.mixer.Sound("sounds/lamp1.ogg")]
        
        pygame.display.set_caption("Server")

    def run(self):
        self.window.fill("Black")
        self.window.blit(self.text, (0, 0))
        
        if self.light:
            self.window.blit(self.lamp[self.light], ((self.width - 500) // 2,
                                                 (self.height - 500) // 2))
        else:
            self.window.blit(self.lamp[self.light], ((self.width - 300) // 2,
                                                 (self.height - 300) // 2))
        
        if self.changed:
            self.lamp_sounds[self.light].play()
            self.changed = False
            
        pygame.display.update()
        self.clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False