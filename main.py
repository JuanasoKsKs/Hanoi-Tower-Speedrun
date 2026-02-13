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

        your_time = font.render("Time: " + str(round(playground.time, 3)), True, base_color)
        your_moves = font.render("Moves: " + str(playground.moves), True, base_color)
        screen.blit(font.render("Your Score", True, base_color), (10, 10))
        screen.blit(your_time, (10,50))
        screen.blit(your_moves, (10,90))
        display_stats(playground, game, screen, font)
        display_instructions(playground, game, screen, font)
        pygame.display.flip()

        dt = clock.tick(60) / 1000
        if game.started == True and game.won == False:
            playground.time += dt
            if playground.capacity == (len(playground.second) or len(playground.third)):
                game.won = True
                verify_scoring(game, playground)
                #game.started = False

def verify_scoring(game, playground):
    scores = game.records[playground.capacity]
    for key, value in scores.items():
        if playground.moves > value[0]:
            continue
        elif playground.moves == value[0]:
            if playground.time > value [1]:
                continue
        for j in range(5, key, -1):
            scores[j] = scores[j-1]
        scores[key] = [playground.moves, round(playground.time, 3)]
        game.update_records()
        break
            


def display_stats(playground, game, screen, font):
    scores = game.records[playground.capacity]
    leyend_place = font.render("Place", True, base_color)
    leyend_moves = font.render("Moves", True, base_color)
    leyend_time = font.render("Time", True, base_color)
    screen.blit(leyend_time, (SCREEN_WIDTH - 100, 10))
    screen.blit(leyend_moves, (SCREEN_WIDTH - 200, 10))
    screen.blit(leyend_place, (SCREEN_WIDTH - 300, 10))
    for i in scores:
        place = scores[i]
        if place[0] == 10000:
            continue
        screen.blit(font.render(f"{i}°-->", True, base_color), (SCREEN_WIDTH -300, 25 * i + 10))
        screen.blit(font.render(f"{place[0]}", True, base_color), (SCREEN_WIDTH -200, 25 * i + 10))
        screen.blit(font.render(f"{place[1]}", True, base_color), (SCREEN_WIDTH -100, 25 * i + 10))

def display_instructions(playground, game, screen, font):
    screen.blit(font.render("Use with LEFT arrow", True, base_color), (SCREEN_WIDTH / 6 - 120, SCREEN_HEIGHT - 50))
    screen.blit(font.render("Use with DOWN arrow", True, base_color), (SCREEN_WIDTH / 2 - 120, SCREEN_HEIGHT - 50))
    screen.blit(font.render("Use with RIGHT arrow", True, base_color), (SCREEN_WIDTH * 5/6 - 120, SCREEN_HEIGHT - 50))
    if game.started:
        screen.blit(font.render('Restart (r)', True, base_color), (350, 10))
    else:
        screen.blit(font.render('SELECT SIZE', True, base_color), (300, 10))
        screen.blit(font.render('(3)', True, base_color), (300, 40))
        screen.blit(font.render('(4)', True, base_color), (350, 40))
        screen.blit(font.render('(5)', True, base_color), (400, 40))
        screen.blit(font.render('(6)', True, base_color), (450, 40))
        screen.blit(font.render('(7)', True, base_color), (300, 75))
        screen.blit(font.render('(8)', True, base_color), (350, 75))
        screen.blit(font.render('(9)', True, base_color), (400, 75))
        screen.blit(font.render('10-(0)', True, base_color), (450, 75))
    
    screen.blit(font.render(f"Perfect Moves for {playground.capacity} Pieces", True, "yellow"), (SCREEN_WIDTH/2, 10))
    screen.blit(font.render(f"{2**playground.capacity - 1}", True, "yellow"), (SCREEN_WIDTH/2 + 150, 35))
    
    
    
def reset_game(game, playground):
    playground.time = 0.0
    game.started = False
    game.won = False
    playground.moves = 0
    playground.pivot = 0
    playground.create_pieces()

def get_event(event, playground, game):
    if event.type == pygame.KEYDOWN:
        if event.scancode == 80 and playground.lock_one == False and game.won == False:
            playground.update()
            playground.lock_one = True
        if event.scancode == 81 and playground.lock_two == False and game.won == False:
            playground.update()
            playground.lock_two = True
        if event.scancode == 79 and playground.lock_three == False and game.won == False:
            playground.update()
            playground.lock_three = True
        if event.unicode == "r":
            reset_game(game, playground)
            game.update_records()
        if event.unicode in ("3", "4", "5", "5", "6", "7", "8", "9", "0") and game.started == False:
            if event.unicode == "0":
                event.unicode = "10"
            playground.capacity = int(event.unicode)
            reset_game(game, playground)
            playground.create_pieces()
    elif event.type == pygame.KEYUP:
        if event.scancode == 80 and playground.lock_one == True:
            playground.lock_one = False
        if event.scancode == 81 and playground.lock_two == True:
            playground.lock_two = False
        if event.scancode == 79 and playground.lock_three == True:
            playground.lock_three = False


if __name__ == "__main__":
    main()
