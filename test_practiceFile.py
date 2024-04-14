import unittest
import app
import practiceFile

class TestApp(unittest.TestCase):

    def test_testAdd(self):
        self.assertEqual(practiceFile.testAdd(7,3), 10)
        self.assertEqual(practiceFile.testAdd(-1,1), 0)
        self.assertEqual(practiceFile.testAdd(-1,-1), -2)



    def test_testDivide(self):
        self.assertEqual(practiceFile.testDivide(5, 2), 2.5)
        self.assertEqual(practiceFile.testDivide(5, -2), -2.5)
        self.assertEqual(practiceFile.testDivide(-5, -2), 2.5)

        # self.assertRaises(ValueError, practiceFile.testDivide, 10, 0)
        with self.assertRaises(ValueError):
            practiceFile.testDivide(10, 0)

if __name__ == '__main__':
    unittest.main()