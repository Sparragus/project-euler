def sumPowers(n):
  total = 0
  for i in range(1,n+1):
    total += i**i
  return total

if __name__ == '__main__':
  print str(sumPowers(1000))[-10:]