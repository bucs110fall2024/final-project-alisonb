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
    
    magic_ring = Button(color = "gold", text = "MR")
    chain_one = Button(color = "blue", text = "Chain 1")
    double_stitch = Button(color = "green", text = "Double")
    treble_stitch = Button(color = "pink", text = "Treble")
    
    self.state = "START"
    #Haven't finished this; have to include the models
    
  def mainloop(self):
    #select state loop (switches between the states)
    while True:
      for event in pygame.events.get():
        if event.type == pygame.Quit:
          pygame.quit()
          exit()
        #elif event.type == pygame.get_pressed():
					#pass

  ### below are some sample loop states ###
  
  def startloop(self): #where the player presses start; will use pygame menu
      pass
      #event loop
      #pygame.display.set_caption("Menu")
      
      #while True:
        #pass
        
      #update data

      #redraw
    
    # 
  def gameloop(self):
  
      #event loop
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
  
  pygame.quit