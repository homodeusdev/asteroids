# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import Player

def main():
  print("Starting Asteroids!")
  print(f"Screen width: {SCREEN_WIDTH}")
  print(f"Screen height: {SCREEN_HEIGHT}")

  pygame.init()
  screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
  pygame.display.set_caption("Asteroids")
  
  player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
  
  updatables = [player]
  drawables = [player]

  clock = pygame.time.Clock()
  
  while True:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        exit()

    screen.fill((0, 0, 0))
    
    for obj in drawables:
        obj.draw(screen)

    current_time = pygame.time.get_ticks() / 1000
    for obj in updatables:
        obj.update(current_time)

    pygame.display.flip()
    clock.tick(60)


if __name__ == "__main__":
  main()
  
