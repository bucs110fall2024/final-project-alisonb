import pygame
import pygame_menu
from src.button import Button
from src.hook import Hook
from src.stitch import Stitch

class Controller:
  
  def __init__(self):
    #setup pygame data
    pygame.init()
    pygame.event.pump()
    self.screen = pygame.display.set_mode((800,600))
    self.width, self.height = pygame.display.get_window_size()
    
    #Models
    self.magic_ring = Button(x = 400, y = 100, text = "MR")
    self.chain_one = Button(x = 500, y = 100, text = "Chain 1") 
    self.double_stitch = Button(x = 600, y = 100, text = "Double") 
    self.treble_stitch = Button(x = 700, y= 100, text = "Treble")   
    
    self.stitch = pygame.sprite.Group()   #I had self-stitch in there
    self.stit_pos = []
    self.current_stitch = None
    self.last_stit_pos = None
    self.hook = Hook()
    self.state = "START"
    
  def mainloop(self):
    #select state loop (switches between the states)
    running = True
    while running:
     if self.state == "START":
       self.startloop()
       
     elif self.state == "GAME":
       self.gameloop()
       self.saveprogressloop()

  def startloop(self): #where the player presses start; will use pygame menu
      self.menu = pygame_menu.Menu("Yarning for More!", self.width-20, self.height/2)
      self.menu.add.label("Ready to begin!", max_char= -1, font_size=18)
      self.menu.add.button('Start', self.start_game, align = pygame_menu.locals.ALIGN_CENTER)
      #Add a background image
      
      #event loop
      while self.state == "START":
        events = pygame.event.get()
        for event in events:
          if event.type == pygame.MOUSEBUTTONDOWN:
            if self.menu.get_current() == self.menu:
              self.state = "GAME"
        
        #update data
        self.menu.update(events)
        #redraw
        self.menu.draw(self.screen)
        pygame.display.flip()
    
  def gameloop(self):
      
       #event loop
      while self.state == "GAME":
        self.screen.fill((0,0,0))
        background = pygame.image.load(f"assets/ballyarnbk.jpg")
        background = pygame.transform.scale(background, (800,600)) 
        self.rect = background.get_rect()
        self.screen.blit(background, (0,0))
        
        font = pygame.font.Font(None,24)
        text = font.render("Click Red (Magic Ring) to get started! G = CH1, O = Double, B = Treble", True, (0,0,0))
        text_rect = text.get_rect()
        self.screen.blit(text, text_rect)
        
        pygame.draw.rect(self.screen,(255,5,0), self.magic_ring.rect) #Red
        pygame.draw.rect(self.screen, (0,250,0), self.chain_one.rect) #Green
        pygame.draw.rect(self.screen, (255,165,0), self.double_stitch.rect) #Orange
        pygame.draw.rect(self.screen, (0,128,128), self.treble_stitch.rect) #Aqua
        
        
        self.hook.image = pygame.transform.scale(self.hook.image, (150,200))
        self.screen.blit(self.hook.image, (690,480))
        
        for event in pygame.event.get():
          if event.type == pygame.QUIT:
                    exit()
          
          elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = event.pos
            if self.magic_ring.rect.collidepoint(mouse_pos):
                  self.current_stitch = 'magic_ring'
                  if self.current_stitch == 'magic_ring':
                    new_stitch = Stitch(680,480)
                    self.stitch.add(new_stitch)
                    self.stit_pos.append((680,480))
                    self.last_stit_pos = (680,480)
                    #self.hook.motion_with_stitch(new_stitch,480)
            
            elif self.chain_one.rect.collidepoint(mouse_pos):
                  self.current_stitch = 'chain_one'
                  if self.current_stitch == 'chain_one':
                    if self.last_stit_pos:
                      x, y = self.last_stit_pos
                      new_pos = (x, y - 60)
                      new_stitch = Stitch(new_pos[0], new_pos[1])
                      self.stitch.add(new_stitch)
                      self.stit_pos.append(new_pos)
                      self.last_stit_pos = new_pos      
            
            elif self.double_stitch.rect.collidepoint(mouse_pos):
                  self.current_stitch = 'double_stitch'
                  if self.current_stitch == 'double_stitch':
                    for i in range(2):
                      if self.last_stit_pos:
                        x, y = self.last_stit_pos
                        new_pos = (x - 10, y - 20)
                        new_stitch = Stitch(new_pos[0], new_pos[1])
                        self.stitch.add(new_stitch)
                        self.stit_pos.append(new_pos)
                        self.last_stit_pos = new_pos 
            
            elif self.treble_stitch.rect.collidepoint(mouse_pos):
                  self.current_stitch = 'treble_stitch'
                  if self.current_stitch == 'treble_stitch':
                    for i in range(3):
                      if self.last_stit_pos:
                        x, y = self.last_stit_pos
                        new_pos = (x-15, y - 20)
                        new_stitch = Stitch(new_pos[0], new_pos[1])
                        self.stitch.add(new_stitch)
                        self.stit_pos.append(new_pos)
                        self.last_stit_pos = new_pos 
              
      #update data
          self.stitch.draw(self.screen) 
      #redraw 
          pygame.display.flip()
          
  def start_game(self):
    self.state = "GAME"