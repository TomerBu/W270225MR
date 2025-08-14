from random import randint


x = randint(0, 400) # 400
y = randint(0, 400) # 200
z = randint(0, 400) # 100


# x = 400
# y = 200

if x > y:
    x, y  = y, x

if y > z:
    y, z = z, y

if x > y:
    x, y = y, x
