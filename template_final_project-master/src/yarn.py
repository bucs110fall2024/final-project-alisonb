import pygame
import json

class Yarn(pygame.sprite.Sprite):
    def __init__(self, image, x, y):
         super().__init__()
         self.image = pygame.image.load(f"/assets/ball-of-yarn.png")
         self.rect = self.image.get_rect()
         self.rect.x = 0
         self.rect.y = 0

#The yarn ball is an image (as of right now, its stationary)