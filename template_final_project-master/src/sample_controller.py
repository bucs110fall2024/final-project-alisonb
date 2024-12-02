import pygame
import yarn
import hook
import stitch

class Controller:
  
  def __init__(self):
    #setup pygame data
    pygame.init()
    pygame.event.pump()
    self.screen = pygame.display.set_mode()
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

  
  ### below are some sample loop states ###

  def menuloop(self):
    pass
      #event loop

      #update data

      #redraw
      #   Buttons are the menu (make so it goes to your game loop)
      
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