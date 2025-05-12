import pygame
from constants import *
from player import Player
from Asteroid import Asteroid
import time
from asteroidfield import AsteroidField
import sys
from shot import Shot

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    frame_count = 0
    start_time = time.time()
    graveyard = set()

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    asteroid_field = AsteroidField()
    asteroid_field.add(updatable)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return

        screen.fill("black")
        updatable.update(dt)
        for sprite in drawable:
            sprite.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60) / 1000

        for asteroid in asteroids:
            if player.collides_with(asteroid):
                print("Game Over!")
                pygame.quit()
                sys.exit()
                return
            for shot in shots:
                if shot.collides_with(asteroid):
                    asteroid.should_delete = True
                    shot.should_delete = True
                    break

        for shot in shots:
            if getattr(shot, "should_delete", False):
                graveyard.add(shot)

        for asteroid in asteroids:
            if getattr(asteroid, "should_delete", False):
                graveyard.add(asteroid)

        for sprite in graveyard:
            sprite.kill()
        graveyard.clear()

        frame_count += 1
        if time.time() - start_time > 1:
            print(f"FPS: {frame_count}")
            frame_count = 0
            start_time = time.time()
        

    
if __name__ == "__main__":
    main()
