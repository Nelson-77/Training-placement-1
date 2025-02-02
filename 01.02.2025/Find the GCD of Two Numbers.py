# Function to find the GCD of two numbers
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# Input numbers
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

# Calculate GCD
result = gcd(num1, num2)

# Print result
print("The GCD is:", result)
