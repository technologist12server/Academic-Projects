result =  None
x =  int(input("Number1: "))
y = int(input("Number2: "))

try:
    result = x / y
except Exception as e:
    print(e)
else:
    print("Division successful. The result is:", result)