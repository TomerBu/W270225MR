from random import randint

rand_number = randint(1, 100)
print(f"psstt then number is: {rand_number}")

attempts = 0 
win = False
while attempts < 5 and not win:
    guess = int(input("Enter your guess:"))
    attempts += 1
    if guess < rand_number:
        print("HIGHER!")
    elif guess > rand_number:
        print("LOWER!")
    else:
        print("CORRECT!")
        win = True

if win:
        print(f"Congratulations! You've guessed the number in {attempts} attempts.")
else:
        print(f"Sorry, you've used all your attempts. The number was {rand_number}.")
