def isPalindrome(word):
  l = len(word)
  for i in range(0,l/2):
    if word[i] != word[ -(i+1) ]:
      return False

  return True


if __name__ == "__main__":
  largestPalindromeProduct = 0
  for a in range(100,1000):
    for b in range(100,1000):
      if isPalindrome(str(a*b)):
        if (a*b) > largestPalindromeProduct:
          largestPalindromeProduct = a*b

  print largestPalindromeProduct