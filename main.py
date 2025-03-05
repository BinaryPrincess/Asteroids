import pygame
from constants import *
from player import Player
import time

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    dt = 0

    frame_count = 0
    start_time = time.time()
            
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            

        screen.fill("black")
        player.update(dt)
        player.draw(screen)
        pygame.display.flip()

        dt = clock.tick(60) / 1000

        frame_count += 1
        if time.time() - start_time > 1:
            print(f"FPS: {frame_count}")
            frame_count = 0
            start_time = time.time()
        

    
if __name__ == "__main__":
    main()
