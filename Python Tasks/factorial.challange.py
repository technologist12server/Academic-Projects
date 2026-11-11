num = {1, 2, 3, 4, 5} #set

for num in range(1, 6):
    factorial = 1
    for i in range(1, num + 1):
        factorial *= i
    print(f"The factorial of {num} is {factorial}")

A = (1, 2, 3, 4, 5) #tuple
for i in A:
    print(i)

B = {"Name": "Vuyo",
     "Surname": "Davids"}
for i in B.values():
    print(i)