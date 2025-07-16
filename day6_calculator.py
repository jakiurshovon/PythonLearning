print("Simple Calculator")
print("-----------------")

while True:
    print("\n1. Add\n2. Subtract\n3. Multiply\n4. Divide\n5. Exit")
    choice = input("Choose an option (1-5): ")

    if choice == '5':
        print("Exiting calculator. Goodbye!")
        break

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if choice == '1':
        result = num1 + num2
        print(f"Result: {result}")
    elif choice == '2':
        result = num1 - num2
        print(f"Result: {result}")
    elif choice == '3':
        result = num1 * num2
        print(f"Result: {result}")
    elif choice == '4':
        if num2 != 0:
            result = num1 / num2
            print(f"Result: {result}")
        else:
            print("Error: Cannot divide by zero.")
    else:
        print("Invalid option. Please choose 1–5.")
    decision = input("Do you want to continue? (yes/no):")
    if decision == "no":
        print("Exiting calculator. Goodbye!")
        break