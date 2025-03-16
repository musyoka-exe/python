#ask for the first number
number1 = float(input("Enter the first number: "))
#ask for the operation
opertion = (input("Enter the operation [+, -, *, /]: "))
#ask for the second number
number2 = float(input("Enter the second number: "))

#do the math
if opertion == "+":
    print(number1 + number2)
elif opertion == "-":
    print(number1 - number2)
elif opertion == "*":
    print(number1 * number2)
elif opertion == "/":
    #check if the second number is not zero for the sake of division
    if number2 != 0:
        print(number1 / number2)
    else:
        print("Error: Division by zero is not allowed.")
else:
    print("Error: Invalid operation.")
    