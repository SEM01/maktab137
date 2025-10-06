'''
دو دکوراتور بنویسید. یکی ورودی های تابع را به
string
تبدیل کند و دیگری طول
string
هر ورودی را چاپ کند. این دو را روی یک تابع تست کنید
'''
def str_deco(func):
    def wrapper(string):
        func(str(string))    
    return wrapper

def str_lengh(func):
    def wrapper(string):
        func(string)
        print(len(string))
    return wrapper
    

@str_deco
@str_lengh
def str_lst(list):
    return list