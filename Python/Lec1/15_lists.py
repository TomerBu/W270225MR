fruit = ["🍏", "🍐", "🍊", "🍋", "🍌", "🍉", "🍇", "🍓", "🍈", "🍒", "🍑", "🍍"]

# loop 3 times
for i in range(3):
    print(i) # 0, 1, 2


# for f in fruit list:
for f in fruit:
    print(f) 

name = 'tomer'
for letter in name:
    print(letter)  # t, o, m, e, r



for i in range(0, 30, 2):
    print(i) #
     


for i in range(1 ,5):
    print(i) # 1, 2, 3, 4
     


number = 1967

# if '7' in str(number):
#     print("Boom")

for digit in str(number):
    if (digit == '7'):
        print("Boom")