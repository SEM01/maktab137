def max_repeat(list):
    result = dict((i, list.count(i)) for i in list)
    max_element = max(result, key=result.get)
    print(f"Maximum Repeat: {max_element}")
    
list=[]
max_repeat(list)