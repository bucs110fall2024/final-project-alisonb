import pygame

class Stitch(pygame.sprite.Sprite):
    def __init__(self, x , y , image = f"assets/single-crochet-circle.jpg"):
        super().__init__()
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = x,y
 
        #Make x and y coincide with the string of yarn
    def other_stit(self, x, y, image = f"assets/single-crochet-x.jpg"):
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = x -5,y -5
        
            
    def move(self,x,y):
            self.rect.x = x
            self.rect.y = y
    
    #Every time the player presses the button, it'll "add" and move
    #the stitch in the "magic ring", then it'll come together at the end
        
    #Make it move 5 to the x, 1 to y 