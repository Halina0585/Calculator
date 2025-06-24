import os
import time
while True:
    num_1 = int(input("first num: "))
    op_1 = input("[+,-,*,/]: ")
    num_2 = int(input("second num: "))
    if op_1 == "+":
        result = num_1 + num_2
        op_1 = "sum"
    elif op_1 == "-":
        result = num_1 - num_2
        op_1 = "subtraction"
    elif op_1 == "*":
        result = num_1 * num_2
        op_1 = "product"
    elif op_1 == "/":
        op_1 = "quotient"
        if num_2 == 0:
            result = "Error: Division by zero"
        else:
            result = num_1 / num_2
    else:
        result = "Error: Invalid "
    input(f"{op_1} of {num_1} and {num_2} is {result}")
    os.system("cls")
# secound part, with ability to add/sub/mul/div the result
    while True:
        num_3 = result
        print(f"first num: {num_3}")
        op_2 = input("[+,-,*,/]: ")
        num_4 = int(input("secound num: "))
        if op_2 == "+":
            result = num_3 + num_4
        elif op_2 == "-":
            result = num_3 - num_4
        elif op_2 == "*":
            result = num_3 * num_4
        elif op_2 == "/":
            if num_4 == 0:
                result = "Error: Division by zero"
            else:
                result = num_3 / num_4
        else:
            result = "Error: Invalid"
        print(result)
        if result != int:
            result = 0
        user_input = input(
            "press enter to continue, type 'c' to clear or type 'exit' to leave: ")
        os.system("cls")
        if user_input == "exit":
            quit()
        elif user_input == "c":
            break
