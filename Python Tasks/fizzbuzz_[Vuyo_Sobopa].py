def fizz_buzz(n):
    # formulate my input
    if n <= 0:
        print("Invalid input. Try again.")
        return
#set range in correspondance with the input
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)

# Ask the user for input
maximum = int(input("Enter the maximum value: "))

# Run the function
fizz_buzz(maximum)
print("FizzBuzz is Easy with practise")