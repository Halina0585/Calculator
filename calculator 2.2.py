# need to add

# clear function at anytime
# negatuve numbers support
# imagenery number support
# failure safe for double decimal

# calculator 2.2

# failure safe
# loop
# clear function at the end
# decimal support
# percentage support


import os

result = "Error: Loop error"

while True:

    while True:

        # to operate on the result
        if result.isdigit():
            number_1 = int(result)
            print(f"first number: {number_1}")
            break

        elif result.find(".") != -1:
            if result.split(".")[0].isdigit() and result.split(".")[1].isdigit():
                number_1 = float(result)
                print(f"first number: {number_1}")
                break

            # a failure safe to prevent failures if result has [e] in it [1.6e *10]
            else:  # add loop
                print("Error: Result has a letter and decimal[.]")
                number_1 = input("enter the first number: ")

                if number_1.find(".") != -1:
                    if number_1.split(".")[0].isdigit() and number_1.split(".")[1].isdigit():
                        number_1 = float(number_1)
                        break
                    else:
                        print("Error: Decimal")

                elif number_1.isdigit():
                    number_1 = int(number_1)
                    break

                else:
                    print("Error: Invalid number.")

        # to input the first number
        else:
            number_1 = input("enter the first number: ")

            if number_1.find(".") != -1:
                if number_1.split(".")[0].isdigit() and number_1.split(".")[1].isdigit():
                    number_1 = float(number_1)
                    break
                else:
                    print("Error: Decimal")

            elif number_1.isdigit():
                number_1 = int(number_1)
                break

            else:
                print("Error: Invalid number.")

    # to input the operations
    while True:
        operation = input(
            "[+][-][*][/],power[**], root[#]\ninteger division[//]\n: ")
        if operation == "+" or operation == "-" or operation == "*" or operation == "/" or operation == "**" or operation == "#" or operation == '//' or operation == "%":
            break

        else:
            print("Error: Invalid operator.")

    # to input the second number
    while True:

        number_2 = input("enter the second number: ")

        if number_2.find(".") != -1:
            if number_2.split(".")[0].isdigit() and number_2.split(".")[1].isdigit():
                number_2 = float(number_2)
                # to prevent division by 0
                if number_2 == 0.0 and operation == "/" or operation == "//":
                    print("cant divide by zero")
                else:
                    break

            else:
                print("Error: Decimal")

        elif number_2.isdigit():
            number_2 = int(number_2)

            # to prevent division by 0
            if number_2 == 0 and operation == "/" or operation == "//":
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

    elif operation == "%":
        operation = f"{number_2}% of {number_1} is "
        result = number_1 * (number_2/100)

    print(f"{operation}{result}")

    # so .isdigit works, since it doesnt work on int()
    result = str(result)

    exit = input("type 'e' to exit,'c' to clear or press enter to continue: ")
    os.system("cls")

    if exit == "e":
        break

    elif exit == "c":
        # so result dont have any number and can bypass result loop
        result = "turning into string"
