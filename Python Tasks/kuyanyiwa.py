import math

num = 1
current_number = num ** 2

while current_number < 20:
    num = int(input(''))
    current_number = num ** 2
    print(f"The square of {current_number} is {math.sqrt(current_number):.2f}.")
