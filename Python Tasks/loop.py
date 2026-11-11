x = 0
while x < 6:
    print("Current value of x", x)
    x = x + 1
else:
    print("x is no longer less than 6")
num = 1
sum = 0
print("enter number for sum, Press '0' to exit")
while num != 0:
    num =int(input(''))
    sum = sum + num
    print("Current sum:", sum)
else:
    print('Loop is completed')