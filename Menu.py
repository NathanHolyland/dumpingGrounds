import pygame

class Button:
    def __init__(self, color, rect, function, toggleable, *args):
        self.color = color
        self.rect = rect
        self.action = function
        self.args = args
        self.toggleable = toggleable
        self.state = False
        
    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect, 0)

    def update(self):
        if self.state:
            self.action(*self.args)
        if not self.toggleable:
            self.state = False

    def check(self, mousePos):
        x, y, w, h = self.rect
        if (x <= mousePos[0] <= x+w) and (y <= mousePos[1] <= y+h):
            if self.toggleable:
                self.state = not self.state
            else:
                self.state = True

def add(*args):
    total = 0
    for item in args:
        total += item
    print(total)

screen = pygame.display.set_mode([500, 500])
b1 = Button((255, 0, 0), [50, 50, 20, 20], add, True, 5, 2, 6, 1051)

running = True
while running:
    b1.draw(screen)
    pygame.display.flip()

    b1.update()

    mousePos = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            b1.check(mousePos)
        
        if event.type == pygame.QUIT:
            running = False
pygame.quit()