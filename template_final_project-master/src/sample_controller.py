import pygame

class Controller:
  
  def __init__(self):
    #setup pygame data
    pygame.init()
    pygame.event.pump()
    self.screen = pygame.display.set_mode()
    #Haven't finished this; have to include the models
    
  def mainloop(self):
    #select state loop
    
  
  ### below are some sample loop states ###

  def menuloop(self):
    
      #event loop

      #update data

      #redraw
      
  def gameloop(self):
      #event loop

      #update data

      #redraw
    
  def gameoverloop(self):
      #event loop

      #update data

      #redraw
