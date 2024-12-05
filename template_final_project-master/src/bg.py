import pygame

class Bg():
    def __init__(self):
        self.w, self.h = pygame.display.get_window_size()
        self.hit_box_width = self.w/ 2
        self.hit_box_height = self.h / 2
        self.hitbox = pygame.rect(0, 0, self.hit_box_width, self.hit_box_height)
       
