#This class is responsible for the majority of the gui in this game

import game
import pygame
import TestTubeGame
import os
import button

#initializing the main class for the gui
class Gui:

    #Init method
    def __init__(self):
        self.Menu_Number = 0


    # This method draws the opening screen
    def opening_screen(self, background_position):
        # Loading in the miage that will be used as a background for the opneing screen
        TEST_TUBE_ROW_IMAGE = pygame.image.load(os.path.join('assets', 'TestTubeGame_TestTubeRow.png'))
        TEST_TUBE_OPENING_SCREEN_IMAGE = pygame.transform.scale(TEST_TUBE_ROW_IMAGE, (TestTubeGame.WIDTH, TestTubeGame.HEIGHT))

        pos_x = background_position
        pos_x -= 1

        # Drawing the background
        TestTubeGame.WINDOW.blit(TEST_TUBE_OPENING_SCREEN_IMAGE, (pos_x, 0))
        TestTubeGame.WINDOW.blit(TEST_TUBE_OPENING_SCREEN_IMAGE, (TestTubeGame.WIDTH + pos_x, 0))

        if (pos_x == -TestTubeGame.WIDTH):
            TestTubeGame.WINDOW.blit(TEST_TUBE_OPENING_SCREEN_IMAGE, (TestTubeGame.WIDTH + pos_x, 0))
            pos_x = 0


        #Creating the menu button
        start_button = button.Button(TestTubeGame.WIDTH//2 - 50, TestTubeGame.HEIGHT//2 - 50, 100, 100, [255,0,0], "Start", [255,255,255])
        start_button.draw_button()

        if start_button.isclicked():
            self.Menu_Number = 1

        return pos_x



