
def squared(x):
    return x ** 2

def toThePowerOfTwo(x):
    print (x ** 2) # side effect

def doNothing(x):
    pass

def sampleIfElse(x):
    if x>10:
        pass
    else:
            print ("x < 10")

##def isOdd(x):
##    return x % 2 != 0

def isOdd(x):
    return "stub you fool you"

##    if x%2 == 1:
##       return True
##    return False

def test_isOdd_0():
    assert not isOdd(0)

def test_isOdd_3():
    assert isOdd(3)

def test_isOdd_4():
    assert not isOdd(4)
    
def test_isOdd_13():
    assert isOdd(13)

def test_isOdd_14():
    assert not isOdd(14)


