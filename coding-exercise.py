# Find the Maximum and Minimum Elements in a List
# Write a Python function to find the maximum and minimum elements in a given list.
# Input: [3, 1, 4, 1, 5, 9]
# Output: (9, 1)


#Using Function
def find_min_max(number):
    maximum = number[0]
    minimum = number[0]
    for n in number:
        if n > maximum:
            maximum = n

        if n < minimum:
            minimum = n

    return maximum, minimum
number = [3, 1, 4, 1, 5, 9]
result = find_min_max(number)
print(result)

#Without function
number = [3, 1, 4, 1, 5, 9]
maximum = number[0]
minimum = number[0]
for n in number:
    if n > maximum:
        maximum = n

    if n < minimum:
        minimum = n
print((maximum, minimum))

# Remove Duplicates from a List
# Write a Python function to remove duplicates from a list while preserving the order.
# Input: [1, 2, 2, 3, 4, 4, 5]
# Output: [1, 2, 3, 4, 5]

#Without function
number: [1, 2, 2, 3, 4, 4, 5]
result = []
for n in number:
    if n not in result:
        result.append(n)
print(result)

#With function
def remove_duplicate(number):
    for n in number:
        if n not in result:
           result.append(n)
    return result
number: [1, 2, 2, 3, 4, 4, 5]
result = remove_duplicate(number)
print(result)




# Find the Intersection of Two Lists
# Write a Python function to find the intersection of two lists.
# Input: [1, 2, 3, 4], [3, 4, 5, 6]
# Output: [3, 4]

list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]
result = []
for n in list1:
    if n in list2:
        result.append(n)
        print(result)
