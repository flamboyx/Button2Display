from settings import *
from button import Button
from input_box import InputBox


class Window:
    def __init__(self):
        pygame.init()

        self.running = True
        self.down = 0

        self.window = pygame.display.set_mode((WIDTH // 3, HEIGHT // 2))
        self.width = self.window.get_width()
        self.height = self.window.get_height()

        self.button = Button((self.width - 300) // 2, self.height // 2)

        self.sound = pygame.mixer.Sound("sounds/lever.ogg")
        
        self.font = FONT
        self.host_text = self.font.render("Host:", False, "White")
        self.port_text = self.font.render("Port:", False, "White")
        
        self.input_box1 = InputBox((self.width - 150) // 2, self.height // 3, 150, 30)
        self.input_box2 = InputBox((self.width - 150) // 2, self.height * 2 // 3, 150, 30)
        self.input_boxes = [self.input_box1, self.input_box2]
        
        self.done = False

        self.clock = pygame.time.Clock()

        pygame.display.set_caption("Client")

    def run(self):
        self.window.fill("Black")
        self.window.blit(self.button.image, self.button.rect)
        
        pygame.display.update()
        self.clock.tick(FPS)

        mouse_pos = pygame.mouse.get_pos()
        mouse_pressed = pygame.mouse.get_pressed()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False
            elif self.button.is_pressed(mouse_pos, mouse_pressed):
                if event.type == pygame.MOUSEBUTTONUP:
                    self.sound.play()
                    if self.down == 0:
                        self.down = 1
                    else:
                        self.down = 0
                        
    def connect(self):
        self.window.fill("Black")
        self.window.blit(self.host_text, ((self.width - 150) // 2 - self.width // 10,
                                          self.height // 3 - self.height // 20))
        self.window.blit(self.port_text, ((self.width - 150) // 2 - self.width // 10,
                                          self.height * 2 // 3 - self.height // 20))
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.done = True
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                   self.done = True
                   self.running = False
            for box in self.input_boxes:
                box.check_event(event)
                
        
            
        for box in self.input_boxes:
            box.update()
            box.draw(self.window)
            
        if self.input_boxes[0].done and self.input_boxes[1].done:
            self.host = self.input_boxes[0].text
            self.port = int(self.input_boxes[1].text)
            self.done = True
        
        pygame.display.update()
        self.clock.tick(FPS)
        
        