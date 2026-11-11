meal_price = input('How much was the meal? ')
tip_percentage = input('What percentage would you like to tip? ')

tip_amount = float(str(meal_price[1:5])) * (float(tip_percentage[0:5]) / 100)
print(f'Leave ${tip_amount:.2f}.')