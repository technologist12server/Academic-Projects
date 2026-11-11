a = [0,1,2,3,4,5]

for x in a:
    print(x)
    if x == 2:
        break

print('------------------')

i = 0
while i < 5:
    i += 1
    if i == 3:
        continue
    print(i)