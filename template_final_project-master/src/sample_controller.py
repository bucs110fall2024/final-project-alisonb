import pygame
import pygame_menu
import json
from src.button import Button
from src.yarn import Yarn
from src.hook import Hook
from src.stitch import Stitch

class Controller:
  
  def __init__(self):
    #setup pygame data
    pygame.init()
    pygame.event.pump()
    self.screen = pygame.display.set_mode()
    self.width, self.height = pygame.display.get_window_size()
    
    magic_ring = Button(color = "gold", text = "MR")
    chain_one = Button(color = "blue", text = "Chain 1")
    double_stitch = Button(color = "green", text = "Double")
    treble_stitch = Button(color = "pink", text = "Treble")
    
    #Models
    self.user = Hook()
    self.ball_yarn = Yarn()
    self.stitches = Stitch()
    
    self.state = "START"
    
  def mainloop(self):
    pass
    #select state loop (switches between the states)
    #while True:
      #for event in pygame.events.get():
        #if event.type == pygame.Quit:
          #pygame.quit()
          #exit()
        #elif event.type == pygame.get_pressed():
					#pass

  ### below are some sample loop states ###
  
  def startloop(self): #where the player presses start; will use pygame menu
      #event loop
      self.menu = pygame_menu.Menu("Yarning for More!", self.width-20, self.height/2)
      self.menu.add.label("Click the button to start", max_char=-1, font_size=14)
      self.menu.add.button('Start', self.start_game, align = pygame_menu.locals.ALIGN_CENTER)
      
      while self.state == "START":
        for event in pygame.event.get():
          if event.type == pygame.MOUSEBUTTONDOWN:
            self.state = "GAME"
        
      #update data
      self.menu.update(pygame.event.get())
      #redraw
      self.menu.draw(self.screen)
      pygame.display.flip()
    
    # 
  def gameloop(self):
      #event loop
      while self.state == "GAME":
        for event in pygame.event.get():
          if event.type == pygame.QUIT:
                    exit()
          elif event.type == pass
      #This is where the if statements for the button happen
      
      #update data
      def save_state(self):
        stitch_state = self.__dict__
        fptr = open("assets/last_state.json", "w")
        json.dump(fptr, stitch_state)
      #redraw 
        def load_state(self):
         fptr = open("assets/last_state.json")
        self.__dict__ = json.loads(fptr)
    
  def saveprogressloop(self):
    pass
      #event loop

      #update data

      #redraw
      
      #Logic for the screen; jst a loop for each screen
      #Think of it has different states; what does it look like when its not doing anything
      #When the game is happening, etc 
      
      #Stitch doesn't have to know about other stitches; the controller should worry
      
      #Motto: "Worry about yourself"
  pygame.quit()