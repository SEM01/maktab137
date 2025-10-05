from functools import wraps



def memo(f):
    memory = {}
    
    @wraps(f)
    def wrapper(*args, **kwargs):
        if args not in memory:
            memory[args] = f(*args, **kwargs)
            print('result saved in memory')
        else:
            print("returning result from saved memory")
            
        return memory[args]
    return wrapper 
@memo
def str_repeat(string1):
    
    string2 = (string1.lower())
    string_lst = string2.split()
    result =(' '.join([char for char in string_lst if char.isalnum()])).split()
    count = {}
    for i in result:
        count[i]=count.get(i,0)+1
    return count
    


string10 = "Salam emroz salam man emroz ? !"
print(str_repeat(string10))
print(str_repeat(string10))
