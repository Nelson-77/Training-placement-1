# Function to check if a number is even or odd
def is_even(n):
    return n % 2 == 0

# Input number
num = int(input("Enter a number: "))

# Check if even or odd
if is_even(num):
    print(num, "is an even number")
else:
    print(num, "is an odd number")
