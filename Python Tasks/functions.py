"""def shop(items, price):
    print('Item: ', items)
    print('Price: ', price)

shop('Bread', 20) """

def std(name, Clas, **Marks):
    print('name: ', name)
    print('Clas: ', Clas)
    print('Marks: ', Marks)

    for x, y in Marks.items():
        print(x, "Marks: ", y)

std('Vuyo', 'Python', clas=100, english=90, maths=80, science=70)
