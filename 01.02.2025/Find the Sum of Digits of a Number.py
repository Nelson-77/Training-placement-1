def sum_of_digits(n):
    total = 0
    while n > 0:
        total += n % 10
        n //= 10
    return total

num = int(input("Enter a number: "))
result = sum_of_digits(num)
print("The sum of digits is:", result)
