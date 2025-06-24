"""
need to add a looping system/ done
need to add other operations/ done
"""
# need to add percent age
# better terminology

# calculator 2.1
# failure safe
# loop
# clear function
result = "Error: Loop error"
while True:

    # input for first number
    while True:
        if result.isdigit():
            number_1 = float(result)
            print(f"first number: {number_1}")
            break
        else:
            number_1 = input("enter the first number: ")
        if number_1.isdigit():
            number_1 = float(number_1)
            break
        else:
            print("Error: Invalid number.")

    # input for operations
    while True:
        operation = input(
            "[+][-][*][/],power[**], root[#]\ndivision in quotient and reminder[//]\n: ")
        if operation == "+" or operation == "-" or operation == "*" or operation == "/" or operation == "**" or operation == "#" or operation == '//':
            break
        else:
            print("Error: Invalid operator.")

    # input for second number
    while True:
        number_2 = input("enter the second number: ")
        if number_2.isdigit():
            number_2 = float(number_2)
            if number_2 == 0 and operation == "/":
                print("Error: Division by zero")
            else:
                break
        else:
            print("Error: Invalid number.")

    # operations
    if operation == "+":
        result = number_1 + number_2
        operation = f"sum of {number_1} and {number_2} is "

    elif operation == "-":
        result = number_1 - number_2
        operation = f"diiferance between {number_2} and {number_1} is "

    elif operation == "*":
        result = number_1 * number_2
        operation = f"product of {number_1} and {number_2} is "

    elif operation == "/":
        operation = f"quotient of {number_1} and {number_2} is "
        result = number_1 / number_2

    elif operation == "**":
        operation = f"{number_1} with power {number_2} is "
        result = number_1 ** number_2

    elif operation == "#":
        operation = f"{number_1} root {number_2} is "
        result = number_1 ** (1/number_2)
        result = round(result, 5)

    elif operation == "//":
        operation = f"division of {number_1} and {number_2} will give "
        quotient = number_1 // number_2
        reminder = number_1 % number_2
        result = f"quotient: {quotient}, and reminder: {reminder}"

    print(f"{operation}{result}")

    result = str(result)  # so .isdigit works, since it doesnt work on int()

    exit = input("type 'e' to exit,'c' to clear or press enter to continue: ")
    if exit == "e":
        break
    elif exit == "c":
        result = "turning into string"
