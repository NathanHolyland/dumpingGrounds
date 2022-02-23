import pygame
from random import randint

class Button:
    def __init__(self, bgColor, texture, rect, toggleable):
        font = pygame.font.SysFont('Comic Sans MS', 30)
        self.texture = texture
        self.color = bgColor
        self.rect = rect
        self.toggleable = toggleable
        self.state = False
        self.visible = True

    def draw(self, surface):
        if self.visible:
            pygame.draw.rect(surface, self.color, self.rect, 0)
            surface.blit(self.texture, (self.rect[0], self.rect[1]))

    def check(self, mousePos):
        x, y, w, h = self.rect
        if self.visible:
            if (x <= mousePos[0] <= x+w) and (y <= mousePos[1] <= y+h):
                if self.toggleable:
                    self.state = not self.state
                else:
                    return True
        return self.state

def checkButtons(buttons, mousePos):
    event_list = {}
    for button in buttons:
        event_list[button] = button.check(mousePos)
    return event_list

screen = pygame.display.set_mode([500, 500])
pygame.font.init()
comic = pygame.font.SysFont("Comic Sans MS", 30)
b1 = Button((255, 0, 0), comic.render("Hello", False, (0, 0, 0)), [50, 50, 60, 20], False)
b2 = Button((0, 0, 255), comic.render("Visibility", False, (0, 0, 0)), [50, 70, 100, 20], True)
bList = [b1,b2]
running = True
while running:
    screen.fill((0,0,0))
    b1.draw(screen)
    b2.draw(screen)
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            button_events = checkButtons(bList, pygame.mouse.get_pos())
            if button_events[b1]:
                colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255)]
                b1.color = colors[randint(0, 2)]
                b1.visible = False
            b1.visible = button_events[b2]


        
        if event.type == pygame.QUIT:
            running = False
pygame.quit()