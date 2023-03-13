num1 = 10
num2 = 15
operator = '*'

def calcule(num1, operator, num2):
    result = 0
    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '*':
        result = num1 * num2
    elif operator == '/':
        result = num1 / num2
    elif operator == '%':
        result = num1 % num2
    return result

print(calcule(num1, operator, num2))