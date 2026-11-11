class ComplexNumber:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __add__(self, other):
        return ComplexNumber(self.real + other.real, self.imag + other.imag)

    def __mul__(self, other):
        real_mul = self.real * other.real - self.imag * other.imag
        imag_mul = self.real * other.imag + self.imag * other.real
        return ComplexNumber(real_mul, imag_mul)

    def __str__(self):
        sign = "+" if self.imag >= 0 else "-"
        imag_val = abs(self.imag)
        return f"{self.real} {sign} {imag_val}i"

num1 = ComplexNumber(2, 3)
num2 = ComplexNumber(1, 2)

print(f"Sum: {num1 + num2}")
print(f"Product: {num1 * num2}")