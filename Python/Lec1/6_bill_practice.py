"""
יש לקלוט סכום של חשבון במסעדה.
יש לקלוט אחוז טיפ שרוצים להשאיר.
יש לקלוט את כמות הסועדים.
הדפיסו כמה כל אחד צריך לשלם.
הדפיסו כמה הסכום כולל הטיפ.
הדפיסו את סכום הטיפ שיש להשאיר.
"""

# inputs:
bill = float(input("Enter the bill amount: "))
tip_percentage = int(input("Enter the tip percentage: "))
num_diners = int(input("Enter the number of diners: "))

# calculations:
tip_amount = bill * tip_percentage // 100
total_amount = bill + tip_amount
total_per_diner = total_amount / num_diners

# outputs:
print(f"Total per diner: {total_per_diner:.2f}")
print(f"Total amount including tip: {total_amount:.2f}")
print(f"Total tip amount: {tip_amount}")