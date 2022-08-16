# this class is meant to create a menu floater that moves across the screen vertically and in random positions

#importing librairies
import copy
import random

import pygame

import TestTubeGame


class Menu_Floater:

    def __init__(self,img, direction):
        self.image = img
        self.current_image = copy.copy(self.image)
        self.direction = direction
        self.angle = 0
        self.s = 1
        self.sp = 1
        self.reset()

    #Method that chooses a random x value and sets the image to it
    def reset(self):
        self.x = random.randint(0, TestTubeGame.WIDTH - self.current_image.get_width())
        self.angle = 0
        self.s = random.randint(0,5)
        self.sp = random.randint(1,15)
        self.current_image = pygame.transform.scale(self.image, (random.randint(int(TestTubeGame.WIDTH // 40), int(
            TestTubeGame.WIDTH // 20)), random.randint(int(TestTubeGame.HEIGHT // 40), int(TestTubeGame.HEIGHT // 20))))
        if self.direction:
            self.y = TestTubeGame.HEIGHT
        else:
            self.y = 0 - self.current_image.get_height()


    # Method that moves the image vertically
    def move(self):
        if self.direction:
            self.y -= self.sp
        else:
            self.y += self.sp

    #Method that spins the object
    def spin(self):
        rotated_image = pygame.transform.rotate(self.current_image, self.angle)
        self.angle += self.s
        return rotated_image


    #Method that draw the object
    def draw(self):
        TestTubeGame.WINDOW.blit(self.spin(), (self.x, self.y))
        self.move()
        self.overpass()

    # Method that checks for overpass
    def overpass(self):
        if self.x > TestTubeGame.WIDTH or self.x < 0 or self.y < 0 - self.current_image.get_height() or self.y > TestTubeGame.HEIGHT:
            self.reset()

