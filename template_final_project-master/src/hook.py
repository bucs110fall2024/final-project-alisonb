import pygame
import stitch

class Hook(pygame.sprite.Sprite):
    def __init__(self, image, x, y, stitch):
        super().__init__()
        self.image = pygame.image.load(f"/assets/hook-img.jpg")
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0

    def motion_with_stitch(self):
        pass
    #I'm confused as to how to link the hook and the stitch 


        
#Need to integrate button and yarn in the motion
# Yarn is an instance varibale of hook (so that they can move together); how would I do that?
#How is it moving?

#How do I show the crochet is being done? Am I thinking in 3D?