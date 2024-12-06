import pygame

class Hook(pygame.sprite.Sprite):
    def __init__(self, x = 800, y = 600, image = f"assets/hook-img.jpg"):
        super().__init__()
        self.image = pygame.image.load(image).convert_alpha()
        self.rect = self.image.get_rect()
        
        self.rect.x = x
        self.rect.y = y
        self.hook_moves = None

    def motion_with_stitch(self,x,y):
        self.rect.x, self.rect.y = x, y
    

#pass coordinates of the needle