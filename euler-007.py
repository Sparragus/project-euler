import math

def isPrime(n):
  if n==1: 
    return False
  for i in range(2,int(math.sqrt(n))+1):
    if (n/float(i))%1 == 0:
      return False
  return True

primes = []
i=1
while len(primes) < 10001:
  i+=1
  if isPrime(i):
    primes.append(i)

print primes[-1]