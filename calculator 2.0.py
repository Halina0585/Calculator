# need to add a looping system/ done
# need to add other operations

# calculator 2.0
# failure safe
# loop
# clear function
result = "Error: "
while True:
    # input for first number
    while True:
        if result.isdigit():
            num_1 = int(result)
            print(f"first number: {num_1}")
            break
        else:
            num_1 = input("enter the first number: ")
        if num_1.isdigit():
            num_1 = int(num_1)
            break
        else:
            print("Error: Invalid number.")
    # input for operations
    while True:
        op_1 = input("[+,-,*,/]: ")
        if op_1 == "+" or op_1 == "-" or op_1 == "*" or op_1 == "/":
            break
        else:
            print("Error: Invalid operator.")
    # input for second number
    while True:
        num_2 = input("enter the second number: ")
        if num_2.isdigit():
            num_2 = int(num_2)
            if num_2 == 0 and op_1 == "/":
                print("Error: Division by zero")
            else:
                break
        else:
            print("Error: Invalid number.")
    # operations
    if op_1 == "+":
        result = num_1 + num_2
        op_1 = f"sum of {num_1} and {num_2}"
    elif op_1 == "-":
        result = num_1 - num_2
        op_1 = f"diiferance between {num_2} and {num_1}"
    elif op_1 == "*":
        result = num_1 * num_2
        op_1 = f"product of {num_1} and {num_2}"
    elif op_1 == "/":
        op_1 = f"quotient of {num_1} and {num_2}"
        result = num_1 / num_2
    print(f"{op_1} is {result}")
    # looping
    result = str(result)
    exit = input("type 'e' to exit,'c' to clear or press enter to continue: ")
    if exit == "e":
        break
    elif exit == "c":
        result = "turning into string"
