import pygame

class Button(pygame.sprite.Sprite): 
    def __init__(self, x, y, width=75, height=75, color=(200, 0, 200), text = ""):
        super().__init__()
        self.image = pygame.Surface((width, height))
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = x, y #The position is given by rect
        self.color = color
        self.image.fill(self.color)