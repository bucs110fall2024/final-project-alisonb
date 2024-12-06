import pygame

class Stitch(pygame.sprite.Sprite):
    def __init__(self, x , y , image = f"assets/single-crochet-circle.jpg"):
        super().__init__()
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = x,y