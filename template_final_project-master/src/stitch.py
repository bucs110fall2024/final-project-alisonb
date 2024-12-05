import pygame

class Stitch(pygame.sprite.Sprite):
    def __init__(self, x, y, image = f"assets/single-crochet-circle.jpg"):
        super().__init__()
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = x,y

        
        
    def add_stit(self, image = f"assets/single-crochet-x.jpg", x = 1, y =2):
        """
        Moving the stitch by a 1 and 2 ixels in x and y directions.

        Args:
            offset_x (int): The number of pixels to move the sprite in the x direction.
            offset_y (int): The number of pixels to move the sprite in the y direction.
        """
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.rect.x += x
        self.rect.y += y  
            
    def move(self,x,y):
            self.rect.x = x
            self.rect.y = y
    
    #Every time the player presses the button, it'll "add" and shift
    #the stitch in the "magic ring", then it'll come together at the end
        