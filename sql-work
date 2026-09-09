# Flatten a Nested List
# Write a Python function to flatten a nested list.
# Input: [[1, 2], [3, 4], [5]]
# Output: [1, 2, 3, 4, 5]



def flatten_list(number):
    result = []
    for n in number:
        for x in n:
            result.append(x)
    return result
number = [[1, 2], [3, 4], [5]]
result = flatten_list(number)
print(result)

# Merge Two Sorted Lists
# Write a Python function to merge two sorted lists into a single sorted list.
# Input: [1, 3, 5], [2, 4, 6]
# Output: [1, 2, 3, 4, 5, 6]
def sorted_list(number):
    result = []
    for n in number:
        for x in n:
            result.append(x)
            result.sort()
    return result

number = [1, 3, 5], [2, 4, 6]
result = sorted_list(number)
print(result)

# Find All Pairs in a List that Sum to a Specific Value
# Write a Python function to find all pairs in a list that sum to a specific value.
# Input: [1, 2, 3, 4, 5], Sum=6
# Output: [(1, 5), (2, 4)]
def sum_value(number, target):
    result = []
    for i in range(len(number)):
        for j in range(i + 1, len(number)):
            if number[i] + number[j] == target:
                result.append((number[i], number[j]))
    return result
number = [1, 2, 3, 4, 5]
target = 6
print(sum_value(number, target))
