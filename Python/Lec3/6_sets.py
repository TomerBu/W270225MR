# creating sets

s1 = set() #empty set


# set from items:
s2 = {1, 2, 3, 6}


my_list = ['a', 'b', 'c']
# convert list to set
s3 = set(my_list)

# create a set from string:
s4 = set('hello') # {'h', 'e', 'l', 'o'}


# set methods:
s = {1, 2, 3, 4, 5}


s.add(6) # added
s.add(6) # rejected

s.update({7, 8, 9}) 
print(s) # {1, 2, 3, 4, 5, 6, 7, 8, 9}

if 7 in s:
    s.remove(7) # raises KeyError if item does not exist!

# remove if exists, does not raise error
s.discard(8)