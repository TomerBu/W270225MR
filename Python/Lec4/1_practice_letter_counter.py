from string import ascii_lowercase as az

counter_dict = {}

for letter in az:
    # if letter.isalpha()
    counter_dict[letter] = 0

text = """
        Mary had a little lamb, little lamb, little lamb.
        Mary had a little lamb, its fleece was white as snow.
        And everywhere that Mary went. Mary went.
       """

text_copy = text.lower().strip()

for letter in text_copy:
    if letter in az:
        counter_dict[letter] += 1

print(counter_dict)