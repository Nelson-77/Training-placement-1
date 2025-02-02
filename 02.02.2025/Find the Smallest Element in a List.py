def find_smallest(lst):
    return min(lst)

input_list = [int(x) for x in input("Enter a list of numbers separated by spaces: ").split()]
smallest_element = find_smallest(input_list)
print("The smallest element is:", smallest_element)
