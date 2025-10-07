'''
Write a function that returns:
    square if input is integer
    length if input is string
    sum if input is list
'''

def type_identifier(data_input):
    if type(data_input)==int:
        return f'{data_input} ^ 2 = {data_input**2}'
    elif type(data_input)==str:
        return f'Length of "{data_input}": {len(data_input)}'
    elif type(data_input)== list:
        return f'Sum {"+".join(str(number) for number in data_input)} = {sum(data_input)}'

