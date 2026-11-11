import math
current_number = int(input('')) ** 2
while math.sqrt(current_number) < 20:
    current_number = int(input('')) ** 2
    print(f'The square of {current_number} is {math.sqrt(int(current_number)):.2f}.')
