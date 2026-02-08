import pygame
from constants import *
from column import Column
from playground import PlayGround
from piece import Piece

def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0.0
    time = 0.0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Hanoi T SPEEDRUN")

    columns = pygame.sprite.Group()
    pieces = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    updatable = pygame.sprite.Group()

    Column.containers = (columns, drawable)
    PlayGround.containers = (updatable)
    Piece.containers = (drawable, pieces)
    

    #first = Column(SCREEN_WIDTH/6 - COLUMN_WIDTH/2, SCREEN_HEIGHT*0.9, COLUMN_WIDTH, COLUMN_HEIGHT)
    #second = Column(SCREEN_WIDTH/2 - COLUMN_WIDTH/2, SCREEN_HEIGHT*0.9, COLUMN_WIDTH, COLUMN_HEIGHT)
    #third = Column(SCREEN_WIDTH*5/6 - COLUMN_WIDTH/2, SCREEN_HEIGHT*0.9, COLUMN_WIDTH, COLUMN_HEIGHT)

    playground = PlayGround(10)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill((50,50,50))
        updatable.update()

        for item in drawable:
            item.draw(screen)

        pygame.display.flip()

        dt = clock.tick(30) / 1000
        time += dt
        #print(round(time, 3))

    

if __name__ == "__main__":
    main()
