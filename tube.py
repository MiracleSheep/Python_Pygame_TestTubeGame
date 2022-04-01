# importing other files
import color
import main

# This is the test tube class for the minigame.
# Things it should be capable of:
# - Drawing itself (It needs to know what colours it has)
class TestTube:

    # This function initializes the variables of the test tube
    def __init__(self, stack):
        self.volume = main.VOLUME
        self.stack = stack

    # This function is intended to count the amount of volume in the test tube
    def checkvolume(self):

        #sum will be equal to the actial volume in the stack
        sum = self.stack.len()

        # making sure that the correct volume is in the test tube
        if sum > self.volume:
            raise Exception("The volume counted is greater than the max volume.")
        elif sum < 0:
            raise Exception("The volume counted is smaller than zero.")
        return sum

    #This method checks if the most recent color is equal to the parameter
    def iscoloursame(self, rgb):
        if self.stack[-1].colour == rgb:
            return True


    # This is a function to check if a move is valid - it does this by making sure that the amount of liquid
    # to be moved to the test tube overfills the tube.
    def ismovelegal(self, rgb):
        self.checkvolume()
        if self.iscoloursame(rgb):
            return True
        else:
            return False

    # This function is meant to add a colour to the test tube
    def addcolor(self, rgb):
        if self.ismovelegal(rgb):
                self.stack.append(color.Colour(rgb))
                self.checkvolume()
        else:
            raise Exception("There was a problem adding the colours.")


    # This function is meant to remove the top colour from the test tube
    def removecolor(self, rgb):
        if self.ismovelegal(rgb):
                    self.iscoloursame(rgb)
                    self.stack.pop()
                    self.checkvolume()
        else:
            raise Exception("There was a problem subtracting the colours.")

    # This function returns the colour at the top of the stack
    def topcolour(self):
        return self.stack[-1]

    # This function returns whether or not the stack is complete
    def iscomplete(self):

        # making a for loop to check if a test tube is full of one colour or empty
        recentcolour = self.topcolour()
        if self.stack.len() == 0:
            return True
        for x in self.stack:
            if self.stack[x].colour == recentcolour:
                pass
            else:
                return False
        return True