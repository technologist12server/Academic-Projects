#countdown - runs while condition is true
count = 3
while count > 0:
    print(count)
    count = count - 1
print('Lift off...')

# password retry until correct
password = input("Enter your password: ")
while password != "secret":
    print("Wrong password, try again.")
    password = input("Enter your password: ")
print("Access granted.")

range(12) #range(start, stop, step)
for number in range(0, 12, 2):
    print(number)

pin = ""
while pin != "1234":
    pin = input("Enter your PIN: ")
print("PIN accepted.")

index = 15
while index >= 0:
    print(f'I am now at {index}')
    index -= 1
