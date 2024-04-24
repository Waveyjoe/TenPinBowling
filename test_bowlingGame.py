#File 1 (Test.py)
#This file has information about test cases which you need to test.

import unittest
import bowlingGame

class TestBowlingGame(unittest.TestCase):


    def setUp(self):
        self.game = bowlingGame.BowlingGame()


    def testGutterGame(self):
        for i in range(0, 20):
            self.game.roll(0)
        self.assertEqual(self.game.score(), 0)


    def testAllOnes(self):
        self.rollMany(1, 20)
        self.assertEqual(self.game.score(), 20)

    def testOneSpare(self):
        self.game.roll(5)
        self.game.roll(5)
        self.game.roll(3)
        self.rollMany(0,17)
        self.assertEqual(self.game.score(), 16)


    def testOneStrike(self):
        self.game.roll(10)
        self.game.roll(4)
        self.game.roll(3)
        self.rollMany(0,16)
        self.assertEqual(self.game.score(), 24)


    def testConsecutiveStrikes(self):
        self.game.roll(10)
        self.game.roll(10)
        self.game.roll(4)
        self.game.roll(3)
        self.rollMany(0,16)
        self.assertEqual(self.game.score(), 48)


    def testMixedStrikesAndSpares(self):
        self.game.roll(10)
        self.game.roll(7)
        self.game.roll(3)
        self.game.roll(4)
        self.game.roll(3)
        self.rollMany(0,15)
        self.assertEqual(self.game.score(), 41)
        

    def testPerfectGame(self):
        self.rollMany(10,12)
        self.assertEqual(self.game.score(), 300)


    def testAllSpares(self):
        self.rollMany(5,21)
        self.assertEqual(self.game.score(), 150)
    

    def rollMany(self, pins,rolls):
        for i in range(rolls):
            self.game.roll(pins)



if __name__ == '__main__':
    unittest.main()