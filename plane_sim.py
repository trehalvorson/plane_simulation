import pygame
pygame.init()

# Creates a window named "Plane Simulation"
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Plane Simulation")

Running = True

while Running:
   
   for event in pygame.event.get():
      if event.type == pygame.QUIT:
         Running = False

   screen.fill((0, 0, 0))
   pygame.draw.circle(screen, (255, 255, 255), (450, 200), 50)
   pygame.display.flip()

pygame.quit()