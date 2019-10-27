import pygame
from pygame.locals import *


class Control:
    def __init__(self):
        self.run = True
        self.direction = "RIGHT"
        self.pause = True

    def control(self):
        """Управление в зависимости от флага"""
        for event in pygame.event.get():
            if event.type == QUIT:
                self.run = False
            elif event.type == KEYDOWN:
                if event.key == K_RIGHT and self.direction != "LEFT":
                    self.direction = "RIGHT"
                elif event.key == K_LEFT and self.direction != "RIGHT":
                    self.direction = "LEFT"
                elif event.key == K_UP and self.direction != "DOWN":
                    self.direction = "UP"
                elif event.key == K_DOWN and self.direction != "UP":
                    self.direction = "DOWN"
                elif event.key == K_ESCAPE:
                    self.run = False
                elif event.key == K_SPACE:
                    if self.pause:
                        self.pause = False
                    elif not self.pause:
                        self.pause = True
