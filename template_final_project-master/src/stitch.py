import pygame

class Stitch(pygame.sprite.Sprite):
    def __init__(self,image,x,y):
        super().__init__()
        self.image = pygame.image.load(f"/assets/single-crochet-x.png")
        self.rect = self.image.get_rect()
        self.x = x 
        self.y = y
        
    def add_stit(self,x,y):
        self.x += 1 
        self.y += 2
    
    #Every time the player presses the button, it'll "add" and shift
    #the stitch in the "magic ring", then it'll come together at the end
        
    #How do I get the positioning for each stich? Has to correspond with the hook
    #Could you use two images in the class? 