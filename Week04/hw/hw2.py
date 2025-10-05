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