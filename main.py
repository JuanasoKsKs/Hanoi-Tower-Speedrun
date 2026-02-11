import pygame
from constants import *
from column import Column
from playground import PlayGround
from piece import Piece
from game import Game
import os
def main():
    pygame.init()
    pygame.font.init()
    font = pygame.font.Font(None, 36)
    clock = pygame.time.Clock()
    dt = 0.0
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

    game = Game()
    playground = PlayGround(3, pieces, game)
    while True:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                return
            get_event(event, playground, game)
        screen.fill((50,50,50))

        for item in drawable:
            item.draw(screen)

        score = font.render(str(round(playground.time, 3)), True, "white")
        moves = font.render("Moves: " + str(playground.moves), True, "white")
        screen.blit(score, (10,10))
        screen.blit(moves, (200,10))

        pygame.display.flip()

        dt = clock.tick(60) / 1000
        if game.started == True and game.won == False:
            playground.time += dt
            if playground.capacity == (len(playground.second) or len(playground.third)):
                game.won = True
                game.started = False
    
def reset_game(game, playground):
    playground.time = 0.0
    game.started = False
    game.won = False
    playground.moves = 0
    playground.pivot = 0
    playground.create_pieces()

def get_event(event, playground, game):
    if event.type == pygame.KEYDOWN:
        if event.unicode == "q" and playground.lock_one == False and game.won == False:
            playground.update()
            playground.lock_one = True
        if event.unicode == "w" and playground.lock_two == False and game.won == False:
            playground.update()
            playground.lock_two = True
        if event.unicode == "e" and playground.lock_three == False and game.won == False:
            playground.update()
            playground.lock_three = True
        if event.unicode == "r":
            reset_game(game, playground)
        if event.unicode in ("3", "4", "5", "5", "6", "7", "8", "9", "0") and game.started == False:
            if event.unicode == "0":
                event.unicode = "10"
            playground.capacity = int(event.unicode)
            reset_game(game, playground)
            playground.create_pieces()
    elif event.type == pygame.KEYUP:
        if event.unicode == "q" and playground.lock_one == True:
            playground.lock_one = False
        if event.unicode == "w" and playground.lock_two == True:
            playground.lock_two = False
        if event.unicode == "e" and playground.lock_three == True:
            playground.lock_three = False


if __name__ == "__main__":
    main()
