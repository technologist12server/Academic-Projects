A = [0,1,2,3,4,5,6,7,8,9]
B = (0,1,2,3,4,5,6,7,8,9)
C = {0,1,2,3,4,5,6,7,8,9}
D = "Vuyo is the best"
E = {"name": "Vuyo", 
     "age": 20, 
     "city": "Cape Town"}
for x, y in E.items():
    print(x, "", y)

print(1 in A)
print('V' in D)
print("L" in D)

for i in A:
    print(i)
for i in E:
    print(i)   
for i in E.values():
    print(i) 

for x in range(0, 10, 2):
    print(x)