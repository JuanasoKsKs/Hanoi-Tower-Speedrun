import pygame
from constants import *
from column import Column
from playground import PlayGround
from piece import Piece
from rules import Rules

def main():
    pygame.init()
    pygame.font.init()
    font = pygame.font.Font(None, 36)

    clock = pygame.time.Clock()
    dt = 0.0
    time = 0.0
    moves = 0
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

    playground = PlayGround(4, pieces)
    rules = Rules()

    while True:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                return
            elif event.type == pygame.KEYDOWN:
                if event.unicode == "1" and playground.lock_one == False:
                    playground.update()
                    playground.lock_one = True
                if event.unicode == "2" and playground.lock_two == False:
                    playground.update()
                    playground.lock_two = True
                if event.unicode == "3" and playground.lock_three == False:
                    playground.update()
                    playground.lock_three = True
            elif event.type == pygame.KEYUP:
                if event.unicode == "1" and playground.lock_one == True:
                    playground.lock_one = False
                if event.unicode == "2" and playground.lock_two == True:
                    playground.lock_two = False
                if event.unicode == "3" and playground.lock_three == True:
                    playground.lock_three = False
        screen.fill((50,50,50))

        for item in drawable:
            item.draw(screen)

        score = font.render(str(round(time, 3)), True, "white")
        moves = font.render("Moves: " + str(playground.moves), True, "white")
        screen.blit(score, (10,10))
        screen.blit(moves, (200,10))

        pygame.display.flip()

        dt = clock.tick(60) / 1000
        if playground.capacity > (len(playground.second) or len(playground.third)):
            rules.won = True
            time += dt
        #print(round(time, 3))

    

if __name__ == "__main__":
    main()
