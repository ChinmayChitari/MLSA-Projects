import math

history = []

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y if y != 0 else "Error: Division by zero"

def power(x, y):
    return math.pow(x, y)

def square_root(x):
    return math.sqrt(x)

while True:
    print("\n--- Calculator Pro ---")
    print("1. Add\n2. Subtract\n3. Multiply\n4. Divide\n5. Power\n6. Square Root\n7. Show History\n8. Exit")
    choice = input("Choose an option: ")

    if choice == "8":
        print("Goodbye! Math conquered!")
        break

    if choice == "7":
        print("\nCalculation History:")
        for h in history:
            print(h)
        continue

    if choice == "6":
        num = float(input("Enter number: "))
        result = square_root(num)
        print("Result:", result)
        history.append(f"sqrt({num}) = {result}")
    else:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == "1":
            result = add(num1, num2)
        elif choice == "2":
            result = subtract(num1, num2)
        elif choice == "3":
            result = multiply(num1, num2)
        elif choice == "4":
            result = divide(num1, num2)
        elif choice == "5":
            result = power(num1, num2)
        else:
            print("Invalid choice")
            continue

        print("Result:", result)
        history.append(f"{num1} op {num2} = {result}")
