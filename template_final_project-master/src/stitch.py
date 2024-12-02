import pygame
import json

class Stitch(pygame.sprite.Sprite):
    def __init__(self,image= f"/assets/single-crochet-circle.jpg"):
        super().__init__()
        self.image = pygame.image.load(f"/assets/single-crochet-x.jpg")
        self.rect = self.image.get_rect()
        self.rect.x = 0 
        self.rect.y = 0
        
    def add_stit(self,x,y):
        self.rect.x += 1 
        self.rect.y += 2
        #Connect to the buttons; use an if statement so it'll run one, two, or three  
    
    #Every time the player presses the button, it'll "add" and shift
    #the stitch in the "magic ring", then it'll come together at the end
        
    #How do I get the positioning for each stich? Has to correspond with the hook
    #Could you use two images in the class? 
    def save_state(self):
        yarn_state = self.__dict__
        fptr = open("assets/last_state.json", "w")
        json.dump(fptr, yarn_state)
        
    def load_state(self):
        fptr = open("assets/last_state.json")
        self.__dict__ = json.loads(fptr)