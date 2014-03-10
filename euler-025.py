def fibo(n):
  a = 1
  b = 1
  for i in range(2,n):
    result = a + b
    b = a
    a = result
  return a

if __name__ == '__main__':
  def euler_025():
    n = 1
    while len(str(fibo(n))) < 1000:
      n += 1
    return n
  print euler_025()