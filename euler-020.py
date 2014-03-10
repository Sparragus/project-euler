factorial = lambda n: 1 if n==0 else n * factorial(n-1)
sum_of_factorial = lambda n: reduce(lambda a,b: int(a) + int(b), str( factorial(n) ) )
print sum_of_factorial(100)