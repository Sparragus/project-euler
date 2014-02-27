for a in range(0,333):
  for b in range(a+1,500):
    c = 1000 - a - b
    if c > b:
      if (a + b + c)==1000 and (a**2 + b**2) == c**2:
        print a*b*c