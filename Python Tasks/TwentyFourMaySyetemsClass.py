
initial_temperature = 25.0
set_temperature = 30.0

class TemperatureConverter:
    def __init__(self, celsius):
        self.__celsius = celsius

    def set_values(self, celsius):
        self.__celsius = celsius

    def get_values(self):
        return self.__celsius

a = set_temperature - initial_temperature
print(set_temperature)
