def f(x):
    return x**2

def derivative(x):
    h = 1./1000.
    rise = f(x + h) - f(x)
    run = h
    slope = rise / run
    return slope

def integral (startingx,endingx,numberofRectangles):
    width = (endingx - startingx)/numberofRectangles
    runningSum = 0
    for i in range(numberofRectangles):
        height = f(startingx + i*width)
        area = height * width
        runningSum += area
    return runningSum
