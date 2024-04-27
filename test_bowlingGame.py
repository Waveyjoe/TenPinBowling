#File 1 (Test.py)
#This file has information about test cases which you need to test.

import unittest
import bowlingGame

class TestBowlingGame(unittest.TestCase):


    def setUp(self):
        '''Set up testing object'''
        self.game = bowlingGame.BowlingGame()


    def testGutterGame(self):
        '''Test that a game with 0 pins knocked down is calculated correctly'''
        for i in range(0, 20):
            self.game.roll(0)
        self.assertEqual(self.game.score(), 0)


    def testAllOnes(self):
        '''Test that a game with 1 pin knocked down per roll is calculated correctly'''
        self.rollMany(1, 20)
        self.assertEqual(self.game.score(), 20)

    def testOneSpare(self):
        '''Test that spares are calculated correctly'''
        self.game.roll(5)
        self.game.roll(5)
        self.game.roll(3)
        self.rollMany(0,17)
        self.assertEqual(self.game.score(), 16)


    def testOneStrike(self):
        '''Test that strikes are calculated correctly'''
        self.game.roll(10)
        self.game.roll(4)
        self.game.roll(3)
        self.rollMany(0,16)
        self.assertEqual(self.game.score(), 24)


    def testConsecutiveStrikes(self):
        '''Test that consecutive strikes are calculated correctly'''
        self.game.roll(10)
        self.game.roll(10)
        self.game.roll(4)
        self.game.roll(3)
        self.rollMany(0,16)
        self.assertEqual(self.game.score(), 48)


    def testMixedStrikesAndSpares(self):
        '''Test that strikes followed by spares are calculated correctly'''
        self.game.roll(10)
        self.game.roll(7)
        self.game.roll(3)
        self.game.roll(4)
        self.game.roll(3)
        self.rollMany(0,15)
        self.assertEqual(self.game.score(), 41)
        
    def testRollInvalidInput(self):
        '''Test that invalid inputs are handled nicely'''
        # Invalid Input: Number of pins knocked over is < 0 or > 10
        with self.assertRaises(ValueError):
            self.game.roll(11)
        with self.assertRaises(ValueError):
            self.game.roll(-1)
        # Invalid Input: Input is not an integer
        with self.assertRaises(TypeError):
            self.game.roll('a')


    def testPerfectGame(self):
        '''Test that a game in which a player gets only strikes is calculated correctly'''
        self.rollMany(10,12)
        self.assertEqual(self.game.score(), 300)


    def testAllSpares(self):
        '''Test that a game in which a player gets only spares is calculated correctly'''
        self.rollMany(5,21)
        self.assertEqual(self.game.score(), 150)

    

    def rollMany(self, pins, rolls):
        '''Function to simulate multiple rolls without having to write seperate lines for each'''
        for i in range(rolls):
            self.game.roll(pins)
        

if __name__ == '__main__':
    unittest.main()