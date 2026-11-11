a = int(input(''))
if a < 12:
    print('You are a child')
elif a >= 12 and a <= 17:
    print('You are a teenager')
elif a >= 18 and a <= 35:
    print('You are a young adult')
elif a >= 36 and a <= 64:
    print('You are a middle-aged adult.')
else:
    print('You are a senior')