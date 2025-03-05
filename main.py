import pygame
from constants import *
from player import Player
import time

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    frame_count = 0
    start_time = time.time()

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            

        screen.fill("black")
        updatable.update(dt)
        for sprite in drawable:
            sprite.draw(screen)
        pygame.display.flip()

        dt = clock.tick(60) / 1000

        frame_count += 1
        if time.time() - start_time > 1:
            print(f"FPS: {frame_count}")
            frame_count = 0
            start_time = time.time()
        

    
if __name__ == "__main__":
    main()
