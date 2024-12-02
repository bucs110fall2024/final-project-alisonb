import pygame

class Stitch(pygame.sprite.Sprite):
    def __init__(self,image= f"/assets/single-crochet-circle.jpg"):
        super().__init__()
        self.image = pygame.image.load(f"/assets/single-crochet-x.jpg")
        self.rect = self.image.get_rect()
        self.rect.x = 0 
        self.rect.y = 0
        is_added = None   
        
    def add_stit(self):
        if self.is_added:
            self.rect.x += 1
            self.rect.y += 2  
    
    #Every time the player presses the button, it'll "add" and shift
    #the stitch in the "magic ring", then it'll come together at the end
        