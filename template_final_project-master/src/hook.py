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
        """
        description: Updates the position of the hook (in relation to the stitches; in the controller)
        argument: x (takes an integer) and y (takes an integer) as its new coordinates
        return: None
        """
        self.rect.x, self.rect.y = x, y