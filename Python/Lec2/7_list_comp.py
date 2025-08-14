# # numbers = [i for i in range(10)]
# numbers = []

# for i in range(10):
#     numbers.append(i)

# print(numbers)


# print([i for i in range(10)])

# print([i**2 for i in range(10)])


from random import randint

random_numbers = [randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100)]

copy = [num for num in random_numbers]

even_numbers = [num for num in random_numbers if num % 2 == 0]
