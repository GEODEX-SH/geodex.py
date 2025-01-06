def get_numbers():
    # Initialize an empty list to store the numbers
    numbers = []
    
    # Loop to get 10 numbers from the user
    for i in range(10):
        while True:
            try:
                # Prompt the user to enter a number
                number = float(input(f"Enter number {i + 1}: "))
                numbers.append(number)
                break
            except ValueError:
                print("Invalid input. Please enter a valid number.")
    
    return numbers

def multiply_numbers(numbers):
    # Initialize the result to 1 (multiplicative identity)
    result = 1
    
    # Multiply all the numbers together
    for number in numbers:
        result *= number
    
    return result

# Get 10 numbers from the user
user_numbers = get_numbers()

# Multiply the numbers and get the result
result = multiply_numbers(user_numbers)

# Print the result
print(f"The result of multiplying the 10 numbers is: {result}")