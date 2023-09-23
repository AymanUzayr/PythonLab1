num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
print("\nSelect operation:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

choice = input("Enter choice (1/2/3/4): ")

if choice in ('1', '2', '3', '4'):
        if choice == '1':
            print("Result:", num1 + num2)
        elif choice == '2':
            print("Result:", num1 - num2)
        elif choice == '3':
            print("Result:", num1 * num2)
        elif choice == '4':
            if num2 == 0:
                print("Cannot divide by zero")
            else:
                print("Result:", num1 / num2)
else:
        print("Invalid input. Please select a valid operation.")
