from random import choice
#import random

my_list = ['a', 'b', 'c', 'd']


random_letter = choice(my_list)


print(random_letter)


my_list = [1, 2, 3, 4]


# add items to the end of the list:
my_list += [5]
my_list.append(6) 



# insert items at a specific position:
my_list.insert(2, 2.5)

print(my_list) # [1, 2, 2.5, 3, 4, 5, 6]


my_list = ['apple', 'banana', 'fig']
# CRUD = create, Read, update, delete

#Read
print(my_list)
print(my_list[0])  # apple

# minus 1 from the end
print(my_list[-1])  # fig

print(my_list[1:3])  # ['banana', 'fig']


my_list = ['A', 'B', 'C']

next = my_list.pop(1) 

print(my_list)  # ['A', 'C']
print(next)     # 'B'



#del my_list[0]  # delete the first item


# crUd:

# Update:

my_list = ['👑', '💍']

my_list[0] = '👑👑'  # update the first item