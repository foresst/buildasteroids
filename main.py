import pygame
from constants import *
from player import Player

def main():
    print("Starting asteroids!")

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    clock = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    Player.containers = (updatable, drawable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    # player2 = Player(SCREEN_WIDTH / 3, SCREEN_HEIGHT / 3)

    # updatable.add(player)
    # drawable.add(player)
    # updatable.add(player2)
    # drawable.add(player2)


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        # set framrate to 60 FPS
        dt = clock.tick(60) / 1000

        for obj in updatable:
            obj.update(dt)

        screen.fill("black")

        for obj in drawable:
            obj.draw(screen)
        
        # redraw the screen
        pygame.display.update()

        

if __name__ == "__main__":
    main()
