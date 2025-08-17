from random import choice

students = {"Mendy", "Eden", "Itay", "Yasmin", "Shani", "Shahar", "Eli", "Noam", "Tal", "Hila"}

# Convert the set to a list 
students = list(students)


winners = set()
while len(winners) < 3:
    winners.add(
        choice(students)
    )

print(winners)
