'''
Write a function that checks if a word or sentence is a palindrome.
'''

def palindrome_check(word):
    if word[:(len(word)//2)] == word[len(word):len(word)//2:-1]:
        return f'"{word}" is PALINDROME'
    else:
        return f'"{word}" not PALINDROME'


