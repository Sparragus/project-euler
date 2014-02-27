def fibonacci(n):
  fibo = [1,2]
  while fibo[-1] <= n:
    fibo.append(fibo[-1] + fibo[-2])
  return fibo

if __name__ == "__main__":
  fibo = fibonacci(4000000)
  filtered = filter(lambda x: x%2 == 0, fibo)
  reduced = reduce(lambda x, y: x+y, filtered)
  print reduced