# This class is responsible for the majority of the gui in this game

import game
import pygame
import TestTubeGame
import os
import button
import math


# initializing the main class for the gui
import menu_floater


class Gui:

    # Init method
    def __init__(self):
        self.Menu_Number = 0
        self.tubes = 0
        self.difficulty = 0
        self.game = None
        self.Minput = True
        self.Kinput = True
        self.undos = 0

    # This method draws the opening screen
    def opening_screen(self, background_position):


        pos_x = background_position
        pos_x -= 1

        # Drawing the background
        TestTubeGame.WINDOW.blit(TestTubeGame.TEST_TUBE_OPENING_SCREEN_IMAGE, (pos_x, 0))
        TestTubeGame.WINDOW.blit(TestTubeGame.TEST_TUBE_OPENING_SCREEN_IMAGE, (TestTubeGame.WIDTH + pos_x, 0))

        if (pos_x == -TestTubeGame.WIDTH):
            TestTubeGame.WINDOW.blit(TestTubeGame.TEST_TUBE_OPENING_SCREEN_IMAGE, (TestTubeGame.WIDTH + pos_x, 0))
            pos_x = 0

        #drawing the random test tubes that are flying around on the start screen
        TestTubeGame.floater_1.draw()
        TestTubeGame.floater_2.draw()
        TestTubeGame.floater_3.draw()
        TestTubeGame.floater_4.draw()
        TestTubeGame.floater_5.draw()
        TestTubeGame.floater_6.draw()
        TestTubeGame.floater_7.draw()
        TestTubeGame.floater_8.draw()
        TestTubeGame.floater_9.draw()
        TestTubeGame.floater_10.draw()


        # Drawing the title
        TestTubeGame.WINDOW.blit(TestTubeGame.TITLE_IMAGE_MODIFIED, (TestTubeGame.WIDTH//2 - (TestTubeGame.TITLE_IMAGE_MODIFIED.get_width())//2, TestTubeGame.HEIGHT*0.2 - (TestTubeGame.TITLE_IMAGE_MODIFIED.get_height())//2))


        if TestTubeGame.start_button.draw_button():
            self.Menu_Number = 1




        return pos_x



    # This method is for the before game menu
    def pregame_menu(self, background_position):


        pos_x = background_position
        pos_x -= 1

        # Drawing the background
        TestTubeGame.WINDOW.blit(TestTubeGame.TEST_TUBE_OPENING_SCREEN_IMAGE, (pos_x, 0))
        TestTubeGame.WINDOW.blit(TestTubeGame.TEST_TUBE_OPENING_SCREEN_IMAGE, (TestTubeGame.WIDTH + pos_x, 0))

        if (pos_x == -TestTubeGame.WIDTH):
            TestTubeGame.WINDOW.blit(TestTubeGame.TEST_TUBE_OPENING_SCREEN_IMAGE, (TestTubeGame.WIDTH + pos_x, 0))
            pos_x = 0

        TestTubeGame.WINDOW.blit(TestTubeGame.DIFFICULTY_RAW, (TestTubeGame.WIDTH // 2 - (TestTubeGame.DIFFICULTY_RAW.get_width()) // 2,TestTubeGame.HEIGHT//7*1 - (TestTubeGame.DIFFICULTY_RAW.get_height()) // 2))
        TestTubeGame.WINDOW.blit(TestTubeGame.NUMBER_OF_UNDOS_MODIFIED, (TestTubeGame.WIDTH // 2 - (TestTubeGame.NUMBER_OF_UNDOS_MODIFIED.get_width()) // 2,TestTubeGame.HEIGHT // 7 * 3 - (TestTubeGame.NUMBER_OF_UNDOS_MODIFIED.get_height()) // 2))




        #This tuple will be used to hold values

        if TestTubeGame.easy_difficulty_button.draw_button():
            self.difficulty = 6
            self.tubes = 6
            TestTubeGame.medium_difficulty_button.deselect()
            TestTubeGame.hard_difficulty_button.deselect()

        if TestTubeGame.medium_difficulty_button.draw_button():
            self.difficulty = 8
            self.tubes = 8
            TestTubeGame.hard_difficulty_button.deselect()
            TestTubeGame.easy_difficulty_button.deselect()

        if TestTubeGame.hard_difficulty_button.draw_button():
            self.difficulty = 10
            self.tubes = 10
            TestTubeGame.easy_difficulty_button.deselect()
            TestTubeGame.medium_difficulty_button.deselect()

        if TestTubeGame.continue_button.draw_button():
            if self.tubes == 0 or self.difficulty == 0:
                TestTubeGame.continue_button.deselect()
            else:
                self.game = game.Game(self.difficulty, self.tubes, self.undos)
                self.Menu_Number = 2

        if TestTubeGame.easy_reverse_button.draw_button():
            self.undos = 0
            TestTubeGame.medium_reverse_button.deselect()
            TestTubeGame.hard_reverse_button.deselect()

        if TestTubeGame.medium_reverse_button.draw_button():
            self.undos = 10
            TestTubeGame.easy_reverse_button.deselect()
            TestTubeGame.hard_reverse_button.deselect()

        if TestTubeGame.hard_reverse_button.draw_button():
            self.undos = 5
            TestTubeGame.medium_reverse_button.deselect()
            TestTubeGame.easy_reverse_button.deselect()

        if TestTubeGame.tutorial_button.draw_button():
            self.Menu_Number = 3

        keys = pygame.key.get_pressed()
        if keys[pygame.K_q] and self.Kinput == True:
            self.Kinput = False
            self.Menu_Number = 0
        elif self.Kinput == False and keys[pygame.K_q] == False:
            self.Kinput = True

        return pos_x

    #This method is for the actual game.

    def game_screen(self):


            TestTubeGame.WINDOW.fill([255,255,255])
            TestTubeGame.WINDOW.blit(TestTubeGame.LAB_MODIFIED, (0,0))

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
            TEST_TUBE_IMAGE = pygame.transform.scale(TestTubeGame.TEST_TUBE_IMAGE,(test_tube_x, test_tube_y))

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
                    self.Menu_Number = 4

            keys = pygame.key.get_pressed()
            if keys[pygame.K_r] and self.Kinput == True:
                self.game.restart()
                self.Kinput = False
            elif keys[pygame.K_q] and self.Kinput == True:
                self.game.reset()
                self.Kinput = False
                self.Menu_Number = 0
            elif keys[pygame.K_u] and self.Kinput == True:
                self.game.reversemove()
                self.Kinput = False
            elif self.Kinput == False and keys[pygame.K_r] == False and keys[pygame.K_q] == False and keys[pygame.K_u] == False:
                self.Kinput = True

    # Menu to show the player how to play
    def tutorial_screen(self):
        TestTubeGame.WINDOW.fill([255, 255, 255])
        TestTubeGame.WINDOW.blit(TestTubeGame.BRICK_MODIFIED, (0,0))
        TestTubeGame.WINDOW.blit(TestTubeGame.CONTROLS_MODIFIED, (TestTubeGame.WIDTH//2 - TestTubeGame.CONTROLS_MODIFIED.get_width()//2, TestTubeGame.HEIGHT //8 * 5 - TestTubeGame.CONTROLS_MODIFIED.get_height()//2))
        TestTubeGame.WINDOW.blit(TestTubeGame.INSTRUCTIONS_MODIFIED, (TestTubeGame.WIDTH//2 - TestTubeGame.CONTROLS_MODIFIED.get_width()//2,TestTubeGame.HEIGHT//8 * 2 - TestTubeGame.INSTRUCTIONS_MODIFIED.get_height()//2))



        if TestTubeGame.return_button.draw_button():
            self.Menu_Number = 1

        keys = pygame.key.get_pressed()
        if keys[pygame.K_q] and self.Kinput == True:
            self.Kinput = False
            self.Menu_Number = 0
        elif self.Kinput == False and keys[pygame.K_q] == False:
            self.Kinput = True

    # Menu to display the pplayer's victory
    def victory_screen(self):
        TestTubeGame.WINDOW.fill([255, 255, 255])
        TestTubeGame.WINDOW.blit(TestTubeGame.CONFET_MODIFIED, (0,0))
        TestTubeGame.WINDOW.blit(TestTubeGame.WON_MODIFIED, (TestTubeGame.WIDTH//2 - TestTubeGame.WON_MODIFIED.get_width()//2,TestTubeGame.HEIGHT//2 - TestTubeGame.WON_MODIFIED.get_height()//2))
        TestTubeGame.WINDOW.blit(TestTubeGame.AMONGUS_MODIFIED, (TestTubeGame.WIDTH/5*1 - TestTubeGame.AMONGUS_MODIFIED.get_width()//2,TestTubeGame.HEIGHT//5*1 - TestTubeGame.AMONGUS_MODIFIED.get_height()//2))
        TestTubeGame.WINDOW.blit(TestTubeGame.HAROLD_MODIFIED, (TestTubeGame.WIDTH//5*1 - TestTubeGame.HAROLD_MODIFIED.get_width()//2,TestTubeGame.HEIGHT//5*4 - TestTubeGame.HAROLD_MODIFIED.get_height()//2))
        TestTubeGame.WINDOW.blit(TestTubeGame.STONKS_MODIFIED, (TestTubeGame.WIDTH//5*4 - TestTubeGame.STONKS_MODIFIED.get_width()//2,TestTubeGame.HEIGHT//5*1 - TestTubeGame.STONKS_MODIFIED.get_height()//2))
        TestTubeGame.WINDOW.blit(TestTubeGame.FORTNITE_MODIFIED, (TestTubeGame.WIDTH//5*4 - TestTubeGame.FORTNITE_MODIFIED.get_width()//2,TestTubeGame.HEIGHT//5*4 - TestTubeGame.FORTNITE_MODIFIED.get_height()//2))
        if TestTubeGame.restart_button.draw_button():
            self.Menu_Number = 0

        keys = pygame.key.get_pressed()
        if keys[pygame.K_q] and self.Kinput == True:
            self.Kinput = False
            self.Menu_Number = 0
        elif self.Kinput == False and keys[pygame.K_q] == False:
            self.Kinput = True






    def isclicked(self, rect):

            # Getting the coordinates of the player's mouse
            pos = pygame.mouse.get_pos()
            click = pygame.mouse.get_pressed()
            if rect.collidepoint(pos[0], pos[1]) and click[0] == 1 and self.Minput == True:
                self.Minput = False
                return True
            elif self.Minput == False and click[0] == 0:
                self.Minput = True
                return False
            else:
                return False














