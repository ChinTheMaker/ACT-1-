def calculator():
    # Display menu
    print("Select operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    # Get user's choice
    choice = input("Enter choice (1/2/3/4): ")

    # Get the numbers from the user
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    # Perform the operation based on user's choice
    if choice == '1':
        result = num1 + num2
        print(f"The result of {num1} + {num2} is {result}")
    elif choice == '2':
        result = num1 - num2
        print(f"The result of {num1} - {num2} is {result}")
    elif choice == '3':
        result = num1 * num2
        print(f"The result of {num1} * {num2} is {result}")
    elif choice == '4':
        if num2 != 0:
            result = num1 / num2
            print(f"The result of {num1} / {num2} is {result}")
        else:
            print("Error! Division by zero.")
    else:
        print("Invalid input. Please select a valid operation.")

# Run the calculator
calculator()
