# Function to count vowels in a string
def count_vowels(s):
    vowels = "aeiouAEIOU"
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count

# Input string
input_str = input("Enter a string: ")

# Count vowels
vowel_count = count_vowels(input_str)

# Print result
print("Number of vowels:", vowel_count)
