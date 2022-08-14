# This class is responsible for the majority of the gui in this game

import game
import pygame
import TestTubeGame
import os
import button
import math


# initializing the main class for the gui
class Gui:

    # Init method
    def __init__(self):
        self.Menu_Number = 0
        self.tubes = 5
        self.difficulty = 5
        self.game = None
        self.input = True

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
            self.difficulty = 6

        if medium_colour_button.draw_button():
            self.difficulty = 8

        if hard_colour_button.draw_button():
            self.difficulty = 10

        if easy_tube_button.draw_button():
            self.tubes = 6

        if medium_tube_button.draw_button():
            self.tubes = 8

        if hard_tube_button.draw_button():
            self.tubes = 10

        if continue_button.draw_button():
            self.game = game.Game(self.difficulty, self.tubes)
            self.Menu_Number = 2

        return pos_x

    #This method is for the actual game.

    def game_screen(self):


            TestTubeGame.WINDOW.fill([255,255,255])
            TEST_TUBE_IMAGE = pygame.image.load(os.path.join('assets', 'test_tube_better.jpeg'))

            #Getting the total amount of area that the testtubes will be in
            available_area = int(TestTubeGame.WIDTH*TestTubeGame.HEIGHT*TestTubeGame.PERCENT_GAME_HEIGHT)

            #Getting the total amount of allowed space for the testubes to take up
            total_test_tube_size = int(available_area*TestTubeGame.PERCENT_TUBE)
            # Getting the allowed area for each test tube
            test_tube_size = total_test_tube_size//self.game.number_of_tubes()
            # Getting the size units that will be used in the ratio
            test_tube_x = math.sqrt(test_tube_size//TestTubeGame.HWR)
            test_tube_y = test_tube_x*TestTubeGame.HWR

            # This is the size of the iage
            TEST_TUBE_IMAGE = pygame.transform.scale(TEST_TUBE_IMAGE,(test_tube_x, test_tube_y))

            # available room for test tubes to be distributed
            available_height = int((TestTubeGame.HEIGHT*(TestTubeGame.PERCENT_GAME_HEIGHT)))
            # This variable will hold the vertical size of each row
            row_size = test_tube_y
            # this variable will hold the number of rows
            row_number = (available_height//row_size)+1
            # how many tubes per row
            row_tube_number = self.game.number_of_tubes()//(row_number-1)


            # Starting a for loop that will be meant to draw all of the test tubes
            for x in range(self.game.number_of_tubes()):

                current_tube_number = (x % row_tube_number)
                current_row_number = (x//row_tube_number)

                current_x = (TestTubeGame.WIDTH//(row_tube_number+1))*(current_tube_number + 1) - test_tube_x//2
                current_y =  ((TestTubeGame.HEIGHT - ((available_height//(row_number)) * (row_number - current_row_number)))) - test_tube_y//2 + current_row_number*(TestTubeGame.BUFFER*test_tube_y)

                rectangle = pygame.draw.rect(TestTubeGame.WINDOW, 255, [current_x,current_y,test_tube_x,test_tube_y])
                TestTubeGame.WINDOW.blit(TEST_TUBE_IMAGE, (current_x, current_y))



                #drawing a rectangle around the selected test tube
                if self.game.tubearray[x] in self.game.selected:
                    pygame.draw.rect(TestTubeGame.WINDOW, 0, [current_x + test_tube_x//2 - (test_tube_x + test_tube_x*TestTubeGame.BORDER_AREA)//2 ,current_y + test_tube_y//2  - (test_tube_y + test_tube_y*TestTubeGame.BORDER_AREA)//2,
                    test_tube_x + test_tube_x*TestTubeGame.BORDER_AREA, (test_tube_y + test_tube_y*TestTubeGame.BORDER_AREA)], 2)


                # This loop is meant to fill up the test tubes with its colours
                for y in range(self.game.tubearray[x].checkvolume()):
                    pygame.draw.rect(TestTubeGame.WINDOW,self.game.tubearray[x].stack[y].colour,
                    [current_x + test_tube_x//2 - test_tube_x*TestTubeGame.SQUARE_WIDTH//2  ,current_y + test_tube_y*TestTubeGame.SQUARE_HEIGHT - ((test_tube_y*TestTubeGame.SQUARE_HEIGHT)//TestTubeGame.VOLUME)*(y+1),
                    test_tube_x*TestTubeGame.SQUARE_WIDTH, (test_tube_y*TestTubeGame.SQUARE_HEIGHT)//TestTubeGame.VOLUME]
                    )

                #addind a selected status to the tube object
                if self.isclicked(rectangle) == True:
                    if self.game.numselected() < 2:
                        if self.game.tubearray[x] not in self.game.selected:
                            self.game.select(self.game.tubearray[x])
                        else:
                            self.game.deselect(self.game.tubearray[x])



            if self.game.numselected() == 2:
                self.game.movecolour(self.game.selected[0], self.game.selected[1])
                if self.game.iswon():
                    self.Menu_Number = 0

            keys = pygame.key.get_pressed()
            if keys[pygame.K_r]:
                self.game.restart()
            elif keys[pygame.K_q]:
                self.Menu_Number = 0










    def isclicked(self, rect):

            # Getting the coordinates of the player's mouse
            pos = pygame.mouse.get_pos()
            click = pygame.mouse.get_pressed()
            if rect.collidepoint(pos[0], pos[1]) and click[0] == 1 and self.input == True:
                self.input = False
                return True
            elif self.input == False and click[0] == 0:
                self.input = True
                return False
            else:
                return False














