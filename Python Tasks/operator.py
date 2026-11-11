class Books:
    def __init__(self, pages):
        self.__pages = pages
    
    def __add__(self, other):
        return self.__pages + other.__pages
    def __mul__(self, other):
        return self.__pages * other.__pages
    def __gt__(self, other):
        return self.__pages > other.__pages
b1 =  Books(100)
b2 =  Books(200)

print(b1 + b2)
print(b1 * b2)
print(b1 > b2)