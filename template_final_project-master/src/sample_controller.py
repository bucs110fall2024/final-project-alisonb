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
    self.screen = pygame.display.set_mode()
    self.width, self.height = pygame.display.get_window_size()
    
    #Models
    self.magic_ring = Button(color = (200,0,200), text = "MR") # Red
    self.chain_one = Button(color = (0,255,0), text = "Chain 1") #Green
    self.double_stitch = Button(color = (255,165,0), text = "Double") #Orange
    self.treble_stitch = Button(color = (0,128,128), text = "Treble") #Aqua    
    
    self.stitch = Stitch()
    self.user = Hook(0,0)
    self.sprites = pygame.sprite.Group((self.stitch))
    
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
      self.menu.add.label("Click the button to start", max_char=-1, font_size=14)
      self.menu.add.button('Start', self.start_game, align = pygame_menu.locals.ALIGN_CENTER)
      #Add a background image
      
      #event loop
      while self.state == "START":
        events = pygame.event.get()
        for event in events:
          if event.type == pygame.MOUSEBUTTONDOWN:
            self.state = "GAME"
        
        #update data
        self.menu.update(events)
        #redraw
        self.menu.draw(self.screen)
        pygame.display.flip()
    
  def gameloop(self):
      #event loop
      #Added image
      background = pygame.image.load('ballyarnbk.jpg')
      
      while self.state == "GAME":
        self.screen.fill((0,0,0))
        self.screen.blit(background, (0,0))
        
        for event in pygame.event.get():
          if event.type == pygame.QUIT:
                    exit()
          elif event.type == pygame.MOUSEBUTTONDOWN:
            if self.magic_ring:
              Stitch.add_stit()
            if self.chain_one:
              Stitch.add_stit()
            if self.double_stitch:
              for i in range(2):
                Stitch.add_stit()
            if self.treble_stitch:
              for i in range(3):
                Stitch.add_stit
                
              
      #Do I have to use collide or collision so that its noticed by the user pressing on it? 
      
      #event.pos into collision()  #HAVE TO USE IT (in the controller; models don't have to know other models exist)
      
      #update data
      self.sprites.update()
      
      #redraw 
      pygame.display.flip()
          
    
  def saveprogressloop(self):
  #Work on this
      #event loop
      
      #update data
      def save_state(self):
        stitch_state = self.__dict__
        fptr = open("assets/last_state.json", "w")
        json.dump(fptr, stitch_state)
      #redraw
      def load_state(self):
         fptr = open("assets/last_state.json")
         self.__dict__ = json.loads(fptr)
      
      
#Logic for the screen; jst a loop for each screen
#Think of it has different states; what does it look like when its not doing anything
#When the game is happening, etc 
      
# Stitch doesn't have to know about other stitches; the controller should worry
# Motto: "Worry about yourself"