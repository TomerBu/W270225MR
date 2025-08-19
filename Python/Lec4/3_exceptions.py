# try:
#     x = int(input("enter a number: "))
#     # do stuff
# except ValueError:
#     print("numbers only")

try:
    x = int(input("enter a number: "))
    result = 10 / x
    print(f"Result: {result}")
except Exception as e:
   print("message", e)
   print("Line number", e.__traceback__.tb_lineno)
   print("File info", e.__traceback__.tb_frame)

print("Good bye")