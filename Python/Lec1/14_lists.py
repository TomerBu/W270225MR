my_list = ['a', 'b', 'c', 'd']

# insert at the end:(push)
my_list.append('e')
my_list += 'fg'
my_list += ['h', 'i']


my_list.insert(9, 'j')

print(my_list) #['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
