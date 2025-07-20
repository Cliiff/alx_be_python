num1 = int(input("Enter the first number:"))
num2 = int(input("Enter the second number:"))
operations = input("Choose the operation (+, -, *, /):")
match operations:
    case "+":
        print ("The result is",num1 + num2)
    case "-":
        print("The result is",num1 - num2)
    case "*":
        print("The result is",num1 * num2)
    case "/":
        print("The result is",num1 / num2)
    case _:
        print("Operation Error")
