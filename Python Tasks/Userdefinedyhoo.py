class InvalidAgeError(Exception):
    """Raised when the provided age is invalid."""
    pass


def validate_age(age):
    if age < 18:
        raise InvalidAgeError("Age must be 18 or above.")
    return age


if __name__ == "__main__":
    for value in (22, 16):
        try:
            age = validate_age(value)
            print(f"Age {age} is valid.")
        except InvalidAgeError as e:
            print(f"InvalidAgeError: {e}")