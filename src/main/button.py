# This class is responsible for creating button and adding them hwere needed

#importing neccesarry librairies
import pygame
import TestTubeGame

#Initializing the button class
class Button:

    #the initializing method
    # It will take all the sizes of the button
    def __init__(self, x,y, width, length, colour, text, textcolour, br1,br2,selectedcolour, toggle):
        self.length = length
        self.width = width
        self.colour = colour
        self.text = text
        self.x = x
        self.y = y
        self.textcolour = textcolour
        self.br1 = br1
        self.br2 = br2
        self.selectedcolour = selectedcolour
        self.selected = False
        self.Minput = True
        self.toggle = toggle

    #This method selects and deselects a button
    def toggleselect(self):
            if self.toggle == True:
                if self.selected == True:
                    self.selected = False
                else:
                    self.selected = True

    #This method deselects the button
    def deselect(self):
        self.selected = False

    #this mehod will be in charge of drawing the button
    def draw_button(self):

        text = TestTubeGame.BUTTON_FONT.render(self.text, True, self.textcolour)
        #Drawing in the square
        if self.isclicked():


            pygame.draw.rect(TestTubeGame.WINDOW, [255, 255, 255], [self.x, self.y, self.width, self.length], self.br1, self.br2)
            text = TestTubeGame.BUTTON_FONT.render(self.text, True, [0, 0, 0])
            return True
        elif self.ishovering():
            pygame.draw.rect(TestTubeGame.WINDOW, [255, 255, 255], [self.x, self.y, self.width, self.length], self.br1, self.br2)
            text = TestTubeGame.BUTTON_FONT.render(self.text, True, [0, 0, 0])
        else:
            # print("self still set to " + str(self.selected))
            if self.selected == False:
                pygame.draw.rect(TestTubeGame.WINDOW, self.colour, [self.x, self.y, self.width, self.length], self.br1, self.br2)
            else:
                pygame.draw.rect(TestTubeGame.WINDOW, self.selectedcolour, [self.x, self.y, self.width, self.length], self.br1, self.br2)
            text = TestTubeGame.BUTTON_FONT.render(self.text, True, self.textcolour)




        #Drawing in the text
        textsize = text.get_size()
        TestTubeGame.WINDOW.blit(text, (self.x + (self.width - textsize[0]) // 2, self.y + (self.length - textsize[1]) // 2))
        return False

    # This method will be used to detect if a button is clicked
    def isclicked(self):

        # Getting the coordinates of the player's mouse
        pos = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        rect = pygame.Rect((self.x, self.y),(self.width, self.length))
        if rect.collidepoint(pos[0], pos[1]) and click[0] == 1 and self.Minput == True:
            self.Minput = False
            self.toggleselect()
            return True
        elif self.Minput == False and click[0] == 0:
            self.Minput = True
            return False
        else:
            return False

    #This method detects when the mouse is hovering over the button
    def ishovering(self):
        pos = pygame.mouse.get_pos()
        rect = pygame.Rect((self.x, self.y), (self.width, self.length))
        if rect.collidepoint(pos[0], pos[1]):
            return True
        else:
            return False





