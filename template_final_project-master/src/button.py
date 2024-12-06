import pygame

class Button(pygame.sprite.Sprite): 
    def __init__(self, x, y, width=75, height=75, color=(200, 0, 200), text= "Press"):
        super().__init__()
        self.image = pygame.Surface((width, height))
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = x, y #The position is given by rect
        self.color = color
        self.image.fill(self.color)
        
        text_color = (255-color[0], 255-color[1], 255-color[2]) #complimentary color
        self.message = pygame.font.SysFont(None, 36).render(text, True, text_color)
        
        self.image.blit(self.message, (20, 20))

    def highlight(self):
        highlight_color = []
        for i, c in enumerate(self.color):
            if c+50 < 255:
                highlight_color.append(c+50) 
            else:
                highlight_color.append(255)
        self.image.fill(highlight_color)
        self.image.blit(self.message, (20, 20))

    def color_default(self):
        self.image.fill(self.color)
        self.image.blit(self.message, (20, 20))
        