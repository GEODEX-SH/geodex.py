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

def divide_numbers(numbers):
    # Initialize the result with the first number
    result = numbers[0]
    
    try:
        # Divide each subsequent number to the result
        for number in numbers[1:]:
            result /= number
    except ZeroDivisionError:
        return "Error: Division by zero is not allowed."
    
    return result

# Get 2numbers from the user
user_numbers = get_numbers()

# Divide the numbers and get the result
result = divide_numbers(user_numbers)

# Print the result
print(f"The result of dividing the 2numbersnumbers numbers is: {result}")