num1 = int(input("Zadej první číslo: "))
num2 = int(input("Zadej druhé číslo: "))
operation = input("Zadej operaci (+, -, *, /): ")

def scitani(num1, num2):
    return num1 + num2

def odcitani(num1, num2):
    return num1 - num2

def nasobeni(num1, num2):
    return num1 * num2

def deleni(num1, num2):
    return num1 / num2

if operation == "+":
    print(scitani(num1, num2))
elif operation == "-":
    print(odcitani(num1, num2))
elif operation == "*":
    print(nasobeni(num1, num2))
elif operation == "/":
    print(deleni(num1, num2))
