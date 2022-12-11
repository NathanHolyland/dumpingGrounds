import pygame

## this UI elements module is dependent on the usage of an "event handler" for the buttons

class Frame:
    def __init__(self, rect, parent:object=None, visible=False):
        self.rect = rect
        self.parent = parent
        self.children = []
        self.visible = visible
        if not (self.parent is None):
            self.parent.addChild(self)

    def drawChildren(self, screen):
        for child in self.children:
            child.draw(screen)

    def draw(self, screen:pygame.display):
        screen_coords = self.getScreenCoords()
        if self.visible:
            pygame.draw.rect(screen, (0, 0, 0), [screen_coords[0], screen_coords[1], self.rect[2], self.rect[3]], 1)
        self.drawChildren(screen)
    
    def addChild(self, x:object):
        self.children.append(x)
    
    def getRelativeCoords(self): # coordinates without respect to parent
        return [self.rect[0], self.rect[1]]
    
    def getScreenCoords(self):
        if self.parent is None:
            return self.getRelativeCoords()
        parentScreenCoords = self.parent.getScreenCoords()
        return [self.rect[0]+parentScreenCoords[0], self.rect[1]+parentScreenCoords[1]]
    
    def setRelativeCoords(self, x):
        rect = [x[0], x[1], self.rect[2], self.rect[3]]
        self.rect = rect
    
    def setScreenCoords(self, x):
        if self.parent is not None:
            parentScreenCoords = self.parent.getScreenCoords()
        else:
            parentScreenCoords = [0, 0]
        
        vec = [x[0]-parentScreenCoords[0], x[1]-parentScreenCoords[1]]
        rect = [vec[0], vec[1], self.rect[2], self.rect[3]]
        self.rect = rect
    
    def setSize(self, x):
        rect = [self.rect[0], self.rect[1], x[0], x[1]]
        self.rect = rect

class Label(Frame):
    def __init__(self, rect, Parent, bg_color, texture=None, width:int=0, visible=True):
        self.texture = texture
        if texture is not None:
            transformedTexture = pygame.transform.scale(texture, [rect[2], rect[3]])
            self.texture = transformedTexture
        self.bg_color = bg_color
        self.width = width
        self.visible = visible

        super().__init__(rect, Parent)
    
    # overrides parent function
    def draw(self, screen:pygame.display):
        screen_coords = self.getScreenCoords()
        pygame.draw.rect(screen, self.bg_color, [screen_coords[0], screen_coords[1], self.rect[2], self.rect[3]], self.width)
        if self.texture is not None:
            screen.blit(self.texture, [screen_coords[0], screen_coords[1], self.rect[2], self.rect[3]])
        self.drawChildren(screen)

class Button(Label):
    def __init__(self, rect, Parent, bg_color, eventHandler, flagName, texture=None, visible=True, toggleable=False, ignoreRepeats=True, width:int=0, defaultData=[]):
        self.defaultData = defaultData
        self.name = flagName
        self.eventHandler = eventHandler
        self.toggleable = toggleable
        self.ignoreRepeats = ignoreRepeats
        if self.ignoreRepeats:
            self.clicked = False
        if self.toggleable:
            self.state = False

        super().__init__(rect, Parent, bg_color, texture, width, visible)

    # do this every frame
    def tick(self):
        if not self.toggleable:
            return
        if self.state:
            self.eventHandler.triggerFlag(self.name, self.passedData)

    # do this for every frame the mouse is held down
    def attemptTrigger(self, mouse_vec, data=None):
        passedData = data
        if data is None:
            passedData = self.defaultData

        if self.validateBounds(mouse_vec):
            if self.ignoreRepeats:
                if self.clicked:
                    return
                self.clicked = True # prevent repeats on the same button press

            if self.toggleable:
                self.state = not self.state 
                self.passedData = passedData # remember what data was passed for future calls
            
            self.eventHandler.triggerFlag(self.name, passedData) # data can be empty
                

    def reset(self): # call this when the mouse is released
        if self.ignoreRepeats:
            self.clicked = False

    def setState(self, new_state:bool):
        self.state = new_state

    def validateBounds(self, vec):
        screen_coords = self.getScreenCoords()
        screen_rect = [screen_coords[0], screen_coords[1], screen_coords[0]+self.rect[2], screen_coords[1]+self.rect[3]]
        if (screen_rect[0] <= vec[0] <= screen_rect[2]) and (screen_rect[1] <= vec[1] <= screen_rect[3]):
            return True
        return False