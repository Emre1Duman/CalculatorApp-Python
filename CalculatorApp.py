import os
clear = lambda: os.system('clear')

# def calcu(first_num, operation, second_num):
#     print(calculation(first_num, operation, second_num))
#     go_again = input(f"Type 'y' to continue calculating with {calc}, type 'n' to start a new calculation or type 'x' to exit calculator. ").lower()
#     if go_again == "x":
#         print("Goodbye")
#         endcalc = True
#     elif go_again == "y":
#         operation = input("Pick an operation: ")
#         second_num = int(input("What's the next number?: "))
#         print(calculation(calc, operation, second_num))
#     elif go_again == "n":
#         print(calculation(first_num, operation, second_num))

def calculation(first_num, operation, second_num):
    endcalc = False
    while endcalc == False:
        if operation == "+":
            calc = first_num + second_num
            print( f"{first_num} + {second_num} = {calc}")
        elif operation == "-":
            calc = first_num - second_num
            print( f"{first_num} - {second_num} = {calc}")
        elif operation == "*":
            calc = first_num * second_num
            print( f"{first_num} * {second_num} = {calc}")
        elif operation == "/":
            calc = first_num / second_num
            return f"{first_num} / {second_num} = {calc}"
        go_again = input(f"Type 'y' to continue calculating with {calc}, type 'n' to start a new calculation or type 'x' to exit calculator. ").lower()
        if go_again == "x":
            print("Goodbye")
            endcalc = True
        elif go_again == "y":
            operation = input("Pick an operation: ")
            second_num = int(input("What's the next number?: "))
            print(calculation(calc, operation, second_num))
        elif go_again == "n":
            clear()
            first_num = int(input("What's the first number?: "))
            print("""+
            -
            *
            / """)
            operation = input("Pick an operation: ")
            second_num = int(input("What's the next number?: "))
            print(calculation(first_num, operation, second_num))

        
        
first_num = int(input("What's the first number?: "))
print("""+
-
*
/ """)
operation = input("Pick an operation: ")
second_num = int(input("What's the next number?: "))

print(calculation(first_num, operation, second_num))
