import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from circleshape import CircleShape
import sys

def main():
    print("Starting asteroids!")

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    clock = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    asteroid_field = AsteroidField()
    
    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        # set framrate to 60 FPS
        dt = clock.tick(60) / 1000

        for obj in updatable:
            obj.update(dt)

        screen.fill("black")

        for obj in asteroids:
            if obj.collide(player):
                sys.exit("Game over!")

        for obj in drawable:
            obj.draw(screen)
        
        # redraw the screen
        pygame.display.update()

        

if __name__ == "__main__":
    main()
