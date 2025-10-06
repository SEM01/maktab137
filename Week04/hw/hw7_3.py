def calculator(number1, number2, operation):
    if operation == "+":
        return f'{number1} + {number2} = {number1+number2}' 
    elif operation == "-":
        return f'{number1} - {number2} = {number1-number2}'
    elif operation == "*":
        return f'{number1} * {number2} = {number1*number2}'
    else:
        return f'{number1} / {number2} = {number1/number2}'
    
print(calculator(2,1,operation="/"))
