# 1. Ask the user for numbers
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# 2. Ask for the operation
print("Choose: +, -, *, /")
choice = input("Enter choice: ")

# 3. Do the math and show the answer
if choice == "+":
    print("Answer:", num1 + num2)

elif choice == "-":
    print("Answer:", num1 - num2)

elif choice == "*":
    print("Answer:", num1 * num2)

elif choice == "/":
    print("Answer:", num1 / num2)

else:
    print("Invalid choice!")