'''
Write a function that takes a number and return 
the first prime number greater than it
'''

def prime_finder(number):
    while number>0:
        if number%2==0 or number%3==0:
            number+=1
        else:
            return number
    
