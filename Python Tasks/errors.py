import math

def number(value):
    try:
        number = float(value)
        if number < 0:
            raise ValueError("Number must be positive.")
        return math.sqrt(number)
     
    except ValueError as e:
         if isinstance(value, str):
            return f"Invalid input. Please enter a valid number"
         else:
             return f"Invalid input. Please enter a positive number."

Result1 = number(9)
Result2 = number('abc')
Result3 = number(-4)

print(f"Result 1: {Result1}")
print(f"Result 2: {Result2}")
print(f"Result 3: {Result3}")

class TeaException(Exception):
    class Tea:
        def __init__(self, msg):
            self.msg = msg
    class Tea:
        def __init__(self, temperature):
            self.temperature = temperature
    def drink_tea(self):
        if self.temperature > 85:
            raise ValueError("Tea is too hot to drink!")
        elif self.temperature < 65:
            raise ValueError("Tea is too cold to drink!")
        else:
            print("Tea is just right to drink!")

cup = Tea(100)
cup.drink_tea()