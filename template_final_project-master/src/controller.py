import pygame
import pygame_menu
import json
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
    self.magic_ring = Button(color = (200,0,200), text = "MR", position = (0,0)) # Red
    self.chain_one = Button(color = (0,255,0), text = "Chain 1", position = (50,150)) #Green
    self.double_stitch = Button(color = (255,165,0), text = "Double", position = (50,250)) #Orange
    self.treble_stitch = Button(color = (0,128,128), text = "Treble", position = (400,550)) #Aqua    
    
    self.stitch = Stitch(20,30)
    self.sprites = pygame.sprite.Group((self.stitch))
    self.current_stitch = None
    #self.user = Hook()
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
        self.rect = background.get_rect()
        self.screen.blit(background, (0,0))
        
        self.magic_ring.draw(self.screen)
        self.chain_one.draw(self.screen)
        self.double_stitch.draw(self.screen)
        self.treble_stitch.draw(self.screen)
        
        for event in pygame.event.get():
          if event.type == pygame.QUIT:
                    exit()
          
          elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = event.pos
            if self.magic_ring.is_clicked(mouse_pos):
                  self.current_stitch = 'magic_ring'
                  if self.current_stitch == 'magic_ring':
                    Stitch.add_stit(self)
                    Stitch.move(self,1,1)
            elif self.chain_one.is_clicked(mouse_pos):
                  self.current_stitch = 'chain_one'
                  if self.current_stitch == 'chain_one':
                    Stitch.add_stit(self)
                    Stitch.move(self,1,1)
            elif self.double_stitch.is_clicked(mouse_pos):
                  self.current_stitch = 'double_stitch'
                  if self.current_stitch == 'double_stitch':
                    Stitch.add_stit(self)
                    Stitch.move(self,2,4)
            if self.treble_stitch.is_clicked(mouse_pos):
                  self.current_stitch = 'treble_stitch'
                  if self.current_stitch == 'treble_stitch':
                    Stitch.add_stit(self)
                    Stitch.move(self,3,6)
              
      #update data
          self.sprites.draw(self.screen) 
      #redraw 
          pygame.display.flip()
          
  def start_game(self):
    self.state = "GAME"
    
  def saveprogressloop(self):

      #update data
      def save_state(self):
        stitch_state = self.__dict__
        fptr = open("assets/last_state.json", "w")
        json.dump(fptr, stitch_state)
      #redraw
      def load_state(self):
         fptr = open("assets/last_state.json")
         self.__dict__ = json.loads(fptr)