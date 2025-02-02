def check_number(n):
    if n > 0:
        return "Positive"
    elif n < 0:
        return "Negative"
    else:
        return "Zero"

num = float(input("Enter a number: "))
result = check_number(num)
print("The number is:", result)
