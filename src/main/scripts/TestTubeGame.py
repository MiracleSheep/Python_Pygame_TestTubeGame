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
import pyautogui
import gui
import button
import menu_floater




# Width and Length of the screen


WIDTH,HEIGHT = pyautogui.size()
# the percent of the test tube width that the liquid will take up
SQUARE_WIDTH = 0.85
# the percent of the test tube height that the liquid will take up
SQUARE_HEIGHT = 0.90
# how many colours in each test tube
VOLUME = 4
# Window of the game
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT),pygame.FULLSCREEN)
#The percent of the screen that the tubes should take up
PERCENT_TUBE = 0.20
# Percent of the screen height taken up by the game
PERCENT_GAME_HEIGHT = 0.75
# PERCENT_GAME_WIDTH = 0.90
# Height buffer between test tubes
BUFFER = 0.5
# The ratio of height to width (blank:one)
HWR = 4
#The percentage of area that the border will be more than the test tube
BORDER_AREA = 0.40

# Declaring constants of the game

#fonts
pygame.font.init()
BUTTON_FONT = pygame.font.SysFont('Corbel', 30)


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

# Setting the windo name of pygame
pygame.display.set_caption("TestTubeGame")

#images
# Loading in the miage that will be used as a background for the opneing screen
TITLE_IMAGE = pygame.image.load(os.path.join('../../../assets', 'Title.png'))
TITLE_IMAGE_MODIFIED = pygame.transform.scale(TITLE_IMAGE, (WIDTH * 0.4, HEIGHT * 0.3))
TEST_TUBE_ROW_IMAGE = pygame.image.load(os.path.join('../../../assets', 'TestTubeGame_TestTubeRow.png'))
TEST_TUBE_OPENING_SCREEN_IMAGE = pygame.transform.scale(TEST_TUBE_ROW_IMAGE, (WIDTH, HEIGHT))
TEST_TUBE_IMAGE = pygame.image.load(os.path.join('../../../assets', 'test_tube_better.jpeg'))
DIFFICULTY_RAW = pygame.image.load(os.path.join('../../../assets', 'Difficulty.png'))
NUMBER_OF_UNDOS_RAW = pygame.image.load(os.path.join('../../../assets', 'Number_of_Undos.png'))
DIFFICULTY_MODIFIED = pygame.transform.scale(DIFFICULTY_RAW,(WIDTH*0.2, HEIGHT*0.1))
NUMBER_OF_UNDOS_MODIFIED = pygame.transform.scale(NUMBER_OF_UNDOS_RAW,(WIDTH*0.2, HEIGHT*0.1))
TUBE_RAW = pygame.image.load(os.path.join('../../../assets', 'Tube.png'))
TUBE1_RAW = pygame.image.load(os.path.join('../../../assets', 'Tube1.png'))
TUBE2_RAW = pygame.image.load(os.path.join('../../../assets', 'tube2.png'))
TUBE3_RAW = pygame.image.load(os.path.join('../../../assets', 'tube3.png'))
TUBE4_RAW = pygame.image.load(os.path.join('../../../assets', 'tube4.png'))
WON_RAW = pygame.image.load(os.path.join('../../../assets', 'You_Win.png'))
AMONGUS_RAW = pygame.image.load(os.path.join('../../../assets', 'Amongus.jpeg'))
CONFET_RAW = pygame.image.load(os.path.join('../../../assets', 'confet.jpeg'))
HAROLD_RAW = pygame.image.load(os.path.join('../../../assets', 'harold.png'))
STONKS_RAW = pygame.image.load(os.path.join('../../../assets', 'stonks.png'))
FORNITE_RAW = pygame.image.load(os.path.join('../../../assets', 'plzbepng.png'))
WON_MODIFIED = pygame.transform.scale(WON_RAW,(WIDTH*0.2, HEIGHT*0.1))
CONFET_MODIFIED = pygame.transform.scale(CONFET_RAW,(WIDTH, HEIGHT))
AMONGUS_MODIFIED = pygame.transform.scale(AMONGUS_RAW,(WIDTH*0.2, HEIGHT*0.2))
HAROLD_MODIFIED = pygame.transform.scale(HAROLD_RAW,(WIDTH*0.2, HEIGHT*0.2))
STONKS_MODIFIED = pygame.transform.scale(STONKS_RAW,(WIDTH*0.2, HEIGHT*0.2))
FORTNITE_MODIFIED = pygame.transform.scale(FORNITE_RAW,(WIDTH*0.2, HEIGHT*0.2))
CONTROLS_RAW = pygame.image.load(os.path.join('../../../assets', 'Controls.png'))
INSTRUCTIONS_RAW = pygame.image.load(os.path.join('../../../assets', 'Instructions.png'))
CONTROLS_MODIFIED = pygame.transform.scale(CONTROLS_RAW,(WIDTH*0.3, HEIGHT*0.3))
INSTRUCTIONS_MODIFIED = pygame.transform.scale(INSTRUCTIONS_RAW,(WIDTH*0.5, HEIGHT*0.4))
BRICK_RAW = pygame.image.load(os.path.join('../../../assets', 'bricks.jpeg'))
BRICK_MODIFIED = pygame.transform.scale(BRICK_RAW,(WIDTH, HEIGHT))



LAB_RAW = pygame.image.load(os.path.join('../../../assets', 'lab.png'))
LAB_MODIFIED = pygame.transform.scale(LAB_RAW,(WIDTH, HEIGHT))

# These are menu floaters for the start screen
floater_1 = menu_floater.Menu_Floater(TUBE_RAW, True)
floater_2 = menu_floater.Menu_Floater(TUBE_RAW, False)
floater_3 = menu_floater.Menu_Floater(TUBE1_RAW, True)
floater_4 = menu_floater.Menu_Floater(TUBE1_RAW, False)
floater_5 = menu_floater.Menu_Floater(TUBE2_RAW, True)
floater_6 = menu_floater.Menu_Floater(TUBE2_RAW, False)
floater_7 = menu_floater.Menu_Floater(TUBE3_RAW, True)
floater_8 = menu_floater.Menu_Floater(TUBE3_RAW, False)
floater_9 = menu_floater.Menu_Floater(TUBE4_RAW, True)
floater_10 = menu_floater.Menu_Floater(TUBE4_RAW, False)




# Here are a load of buttons

# Creating the menu button
start_button = button.Button(WIDTH // 2 - (WIDTH * 0.08) // 2,HEIGHT // 7 * 3 - (HEIGHT * 0.1) // 2, WIDTH * 0.08,HEIGHT * 0.1, [0, 0, 0], "Play", [255, 255, 255], 0, 30, [255, 255, 255], False)

# These are buttons that will be used in order to detect how many colours will be used
easy_difficulty_button = button.Button((WIDTH // 4) - (WIDTH * 0.08) // 2,(HEIGHT // 7) * 2 - (HEIGHT * 0.1) // 2,WIDTH * 0.08, HEIGHT * 0.1, [255, 0, 0], "Easy",[255, 255, 255], 0, 15, [0, 0, 255], True)
medium_difficulty_button = button.Button((WIDTH // 4) * 2 - (WIDTH * 0.08) // 2,(HEIGHT // 7) * 2 - (HEIGHT * 0.1) // 2,WIDTH * 0.08, HEIGHT * 0.1, [255, 0, 0], "Medium",[255, 255, 255], 0, 15, [0, 0, 255], True)
hard_difficulty_button = button.Button((WIDTH // 4) * 3 - (WIDTH * 0.08) // 2,(HEIGHT // 7) * 2 - (HEIGHT * 0.1) // 2,WIDTH * 0.08, HEIGHT * 0.1, [255, 0, 0], "Hard",[255, 255, 255], 0, 15, [0, 0, 255], True)

# These are buttons that will be used to detect the undo limit
easy_reverse_button = button.Button((WIDTH // 4) - (WIDTH * 0.08) // 2,(HEIGHT // 7) * 4 - (HEIGHT * 0.1) // 2,WIDTH * 0.08, HEIGHT * 0.1, [255, 0, 0], "Infinite",[255, 255, 255], 0, 15, [0, 0, 255], True)
medium_reverse_button = button.Button((WIDTH // 4) * 2 - (WIDTH * 0.08) // 2,(HEIGHT // 7) * 4 - (HEIGHT * 0.1) // 2,WIDTH * 0.08, HEIGHT * 0.1, [255, 0, 0], "Ten",[255, 255, 255], 0, 15, [0, 0, 255], True)
hard_reverse_button = button.Button((WIDTH // 4) * 3 - (WIDTH * 0.08) // 2,(HEIGHT // 7) * 4 - (HEIGHT * 0.1) // 2,WIDTH * 0.08, HEIGHT * 0.1, [255, 0, 0], "Five",[255, 255, 255], 0, 15, [0, 0, 255], True)

# This is the continue button
continue_button = button.Button((WIDTH // 12) * 10 - (WIDTH * 0.2) // 2,(HEIGHT // 7) * 6 - (HEIGHT * 0.1) // 2,WIDTH * 0.2, HEIGHT * 0.1, [255, 0, 0], "Start",[255, 255, 255], 0, 15, [255, 255, 255], False)

# This is the button that will be used for the how to play screen
tutorial_button = button.Button((WIDTH // 12) * 2 - (WIDTH * 0.2) // 2,(HEIGHT // 7) * 6 - (HEIGHT * 0.1) // 2,WIDTH * 0.2, HEIGHT * 0.1, [255, 0, 0], "How to play",[255, 255, 255], 0, 15, [255, 255, 255], False)

#restart button
restart_button = button.Button((WIDTH // 2) - (WIDTH * 0.3) // 2,(HEIGHT // 8) * 5 - (HEIGHT * 0.1) // 2,WIDTH * 0.3, HEIGHT * 0.1, [0, 255, 0], "Return To Start",[255, 255, 255], 0, 50, [255, 255, 255], False)

#return button
return_button = button.Button((WIDTH // 2) - (WIDTH * 0.2) // 2,(HEIGHT // 8) * 7 - (HEIGHT * 0.1) // 2,WIDTH * 0.2, HEIGHT * 0.1, [121, 17, 186], "Return",[255, 255, 255], 0, 50, [255, 255, 255], False)


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
        elif Graphical_User_Interface.Menu_Number == 3:
            Graphical_User_Interface.tutorial_screen()
        elif Graphical_User_Interface.Menu_Number == 4:
            Graphical_User_Interface.victory_screen()

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

