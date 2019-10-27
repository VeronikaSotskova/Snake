import pygame
from control import Control
from snake import Snake
from gui import Gui
from food import Food

pygame.init()
window = pygame.display.set_mode((441,441))
clock = pygame.time.Clock()
pygame.display.set_caption('Snake')
control = Control()
snake = Snake()
gui = Gui()
food = Food()
gui.init_field()
food.get_food_position(gui)

while control.run:
    gui.check_win_or_lose()
    control.control()
    window.fill(pygame.Color('Black'))
    if gui.game == "GAME":
        snake.draw_snake(window)
        food.draw_food(window)
    elif gui.game == "WIN":
        gui.draw_win(window)
    elif gui.game == "LOSE":
        gui.draw_lose(window)

    gui.draw_indicator(window)
    gui.draw_level(window)
    if control.pause and gui.game == "GAME":
        snake.move(control)
        snake.check_barrier(gui)
        snake.eat(food, gui)
        snake.check_snake_to_window()
        snake.animation()
    #var_speed += 3

    pygame.display.flip()
    clock.tick(10)