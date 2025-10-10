'''
ماشین حساب: تابعی که دو عدد از نوع
positional only
دریافت کند و عملگرهای اصلی جمع ضرب تفریق تقسیم به صورت
keyword only 
دریافت کند و نتیجه را برگرداند
'''
def calculator(number1, number2,/,*, operation):
    if operation == "+":
        return f'{number1} + {number2} = {number1+number2}' 
    elif operation == "-":
        return f'{number1} - {number2} = {number1-number2}'
    elif operation == "*":
        return f'{number1} * {number2} = {number1*number2}'
    else:
        return f'{number1} / {number2} = {number1/number2}'
    
print(calculator(2,1,operation="/"))
