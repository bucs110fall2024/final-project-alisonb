import pygame
import json

class Yarn(pygame.sprite.Sprite):
    def __init__(self, image, x, y):
         super().__init__()
         #Need to figure out how to load an image (image yet to be loaded)
         self.image = pygame.image.load(f‘/assets/{name}.png’)
         self.rect = self.image.get_rect()
         self.rect.x = 0
         self.rect.y = 0
    
    def motion(self):
        pass
    #Need to integrate button with the hook; how do I make it look as if its moving?
    #I assume I need to use blitzing 
        
    def save_state(self):
        yarn_state = self.__dict__
        fptr = open("assets/last_state.json", "w")
        json.dump(fptr, yarn_state)
        
    def load_state(self):
        fptr = open("assets/last_state.json")
        self.__dict__ = json.loads(fptr)