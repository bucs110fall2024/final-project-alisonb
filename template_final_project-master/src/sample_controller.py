import pygame
import Button
#import src.yarn import Yarn
#import src.hook import Hook
#import src.stitch import Stitch

class Controller:
  
  def __init__(self):
    #setup pygame data
    pygame.init()
    pygame.event.pump()
    self.screen = pygame.display.set_mode()
    
    chain_one = Button(color = "blue", text = "Chain 1")
    double_stitch = Button(color = "green", text = "Double")
    treble_stitch = Button(color = "pink", text = "Treble")
    #Haven't finished this; have to include the models
    
  def mainloop(self):
    #select state loop
    while True:
      for event in pygame.events.get():
        if event.type == pygame.Quit:
          pygame.quit()
          exit()
        #elif event.type == pygame.get_pressed():
					#pass
     #These are for the buttons

  ### below are some sample loop states ###

#This is for start and quit 
  def menuloop(self):
      pass
      #event loop
      #pygame.display.set_caption("Menu")
      
      #while True:
        #pass
        
      #update data

      #redraw
      
  def gameloop(self):
    pass
      #event loop

      #update data

      #redraw
    
  def gameoverloop(self):
    pass
      #event loop

      #update data

      #redraw