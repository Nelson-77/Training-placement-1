def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

fahrenheit = float(input("Enter temperature in Fahrenheit: "))
celsius = fahrenheit_to_celsius(fahrenheit)
print("Temperature in Celsius:", celsius)
