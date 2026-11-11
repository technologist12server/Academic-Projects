class Person1:
    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city

    def display_info(self):
        print("Name:", self.name, 'Age:', self.age, "City:",self.city)

p1 = Person1("John Doe", 30, "New York")
p1.display_info()