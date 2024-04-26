		
#File 2 (BowlingGame.py)
#This file has information about Bowling Game for which the description is provided in project assessment.

class BowlingGame:
    # 
    def __init__(self):
        '''Initiate game with an empty 
        list which will hold the scores 
        of each roll'''
        self.rolls=[]

    # 
    def roll(self,pins):
        '''Append rolls list with the 
        number of pins knocked down on
         each roll, input must be whole number from 0 - 10'''
        # Invalid Input Catch: Number of pins knocked over is < 0 or > 10
        if pins < 0 or pins > 10:
            raise ValueError("Input must be a whole number from 0 - 10")
        # Invalid Input Catch: non-integer
        if not isinstance(pins, int):
            raise TypeError("Input must be a whole number from 0 - 10")
        self.rolls.append(pins)

     
    def score(self):
        '''Calculate the total score'''
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

    def isStrike(self, rollIndex):
        '''Function that returns a boolean to determine if a roll is a strike'''
        return self.rolls[rollIndex] == 10

    def isSpare(self, rollIndex):
        '''Function that returns a boolean to determine if a roll is a spare'''
        return self.rolls[rollIndex]+ self.rolls[rollIndex+1]==10
    
  
    def strikeScore(self,rollIndex):
        '''Calculate the score from a strike by adding 10 + the next 2 rolls'''
        return  10+ self.rolls[rollIndex+1]+ self.rolls[rollIndex+2]

    def spareScore(self,rollIndex):
        '''Calculate the score from a spare by adding 10 + the next roll'''
        return  10+ self.rolls[rollIndex+2]

    def frameScore(self, rollIndex):
        '''Calculate the score from an open frame by adding the 2 rolls together'''
        return self.rolls[rollIndex] + self.rolls[rollIndex + 1]
		

#Your tasks for code parts:
#1: If there are any bugs in the code, you have to remove using debugging and run the project and test cases.
#2: Refactor the code (Improve its structure without changing external behaviour).
#3: Report everything using github commits and versioning control.


###### Important #####
# Please complete your project and all tasks according to assessment description provided in CANVAS.