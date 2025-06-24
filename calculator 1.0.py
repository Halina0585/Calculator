import os
num_1 = int(input("first number: "))
op_1 = input("operation[+,-,*,/]: ")
num_2 = int(input("second number: "))
if op_1 == "+":
    result = num_1 + num_2
elif op_1 == "-":
    result = num_1 - num_2
elif op_1 == "*":
    result = num_1 * num_2
elif op_1 == "/":
    if num_2 == 0:
        result = "Error: Division by zero"
    else:
        result = num_1 / num_2
else:
    result = "Error: Invalid operation"
input(result)
os.system("cls")
# first part of the caculator
while True:
    num_3 = result
    print(f"first number: {num_3}")
    op_2 = input("operation[+,-,*,/]: ")
    num_4 = int(input("secound number: "))
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
        result = "Error: Invalid operation"
    print(result)
    user_input = input("press enter to continue or type 'exit' to leave")
    os.system("cls")
    if user_input == "exit":
        quit()
# secound part, with ability to add/sub/mul/div the result
