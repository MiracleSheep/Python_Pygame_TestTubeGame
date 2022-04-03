# This is the main class for the test tube game. It is responsible for all the interactions and setting up the game.

#importing classes
import tube
import color
import main
import random

#Declaring the class
class Game:

    # init method
    def __init__(self, difficulty, tubes):
        # variable for storing all the tubes
        self.tubearray = self.settubes(difficulty, tubes)

        # calling the function to create tubes

    # method to start the game
    def startgame(self):
        pass

    # method to fill the array with tubes
    def settubes(self, difficulty, tubes):
        # deciding on the number of colours
        colournum = difficulty

        #checking if the difficulty value is too high
        if colournum > 10:
            colournum = 10

        # this array is for the number of any given colour
        # the total number of colour units allowed for each colour are stored in this array
        colourlist = [main.VOLUME] * colournum

        # initializing tubearray
        tubearray = [0] * tubes

        # Calculating the number of empty tubes that should exist
        emptytubes = int(round(tubes/5))
        if emptytubes < 1:
            emptytubes = 1


        # filling tube arrray with test tube objects
        for x in range(0,tubes):
            tubearray[x] = tube.TestTube(self.fillstack(colourlist))

        # filling the array with empty testubeobjescts
        for x in range(0, emptytubes):
            tubearray.append(tube.TestTube(list()))

        return tubearray

    #method to fill a stack with colours
    def fillstack(self, colourlist):

        stack = [color.Colour(main.WHITE)] * main.VOLUME

        for x in range(0,main.VOLUME):

            while True:
                cnum = random.randint(0,len(colourlist) - 1)
                if colourlist[cnum] > 0:
                    colourlist[cnum] = colourlist[cnum] - 1
                    break

            stack[x] = color.Colour(main.DIFFICULTY_ORDER[cnum])

        return stack

    # method to fill stack with nothing
    def emptystack(self):
        array = [0]*main.VOLUME
        return array

    # method to do a colour transaction between two test tubes
    def movecolour(self,initial,final):

        istherespace = True
        while istherespace:
            if self.tubearray[initial].topcolour().colour == self.tubearray[final].topcolour().colour or self.tubearray[final].isempty():
                if self.tubearray[final].checkvolume() < main.VOLUME:
                    movecolour = self.tubearray[initial].topcolour()
                    self.tubearray[initial].removecolor(movecolour)
                    self.tubearray[final].addcolor(movecolour)
                else:
                    istherespace = False
            else:
                istherespace = False


    # method to detect if a game is won
    def iswon(self):
        for x in range(0,len(self.tubearray)):
            if self.tubearray[x].iscomplete() == False:
                return False
        return True


