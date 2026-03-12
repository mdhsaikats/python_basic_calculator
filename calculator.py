while True:
    number1 = int(input("Enter the Number 1: "))
    number2 = int(input("Enter the Number 2: "))
    operator = input("Enter the operator: ")
    match operator:
        case "+":
            print(number1 + number2)
        case "-":
            print(number1 - number2)
        case "*":
            print(number1 * number2)
        case "/":
            if number2 == 0:
                print("Cannot divide by zero")
            else:
                print(number1 / number2)
        case "exit":
            print("Exiting the calculator")
            break
