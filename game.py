# This is the main class for the test tube game. It is responsible for all the interactions and setting up the game.

#importing classes
import move
import tube
import color
import TestTubeGame
import random
import copy

#Declaring the class
class Game:

    # init method
    def __init__(self, difficulty, tubes,undos):
        # variable for backing up the colours in the game
        self.backup  = self.settubes(difficulty, tubes)
        # variable for storing all the tubes
        self.tubearray = copy.deepcopy(self.backup)
        # variable that holds all the moves in the game
        self.all_moves = []
        #variable for the tubes that have been selected
        self.selected = []
        self.infiniteundoes = False
        self.undos = undos

        if undos == 0: self.infiniteundoes = True

    # Method that restarts the game and restores the initial colour setup
    def restart(self):
        self.tubearray = copy.deepcopy(self.backup)
        self.reset()

    # method that reverses a move
    def reversemove(self):
        if self.infiniteundoes == True or self.undos > 0:
            if len(self.all_moves) > 0:
                for x in range(self.all_moves[-1].units):
                    self.forcemovecolour(self.all_moves[-1].final,self.all_moves[-1].initial)
                self.all_moves.pop()
                self.undos -= 1




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

    def reset(self):
        self.all_moves.clear()


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

    # Method that forces a colour move (for reversing)
    def forcemovecolour(self, initial, final):
        first = self.tubearray.index(initial)
        last = self.tubearray.index(final)
        movecolour = self.tubearray[first].topcolour()
        self.tubearray[first].forceremovecolor(movecolour)
        self.tubearray[last].forceaddcolor(movecolour)


    # method to do a colour transaction between two test tubes
    def movecolour(self,initial,final):
        first = self.tubearray.index(initial)
        last = self.tubearray.index(final)
        num = 0


        istherespace = True
        while istherespace:
            if self.tubearray[first].iscoloursame(self.tubearray[last].topcolour()) or self.tubearray[last].isempty():
                if self.tubearray[last].checkvolume() < TestTubeGame.VOLUME:
                    movecolour = self.tubearray[first].topcolour()
                    if not self.tubearray[first].isempty():
                        num += 1
                        istherespace = self.tubearray[first].removecolor(movecolour)
                        istherespace = self.tubearray[last].addcolor(movecolour)
                    else:
                        istherespace = False

                else:
                    istherespace = False
            else:
                istherespace = False

        self.deselectall()
        self.all_moves.append(move.Move(initial, final, num))


    # method to detect if a game is won
    def iswon(self):
        for x in range(0,len(self.tubearray)):
            if self.tubearray[x].iscomplete() == False:
                return False
        self.all_moves.clear()
        return True

    #Method to count the total number of tubes
    def number_of_tubes(self):
        return len(self.tubearray)




