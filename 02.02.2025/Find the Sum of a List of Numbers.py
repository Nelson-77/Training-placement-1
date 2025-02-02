def sum_of_list(lst):
    return sum(lst)

input_list = [int(x) for x in input("Enter a list of numbers separated by spaces: ").split()]
total_sum = sum_of_list(input_list)
print("The sum of the list is:", total_sum)
