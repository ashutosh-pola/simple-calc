value1 = input("Enter a number: ")
value2 = input("Enter another number: ")
value1 = float(value1)
value2 = float(value2)
operator = input("Enter a operator: ")

while operator not in ["+", "-", "*", "/" ]:
    print("Invalid operator")
    operator = input("Enter a operator: ")
if operator == "+":
    print(value1 + value2)
elif operator == "-":
    print(value1 - value2)
elif operator == "*":
    print(value1 * value2)
elif operator == "/":
    print(value1/value2)
elif operator == "^":
    print(value1 ** value2)
elif operator == "%":
    print(value1 % value2)
