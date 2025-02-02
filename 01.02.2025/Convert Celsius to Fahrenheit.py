# Function to convert Celsius to Fahrenheit
def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

# Input temperature in Celsius
celsius = float(input("Enter temperature in Celsius: "))

# Convert to Fahrenheit
fahrenheit = celsius_to_fahrenheit(celsius)

# Print result
print("Temperature in Fahrenheit:", fahrenheit)
