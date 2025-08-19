harry_potter_books = {
    "Philosopher's Stone": 1997,
    "Chamber of Secrets": 1998,
    "Prisoner of Azkaban": 1999,
    "Goblet of Fire": 2000,
    "Order of the Phoenix": 2003,
    "Half-Blood Prince": 2005,
    "Deathly Hallows": 2007
}

# dictionary keys:
for k in harry_potter_books.keys():
    print(k)

# dictionary values:
for v in harry_potter_books.values():
    print(v) # 1997

# dictionary values:
for name, year in harry_potter_books.items():
    print(name,":", year, sep="🍏", end="💲\n") 





person1 = {
    "name": "Harry",
    "age": 11,
}

# check if key exists in the dict:

if "name" in person1:
    print(person1["name"])


if "birthday" not in person1:
    print("birthday not set")