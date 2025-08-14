# list comprehension

"""
list of squares:
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
"""

squares = []

for i in range(10):
    squares += [i**2]

print(squares)

print([n**2 for n in range(10)])


numbers = [i for i in range(10)]

print(numbers) #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]