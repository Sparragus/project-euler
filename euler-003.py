import math

def hasDecimals(n):
  return (n - int(n)) > 0

def isPrime(n):
  for i in range(2,int(math.sqrt(n))+1):
    if not hasDecimals(n/float(i)):
      return False
  return True

def getPrimeFactors(n):
  primes = []
  if isPrime(n):
    return n
  else:
    i = 2
    while i <= n/2 and hasDecimals(n/float(i)):
      i += 1
    primes.append(i)
    primes.append(getPrimeFactors(n/i))
    return primes

if __name__ == "__main__":
  print  getPrimeFactors(600851475143)