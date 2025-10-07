'''
Write a function that shifts each letter in a string
to the next letter in the alphabet.(abc->bcd)
'''

def letter_shift(string):
    convert_to_ascii_numbers = [ord(char)+1 for char in string]
    converted_charcaters = [chr(char) for char in convert_to_ascii_numbers]
    join_letters = "".join(converted_charcaters)
    print(f'{string}--->{join_letters}')
    


letter_shift("salam")