import pygame
from control import Control
from snake import Snake
from gui import Gui, print_text, draw_lose
from food import Food
from const import Const
from button import Button
from pygame.locals import *

pygame.init()
window = pygame.display.set_mode((Const.SCREEN_WIDTH, Const.SCREEN_HEIGHT))
clock = pygame.time.Clock()
pygame.display.set_caption('Snake')
control = Control()
snake = Snake()
gui = Gui()
food = Food()
gui.init_field()
food.get_food_position(gui)


def restart_settings():
    snake.head = [Const.START_X_HEAD, Const.START_Y_HEAD]
    snake.body = [[Const.START_X_HEAD, Const.START_Y_HEAD], [Const.START_X_HEAD - 11, Const.START_Y_HEAD],
                  [Const.START_X_HEAD - 22, Const.START_Y_HEAD]]
    gui.indicator = [[12, 34]]
    gui.game = "GAME"
    control.direction = "RIGHT"
    control.pause = True
    control.run = True


def show_menu():
    menu_bg = pygame.image.load("images/bg.jpg")
    menu_bg = pygame.transform.scale(menu_bg, (Const.SCREEN_WIDTH, Const.SCREEN_HEIGHT))
    show = True
    button = Button(100, 50)
    while show:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
        window.blit(menu_bg, (0, 0))
        print_text('SNAKE', 150, 20, pygame.Color('Black'), 'monaco', 60, window)
        button.draw(100,100, 'Start', window, (0,0,0), 'monaco', 25, start_game)
        button.draw(100,200, 'Records', window, (0,0,0), 'monaco', 25)
        button.draw(100,300, 'Exit', window, (0,0,0), 'monaco', 25, exit)
        pygame.display.update()
        pygame.display.flip()


def start_game():
    restart_settings()
    game_cycle()


def game_cycle():
    while control.run:
        for event in pygame.event.get():
            if event.type == QUIT:
                control.run = False
                pygame.quit()
            elif event.type == KEYDOWN:
                if event.key == K_RIGHT and control.direction != "LEFT":
                    control.direction = "RIGHT"
                elif event.key == K_LEFT and control.direction != "RIGHT":
                    control.direction = "LEFT"
                elif event.key == K_UP and control.direction != "DOWN":
                    control.direction = "UP"
                elif event.key == K_DOWN and control.direction != "UP":
                    control.direction = "DOWN"
                elif event.key == K_ESCAPE:
                    control.run = False
                elif event.key == K_SPACE:
                    control.pause = not control.pause
                elif event.key == pygame.K_RETURN and (gui.game == 'LOSE' or gui.game == 'WIN'):
                    control.run = True
                    control.pause = True
                    gui.game = "GAME"
                    restart_settings()
                    game_cycle()

        gui.check_win_or_lose()
        window.fill(pygame.Color('Black'))

        if gui.game == "GAME":
            snake.draw_snake(window)
            food.draw_food(window)

        # если победа
        elif gui.game == "WIN":
            gui.draw_win(window)

        # если поражение
        elif gui.game == "LOSE":
            draw_lose(window)

        gui.show_score(window)
        gui.draw_indicator(window)
        gui.draw_level(window)

        # если игра на паузе
        if control.pause and gui.game == "GAME":
            print_text("PAUSE", 150, 100, pygame.Color("White"), "monaco", 60, window)
            print_text("press space to return", 150, 240, pygame.Color("Grey"), 'monaco', 20, window)

        # если игра не на паузе
        if not control.pause and gui.game == "GAME":
            snake.move(control)
            snake.check_barrier(gui)
            snake.eat(food, gui)
            snake.check_snake_to_window()
            snake.animation()

        pygame.display.flip()
        pygame.display.update()
        clock.tick(15)


show_menu()
