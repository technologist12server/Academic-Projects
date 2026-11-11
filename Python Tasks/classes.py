"""class Student:
    def __init__(self):
        self.name = "John Doe"
        self.age = 20
        self.grade = 12
        self.subject = "Mathematics"
        self.marks = 90

    def talk(self):
        print("Name -", self.name)
        print("Age -", self.age)
        print("Grade -", self.grade)
        print("Subject  -", self.subject)
        print("Marks -", self.marks)

s1 = Student()
print(s1.subject)"""

"""n =  input('Name: ')
a = int(input('Enter age: '))
m = int(input('Enter marks: '))"""

class Student:
    def __init__(self, n, a, **m):
        self.name = n
        self.age = a
        self.marks = m
    
    def display(self):
        print("Hi", self.name)
        print("Your age", self.age)
        print("Your marks", self.marks)

s1 = Student("Dyan", 20, history=21, math=20)
s1.display()

"""print("--------")

s2 = Student("John", 30, Mathematics=80, Science=90, English=85, History=75)
s2.display()"""

"""class Student:
    def __init__(self, n):
        self.name = n
       
    
    def display(self):
        print("Hi", self.name)

s1 = Student("Dyan")
s1.display()"""