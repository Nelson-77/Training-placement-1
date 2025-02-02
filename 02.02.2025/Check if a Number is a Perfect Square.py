import math

def is_perfect_square(n):
    return math.isqrt(n) ** 2 == n

num = int(input("Enter a number: "))
if is_perfect_square(num):
    print(num, "is a perfect square")
else:
    print(num, "is not a perfect square")
