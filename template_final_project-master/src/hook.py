import pygame
import yarn

class Hook(pygame.sprite.Sprite):
    def __init__(self, image, x, y, var):
        super().__init__()
        #Need to figure out how to upload image
        self.image = pygame.image.load(f‘/assets/{name}.png’)
		self.rect = self.image.get_rect()
		self.rect.x = 0
		self.rect.y = 0
        self.var = yarn.motion()


    def move_with_yarn(self):
        pass 


        
#Need to integrate button and yarn in the motion
# Yarn is an instance varibale of hook (so that they can move together); how would I do that?
#How is it moving?

#How do I show the crochet is being done? Am I thinking in 3D?