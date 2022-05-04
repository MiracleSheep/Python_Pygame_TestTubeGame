# This class is responsible for creating button and adding them hwere needed

#importing neccesarry librairies
import pygame
import TestTubeGame

#Initializing the button class
class Button:

    #the initializing method
    # It will take all the sizes of the button
    def __init__(self, x,y, length, width, colour, text, textcolour):
        self.length = length
        self.width = width
        self.colour = colour
        self.text = text
        self.x = x
        self.y = y
        self.textcolour = textcolour

    #this mehod will be in charge of drawing the button
    def draw_button(self):
        #Drawing in the square
        if self.isclicked():
            pygame.draw.rect(TestTubeGame.WINDOW, [255,255,255], [self.x, self.y, self.width, self.length])
        else:
            pygame.draw.rect(TestTubeGame.WINDOW, self.colour, [self.x, self.y, self.width, self.length])

        #Drawing in the text
        # defining a font
        pygame.font.init()
        smallfont = pygame.font.SysFont('Corbel', self.width//2)
        text = smallfont.render(self.text, True, self.textcolour)
        TestTubeGame.WINDOW.blit(text, (self.x + self.width//2, self.y + self.length//2))

    # This method will be used to detect if a button is clicked
    def isclicked(self):

        # Getting the coordinates of the player's mouse
        mouse = pygame.mouse.get_pos()

        # Checking if the mouse is inside the box and if the user had pressed the mouse
        if mouse[0] >= self.x and mouse[0] <= (self.x + self.width) and mouse[1] >= self.y and mouse[1] <= self.y + self.length:
            ev = pygame.event.get()
            # proceed events
            for event in ev:
                # handle MOUSEBUTTONUP
                if event.type == pygame.MOUSEBUTTONUP:
                    return True


        return False





