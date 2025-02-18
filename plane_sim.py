import pygame
pygame.init()

# Creates a window named "Plane Simulation"
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Plane Simulation")

plane = {"xPos": 0, "yPos": 0, "xVelocity": 0, "yVelocity": 0}

Running = True

while Running:
   
   for event in pygame.event.get():
      if event.type == pygame.QUIT:
         Running = False

   plane["yPos"] += (200 - plane["yPos"]) / 200
   print(plane["yPos"])

   screen.fill((0, 0, 0))
   pygame.draw.circle(screen, (255, 255, 255), (400, (300 - plane["yPos"])), 50)
   pygame.display.flip()

pygame.quit()
