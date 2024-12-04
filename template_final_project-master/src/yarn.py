import pygame
import json

class Yarn():
    def __init__(self, image, x, y):
         super().__init__()
         self.image = pygame.image.load(f"/assets/ball-of-yarn.png")
         self.rect = self.image.get_rect()
         self.rect.x = 0
         self.rect.y = 0



#Just make it into the background (make it into a surface)