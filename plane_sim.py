import math

import pygame
pygame.init()

# Creates a window named "Plane Simulation"
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Plane Simulation")
clock = pygame.time.Clock()

plane = {"xPos": 0, "yPos": 0, "xVelocity": 0, "yVelocity": 0, "thrust": 0.1, "angle": 5}
gravity = -0.163

Running = True

while Running:
   
   for event in pygame.event.get():
      if event.type == pygame.QUIT:
         Running = False

   lift = plane["xVelocity"] * math.sin(math.radians(plane["angle"]))   
   plane["xVelocity"] = plane["xVelocity"] * math.cos(math.radians(plane["angle"]))

   plane["xVelocity"] += plane["thrust"]
   plane["yVelocity"] += lift + gravity

   plane["xPos"] += plane["xVelocity"]
   plane["yPos"] += plane["yVelocity"]

   print(plane["xPos"])
   print(plane["yPos"])

   screen.fill((0, 0, 0))
   pygame.draw.circle(screen, (255, 255, 255), (400, (300 - plane["yPos"])), 50)
   pygame.display.flip()
   clock.tick(60)

pygame.quit()
