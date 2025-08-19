# new dictionary
dict1 = {}
dict2 = dict()

# must use "" for keys
dict3 = {
    "name":"dave",
    "age":20
}

dict4 = dict(name="dave", age=20)

# read values from dict:
print(dict3["name"]) #dave
print(dict3.get("age"))#20


# access non-exiting value:
print(dict3.get("id"))#None
print(dict3["id"])#raises KeyError



# update and delete:
counter_dictionary = {
    "a": 3, 
    "b": 1, 
    "c": 2
}

# update a value:
counter_dictionary["b"] = 2

# add a value:
counter_dictionary["d"] = 1

# remove a value:
del counter_dictionary["d"]
a = counter_dictionary.pop("a")

# remove a value from the end:
last_item = counter_dictionary.popitem()
# remove all items:
counter_dictionary.clear()


text = """
        Mary had a little lamb, little lamb, little lamb.
        Mary had a little lamb, its fleece was white as snow.
        And everywhere that Mary went. Mary went.
       """