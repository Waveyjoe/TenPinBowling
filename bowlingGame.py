		
#File 2 (BowlingGame.py)
#This file has information about Bowling Game for which the description is provided in project assessment.

class BowlingGame:
    # Initiate game with an empty list which will hold the scores of each roll
    def __init__(self):
        self.rolls=[]

    # Append rolls list with the number of pins knocked down on each roll
    def roll(self,pins):
        # Invalid Input: Number of pins knocked over is < 0 or > 10
        if pins < 0 or pins > 10:
            raise ValueError("Input must be a whole number from 0 - 10")
        # Invalid Input: non-integer
        if not isinstance(pins, int):
            raise TypeError("Input must be a whole number from 0 - 10")
        
        self.rolls.append(pins)

    # Calculate the total score
    def score(self):
        result = 0
        rollIndex=0
        for frameIndex in range(10):
            if self.isStrike(rollIndex):
                result += self.strikeScore(rollIndex)
                rollIndex +=1
            elif self.isSpare(rollIndex):
                result += self.spareScore(rollIndex)
                rollIndex +=2
            else:
                result += self.frameScore(rollIndex)
                rollIndex +=2
        return result

    # Boolean to determine if a roll is a strike
    def isStrike(self, rollIndex):
        return self.rolls[rollIndex] == 10

    # Boolean to determine if a roll is a spare
    def isSpare(self, rollIndex):
        return self.rolls[rollIndex]+ self.rolls[rollIndex+1]==10
    
    #  Calculate the score from a strike by adding 10 + the next 2 rolls
    def strikeScore(self,rollIndex):
        return  10+ self.rolls[rollIndex+1]+ self.rolls[rollIndex+2]

    #  Calculate the score from a spare by adding 10 + the next roll
    def spareScore(self,rollIndex):
        return  10+ self.rolls[rollIndex+2]

    # Calculate the score from an open frame by adding the 2 rolls together
    def frameScore(self, rollIndex):
        return self.rolls[rollIndex] + self.rolls[rollIndex + 1]
		

#Your tasks for code parts:
#1: If there are any bugs in the code, you have to remove using debugging and run the project and test cases.
#2: Refactor the code (Improve its structure without changing external behaviour).
#3: Report everything using github commits and versioning control.


###### Important #####
# Please complete your project and all tasks according to assessment description provided in CANVAS.