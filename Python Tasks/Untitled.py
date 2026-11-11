class InvalidAgeError(Exception):
    pass

def validate_age(age):
    if age < 18:
        raise InvalidAgeError("Age must be 18 or above.")
    return "Age is valid"

try:
    print(validate_age(22))
    print(validate_age(16))
except InvalidAgeError as e:
    print(f"InvalidAgeError: {e}")