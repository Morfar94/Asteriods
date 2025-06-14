import pygame
from constants import *
from player import Player
from asteroidfield import *
from asteroid import *
from shot import *
import sys

def main():
    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    
    AsteroidField.containers = (updateable)
    Asteroid.containers = (asteroids, updateable, drawable)
    asteroidfield = AsteroidField()

    Player.containers = (updateable, drawable)

    Shot.containers = (shots, updateable, drawable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    
    dt = 0

    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        updateable.update(dt)

        for asteroid in asteroids:
            if asteroid.collide(player):
                print("Game over!")
                sys.exit()
            for shot in shots:
                if shot.collide(asteroid):
                    shot.kill()
                    asteroid.split()




        for draws in drawable:
            draws.draw(screen)

        pygame.display.flip()

        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()