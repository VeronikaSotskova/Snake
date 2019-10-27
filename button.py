import pygame

import gui


class Button:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.inactive_color = (13, 162, 58)
        self.active_color = (23, 204, 58)

    def draw(self, x, y, msg, win, font_color, font_type, font_size, action=None):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        if x < mouse[0] < x + self.width and y < mouse[1] < y + self.height:
            pygame.draw.rect(win, self.active_color, (x, y, self.width, self.height))
            if click[0] == 1 and action is not None:
                action()
        else:
            pygame.draw.rect(win, self.inactive_color, (x, y, self.width, self.height))

        gui.print_text(msg, x + 15, y + 15, font_color, font_type, font_size, win)
