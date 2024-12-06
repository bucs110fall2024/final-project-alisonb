import pygame
from src.stitch import Stitch

class Hook(pygame.sprite.Sprite):
    def __init__(self, image = f"assets/hook-img.jpg"):
        super().__init__()
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.rect.x = 680
        self.rect.y = 480
        self.hook_moves = None

    def motion_with_stitch(self,stitch_sprite):
            self.rect.x = stitch_sprite.rect.x
            self.rect.y = stitch_sprite.rect.y
    



#pass coordinates of the needle

#Should the needle know where the stitch is? (Either in the control or as a method); how would I pass the coordinates
#https://www.pygame.org/docs/ref/sprite.html