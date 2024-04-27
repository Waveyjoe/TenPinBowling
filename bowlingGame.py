		
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
        '''
        Append rolls list with the 
        number of pins knocked down on
        each roll.

        Args:
            pins(int): 
                The number of pins knocked down in a roll.

        Raises:
            ValueError: 
                If number of pins is below 0 or above 10.
            TypeError: 
                If pins is not an integer.
        '''

        # Invalid Input Catch: Number of pins knocked over is < 0 or > 10
        if pins < 0 or pins > 10:
            raise ValueError("Input must be a whole number from 0 - 10")
        # Invalid Input Catch: non-integer
        if not isinstance(pins, int):
            raise TypeError("Input must be a whole number from 0 - 10")
        # Append pins to rolls list
        self.rolls.append(pins)

     
    def score(self):
        '''
        Calculate the total score for the game.
        
        Args: 
            None, runs functions on the rolls list to calculate total score.

        Return:
            int: The final score of the game after points are calculated.
        '''
        
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
        '''
        Function that returns a boolean to determine if a roll is a strike
        
        Args: 
            rollIndex(int): The index of the roll in the rolls list
        
        Returns:
            boolean: True if the roll at the specified index is a strike, otherwise false.
        '''
        return self.rolls[rollIndex] == 10

    def isSpare(self, rollIndex):
        '''
        Function that returns a boolean to determine if a roll is a spare
        
        Args: 
            rollIndex(int): The index of the roll in the rolls list

        Returns:
            boolean: True if the roll at the specified index is a spare, otherwise false.
        '''
        return self.rolls[rollIndex]+ self.rolls[rollIndex+1]==10
    
  
    def strikeScore(self,rollIndex):
        '''
        Calculate the score from a strike
        
        Args:
            rollIndex(int): The index of the roll in the rolls list.

        Returns:
            integer: The score for the frame; 10 + the scores for following 2 rolls

        '''
        return  10+ self.rolls[rollIndex+1]+ self.rolls[rollIndex+2]

    def spareScore(self,rollIndex):
        '''
        Calculate the score from a spare

        Args:
            rollIndex(int): The index of the roll in the rolls list.

        Returns:
            integer: The score for the frame; 10 + the scores for following roll
        
        '''
        return  10+ self.rolls[rollIndex+2]

    def frameScore(self, rollIndex):
        '''
        Calculate the score from an open frame by adding the 2 rolls together

        Args:
            rollIndex(int): The index of the roll in the rolls list.

        Returns:
            integer: The score for the frame; sum of both rolls.
        
        '''
        return self.rolls[rollIndex] + self.rolls[rollIndex + 1]
		

#Your tasks for code parts:
#1: If there are any bugs in the code, you have to remove using debugging and run the project and test cases.
#2: Refactor the code (Improve its structure without changing external behaviour).
#3: Report everything using github commits and versioning control.


###### Important #####
# Please complete your project and all tasks according to assessment description provided in CANVAS.