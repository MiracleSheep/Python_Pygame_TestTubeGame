# This is the main class for the test tube game. It is responsible for all the interactions and setting up the game.

#importing classes
import tube
import color
import TestTubeGame
import random
import copy

#Declaring the class
class Game:

    # init method
    def __init__(self, difficulty, tubes):
        # variable for storing all the tubes
        self.backup  = self.settubes(difficulty, tubes)
        self.tubearray = copy.deepcopy(self.backup)
        #variable for the tubes that have been selected
        self.selected = []

    # Method that restarts the game and restores the initial colour setup
    def restart(self):
        self.tubearray = copy.deepcopy(self.backup)


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
        colourlist = [TestTubeGame.VOLUME] * colournum

        # initializing tubearray
        tubearray = [0] * tubes

        # Calculating the number of empty tubes that should exist
        emptytubes = int(round(tubes/5))
        if emptytubes < 2:
            emptytubes = 2


        # filling tube arrray with test tube objects
        for x in range(0,tubes):
            tubearray[x] = tube.TestTube(self.fillstack(colourlist))

        # filling the array with empty testubeobjescts
        for x in range(0, emptytubes):
            tubearray.append(tube.TestTube(list()))

        return tubearray

    # Method that returns the number of test tubes that have been selected
    def numselected(self):
        return len(self.selected)

    # Returns the number of test tubes not selected
    def numunselected(self):
        return len(self.tubearray) - len(self.selected)


    # Method that deselects a test tube
    def deselect(self, x):
        self.selected.remove(x)

    # method that delects all the test tubes
    def deselectall(self):
        self.selected.clear()

    # Method that selects a test tube
    def select(self, x):
        self.selected.append(x)




    #method to fill a stack with colours
    def fillstack(self, colourlist):

        stack = [color.Colour(TestTubeGame.WHITE)] * TestTubeGame.VOLUME

        for x in range(0, TestTubeGame.VOLUME):

            while True:
                cnum = random.randint(0,len(colourlist) - 1)
                if colourlist[cnum] > 0:
                    colourlist[cnum] = colourlist[cnum] - 1
                    break

            stack[x] = color.Colour(TestTubeGame.DIFFICULTY_ORDER[cnum])

        return stack

    # method to fill stack with nothing
    def emptystack(self):
        array = [0] * TestTubeGame.VOLUME
        return array

    # method to do a colour transaction between two test tubes
    def movecolour(self,initial,final):
        first = self.tubearray.index(initial)
        last = self.tubearray.index(final)


        istherespace = True
        while istherespace:
            if self.tubearray[first].iscoloursame(self.tubearray[last].topcolour()) or self.tubearray[last].isempty():
                if self.tubearray[last].checkvolume() < TestTubeGame.VOLUME:
                    movecolour = self.tubearray[first].topcolour()
                    if not self.tubearray[first].isempty():
                        istherespace = self.tubearray[first].removecolor(movecolour)
                        istherespace = self.tubearray[last].addcolor(movecolour)
                    else:
                        istherespace = False

                else:
                    istherespace = False
            else:
                istherespace = False

        self.deselectall()


    # method to detect if a game is won
    def iswon(self):
        for x in range(0,len(self.tubearray)):
            if self.tubearray[x].iscomplete() == False:
                return False
        return True

    #Method to count the total number of tubes
    def number_of_tubes(self):
        return len(self.tubearray)




