def add(a, b):
    return a+b
def subtract(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    if b!=0:
       return a/b
    else:
        return "Cannot divide by zero"
print("Simple Calculator")
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print("Sum: ", num1 + num2)
print("Sub: ", num1 - num2)
print("Mul: ", num1 * num2)
print("Div: ", num1 / num2)
print("Frac: ", num1 // num2)
print("Mod: ", num1 % num2)