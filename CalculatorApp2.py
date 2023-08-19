#Calculator

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}


def calculator():
    num1 = float(input("What's the first number?: "))
    for operation in operations:
        print(operation)
    should_continue = True

    while should_continue:
        operation_symbol = input("Pick an operation: ")
        num2 = float(input("What's the next number?: "))
        calculation = operations[operation_symbol]
        answer = calculation(num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {answer}")

        go_again = input(f"Type 'y' to continue calculating with {answer}, type 'n' to start a new calculation or type 'x' to exit.")
        if go_again == "y":
            num1 = answer
        elif go_again == "n":
            should_continue = False
            calculator()
        elif go_again == "x":
            print("Goodbye")
            should_continue = False



calculator()