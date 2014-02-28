squareOfSum = reduce(lambda a,b:a+b, range(1,101))**2
sumofSquares = reduce(lambda a,b:a+b, map(lambda x: x**2, range(1,101)))

print squareOfSum - sumofSquares