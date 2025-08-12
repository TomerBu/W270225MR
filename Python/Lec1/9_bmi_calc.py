weight = int(input("Enter your weight in kg: "))
height = int(input("Enter your height in cm: ")) / 100 #

bmi = weight / height ** 2

if bmi < 18.5:
    print("Underweight")
elif bmi < 25:
    print("Normal weight")
elif bmi < 30:
    print("Overweight")
else:
    print("Very Overweight")
