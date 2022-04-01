#########################################################################################################
#                                                                                                       #
# Date created: 2022/01/06                                                                              #
# Author: John Khalife                                                                                  #
# Description: This is a test tube sorting game in 2d graphics. It includes an algorhythim to solve it. #
#                                                                                                       #
#########################################################################################################

# Importing relevant librairies

# Library for pygame (end 2d graphics)
import pygame
import os
import game




# Declaring constants of the game

# Width of the screen
WIDTH = 400
# Length of the screen
HEIGHT = 400
# The size of the test tubes
VOLUME = 4

# Window of the game
# WINDOW = pygame.display.set_mode((WIDTH,HEIGHT))
# Colours
WHITE = (255,255,255)
RED = (255,0,0)
BLUE = (0, 0,255)
PURPLE = (127,0,255)
PINK = (255,0,255)
YELLOW = (255,255,0)
AQUA = (0,255,255)
LIGHT_BLUE = (0,128,255)
ORANGE = (255,128,0)
GREEN = (0,153,0)
LIGHT_GREEN = (128,255,0)

# A list of all colours that can be in a test tube
# For the testube object
DIFFICULTY_ORDER = [RED, BLUE, GREEN, YELLOW, PINK, PURPLE, ORANGE, AQUA, LIGHT_GREEN, LIGHT_BLUE]


# A value that sets the FPS of the game
FPS = 60
# grabbing an image from the assets folder using the os library to get the path to the image
# TEST_TUBE_IMAGE = pygame.image.load(os.path.join('assets','test_tube'))
# TEST_TUBE = pygame.transform.scale(TEST_TUBE_IMAGE, (55, 401))

# # Setting the windo name of pygame
# pygame.display.set_caption("TestTubeGame")


# A function to draw the windo and add a white background
# def draw_window():


    # WINDOW.fill(WHITE)
    # WINDOW.blit(TEST_TUBE_IMAGE, (300,100))
    # pygame.display.update()


# Main function for the program
def main():

    boolcontinue = True
    while boolcontinue:

        # Asking the user if they would like to start a game of test tube sorting
        response = input("Would you like to start a game of test tube sorting?")

        # checking what the user's response was
        if response == 1:

            # starting a game loop
            #Asking for the difficulty of the game
            difficulty = input("Please enter a number for difficulty")
            tubes = input("Please enter a number for number of test tubes")

            continuegame = True
            g = game.Game(difficulty,tubes)
            while continuegame:

                checktubes = True
                while checktubes:
                    print("There are " + g.tubearray.len() + "tubes in this game.")
                    check = input("Please choose a tube to check")









        else:
            # asking the user if they would like to quit the program
            response = input("Would you like to quit the program?")
            if response == 1:
                print("Good choice. Ending this horrible game now...")
                boolcontinue = False
            else:
                print("Okay, I'm going to ask you the same question again you weirdo")

    pass








    # # Declaring a clock object
    # clock = pygame.time.Clock()
    #
    # # This is the while loop that controls the game
    # run = True
    # while run:
    #     # Making the while loop run at a specific speed
    #     clock.tick(FPS)
    #
    #     # making a for loop to iterate through all the current occuring events of pygame
    #     for event in pygame.event.get():
    #         # checking if a quit event occurs
    #         if event.type == pygame.QUIT:
    #             run = False
    #
    #     # calling the draw windo function
    #     draw_window()
    #
    # pygame.quit()




if __name__ == "__main__":
    main()

