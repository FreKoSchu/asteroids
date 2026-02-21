import pygame
import constants
from logger import log_state
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
    
    pygame.init()
    screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    asteroids = pygame.sprite.Group()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    player = Player(constants.SCREEN_WIDTH/2, constants.SCREEN_HEIGHT/2)
    
    asteroidfield = AsteroidField()

    
    

    dt = 0
    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        dt=clock.tick(60)/1000
            
        
        screen.fill("black")
        
        for item in drawable:
            item.draw(screen) 

        for item in updatable:
            item.update(dt)
            
        pygame.display.flip()
        
    
    



if __name__ == "__main__":
    main()
