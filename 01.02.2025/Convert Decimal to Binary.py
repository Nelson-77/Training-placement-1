def decimal_to_binary(n):
    return bin(n).replace("0b", "")

decimal_number = int(input("Enter a decimal number: "))
binary_number = decimal_to_binary(decimal_number)
print("Binary representation of", decimal_number, "is:", binary_number)
