import pygame
from const import Const


class Snake:
    def __init__(self):

        self.head = [Const.START_X_HEAD, Const.START_Y_HEAD]
        self.body = [[Const.START_X_HEAD, Const.START_Y_HEAD], [Const.START_X_HEAD - 11, Const.START_Y_HEAD],
                     [Const.START_X_HEAD - 22, Const.START_Y_HEAD]]

    def move(self, control):
        """Движение змеей в зависимости от направления"""
        if control.direction == "RIGHT":
            self.head[0] += Const.SIZE_SPACE + Const.SIZE_BLOCK
        elif control.direction == "LEFT":
            self.head[0] -= Const.SIZE_SPACE + Const.SIZE_BLOCK
        elif control.direction == "UP":
            self.head[1] -= Const.SIZE_SPACE + Const.SIZE_BLOCK
        elif control.direction == "DOWN":
            self.head[1] += Const.SIZE_SPACE + Const.SIZE_BLOCK

    def animation(self):
        """Прибавляем в начало списка тела голову и удаляем хвост"""
        self.body.insert(0, list(self.head))
        self.body.pop()

    def draw_snake(self, window):
        """Отрисовка змеи на экране"""
        for segment in self.body:
            pygame.draw.rect(window, pygame.Color("Green"), pygame.Rect(segment[0], segment[1],
                                                                        Const.SIZE_BLOCK, Const.SIZE_BLOCK))

    def check_snake_to_window(self):
        """Отслеживает достижение змеей края экрана"""
        if self.head[0] == Const.INTERSECT_BORDER_RIGHT:
            self.head[0] = Const.START_LEFT_BORDER
        elif self.head[0] == Const.INTERSECT_LEFT_BORDER:
            self.head[0] = Const.START_RIGHT_BORDER
        elif self.head[1] == Const.INTERSECT_UP_BORDER:
            self.head[1] = Const.START_DOWN_BORDER
        elif self.head[1] == Const.INTERSECT_DOWN_BORDER:
            self.head[1] = Const.START_UP_BORDER

    def eat(self, food, gui):
        """Проверяет столкновение змеи и еды"""
        if self.head == food.food_position:
            self.body.append(food.food_position)
            food.get_food_position(gui)
            gui.get_new_indicator()

    def check_barrier(self, gui):
        """Проверяет столкновение змеи"""
        if self.head in gui.barrier:
            self.body.pop()
            gui.indicator.pop()
        if self.head in self.body[1:]:
            self.body.pop()
            gui.indicator.pop()
