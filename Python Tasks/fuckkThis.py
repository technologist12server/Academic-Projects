import math
current_number = 1
while current_number < 20:
    num = int(input(''))
    current_number = num ** 2
    if current_number >= 20:
        break
    print(f"The square of {math.sqrt(current_number)} is {current_number:.2f}.")

