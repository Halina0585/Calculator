# lacks: failure safe against symbols, spaces and blank inputs
# and compact design

import os

result = "Assigning result a value!"

while True:

    while True:

        if not any(alpha.isalpha() for alpha in result):
            if result.count("-") == 0 or result.find("-") == 0:
                if result.count(".") == 1 or result.count(".") == 0:
                    num_1 = float(result)
                    print(num_1)
                    break
        else:
            if result != "Assigning result a value!":
                print("Error: Result contanes an alphabet!")
            else:
                result = "to prevent endless looping"
        num_1 = input("first number: ")
        if not any(digit.isalpha() for digit in num_1):
            if num_1.count("-") == 0 or num_1.find("-") == 0:
                if num_1.count(".") == 1 or num_1.count(".") == 0:
                    num_1 = float(num_1)
                    break
                else:
                    print("Error: Invalid decimal number!")
            else:
                print("Error: Invalid negative number!")
        else:
            print("Error: Not a valid number!")

    while True:

        op = input(
            "[+][-][*][/][%],power[**], root[#]\ninteger division[//]\n: ")

        if op == "+" or op == "-" or op == "*" or op == "/" or op == "**" or op == "#" or op == '//' or op == "%":
            break

        else:
            print("Error: Invalid operator.")

    while True:
        num_2 = input("second number: ")
        if not any(alpha.isalpha() for alpha in num_2):
            if num_2.count("-") == 0 or num_2.find("-") == 0:
                if num_2.count(".") == 1 or num_2.count(".") == 0:
                    num_2 = float(num_2)
                    if num_2 == 0.0 and op == "/" or op == "//":
                        print("cant divide by zero")
                    else:
                        break
                else:
                    print("Error: Invalid decimal number!")
            else:
                print("Error: Invalid negative number!")
        else:
            print("Error: Not a valid number!")

    if op == "+":
        result = num_1 + num_2
        op = f"sum of {num_1} and {num_2} is "

    elif op == "-":
        result = num_1 - num_2
        op = f"diiferance between {num_2} and {num_1} is "

    elif op == "*":
        result = num_1 * num_2
        op = f"product of {num_1} and {num_2} is "

    elif op == "/":
        op = f"quotient of {num_1} and {num_2} is "
        result = num_1 / num_2

    elif op == "**":
        op = f"{num_1} with power {num_2} is "
        result = num_1 ** num_2

    elif op == "#":
        op = f"{num_1} root {num_2} is "
        result = num_1 ** (1/num_2)
        result = round(result, 5)

    elif op == "//":
        op = f"division of {num_1} and {num_2} will give "
        quotient = num_1 // num_2
        reminder = num_1 % num_2
        result = f"quotient: {quotient}, and reminder: {reminder}"

    elif op == "%":
        op = f"{num_2}% of {num_1} is "
        result = num_1 * (num_2/100)

    print(f"{op}{result}")

    # so .isdigit works, since it doesnt work on int()
    result = str(result)

    exit = input("type 'e' to exit,'c' to clear or press enter to continue: ")
    os.system("cls")

    if exit == "e":
        break

    elif exit == "c":
        # so result dont have any number and can bypass result loop
        result = "turning into string"
