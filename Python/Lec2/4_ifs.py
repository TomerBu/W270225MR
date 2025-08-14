grade = int(input("Enter your grade: "))


if grade > 56:
    print("עברת את המבחן")
else:
    print("לא עברת את המבחן")


# short if/else syntax:

print("עברת את המבחן" if grade > 56 else "לא עברת את המבחן")