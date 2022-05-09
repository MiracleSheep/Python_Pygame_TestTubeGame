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
        self.tubes = 5
        self.difficulty = 5
        self.game = None


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
        start_button = button.Button(TestTubeGame.WIDTH//2 - 50, TestTubeGame.HEIGHT//2 - 50, 100, 100, [255,0,0], "Start", [255,255,255], 10)


        if start_button.draw_button():
            self.Menu_Number = 1
            print("Button clicked")



        return pos_x



    # This method is for the before game menu
    def pregame_menu(self, background_position):

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



        # These are buttons that will be used in order to detect how many colours will be used
        easy_colour_button = button.Button((TestTubeGame.WIDTH // 4) - 50, (TestTubeGame.HEIGHT // 6)*2 - 50, 100, 100, [255, 0, 0],"Easy", [255, 255, 255], 10)
        medium_colour_button = button.Button((TestTubeGame.WIDTH // 4)*2 - 50, (TestTubeGame.HEIGHT // 6)*2 - 50, 100, 100, [255, 0, 0],"Medium", [255, 255, 255], 10)
        hard_colour_button = button.Button((TestTubeGame.WIDTH // 4)*3 - 50, (TestTubeGame.HEIGHT // 6)*2 - 50, 100, 100, [255, 0, 0],"Hard", [255, 255, 255], 10)


        # These are buttons that will be used to detect the tube number
        easy_tube_button = button.Button((TestTubeGame.WIDTH // 4) - 50, (TestTubeGame.HEIGHT // 6)*4 - 50, 100, 100, [255, 0, 0],"Easy", [255, 255, 255], 10)
        medium_tube_button = button.Button((TestTubeGame.WIDTH // 4)*2 - 50, (TestTubeGame.HEIGHT // 6)*4 - 50, 100, 100, [255, 0, 0],"Medium", [255, 255, 255], 10)
        hard_tube_button = button.Button((TestTubeGame.WIDTH // 4)*3 - 50, (TestTubeGame.HEIGHT // 6)*4 - 50, 100, 100, [255, 0, 0],"Hard", [255, 255, 255], 10)


        #This is the continue button
        continue_button = button.Button((TestTubeGame.WIDTH // 4) * 2 - 50, (TestTubeGame.HEIGHT // 6) * 5 - 50, 100, 100, [255, 0, 0], "Continue", [255, 255, 255], 10)

        #This tuple will be used to hold values

        if easy_colour_button.draw_button():
            self.difficulty = 4

        if medium_colour_button.draw_button():
            self.difficulty = 7

        if hard_colour_button.draw_button():
            self.difficulty = 10

        if easy_tube_button.draw_button():
            self.tubes = 5

        if medium_tube_button.draw_button():
            self.tubes = 7

        if hard_tube_button.draw_button():
            self.tubes = 10

        if continue_button.draw_button():
            self.game = game.Game(self.difficulty, self.tubes)
            self.Menu_Number = 2

        return pos_x

    #This method is for the actual game.

    def game_screen(self):
            TestTubeGame.WINDOW.fill([255,255,255])
            TEST_TUBE_IMAGE = pygame.image.load(os.path.join('assets', 'test_tube_better.png'))
            TEST_TUBE_IMAGE = pygame.transform.scale(TEST_TUBE_IMAGE,(TestTubeGame.WIDTH//20, TestTubeGame.HEIGHT//5))


            # Starting a for loop that will be meant to draw all of the test tubes
            for x in range(self.tubes):

                current_x = 0
                current_y = 0

                if x >= 5:
                    current_x = (TestTubeGame.WIDTH // 6) * (x - 4) - (TestTubeGame.WIDTH // 20) // 2
                    current_y = (TestTubeGame.HEIGHT // 3) * 2 - (TestTubeGame.HEIGHT // 10) // 2
                    TestTubeGame.WINDOW.blit(TEST_TUBE_IMAGE, (current_x,current_y))
                else:
                    current_x = ((TestTubeGame.WIDTH//6)*(x+1)) - ((TestTubeGame.WIDTH//20)//2)
                    current_y =  (TestTubeGame.HEIGHT//3)*1 - (TestTubeGame.HEIGHT//10)//2
                    TestTubeGame.WINDOW.blit(TEST_TUBE_IMAGE, (current_x,current_y))

                #This loop is meant to fill up the test tubes with its colours
                for x in range(self.game.tubearray[x].checkvolume()):
                    pygame.draw.rect(TestTubeGame.WINDOW,self.game.tubearray[x].topcolour().colour, [current_x + (TestTubeGame.WIDTH//20 - 30)//2 ,(current_y + (TestTubeGame.HEIGHT//5 - 10) - ((TestTubeGame.HEIGHT//5)//TestTubeGame.VOLUME - 10)*x), TestTubeGame.WIDTH//20 - 30, (TestTubeGame.HEIGHT//5)//TestTubeGame.VOLUME - 10])















