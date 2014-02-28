from operator import add
import math


def hasRemainder(n):
  return (n - int(n)) > 0

def isPrime(n):
  for i in range(2,int(math.sqrt(n))+1):
    if not hasRemainder(n/float(i)):
      return False
  return True

if __name__ == '__main__':
  print reduce(add, [x for x in range(2,2000000+1) if isPrime(x)])

  # SUPER INEFFICIENT SOLUTION. Takes a super long time: 260 seconds