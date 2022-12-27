new_list = [1, 2, 3]

# accessing values
result = new_list[0]

# searching in the list
if 1 in new_list:
    print(True)

for n in new_list:
    if n == 1:
        print(True)
        break


# appending things to a list
numbers = []
len(numbers)  # should return 0, because list is empty

numbers.append(2)  # add's two to the end of the list
numbers.append(200)
len(numbers)
print(numbers)
