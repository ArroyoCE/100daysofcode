import lib.art


def calculation(number_a, number_b, symbol):
    """ Takes two numbers and calculates according to the parameter passed"""
    if symbol == "+":
        return number_a + number_b
    elif symbol == "-":
        return number_a - number_b
    elif symbol == "*":
        return number_a * number_b
    else:
        return number_a / number_b


print(lib.art.logo)


number1 = float(input("What's the first number? "))
print("+", "-", "*", "/", sep="\n")
operation = input("What's the operation? ")
number2 = float(input("What's the second number? "))
result = calculation(number1, number2, operation)
print(f"\n{number1} " + operation + f" {number2} = {result}")
more = input(f"\nDo you want to continue calculating with {result}? ('y' or 'n') ")
while True:

    if more.lower() == 'y':
        number1 = result
        operation = input("What's the operation? ")
        number2 = float(input("What's the second number? "))
        result = calculation(number1, number2, operation)
        print(f"\n{number1} " + operation + f" {number2} = {result}")
    else:
        break

    more = input(f"\nDo you want to continue calculating with {result}? ('y' or 'n') ")
