class InvalidAgeError(Exception): 
        pass    
        def __init__ (self, age):
            self.age = age
        def validate(self):
            try:
                if self.age <= 18:
                    raise InvalidAgeError("Age must be 18 or above.")
                elif self.age >= 18:
                    print("Age is valid")
            except InvalidAgeError as e:
                print(f"InvalidAgeError: {e}")

age = InvalidAgeError(22)
age.validate()
age = InvalidAgeError(16)
age.validate()
