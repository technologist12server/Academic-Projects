"""class Speed:
    def __init__(self):
        self.speed = 10
        self.__new_speed = 60
    
    def get_new_speed(self):
        return self.__new_speed
    
    def set_new_speed(self, new_speed):
        self.__new_speed = new_speed

s = Speed()
print(s.get_new_speed())
s.set_new_speed(100)
print(s.get_new_speed())"""

# single underscore _var is a convention to indicate that the variable is intended for internal use (not enforced by the language)
# double underscore __var is used for name mangling to make the variable private and not accessible
#class example

class Example:
    def __init__(self):
        self.x = 10
        self._y = 50
        self.__z = 100
    
    def public_method(self):
        print(self.x)
        print(self._y)
        print(self.__z)
        self.__private_method()

    def __private_method(self):
        print("Inside private method.")

s = Example()
s.public_method()
#s.__private_method()