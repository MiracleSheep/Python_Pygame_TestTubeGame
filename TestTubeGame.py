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
import gui




# Declaring constants of the game

# Width of the screen
WIDTH = 1000
# Length of the screen
HEIGHT = 1000
# The size of the test tubes
VOLUME = 4
# Window of the game
WINDOW = pygame.display.set_mode((WIDTH,HEIGHT))
#The percent of the screen that the tubes should take up
PERCENT_TUBE = 0.35
# The ratio of height to width (blank:one)
HWR = 4
# Colours
WHITE = pygame.Color(255,255,255)
RED = pygame.Color(255,0,0)
BLUE = pygame.Color(0, 0,255)
PURPLE = pygame.Color(127,0,255)
PINK = pygame.Color(255,0,255)
YELLOW = pygame.Color(255,255,0)
AQUA = pygame.Color(0,255,255)
LIGHT_BLUE = pygame.Color(0,128,255)
ORANGE = pygame.Color(255,128,0)
GREEN = pygame.Color(0,153,0)
LIGHT_GREEN = pygame.Color(128,255,0)
# A list of all colours that can be in a test tube
# For the testube object
DIFFICULTY_ORDER = [RED, BLUE, GREEN, YELLOW, PINK, PURPLE, ORANGE, AQUA, LIGHT_GREEN, LIGHT_BLUE]
COLOUR_NAMES = ["Red", "Blue", "Green", "Yellow", "Pink", "Purple", "Orange", "Aqua", "Light_Green", "Light_Blue"]
# A value that sets the FPS of the game
FPS = 60
# grabbing an image from the assets folder using the os library to get the path to the image
TEST_TUBE_IMAGE = pygame.image.load(os.path.join('assets','test_tube.png'))
TEST_TUBE = pygame.transform.scale(TEST_TUBE_IMAGE, (55, 401))

# Setting the windo name of pygame
pygame.display.set_caption("TestTubeGame")


# A function to draw the windo and add a white background
def draw_window():


    WINDOW.fill(WHITE)
    WINDOW.blit(TEST_TUBE_IMAGE, (300,100))



# Main function for the program
def main():

    # Declaring a gui object
    Graphical_User_Interface = gui.Gui()

    # Declaring a clock object
    clock = pygame.time.Clock()

    # This variable is responsible for any moving background
    background_position_x = 0

    # This is the while loop that controls the game
    run = True
    while run:
        # Making the while loop run at a specific speed
        clock.tick(FPS)

        # making a for loop to iterate through all the current occuring events of pygame
        for event in pygame.event.get():
            # checking if a quit event occurs
            if event.type == pygame.QUIT:
                run = False

        # This is a row of if statements that check what the menu number is
        if Graphical_User_Interface.Menu_Number == 0:
            background_position_x = Graphical_User_Interface.opening_screen(background_position_x)
        elif Graphical_User_Interface.Menu_Number == 1:
            background_position_x = Graphical_User_Interface.pregame_menu(background_position_x)
        elif Graphical_User_Interface.Menu_Number == 2:
            Graphical_User_Interface.game_screen()
            pass

        pygame.display.update()


    pygame.quit()












    # boolcontinue = True
    # while boolcontinue:
    #
    #     # Asking the user if they would like to start a game of test tube sorting
    #     response = input("Would you like to start a game of test tube sorting?")
    #
    #     # checking what the user's response was
    #     if response == '1':
    #
    #         # starting a game loop
    #         #Asking for the difficulty of the game
    #         difficulty = input("Please enter a number for difficulty")
    #         tubes = input("Please enter a number for number of test tubes")
    #         difficulty = int(difficulty)
    #         tubes = int(tubes)
    #
    #         continuegame = True
    #         g = game.Game(difficulty,tubes)
    #         while continuegame:
    #
    #             checktubes = True
    #             while checktubes:
    #                 print("There are " + str(len(g.tubearray)) + " tubes in this game.")
    #                 check = input("Please choose a tube to check")
    #                 check = int(check)
    #
    #                 if check - 1 > len(g.tubearray) - 1 or check - 1 < 0:
    #                     print("That is not a viable number")
    #                 else:
    #                     if g.tubearray[check - 1].isempty():
    #                         print("Empty")
    #                     else:
    #                         for x in range(0,len(g.tubearray[check - 1].stack)):
    #                             for y in range(0, len(DIFFICULTY_ORDER)):
    #                                 if DIFFICULTY_ORDER[y] == g.tubearray[check - 1].stack[x].colour:
    #                                     print(COLOUR_NAMES[y])
    #
    #
    #
    #
    #                 print("Those are all the colours in that tube.")
    #                 response = input("Would you like to move on?")
    #                 if response == '1':
    #                     checktubes = False
    #                 else:
    #                     checktubes = True
    #
    #
    #             initial = input("What tube would you like to select?")
    #             final = input("What final tube would you like to select?")
    #             initial  = int(initial)
    #             final = int(final)
    #             g.movecolour(initial-1,final-1)
    #
    #
    #             if g.iswon():
    #                 print("Congratulations, you win!")
    #                 continuegame = False
    #
    #
    #
    #
    #
    #
    #
    #
    #
    #
    #
    #
    #
    #
    #     else:
    #         # asking the user if they would like to quit the program
    #         response = input("Would you like to quit the program?")
    #         if response == '1':
    #             print("Good choice. Ending this horrible game now...")
    #             boolcontinue = False
    #         else:
    #             print("Okay, I'm going to ask you the same question again you weirdo")

    pass













if __name__ == "__main__":
    main()

