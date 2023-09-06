# 1.1 Implement a recursive function to calculate the factorial of a given number.
"""
Formula => n * (n-1)!
if n = 6 => 6 * 5! ---> 6 * 5 * 4 * 3 * 2 * 1
"""

def fact_rec(n):
  if n == 0 or n == 1:
    return 1
  else:
    return n * fact_rec(n - 1)


number = int(input("Enter a value: "))
res = fact_rec(number)

print("The factorial of {} is {}".format(number, res))
