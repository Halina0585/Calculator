def add(x, y):
    return x + y


def sub(x, y):
    return x - y


def multi(x, y):
    return x * y


def division(x, y):
    try:
        return x / y
    except ZeroDivisionError:
        return "Not Defined"


def exponent(x, y):
    try:
        return x ** y
    except OverflowError:
        return "Error: Result too large!"


def root(x, y):
    root = x ** (1/y)
    try:
        root = round(root, 10)
        return root
    except:
        return root


def percent(x, y):
    return x * y/100


while True:

    while True:

        try:
            num_1 = float(input("First Number: "))
            break
        except:
            print("Error: Invalid Number!")

    while True:

        operation = input(
            "[+][-][*][/][%]\npower[**],root[#]\n: ")

        if operation in ("+", "-", "*", "/", "**", "#", '//', "%"):
            break

        else:
            print("Error: Invalid operator.")

    while True:

        try:
            num_2 = float(input("Second Number: "))
            break
        except:
            print("Error: Invalid Number!")

    if operation == "+":
        print(f"{num_1} + {num_2} =", add(num_1, num_2))

    elif operation == "-":
        print(f"{num_1} - {num_2} =", sub(num_1, num_2))

    elif operation == "*":
        print(f"{num_1} * {num_2} =", multi(num_1, num_2))

    elif operation == "/":
        print(f"{num_1} / {num_2} =", division(num_1, num_2))

    elif operation == "**":
        print(f"{num_1} power {num_2} =", exponent(num_1, num_2))

    elif operation == "#":
        print(f"{num_1} root {num_2} =", root(num_1, num_2))

    elif operation == "%":
        print(f"{num_2}% of {num_1} =", percent(num_1, num_2))

    to_exit = input("press enter to continue, or type 'e' to exit. ")

    if to_exit.lower() == 'e':
        print("Guess I was not needed anymore, farewell")
        break
