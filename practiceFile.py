def testAdd(a, b):
        return a + b

def testDivide(a, b):
        
        if b == 0:
            raise ValueError('Can not divide by zero')
        return a / b
