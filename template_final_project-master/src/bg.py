import pygame

class Bg():
    def __init__(self, image):
        self.w, self.h = pygame.display.get_window_size()
        self.hit_box_width = self.w/ 2
        self.hit_box_height = self.h / 2
        self.hitbox = pygame.rect(0, 0, self.hit_box_width, self.hit_box_height)
        self.image = (f"assets/ballyarnbk.jpg")
        self.rect = self.image.load(f"assets/ballyarnbk.jpg")
