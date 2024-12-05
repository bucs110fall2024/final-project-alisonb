import pygame
from src.stitch import Stitch

class Hook(pygame.sprite.Sprite):
    def __init__(self, image, x, y):
        super().__init__()
        self.image = pygame.image.load(f"/assets/hook-img.jpg")
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        hook_moves = None

    def motion_with_stitch(self):
        pass
    #I'm confused as to how to link the hook and the stitch 


#Need to integrate button and yarn in the motion

#pass coordinates of the needle

#Should the needle know where the stitch is? (Either in the control or as a method); how would I pass the coordinates
#https://www.pygame.org/docs/ref/sprite.html