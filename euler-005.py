def hasRemainder(n):
  return n%1 > 0

if __name__ == '__main__':
  found = False
  n = 20
  divisors = range(11,20+1)

  while not found:
    print "Testing: " + str(n)
    if n%3 != 0 or n%5 != 0 or n%7 != 0:
      n += 20
    elif True in map(hasRemainder, map(lambda x: n/float(x), divisors)):
      n += 20
    else:
      found = True
  print "Found: " + str(n)