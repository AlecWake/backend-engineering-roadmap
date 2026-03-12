number1 = int(input("Number1: "))
number2 = int(input("Number2: "))
operator = input("Operator: ")

if operator == "+":
    value = number1 + number2
elif operator == "-":
    value = number1 - number2
elif operator == "*":
    value = number1 * number2
elif operator == "/":
    if number2 != 0:
        value = number1 / number2
    else:
        value = "Division by 0 error"
else:
    value = "incorrect operator"
print("value", value)